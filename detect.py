import cv2
from ultralytics import YOLO
import sys
import numpy as np

def detect_and_show_image(image_path):
    model = YOLO('yolov8m.pt')  # Load YOLOv8 model
    results = model(image_path,show=True,save=True,save_txt=True,save_conf=True)
    # cv2.imshow('Frame', np.squeeze(results[0].plot()))

def detect_and_show_video(video_path):
    model = YOLO('yolov8m.pt')  # Load YOLOv8 model
    results=model.predict(source=str(video_path),show=True)

def main():
    if len(sys.argv) != 3:
        print("Usage: python detect_with_opencv.py <mode> <path>")
        print("<mode> should be 'image' or 'video'")
        return

    mode = sys.argv[1]
    file_path = sys.argv[2]

    if mode == "image":
        detect_and_show_image(file_path)
    elif mode == "video":
        detect_and_show_video(file_path)
    else:
        print("Invalid mode. Use 'image' or 'video'.")

if __name__ == "__main__":
    main()
