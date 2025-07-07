from ultralytics import YOLO
import matplotlib.pyplot as plt

def train_model():
    model = YOLO("yolo11n.pt")
    results = model.train(
        data="Lax_OB/lax.yaml", 
        epochs=10, 
        imgsz=640, 
        device=0
    )

    metrics = model.val()
    print(metrics.box.maps)
    return results

if __name__ == '__main__':
    res = train_model()

#py -3.12 base_yolo_model.py