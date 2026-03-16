from dotenv import load_dotenv
import os
load_dotenv()

class IntelConfig:

    @staticmethod
    def get_bootstrap_servers(self):
        if os.getenv("BOOTSTRAP_SERVERS"):
            return os.getenv("BOOTSTRAP_SERVERS")
        return False