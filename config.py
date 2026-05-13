import os
from pymongo import MongoClient
import gridfs

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
MONGODB_DB_NAME = "job_portal_db"

# Initialize MongoDB Client
client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]

# GridFS for file storage
fs = gridfs.GridFS(db)

# Database Collections
collections = {
    "users": db.users,
    "candidates": db.candidates,
    "companies": db.companies,
    "jobs": db.jobs,
    "applications": db.applications,
    "admin": db.admin,
    "contacts": db.contacts
}

def get_db():
    """Get database instance"""
    return db

def close_db():
    """Close database connection"""
    client.close()
