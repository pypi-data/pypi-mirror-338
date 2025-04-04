import json
import os
import tempfile
from typing import Any, Dict, List, Optional, Union, cast

import httpx
import jsonref
import yaml
from prance import ResolvingParser
from prance.util.url import ResolutionError
from pydantic import BaseModel

from .tool import Tool
from .tool_registry import ToolRegistry


def parse_openapi_spec(source: str) -> Dict:
    """
    Parse an OpenAPI specification, supporting JSON/YAML file paths or URLs.

    :param source: A local file path or remote URL
    :return: The parsed OpenAPI specification as a dictionary
    """
    try:
        # 1. If the source is a URL, download to temp file first
        if source.startswith("http"):
            with tempfile.NamedTemporaryFile(suffix=".json", delete=True) as temp_file:
                with httpx.Client() as client:
                    response = client.get(source)
                    response.raise_for_status()
                    temp_file.write(response.content)
                    temp_file.flush()
                
                parser = ResolvingParser(temp_file.name)
                return parser.specification

        # 2. If the source is a local file, check if it exists
        if not os.path.exists(source):
            raise FileNotFoundError(f"File not found: {source}")

        with open(source, "r", encoding="utf-8") as file:
            content = file.read()

        # 3. Parse JSON files
        if source.endswith(".json"):
            parser = ResolvingParser(content)
            return parser.specification

        # 4. Parse YAML files
        if source.endswith(".yaml"):
            parser = ResolvingParser(content)
            return parser.specification

    except (json.JSONDecodeError, yaml.YAMLError) as e:
        raise ValueError(f"Failed to parse OpenAPI specification: {e}")
    except ResolutionError as e:
        raise ValueError(f"Failed to resolve URL specification: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")


def openapi_to_function_schema(openapi_spec: Dict[str, Any]) -> Dict[str, Any]:
    """Convert OpenAPI schema to OpenAI function calling compatible schema.

    Args:
        openapi_spec: The OpenAPI specification (dict or file path)

    Returns:
        Dictionary containing OpenAI function calling compatible schema
    """

    # $ref references are already resolved by read_openapi_spec
    spec = openapi_spec

    functions = []
    for path, methods in spec.get("paths", {}).items():
        for method, spec in methods.items():
            method = method.lower()
            if method not in ["get", "post", "put", "delete"]:
                continue

            # Create function schema
            func = {
                "name": spec.get("operationId", f'{method}_{path.replace("/", "_")}'),
                "description": spec.get("description", spec.get("summary", "")),
                "parameters": {"type": "object", "properties": {}, "required": []},
            }

            # Handle parameters
            for param in spec.get("parameters", []):
                param_schema = param.get("schema", {})
                func["parameters"]["properties"][param["name"]] = {
                    "type": param_schema.get("type", "string"),
                    "description": param.get("description", ""),
                }
                if param.get("required", False):
                    func["parameters"]["required"].append(param["name"])

            # Handle request body
            if "requestBody" in spec:
                content = spec["requestBody"].get("content", {})
                if "application/json" in content:
                    schema = content["application/json"].get("schema", {})
                    for prop_name, prop_schema in schema.get("properties", {}).items():
                        func["parameters"]["properties"][prop_name] = {
                            "type": prop_schema.get("type", "string"),
                            "description": prop_schema.get("description", ""),
                        }
                    if "required" in schema:
                        func["parameters"]["required"].extend(schema["required"])

            functions.append(func)

    return {"functions": functions}


class OpenAPIToolWrapper:
    """Wrapper class providing both async and sync versions of OpenAPI tool calls."""

    def __init__(
        self,
        base_url: str,
        name: str,
        method: str,
        path: str,
        params_schema: Dict[str, Any],
    ) -> None:
        self.base_url = base_url
        self.name = name
        self.method = method.lower()
        self.path = path
        self.params_schema = params_schema
        self.required_params = params_schema.get("required", [])

    def _validate_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Validate input parameters against schema."""
        validated = {}
        for param, schema in self.params_schema.get("properties", {}).items():
            if param in params:
                validated[param] = params[param]
            elif param in self.required_params:
                raise ValueError(f"Missing required parameter: {param}")
        return validated

    async def call_async(self, **kwargs: Any) -> Any:
        """Async implementation of OpenAPI tool call."""
        validated_params = self._validate_params(kwargs)

        async with httpx.AsyncClient() as client:
            if self.method == "get":
                response = await client.get(
                    f"{self.base_url}{self.path}", params=validated_params
                )
            else:
                response = await client.request(
                    self.method, f"{self.base_url}{self.path}", json=validated_params
                )

            response.raise_for_status()
            return response.json()

    def call_sync(self, **kwargs: Any) -> Any:
        """Synchronous implementation of OpenAPI tool call."""
        validated_params = self._validate_params(kwargs)

        with httpx.Client() as client:
            if self.method == "get":
                response = client.get(
                    f"{self.base_url}{self.path}", params=validated_params
                )
            else:
                response = client.request(
                    self.method, f"{self.base_url}{self.path}", json=validated_params
                )

            response.raise_for_status()
            return response.json()

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the wrapper directly callable, using sync version by default."""
        return self.call_sync(**kwargs)

    async def __acall__(self, *args: Any, **kwargs: Any) -> Any:
        """Async version of __call__, allows await wrapper() syntax."""
        return await self.call_async(**kwargs)


class OpenAPITool(Tool):
    """Wrapper class for OpenAPI tools that preserves original function metadata."""

    @classmethod
    def from_openapi_spec(
        cls, base_url: str, path: str, method: str, spec: Dict[str, Any]
    ) -> "OpenAPITool":
        """Create an OpenAPITool from OpenAPI specification."""
        operation_id = spec.get("operationId", f'{method}_{path.replace("/", "_")}')
        description = spec.get("description", spec.get("summary", ""))

        # Convert OpenAPI parameters to function parameters schema
        parameters = {"type": "object", "properties": {}, "required": []}

        # Handle path/query parameters
        for param in spec.get("parameters", []):
            param_schema = param.get("schema", {})
            parameters["properties"][param["name"]] = {
                "type": param_schema.get("type", "string"),
                "description": param.get("description", ""),
            }
            if param.get("required", False):
                parameters["required"].append(param["name"])

        # Handle request body
        if "requestBody" in spec:
            content = spec["requestBody"].get("content", {})
            if "application/json" in content:
                schema = content["application/json"].get("schema", {})
                for prop_name, prop_schema in schema.get("properties", {}).items():
                    parameters["properties"][prop_name] = {
                        "type": prop_schema.get("type", "string"),
                        "description": prop_schema.get("description", ""),
                    }
                if "required" in schema:
                    parameters["required"].extend(schema["required"])

        wrapper = OpenAPIToolWrapper(
            base_url=base_url,
            name=operation_id,
            method=method,
            path=path,
            params_schema=parameters,
        )

        return cls(
            name=operation_id,
            description=description,
            parameters=parameters,
            callable=wrapper,
            is_async=False,
        )


class OpenAPIIntegration:
    """Handles integration with OpenAPI services for tool registration."""

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    async def register_openapi_tools_async(self, openapi_url: str) -> None:
        """
        Async implementation to register all tools from an OpenAPI specification.

        Args:
            openapi_url: URL to fetch OpenAPI specification (e.g. "http://localhost:8000/openapi.json")
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(openapi_url)
            response.raise_for_status()
            openapi_spec = response.json()

            base_url = openapi_spec.get("servers", [{}])[0].get("url", "")

            for path, methods in openapi_spec.get("paths", {}).items():
                for method, spec in methods.items():
                    if method.lower() not in ["get", "post", "put", "delete"]:
                        continue

                    tool = OpenAPITool.from_openapi_spec(
                        base_url=base_url, path=path, method=method, spec=spec
                    )
                    self.registry.register(tool)

    def register_openapi_tools(self, openapi_url: str) -> None:
        """
        Register all tools from an OpenAPI specification (synchronous entry point).

        Args:
            openapi_url: URL to fetch OpenAPI specification
        """
        import asyncio

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        if loop.is_running():
            future = asyncio.run_coroutine_threadsafe(
                self.register_openapi_tools_async(openapi_url), loop
            )
            return future.result()
        else:
            return loop.run_until_complete(
                self.register_openapi_tools_async(openapi_url)
            )
