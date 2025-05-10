"""
A workout session which can have a single Workout
"""

import uuid
from datetime import datetime
from backend.models.Workout import Workout


class Session:
    """
    A class representing a workout session.

    Attributes:
      id (str): A unique identifier for the session, generated using UUID.
      workout_id (str): The ID of the associated workout.
      date (datetime): The date and time of the session. Defaults to the current UTC time.

    Methods:
      add():
        Simulates adding the session to a database or list.
      delete():
        Simulates deleting the session.
      __str__():
        Returns a string representation of the session instance.
    """
    def __init__(
        self,
        workout: Workout,
        date: datetime = None
    ):
        self.id = str(uuid.uuid4())  # Unique identifier
        self.workout = workout
        self.date = date or datetime.timezone.utcnow()

    def add(self):
        # Simulate adding the session to a database or list
        print(f"Session '{self.id}' added successfully!")

    def delete(self):
        # Simulate deleting the session
        print(f"Session '{self.id}' deleted successfully!")

    def __str__(self):
        return (
            f"Session(id={self.id}, workout_id='{self.workout_id}', "
            f"date={self.date})"
        )
