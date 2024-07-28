from app.db import models

from sqlalchemy.orm import Session
from sqlalchemy import select, update

# --- Exception classes ---
class EdgeSensorNotFound(Exception):
    def __init__(self, message="Edge sensor not found."):
        self.message = message
        super().__init__(self.message)

class EdgeSensorAlreadyExists(Exception):
    def __init__(self, message="Edge sensor already exists."):
        self.message = message
        super().__init__(self.message)


# --- CRUD methods for EdgeSensor ---

def read_edge_sensors(session: Session, paginate=False, page=0, page_size=10) -> list[models.EdgeSensor]:
    query = select(models.EdgeSensor)
    if paginate:
        query = query.offset(page).limit(page_size)
    result = session.execute(query)

    return result.scalars().all()

def read_edge_sensor(session: Session, device_name: str) -> models.EdgeSensor:
    query = select(models.EdgeSensor).where(
        models.EdgeSensor.device_name == device_name
    )
    result = session.execute(query).scalars().first()

    # Check if the edge sensor exists
    if not result:
        raise EdgeSensorNotFound
    
    return result

def create_edge_sensor(session: Session, fields: dict):
    device_name = fields["device_name"]
    query = select(models.EdgeSensor).where(
        models.EdgeSensor.device_name == device_name
    )
    result = session.execute(query).scalars().first()
    if result:
        raise EdgeSensorAlreadyExists
    
    db_instance = models.EdgeSensor(**fields)
    session.add(db_instance)
    session.commit()
    session.refresh(db_instance)
    
def update_edge_sensor(session: Session, device_name: str, fields: dict):
    # Check if the device_name is the same
    assert fields["device_name"] == device_name

    # Check if the edge sensor exists
    read_edge_sensor(session=session, device_name=device_name)

    query = update(models.EdgeSensor).where(
        models.EdgeSensor.device_name == device_name
    ).values(fields)
    session.execute(query)
    session.commit()

def delete_edge_sensor(session: Session, device_name: str):
    # Check if the edge sensor exists
    sensor = read_edge_sensor(session=session, device_name=device_name)

    session.delete(sensor)
    session.commit()

