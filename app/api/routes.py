
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from app.db import crud
from app.api import schemas
from app.api.dependencies import get_session

router = APIRouter()

    
# --- Edge Sensor ---

@router.get("/sensors", status_code=status.HTTP_200_OK, tags=["Edge Sensor"])
async def read_edge_sensors(session: Session = Depends(get_session)) -> list[schemas.ReadEdgeSensor]:
    """
    GET /sensor endpoint

    Endpoint to return all edge sensors.
    """
    return crud.read_edge_sensors(session=session)

@router.get("/sensor/{sensor_name}", status_code=status.HTTP_200_OK, tags=["Edge Sensor"])
async def read_edge_sensor(sensor_name: str, session: Session = Depends(get_session)) -> Optional[schemas.ReadEdgeSensor]:
    """
    GET /sensor/{sensor_name} endpoint

    Endpoint to return a specific edge sensor.
    """

    try:
        return crud.read_edge_sensor(session=session, device_name=sensor_name)
    except crud.EdgeSensorNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Edge sensor not found")
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something went wrong")

@router.post("/sensor", status_code=status.HTTP_201_CREATED, tags=["Edge Sensor"])
async def create_edge_sensor(sensor: schemas.CreateEdgeSensor, session: Session = Depends(get_session)):
    """
    POST /sensor endpoint

    Endpoint to create a new edge sensor.
    """
    
    try:
        crud.create_edge_sensor(session=session, fields=sensor.model_dump())
    except crud.EdgeSensorAlreadyExists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Edge sensor already exists")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something went wrong")
    
@router.put("/sensor/{sensor_name}", status_code=status.HTTP_200_OK, tags=["Edge Sensor"])
async def update_edge_sensor(sensor_name: str, sensor: schemas.UpdateEdgeSensor, session: Session = Depends(get_session)):
    """
    PUT /sensor endpoint

    Endpoint to update an existing edge sensor.
    """
    
    try:
        crud.update_edge_sensor(session=session, device_name=sensor_name, fields=sensor.model_dump())
    except crud.EdgeSensorNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Edge sensor not found")
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something went wrong")

@router.delete("/sensor/{sensor_name}", status_code=status.HTTP_200_OK, tags=["Edge Sensor"])
async def delete_edge_sensor(sensor_name: str, session: Session = Depends(get_session)):
    """
    DELETE /sensor/{sensor_name} endpoint

    Endpoint to delete an existing edge sensor.
    """
    
    try:
        crud.delete_edge_sensor(session=session, device_name=sensor_name)
    except crud.EdgeSensorNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Edge sensor not found")
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something went wrong")

