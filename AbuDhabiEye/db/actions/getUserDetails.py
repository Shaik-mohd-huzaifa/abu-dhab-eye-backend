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

def getUserDetailsfromDB(username, email):
    connection = pymysql.connect(
        host=ENDPOINT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        port=PORT,  # Ensure the port is correctly included
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        # Use a context manager for the cursor
        with connection.cursor() as cursor:
            # Check if the user already exists
            cursor.execute("SELECT * FROM user_details WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user:
                return user

            # Insert new user if not found
            cursor.execute(
    """
    INSERT INTO user_details 
    (username, email, phone, language, nationality, gender, travel_preference, culture, cuisine, shopping, adventure_activities, profile_img, age)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, 
    (username, email, "", "", "", "", "", "", "", "", "", "", "")
)

            connection.commit()

            # Retrieve the newly inserted user
            cursor.execute("SELECT * FROM user_details WHERE email = %s", (email,))
            return cursor.fetchone()

    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
        raise

    # No explicit cursor.close() needed with `with` statement
