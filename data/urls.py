import os
from dotenv import load_dotenv

load_dotenv()


class Urls:
    enter_url = os.getenv("BASE_URL")
