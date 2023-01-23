import flask
from flask import request, jsonify
from db import Database

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>VLib - Online Library</h1>
                <p>A flask api implementation for book information.   </p>'''


@app.route('/api/getlastrowsensordata', methods=['GET'])
def get_last_row_sensor_data():
    db = Database()
    data = db.get_last_row_sensor_data()
    ids = []
    temperatures = []
    humidities = []
    timestamps = []
    for (id, temperature, humidity, timestamp) in data:
        ids.append(id)
        temperatures.append(temperature)
        humidities.append(humidity)
        timestamps.append(timestamp)
    data_json = {
        'ids': ids,
        'temperatures': temperatures,
        'humidities': humidities,
        'timestamps': timestamps,
        'Status Code': 200
    }
    return jsonify(data_json)


@app.route('/api/getlastsensordata', methods=['GET'])
def get_last_sensor_data():
    db = Database()
    data = db.get_last_sensor_data()
    ids = []
    temperatures = []
    humidities = []
    timestamps = []
    for (id, temperature, humidity, timestamp) in data:
        ids.append(id)
        temperatures.append(temperature)
        humidities.append(humidity)
        timestamps.append(timestamp)
    data_json = {
        'ids': ids,
        'temperatures': temperatures,
        'humidities': humidities,
        'timestamps': timestamps,
        'Status Code': 200
    }
    return jsonify(data_json)


@app.route('/api/getlastdaysensordata', methods=['GET'])
def get_last_day_sensor_data():
    db = Database()
    data = db.get_last_day_sensor_data()
    hours = []
    days = []
    temperatures = []
    humidities = []
    for (temperature, humidity, hour, day) in data:
        hours.append(str(hour) + ":00")
        days.append(str(day))
        temperatures.append(round(temperature, 2))
        humidities.append(round(humidity, 2))
    data_json = {
        'hours': hours,
        'days': days,
        'temperatures': temperatures,
        'humidities': humidities,
        'Status Code': 200
    }
    response = flask.jsonify(data_json)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/getlastweeksensordata', methods=['GET'])
def get_last_week_sensor_data():
    db = Database()
    data = db.get_last_week_sensor_data()
    hours = []
    days = []
    temperatures = []
    humidities = []
    for (temperature, humidity, hour, day) in data:
        hours.append(str(hour) + ":00")
        days.append(str(day))
        temperatures.append(round(temperature, 2))
        humidities.append(round(humidity, 2))
    data_json = {
        'hours': hours,
        'days': days,
        'temperatures': temperatures,
        'humidities': humidities,
        'Status Code': 200
    }
    response = flask.jsonify(data_json)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/getsensordata', methods=['GET'])
def get_sensor_data():
    db = Database()
    data = db.get_sensor_data()
    ids = []
    temperatures = []
    humidities = []
    timestamps = []
    for (id, temperature, humidity, timestamp) in data:
        ids.append(id)
        temperatures.append(temperature)
        humidities.append(humidity)
        timestamps.append(timestamp)
    data_json = {
        'ids': ids,
        'temperatures': temperatures,
        'humidities': humidities,
        'timestamps': timestamps,
        'Status Code': 200
    }
    response = flask.jsonify(data_json)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/addsensordata', methods=['POST'])
def add_sensor_data():
    db = Database()
    postedData = request.get_json()
    temperature = postedData["temperature"]
    humidity = postedData["humidity"]
    Database().insert_sensor_data(temperature, humidity)
    return jsonify("Data inserted successfully")


if __name__ == "__main__":
    # context = ('./keys/cert.pem', './keys/key.pem')
    app.run(host='0.0.0.0', port=5000, debug=True)
