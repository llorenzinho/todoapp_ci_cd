from pydantic import BaseModel

API_VERSION = "0.0.1"

class ApiVersionOutDTO(BaseModel):
    version: str

def get_api_version() -> ApiVersionOutDTO:
    return ApiVersionOutDTO(version=API_VERSION)
