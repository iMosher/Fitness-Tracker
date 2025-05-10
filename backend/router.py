from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/health")
async def health():
    return {"status": "healthy"}

  
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
