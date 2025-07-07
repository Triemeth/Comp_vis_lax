from ultralytics import YOLO
import matplotlib.pyplot as plt

model = YOLO("yolo11n.pt")

results = model.train(data = "lax.yml", epochs = 100, imgsz=640)

metrics = model.val()
metrics.box.maps
#py -3.12 base_yolo_model.py