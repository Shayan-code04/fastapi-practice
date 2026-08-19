from database import engine, Base
from models import User, Job


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")