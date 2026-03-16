
class DbInit:
    def __init__(self,conn):
        self.conn = conn

    def create_tables(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""CREATE DATABASE if not EXISTS digital_hunter""")
            self.conn.commit()
            self.conn.select_db('digital_hunter')

        with self.conn.cursor() as cursor:
            cursor.execute(
            """CREATE TABLE if not EXISTS  intel(
                timestamp DATETIME ,
                signal_id VARCHAR(50),
                entity_id VARCHAR(50),
     	        reported_lat FLOAT,
     	        reported_lon FLOAT,
     	        signal_type VARCHAR(50),
                priority_level INT) """)

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS attack(
                timestamp DATETIME,
                attack_id VARCHAR(50),
                entity_id VARCHAR(50),
                weapon_type  VARCHAR(30))""")

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS damage(
                timestamp DATETIME,
                attack_id VARCHAR(50),
                entity_id VARCHAR(50),
                result  VARCHAR(30))""" )

            cursor.execute(
            """CREATE TABLE IF NOT EXISTS target_bank(
                attack_id VARCHAR(50) UNIQUE,
                 reported_lat FLOAT,
                reported_lon FLOAT,
                movement_distance  FLOAT,
            	status VARCHAR(50))""")

            self.conn.commit()











