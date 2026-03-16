

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
            print(data)

            cursor.execute(sql,data)
            self.conn.commit()


