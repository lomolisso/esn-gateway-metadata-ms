import pytz
from app.db import Base

from sqlalchemy import Boolean, Column
from sqlalchemy.types import String, DateTime, Integer

from datetime import datetime
from app.core.config import TIMEZONE


def tz_now():
    tz = pytz.timezone(TIMEZONE)
    return datetime.now(tz)

class EdgeSensor(Base):
    """
    Edge sensor table

    Attributes:
    id: Integer, primary key
    device_name: String, name of the edge sensor
    device_address: String, address of the edge sensor
    provisioned: Boolean, whether the edge sensor is provisioned or not
    registered_at: DateTime, timestamp when the edge sensor was registered in the database.
    """

    __tablename__ = "edge_sensor_table"

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String(50), nullable=False, unique=True)
    device_address = Column(String(50), nullable=False, unique=True)
    provisioned = Column(Boolean, default=False)
    registered_at = Column(DateTime, default=tz_now)
