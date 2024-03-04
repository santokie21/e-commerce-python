from ultralytics import YOLO  # Import the YOLO class

def detect_objects_in_image(image_path):
    # Load the pre-trained YOLOv8 model
    model = YOLO('models/yolov8m.pt')  # You can specify a custom model path or one of the pre-trained models
    
    # Perform detection
    results = model(image_path,show=True,save=True,save_txt=True,save_conf=True)
    
    # Extract detected class names
    detected_classes=results[0].tojson()

    return detected_classes

# For video, you can process it frame by frame or extract key frames to run detection.
# Handling video requires more computational resources, especially for real-time processing.
