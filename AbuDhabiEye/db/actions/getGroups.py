import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch database credentials from environment variables
ENDPOINT = os.getenv("AWS_RDS_ENDPOINT")
USER = os.getenv("AWS_RDS_USER")
PASSWORD = os.getenv("AWS_RDS_PASSWORD")
DATABASE = os.getenv("AWS_RDS_DATABASE")
PORT = 3306

def getAllTravelGroups():
    connection = pymysql.connect(
        host=ENDPOINT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        port=PORT,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    
    try:
        with connection.cursor() as cursor:
            # Retrieve all entries from the travel_groups table
            cursor.execute("SELECT * FROM travel_groups")
            travel_groups = cursor.fetchall()
            return travel_groups

    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
        raise
