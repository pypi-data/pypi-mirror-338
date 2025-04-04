from pydantic import BaseModel, Field
from typing import Callable, Any, Awaitable, Dict
from mcp.types import ReadResourceResult, Resource, PromptMessage, ServerCapabilities

class Config(BaseModel):
	warn_on_duplicates: bool = Field(description="warn on duplicates", default=False)
	capabilities: ServerCapabilities = Field(description="capabilities of mcp")
	name: str
	version: str

class Tool(BaseModel):
	name: str = Field(description="name of tool")
	description: str = Field(description="description of tool")
	input_schema: dict[str, Any] = Field(description="input schema of tool")
	fn: Callable[..., Any] = Field(description="callable function of tool")

class ToolCall(BaseModel):
	name: str = Field(description="name")
	arguments: Dict[str, Any] = Field(description="arguments")

class ResourceModel(BaseModel):
	uri: str = Field(description="uri of resource")
	name: str = Field(description="name of resource")
	description: str = Field(description="description of resource")
	mime_type: str = Field(description="mime type of resource")
	size: int | None = Field(description="size of resource", default=None)
	read_fn: Callable[[str], Awaitable[list[ReadResourceResult]]] = Field(description="read function of resource")
	list_fn: Callable[..., list[Resource]] = Field(description="list function of resource")

class ArgumentModel(BaseModel):
	name: str = Field(description="name of argument")
	description: str = Field(description="description of argument")
	required: bool = Field(description="required or not", default=False)

class PromptModel(BaseModel):
	name: str = Field(description="name of prompt")
	description: str = Field(description="description of prompt")
	arguments: list[ArgumentModel] = Field(description="list of arguments")
	prompt_fn: Callable[[Dict[str, str]], list[PromptMessage]] = Field(description="function to get prompt")

class PromptRequest(BaseModel):
    name: str
    arguments: Dict[str, str]