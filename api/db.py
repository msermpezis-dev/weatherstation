import mysql.connector


class Database:
    cnx = mysql.connector.connect(
        host="192.168.1.182",
        database="sensor_db",
        user="root",
        password="jC$#avKd9&c3#z"
    )

    cursor = cnx.cursor()

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
                            "WHERE timestamp BETWEEN(DATE_SUB(NOW(), INTERVAL 5 DAY)) AND NOW() "
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

    def db_close(self):
        self.cursor.close()
        self.cnx.close()

