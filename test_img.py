from ultralytics import YOLO
import cv2

def get_pre_made_model():
    loaded_model = YOLO("lax_model.pt")

    for img_path in ["display_imgs/solo_test_lax_CV_1.jpg", "display_imgs/solo_test_lax_CV_2.jpg"]:
        results = loaded_model.predict(img_path, imgsz=640, conf=0.5)

        for r in results:
            print(f"Detected classes: {r.names}")
            print(f"Number of detections: {len(r.boxes)}")
            print(f"Original image size: {r.orig_shape}")

            annotated_img = r.plot()

            resized = cv2.resize(annotated_img, (800, 600)) if annotated_img.shape[0] > 1000 else annotated_img

            cv2.imshow("YOLOv8 Prediction", resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == '__main__':
    get_pre_made_model()


#py -3.12 test_img.py