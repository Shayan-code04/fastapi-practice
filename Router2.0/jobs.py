from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from database import get_db
from schemas import JobCreate, JobResponse


router = APIRouter()


@router.post("/jobs", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(
        db,
        job.user_id,
        job.company,
        job.role
    )


@router.get("/jobs", response_model=list[JobResponse])
def get_jobs(user_id: int, db: Session = Depends(get_db)):
    return crud.get_jobs_by_user(db, user_id)