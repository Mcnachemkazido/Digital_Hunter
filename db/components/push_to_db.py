

class PushToDb:
    def __init__(self,conn):
        self.conn = conn
        self.conn.select_db('digital_hunter')

    def insert_into_intel(self,data):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO `intel`(`timestamp`, `signal_id`, `entity_id`,
             `reported_lat`, `reported_lon`, `signal_type`, `priority_level`)
              VALUES (%s,%s,%s,%s,%s,%s,%s)"""

            data = (data['timestamp'],data['signal_id'],data['entity_id'],
                    data['reported_lat'],data['reported_lon'],data['signal_type'],
                    data['priority_level'])

            cursor.execute(sql,data)
            self.conn.commit()


    def insert_into_attack(self,data):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO `attack`(`timestamp`, `attack_id`, `entity_id`, `weapon_type`)
             VALUES (%s,%s,%s,%s)"""

            data = (data['timestamp'], data['attack_id'], data['entity_id'],
                    data['weapon_type'])

            cursor.execute(sql, data)
            self.conn.commit()


    def insert_into_damage(self,data):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO `damage`(`timestamp`, `attack_id`, `entity_id`, `result`)
             VALUES (%s,%s,%s,%s)"""

            data = (data['timestamp'], data['attack_id'], data['entity_id'],
                    data['result'])

            cursor.execute(sql, data)
            self.conn.commit()


    def insert_into_target_bank(self,data):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO `target_bank`(`attack_id`, `reported_lat`, 
            `reported_lon`, `movement_distance`, `status`)
             VALUES (%s,%s,%s,%s,%s)"""

            data = (data['attack_id'], data['reported_lat'], data['reported_lon'],
                    data['movement_distance'],data['status'])

            cursor.execute(sql, data)
            self.conn.commit()





