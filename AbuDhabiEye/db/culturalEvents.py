eventsSchema = """CREATE TABLE cultural_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL,
    event_description TEXT NOT NULL,
    event_image VARCHAR(255),
    event_cover_image VARCHAR(255),
    tag VARCHAR(100), 
    activity_type VARCHAR(100),
    activity_name VARCHAR(100),
    activity_description TEXT,
    host VARCHAR(255),
    attendees INT
);
"""
