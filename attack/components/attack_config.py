from dotenv import load_dotenv
import os
load_dotenv()

class AttackConfig:

    @staticmethod
    def get_bootstrap_servers():
        if os.getenv("BOOTSTRAP_SERVERS"):
            return os.getenv("BOOTSTRAP_SERVERS")
        return False