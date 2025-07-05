from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    id: Any
    name: str
    contact_details: str


class ReadUsers(BaseModel):
    id: Any
    name: str
    contact_details: str
    class Config:
        from_attributes = True


class Appointments(BaseModel):
    id: Any
    user_id: int
    appointment_type_id: int
    date: datetime.date
    time: datetime.time
    duration: int
    description: str
    calendar_id: str
    event_id: str


class ReadAppointments(BaseModel):
    id: Any
    user_id: int
    appointment_type_id: int
    date: datetime.date
    time: datetime.time
    duration: int
    description: str
    calendar_id: str
    event_id: str
    class Config:
        from_attributes = True


class AppointmentTypes(BaseModel):
    id: Any
    name: str


class ReadAppointmentTypes(BaseModel):
    id: Any
    name: str
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    contact_details: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostAppointments(BaseModel):
    id: int = Field(...)
    user_id: int = Field(...)
    appointment_type_id: int = Field(...)
    date: Any = Field(...)
    time: str = Field(..., max_length=100)
    duration: int = Field(...)
    description: str = Field(..., max_length=100)
    calendar_id: str = Field(..., max_length=100)
    event_id: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostAppointmentTypes(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

