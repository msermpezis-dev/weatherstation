import mysql.connector


class Database:
    cnx = mysql.connector.connect(
        host="localhost",
        database="sensor_db",
        user="root",
        password=""
    )

    cursor = cnx.cursor()

    def get_sensor_data(self):
        self.cursor.execute("SELECT id, temperature, humidity, timestamp FROM sensor")
        return self.cursor

    def insert_sensor_data(self, temperature, humidity):  # insert data into UserData table
        self.cursor.execute("INSERT INTO sensor (temperature, humidity) "
                            "VALUES(%s, %s)",
                            (temperature, humidity,))
        self.cnx.commit()

    def db_close(self):
        self.cursor.close()
        self.cnx.close()
