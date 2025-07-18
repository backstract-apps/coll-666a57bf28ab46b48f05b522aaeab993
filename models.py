from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Users(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    name = Column(String, primary_key=False)
    contact_details = Column(String, primary_key=False)


class Appointments(Base):
    __tablename__ = 'appointments'
    id = Column(String, primary_key=True)
    user_id = Column(Integer, primary_key=False)
    appointment_type_id = Column(Integer, primary_key=False)
    date = Column(Date, primary_key=False)
    time = Column(Time, primary_key=False)
    duration = Column(Integer, primary_key=False)
    description = Column(String, primary_key=False)
    calendar_id = Column(String, primary_key=False)
    event_id = Column(String, primary_key=False)


class AppointmentTypes(Base):
    __tablename__ = 'appointment_types'
    id = Column(String, primary_key=True)
    name = Column(String, primary_key=False)


