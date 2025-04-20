from pydantic import BaseModel, Field
from typing import List, Optional

class Param(BaseModel):
    """
    Model for the parameters associated with an endpoint.
    """
    name: str
    value: str
    process_status: Optional[str] = Field(default="pending", description="Status of the parameter processing")

class Endpoint(BaseModel):
    """
    Model for the endpoint details.
    """
    url: str
    params: List[Param] = []  # List of parameters associated with the endpoint
    status: Optional[str] = None  # Status of the URL (e.g., 'active', 'inactive', 'error')
    length: Optional[int] = None  # Length of the response body
    process_status: Optional[str] = Field(default="pending", description="Status of the URL processing")

class Response(BaseModel):
    """
    Model for storing responses.
    """
    url: str
    status_code: int
    response_body: Optional[str] = None  # Response content, if needed
    timestamp: Optional[str] = None  # Timestamp when the response was received
    process_status: Optional[str] = Field(default="pending", description="Status of the response processing")

class Domain(BaseModel):
    """
    Model for a domain, containing all the endpoints and parameters.
    """
    domain_name: str
    endpoints: List[Endpoint] = []
    responses: List[Response] = []

    class Config:
        # To allow MongoDB to serialize the data
        arbitrary_types_allowed = True
