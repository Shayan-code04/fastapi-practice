from sqlalchemy.orm import Session

from models import User, Job


def create_user(db: Session, email: str, password: str):
    user = User(
        email=email,
        password=password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_job(
    db: Session,
    user_id: int,
    company: str,
    role: str
):
    job = Job(
        user_id=user_id,
        company=company,
        role=role
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def get_jobs_by_user(db: Session, user_id: int):
    return db.query(Job).filter(Job.user_id == user_id).all()


def update_job_status(
    db: Session,
    job_id: int,
    new_status: str
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if job is None:
        return None

    job.status = new_status

    db.commit()
    db.refresh(job)

    return job


def delete_job(db: Session, job_id: int):
    job = db.query(Job).filter(Job.id == job_id).first()

    if job is None:
        return None

    db.delete(job)
    db.commit()

    return job