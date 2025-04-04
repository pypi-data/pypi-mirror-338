from mcp.types import (
    EmbeddedResource,
    ImageContent,
    TextContent,
)
from collections.abc import Sequence
from mcp.server.fastmcp.utilities.types import Image
from mcp.server.lowlevel.helper_types import ReadResourceContents
import json
import pydantic_core
from typing import Any

def _convert_to_content(
    result: Any,
) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """Convert a result to a sequence of content objects."""
    if result is None:
        return []

    if isinstance(result, TextContent | ImageContent | EmbeddedResource):
        return [result]

    if isinstance(result, Image):
        return [result.to_image_content()]

    if isinstance(result, list | tuple):
        return list(chain.from_iterable(_convert_to_content(item) for item in result))  # type: ignore[reportUnknownVariableType]

    if not isinstance(result, str):
        try:
            result = json.dumps(pydantic_core.to_jsonable_python(result))
        except Exception:
            result = str(result)

    return [TextContent(type="text", text=result)]

def _convert_to_read_resource(result: Any) -> list[ReadResourceContents]:
    if result is None:
        return []
    
    if isinstance(result, ReadResourceContents):
        return [result]
    
    if "blob" in result:
        # Assuming blob is base64-encoded; decode to bytes
        import base64
        try:
            content = base64.b64decode(result["blob"])
        except Exception:
            content = b"[Binary data could not be decoded]"
        return [ReadResourceContents(
            content=content,
            mime_type=result["mimeType"]
        )]
    
    if "text" in result:
        return [ReadResourceContents(
            content=result["text"],
            mime_type=result["mimeType"]
        )]
    
    return [ReadResourceContents(
        content=result["text"],
        mime_type=result["mimeType"]
    )]

def _convert_to_prompt_message_content(
    result: Any,
) -> TextContent | ImageContent | EmbeddedResource:
	"""Convert a result to a sequence of content objects."""
	if result is None:
		return None

	if isinstance(result, TextContent | ImageContent | EmbeddedResource):
		return result

	if result["type"] == "image":
		return result.to_image_content()

	if isinstance(result, list | tuple):
		raise ValueError("result cannot be a list, it should be Content")
	
	if result["type"] == "text":
		return TextContent(type="text", text=result["text"])

	if not isinstance(result, str):
		try:
			result = json.dumps(pydantic_core.to_jsonable_python(result))
		except Exception:
			result = str(result)

	return TextContent(type="text", text=result)