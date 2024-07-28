from datetime import datetime
from pydantic import BaseModel
from typing import Optional

# --- Device Schemas ---
class BaseDeviceSchema(BaseModel):
    """
    Basic device schema.
    """
    device_name: str

class CreateEdgeSensor(BaseDeviceSchema):
    """
    Schema for creating an edge sensor.
    """
    device_address: str

class UpdateEdgeSensor(BaseDeviceSchema):
    """
    Schema for updating an edge sensor.
    """

    device_address:  Optional[str] = None
    provisioned: Optional[bool] = None

class ReadEdgeSensor(BaseDeviceSchema):
    """
    Schema for returning an edge sensor.
    """

    device_address: str
    provisioned: bool

    class Config:
        from_attributes = True
