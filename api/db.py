import mysql.connector


class Database:
    def __init__(self):
        config = {
            "host": "192.168.1.182",
            "database": "sensor_db",
            "user": "root",
            "password": "jC$#avKd9&c3#z",
            'raise_on_warnings': True, }
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

    def __del__(self):
        self.cnx.close()
        self.cursor.close()

    def get_last_row_sensor_data(self):
        self.cursor.execute("SELECT id, temperature, humidity, DAY(timestamp) FROM sensor "
                            "ORDER BY id DESC LIMIT 1;")
        return self.cursor

    def get_last_sensor_data(self):
        self.cursor.execute("SELECT id, temperature, humidity, DAY(timestamp) FROM sensor "
                            "WHERE timestamp BETWEEN(DATE_SUB(NOW(), INTERVAL 5 MINUTE)) AND NOW();")
        return self.cursor

    def get_last_day_sensor_data(self):
        self.cursor.execute("SELECT AVG(temperature), AVG(humidity), hour( timestamp ), DAY( timestamp ) "
                            "FROM sensor "
                            "WHERE timestamp BETWEEN(DATE_SUB(NOW(), INTERVAL 1 DAY)) AND NOW() "
                            "GROUP BY hour( timestamp ), DAY( timestamp );")
        return self.cursor

    def get_last_week_sensor_data(self):
        self.cursor.execute("SELECT AVG(temperature), AVG(humidity), hour( timestamp ), DAY( timestamp ) "
                            "FROM sensor "
                            "WHERE timestamp BETWEEN(DATE_SUB(NOW(), INTERVAL 7 DAY)) AND NOW() "
                            "GROUP BY hour( timestamp ), DAY( timestamp );")
        return self.cursor

    def get_sensor_data(self):
        self.cursor.execute("SELECT id, temperature, humidity, DAY(timestamp) FROM sensor;")
        return self.cursor

    def insert_sensor_data(self, temperature, humidity):  # insert data into UserData table
        self.cursor.execute("INSERT INTO sensor (temperature, humidity) "
                            "VALUES(%s, %s);",
                            (temperature, humidity,))
        self.cnx.commit()


