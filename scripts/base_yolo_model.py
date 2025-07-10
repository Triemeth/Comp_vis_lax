from ultralytics import YOLO
import matplotlib.pyplot as plt

def train_model():
    model = YOLO("yolo11n.pt")
    results = model.train(
        data="Lax_OB/lax.yaml",
        save = True, 
        epochs=100, 
        imgsz=640, 
        device=0
    )

    metrics = model.val()
    model.save("lax_model.pt")

    return results, metrics

if __name__ == '__main__':
    res, met = train_model()
#py -3.12 base_yolo_model.py