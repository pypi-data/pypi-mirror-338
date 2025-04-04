#from pydantic import BaseModel, Field
from typing import TypedDict

class ClientConfig(TypedDict):
	server_url: str