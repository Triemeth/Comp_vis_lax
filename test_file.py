from roboflow import Roboflow
import os
from dotenv import load_dotenv

load_dotenv('/app/.env')

API_KEY = os.getenv("API_KEY")

rf = Roboflow(api_key=API_KEY)
project = rf.workspace("ryseai").project("lacrosse-object-detection")
version = project.version(5)
dataset = version.download("yolov11")

print("hello")