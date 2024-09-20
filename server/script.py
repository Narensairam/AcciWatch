from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import pandas as pd
from io import StringIO
import pymysql
import clusteringModel
import login

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Jpsb-123',
    'database': 'accidentAnalysis'
}

url = "./../Accident Data Analysis/Copy_of_AccidentReports.csv"
data = pd.read_csv(url)


app = Flask(__name__)
CORS(app,resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route("/")
@cross_origin()

def home():
    return "Hello, first react+flask app"

@app.route('/login', methods=['POST'])
def login_route_script():
    return

@app.route('/coordinates')
def get_data():
    data1 = data[['Latitude', 'Longitude']]
    data1 = data1[(data1['Latitude']!=0.0) & (data1['Latitude']!=0.0)]
    data_json = data1.to_json(orient='records')
    return data_json

@app.route('/get_cluster')
def get_cluster():
    data = clusteringModel.cluster()
    data_json = data.to_json(orient="records")
    return data_json

@app.route('/district_rank')
def ranking():
    ranks = data['DISTRICTNAME'].value_counts()
    ranks_json = ranks.to_json()
    return Response(ranks_json, mimetype='application/json')

@app.route('/upload_report', methods=['POST'])
def receive_message():
    # Check if the POST request contains a file
    if 'csvFile' not in request.files:
        return 'No file part', 400

    file = request.files['csvFile']
    
    # Ensure that a file is selected
    if file.filename == '':
        return 'No selected file', 400

    # Read CSV file content
    df = pd.read_csv(file)
    df = df.where(pd.notnull(df), None)
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
        
    for row in df.itertuples(index=False):
        sql = """
        INSERT INTO accidentReports (districtName, unitName, crimeNo, year, RI, noOfVehicleInvolved, accidentClassification, accidentSpot, accidentLocation, accidentSubLocation, accidentSpotB, mainCause, hitRun, severity, collisionType, junctionControl, roadCharacter, roadType, surfaceType, surfaceCondition, roadCondition, weather, laneType, roadMarkings, spotConditions, sideWalk, roadJunction, collisionTypeB, accidentRoad, landmarkFirst, landmarkSecond, distanceLandMarkFirst, distanceLandMarkSecond, accidentDescription, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(sql, tuple(row))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return "CSV file received and processed and uploaded"

if __name__=='__main__':
    app.run(debug=True)
