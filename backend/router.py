from fastapi import APIRouter

router = APIRouter()

@router.get("/logworkout")
def logWorkout():
    return{
        "message": "this is where workouts will be logged"
    }

@router.get('/viewworkout')
def viewWorkout():
    return {
        "message" : "view workouts here"
    }