import uuid
from datetime import datetime


class Workout:
    """
    A class representing a workout session.

    Attributes:
      id (str): A unique identifier for the workout, generated using UUID.
      name (str): The name of the workout.
      description (str): A brief description of the workout.
      duration_minutes (int): The duration of the workout in minutes.
      date (datetime): The date and time of the workout. Defaults to the current UTC time.

    Methods:
      add():
        Simulates adding the workout to a database or list.
      delete():
        Simulates deleting the workout.
      __str__():
        Returns a string representation of the workout instance.
    """
    def __init__(
        self,
        name: str,
        description: str,
        duration_minutes: int,
        date: datetime = None
    ):
        self.id = str(uuid.uuid4())  # Unique identifier
        self.name = name
        self.description = description
        self.duration_minutes = duration_minutes
        self.date = date or datetime.timezone.utcnow()

    def add(self):
        # Simulate adding the workout to a database or list
        print(f"Workout '{self.name}' added successfully!")

    def delete(self):
        # Simulate deleting the workout
        print(f"Workout '{self.name}' deleted successfully!")

    def __str__(self):
        return (
            f"Workout(id={self.id}, name='{self.name}', "
            f"description='{self.description}', "
            f"duration_minutes={self.duration_minutes}, "
            f"date={self.date})"
        )
