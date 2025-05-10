import uuid
from datetime import datetime
from backend.models.Exercise import Exercise  # Assuming Exercise is defined in Exercise.py


class Workout:
    """
    A class representing a workout session.

    Attributes:
      id (str): A unique identifier for the workout, generated using UUID.
      name (str): The name of the workout.
      description (str): A brief description of the workout.
      duration_minutes (int): The duration of the workout in minutes.
      date (datetime): The date and time of the workout. Defaults to the current UTC time.
      exercises (list): A list of exercises associated with the workout.

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
        date: datetime = None,
        exercises: list[Exercise] = None  # Optional for initialization
    ):
        self.id = str(uuid.uuid4())  # Unique identifier
        self.name = name
        self.description = description
        self.duration_minutes = duration_minutes
        self.date = date or datetime.timezone.utcnow()
        self.exercises = exercises or None

    def add(self):
        # Simulate adding the workout to a database or list
        print(f"Workout '{self.name}' added successfully!")

    def delete(self):
        # Simulate deleting the workout
        print(f"Workout '{self.name}' deleted successfully!")

    def add_exercise(self, exercise):
        """
        Adds an exercise to the workout.

        Args:
          exercise (Exercise): The exercise to be added.
        """
        self.exercises.append(exercise)
        print(f"Exercise '{exercise.name}' added to workout '{self.name}'.")

    def remove_exercise(self, exercise):
        """
        Removes an exercise from the workout.

        Args:
          exercise (Exercise): The exercise to be removed.
        """
        self.exercises.remove(exercise)
        print(f"Exercise '{exercise.name}' removed from workout '{self.name}'.")

    def get_exercises(self):
        """
        Returns the list of exercises in the workout.

        Returns:
          list: A list of exercises associated with the workout.
        """
        return self.exercises

    def __str__(self):
        return (
            f"Workout(id={self.id}, name='{self.name}', "
            f"description='{self.description}', "
            f"duration_minutes={self.duration_minutes}, "
            f"date={self.date})"
        )
