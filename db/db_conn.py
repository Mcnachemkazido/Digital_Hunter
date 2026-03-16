import pymysql

class DbConn:
    def __init__(self,host,port,user,password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def get_conn(self):
        try:
            return pymysql.connect(
                host=self.host,
               port=self.port,
               user=self.user,
               password=self.password)

        except pymysql.err.OperationalError as e :
            print(e)
            raise



