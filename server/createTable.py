import pymysql

# Database connection info without specifying the database
db_config_without_db = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Jpsb-123'
}

# Database name
database_name = 'accidentAnalysis'

# First connection: to create the database if it doesn't exist
initial_connection = pymysql.connect(**db_config_without_db)
initial_cursor = initial_connection.cursor()
initial_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
initial_cursor.close()
initial_connection.close()

# Update db_config to include the database now that it exists
db_config_with_db = db_config_without_db.copy()
db_config_with_db['database'] = database_name

# Second connection: to create the table within the database
connection = pymysql.connect(**db_config_with_db)
cursor = connection.cursor()

accidentReportSQL = """
CREATE TABLE IF NOT EXISTS accidentReports (
    districtName VARCHAR(255),
    unitName VARCHAR(255),
    crimeNo VARCHAR(255) NOT NULL,
    year INT,
    RI INT,
    noOfVehicleInvolved INT,
    accidentClassification VARCHAR(255),
    accidentSpot VARCHAR(255),
    accidentLocation VARCHAR(255),
    accidentSubLocation VARCHAR(255),
    accidentSpotB VARCHAR(255),
    mainCause VARCHAR(255),
    hitRun VARCHAR(255),
    severity VARCHAR(255),
    collisionType VARCHAR(255),
    junctionControl VARCHAR(255),
    roadCharacter VARCHAR(255),
    roadType VARCHAR(255),
    surfaceType VARCHAR(255),
    surfaceCondition VARCHAR(255),
    roadCondition VARCHAR(255),
    weather VARCHAR(255),
    laneType VARCHAR(255),
    roadMarkings VARCHAR(255),
    spotConditions VARCHAR(255),
    sideWalk VARCHAR(255),
    roadJunction VARCHAR(255),
    collisionTypeB VARCHAR(255),
    accidentRoad VARCHAR(255),
    landmarkFirst VARCHAR(255),
    landmarkSecond VARCHAR(255),
    distanceLandMarkFirst VARCHAR(255),
    distanceLandMarkSecond VARCHAR(255),
    accidentDescription TEXT,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    PRIMARY KEY (crimeNo)
);
"""

cursor.execute(accidentReportSQL)

connection.commit()
cursor.close()
connection.close()

print("Table created successfully!")
