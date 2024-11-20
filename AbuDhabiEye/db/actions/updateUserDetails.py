import os
from dotenv import load_dotenv
import pymysql
# Load environment variables from .env file
load_dotenv()

# Fetch database credentials from environment variables
ENDPOINT = os.getenv("AWS_RDS_ENDPOINT")
USER = os.getenv("AWS_RDS_USER")
PASSWORD = os.getenv("AWS_RDS_PASSWORD")
DATABASE = os.getenv("AWS_RDS_DATABASE")
PORT = 3306


def updateUserDetails(details):
    connection = pymysql.connect(
        host=ENDPOINT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        port=PORT,  # Ensure the port is correctly included
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    cursor = connection.cursor()

    # Extract values from the JSON object
    username = details.get("username", "")
    email = details.get("email", "")
    phone = details.get("phone", "")
    age = details.get("age", None)
    language = details.get("language", "")
    nationality = details.get("nationality", "")
    gender = details.get("gender", "")
    travel_preference = details.get("travel_preference", "")
    culture = details.get("culture", "")
    cuisine = details.get("cuisine", "")
    shopping = details.get("shopping", "")
    adventure_activities = details.get("adventure_activities", "")
    profile_img = details.get("profile_img", "")

    try:
        if not email:
            raise ValueError("Email is required to update user details.")

        # Dynamically build the SET clause for fields that are not empty or None
        update_fields = []
        update_values = []

        if username:
            update_fields.append("username = %s")
            update_values.append(username)
        if phone:
            update_fields.append("phone = %s")
            update_values.append(phone)
        if age is not None:
            update_fields.append("age = %s")
            update_values.append(age)
        if language:
            update_fields.append("language = %s")
            update_values.append(language)
        if nationality:
            update_fields.append("nationality = %s")
            update_values.append(nationality)
        if gender:
            update_fields.append("gender = %s")
            update_values.append(gender)
        if travel_preference:
            update_fields.append("travel_preference = %s")
            update_values.append(travel_preference)
        if culture:
            update_fields.append("culture = %s")
            update_values.append(culture)
        if cuisine:
            update_fields.append("cuisine = %s")
            update_values.append(cuisine)
        if shopping:
            update_fields.append("shopping = %s")
            update_values.append(shopping)
        if adventure_activities:
            update_fields.append("adventure_activities = %s")
            update_values.append(adventure_activities)
        if profile_img:
            update_fields.append("profile_img = %s")
            update_values.append(profile_img)

        if not update_fields:
            raise ValueError("No fields to update.")

        # Add email for WHERE clause
        update_values.append(email)

        # Generate SQL query dynamically
        query = f"UPDATE user_details SET {', '.join(update_fields)} WHERE email = %s"

        # Execute the query
        cursor.execute(query, update_values)

        # Commit the transaction to save changes
        connection.commit()

        return {"email": email, "username": username}

    except Exception as e:
        return {"status": "error", "message": str(e)}

