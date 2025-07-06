from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    record_to_be_added = {"id": id, "name": name, "contact_details": contact_details}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res


async def put_users_id(db: Session, id: int, name: str, contact_details: str):

    query = db.query(models.Users)
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_details": contact_details,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_appointments(db: Session):

    query = db.query(models.Appointments)

    appointments_all = query.all()
    appointments_all = (
        [new_data.to_dict() for new_data in appointments_all]
        if appointments_all
        else appointments_all
    )
    res = {
        "appointments_all": appointments_all,
    }
    return res


async def get_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)

    appointments_one = query.first()

    appointments_one = (
        (
            appointments_one.to_dict()
            if hasattr(appointments_one, "to_dict")
            else vars(appointments_one)
        )
        if appointments_one
        else appointments_one
    )

    res = {
        "appointments_one": appointments_one,
    }
    return res


async def post_appointments(db: Session, raw_data: schemas.PostAppointments):
    id: int = raw_data.id
    user_id: int = raw_data.user_id
    appointment_type_id: int = raw_data.appointment_type_id
    date: datetime.date = raw_data.date
    time: str = raw_data.time
    duration: int = raw_data.duration
    description: str = raw_data.description
    calendar_id: str = raw_data.calendar_id
    event_id: str = raw_data.event_id

    record_to_be_added = {
        "id": id,
        "date": date,
        "time": time,
        "user_id": user_id,
        "duration": duration,
        "event_id": event_id,
        "calendar_id": calendar_id,
        "description": description,
        "appointment_type_id": appointment_type_id,
    }
    new_appointments = models.Appointments(**record_to_be_added)
    db.add(new_appointments)
    db.commit()
    db.refresh(new_appointments)
    appointments_inserted_record = new_appointments.to_dict()

    res = {
        "appointments_inserted_record": appointments_inserted_record,
    }
    return res


async def put_appointments_id(
    db: Session,
    id: int,
    user_id: int,
    appointment_type_id: int,
    date: str,
    time: str,
    duration: int,
    description: str,
    calendar_id: str,
    event_id: str,
):

    query = db.query(models.Appointments)
    appointments_edited_record = query.first()

    if appointments_edited_record:
        for key, value in {
            "id": id,
            "date": date,
            "time": time,
            "user_id": user_id,
            "duration": duration,
            "event_id": event_id,
            "calendar_id": calendar_id,
            "description": description,
            "appointment_type_id": appointment_type_id,
        }.items():
            setattr(appointments_edited_record, key, value)

        db.commit()
        db.refresh(appointments_edited_record)

        appointments_edited_record = (
            appointments_edited_record.to_dict()
            if hasattr(appointments_edited_record, "to_dict")
            else vars(appointments_edited_record)
        )
    res = {
        "appointments_edited_record": appointments_edited_record,
    }
    return res


async def delete_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        appointments_deleted = record_to_delete.to_dict()
    else:
        appointments_deleted = record_to_delete
    res = {
        "appointments_deleted": appointments_deleted,
    }
    return res


async def get_appointment_types(db: Session):

    query = db.query(models.AppointmentTypes)

    appointment_types_all = query.all()
    appointment_types_all = (
        [new_data.to_dict() for new_data in appointment_types_all]
        if appointment_types_all
        else appointment_types_all
    )
    res = {
        "appointment_types_all": appointment_types_all,
    }
    return res


async def get_appointment_types_id(db: Session, id: int):

    query = db.query(models.AppointmentTypes)

    appointment_types_one = query.first()

    appointment_types_one = (
        (
            appointment_types_one.to_dict()
            if hasattr(appointment_types_one, "to_dict")
            else vars(appointment_types_one)
        )
        if appointment_types_one
        else appointment_types_one
    )

    res = {
        "appointment_types_one": appointment_types_one,
    }
    return res


async def post_appointment_types(db: Session, raw_data: schemas.PostAppointmentTypes):
    id: int = raw_data.id
    name: str = raw_data.name

    record_to_be_added = {"id": id, "name": name}
    new_appointment_types = models.AppointmentTypes(**record_to_be_added)
    db.add(new_appointment_types)
    db.commit()
    db.refresh(new_appointment_types)
    appointment_types_inserted_record = new_appointment_types.to_dict()

    res = {
        "appointment_types_inserted_record": appointment_types_inserted_record,
    }
    return res


async def put_appointment_types_id(db: Session, id: int, name: str):

    query = db.query(models.AppointmentTypes)
    appointment_types_edited_record = query.first()

    if appointment_types_edited_record:
        for key, value in {"id": id, "name": name}.items():
            setattr(appointment_types_edited_record, key, value)

        db.commit()
        db.refresh(appointment_types_edited_record)

        appointment_types_edited_record = (
            appointment_types_edited_record.to_dict()
            if hasattr(appointment_types_edited_record, "to_dict")
            else vars(appointment_types_edited_record)
        )
    res = {
        "appointment_types_edited_record": appointment_types_edited_record,
    }
    return res


async def delete_appointment_types_id(db: Session, id: int):

    query = db.query(models.AppointmentTypes)

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        appointment_types_deleted = record_to_delete.to_dict()
    else:
        appointment_types_deleted = record_to_delete
    res = {
        "appointment_types_deleted": appointment_types_deleted,
    }
    return res
