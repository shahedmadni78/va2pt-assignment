import os
import psycopg2
from psycopg2 import sql

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://shahed:shahed123@db:5432/projectdb")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)
