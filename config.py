import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    API_ID = os.getenv('28372387')
    API_HASH = os.getenv('11edc85521fb2d8f75e751bb284507e1')
    BOT_TOKEN = os.getenv('7947440196:AAHH1fSzRvwvh6OI_61pBDYC6JUjQthvCYc')
