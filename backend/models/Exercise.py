"""
Class representing an exercise in a workout program.
This class is used to define the properties and methods associated with an exercise.
It includes attributes such as name, description, duration
"""

import uuid
from datetime import datetime


class Exercise:
    """
    A class representing an exercise in a workout program.

    Attributes:
      id (str): A unique identifier for the exercise, generated using UUID.
      name (str): The name of the exercise.
      description (str): A brief description of the exercise.

    Methods:
      add():
        Simulates adding the exercise to a database or list.
      delete():
        Simulates deleting the exercise.
      __str__():
        Returns a string representation of the exercise instance.
    """
    def __init__(
        self,
        name: str,
        description: str,
        duration_minutes: int = 0,
        weight: float = 0,
        sets: float = 0,
        reps: float = 0,
    ):
        self.id = str(uuid.uuid4())  # Unique identifier
        self.name = name
        self.description = description
        self.duration_minutes = duration_minutes

    def add(self):
        # Simulate adding the exercise to a database or list
        print(f"Exercise '{self.name}' added successfully!")

    def delete(self):
        # Simulate deleting the exercise
        print(f"Exercise '{self.name}' deleted successfully!")

    def __str__(self):
        return (
            f"Exercise(id={self.id}, name='{self.name}', "
            f"description='{self.description}', "
            f"duration_minutes={self.duration_minutes}, "
            f"date={self.date})"
        )
