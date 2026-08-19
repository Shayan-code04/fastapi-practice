from database import SessionLocal

from crud import (
    create_user,
    get_user_by_email,
    create_job,
    get_jobs_by_user,
    update_job_status,
    delete_job
)


db = SessionLocal()

try:

    # CREATE USER
    user = create_user(
        db,
        "test@gmail.com",
        "1234"
    )

    print("Created user:", user.email)
    print("User ID:", user.id)


    # GET USER
    found_user = get_user_by_email(
        db,
        "test@gmail.com"
    )

    print("Found user:", found_user.email)


    # CREATE JOB
    job = create_job(
        db,
        user.id,
        "Google",
        "Software Engineer"
    )

    print("Created job:", job.company)
    print("Job ID:", job.id)
    print("Job status:", job.status)


    # GET JOBS
    jobs = get_jobs_by_user(
        db,
        user.id
    )

    print("Number of jobs:", len(jobs))


    # UPDATE JOB
    updated_job = update_job_status(
        db,
        job.id,
        "Interview"
    )

    print("Updated status:", updated_job.status)


    # DELETE JOB
    deleted_job = delete_job(
        db,
        job.id
    )

    print("Deleted job:", deleted_job.id)


finally:
    db.close()