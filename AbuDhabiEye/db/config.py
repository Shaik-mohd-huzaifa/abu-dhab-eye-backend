# import os
# import pymysql.cursors
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Fetch database credentials from environment variables
# ENDPOINT = os.getenv("AWS_RDS_ENDPOINT")
# USER = os.getenv("AWS_RDS_USER")
# PASSWORD = os.getenv("AWS_RDS_PASSWORD")
# DATABASE = os.getenv("AWS_RDS_DATABASE")
# PORT = 3306

# # USER = "admin"      # AWS RDS MySQL username
# # PASSWORD = "x#Kp3WL.2xWg8Tg"      # AWS RDS MySQL password
# # ENDPOINT = "zest-healthcare-chatapp.c5um0awogh52.us-east-1.rds.amazonaws.com"      # AWS RDS endpoint (e.g., example.abcdefghij.us-west-2.rds.amazonaws.com)
# # PORT = 3306 
# # DATABASE = "abuDhabiEye" 

# # Establish connection to the MySQL database
# try:
#     connection = pymysql.connect(
#         host=ENDPOINT,
#         user=USER,
#         password=PASSWORD,
#         database=DATABASE,
#         port=PORT,  # Ensure the port is correctly included
#         charset="utf8mb4",
#         cursorclass=pymysql.cursors.DictCursor,
#     )

#     print("Connection Established")

#     # Use a cursor to interact with the database
#     with connection.cursor() as cursor:
#         # Define your SQL query here
#         # Example: cursor.execute("SELECT * FROM your_table;")
        
#         # Fetch some data (example)
#         cursor.execute("SELECT VERSION();")
#         version = cursor.fetchone()
#         print("Database Version:", version)

#         # Commit any changes if necessary
#         connection.commit()

# except pymysql.MySQLError as e:
#     print("Error while connecting to MySQL:", e)
