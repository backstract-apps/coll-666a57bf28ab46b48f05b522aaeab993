from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(id: int, name: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, id, name, contact_details)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/')
async def get_appointments(db: Session = Depends(get_db)):
    try:
        return await service.get_appointments(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/id')
async def get_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_appointments_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/appointments/')
async def post_appointments(raw_data: schemas.PostAppointments, db: Session = Depends(get_db)):
    try:
        return await service.post_appointments(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/appointments/id/')
async def put_appointments_id(id: int, user_id: int, appointment_type_id: int, date: str, time: Annotated[str, Query(max_length=100)], duration: int, description: Annotated[str, Query(max_length=100)], calendar_id: Annotated[str, Query(max_length=100)], event_id: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_appointments_id(db, id, user_id, appointment_type_id, date, time, duration, description, calendar_id, event_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/appointments/id')
async def delete_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_appointments_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointment_types/')
async def get_appointment_types(db: Session = Depends(get_db)):
    try:
        return await service.get_appointment_types(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointment_types/id')
async def get_appointment_types_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_appointment_types_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/appointment_types/')
async def post_appointment_types(raw_data: schemas.PostAppointmentTypes, db: Session = Depends(get_db)):
    try:
        return await service.post_appointment_types(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/appointment_types/id/')
async def put_appointment_types_id(id: int, name: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_appointment_types_id(db, id, name)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/appointment_types/id')
async def delete_appointment_types_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_appointment_types_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

