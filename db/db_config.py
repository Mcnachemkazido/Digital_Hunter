from dotenv import load_dotenv
import os
load_dotenv()

class DbConfig:

    @staticmethod
    def get_host(self):
        if os.getenv("SQL_HOST"):
            return os.getenv("SQL_HOST")
        return False

    @staticmethod
    def get_port(self):
        if os.getenv("SQL_PORT"):
            return os.getenv("SQL_PORT")
        return False

    @staticmethod
    def get_user(self):
        if os.getenv("SQL_USER"):
            return os.getenv("SQL_USER")
        return False

    @staticmethod
    def get_password(self):
        if os.getenv("SQL_PASSWORD"):
            return os.getenv("SQL_PASSWORD")
        return False