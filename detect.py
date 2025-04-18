import cv2
from ultralytics import YOLO
import os

# Load the trained model
model = YOLO('D:\\Pothole_Detection_YOLOv8\\runs\\detect\\train2\\weights\\best.pt')  # Update with your trained model path

# Open the video file
video_path = 'D:\\Pothole_Detection_YOLOv8\\input\\sample_video.mp4'  # Replace with your video path
if not os.path.exists(video_path):
    print(f"Error: Video file not found at {video_path}")
    exit()

cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print(f"Error: Unable to open video file at {video_path}")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)  # Ensure FPS is a float

# Define the codec and create a VideoWriter object to save the output video
output_path = 'D:\\Pothole_Detection_YOLOv8\\output\\output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Check if VideoWriter opened successfully
if not out.isOpened():
    print(f"Error: Unable to open VideoWriter at {output_path}")
    exit()

# Process each frame from the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Finished processing video.")
        break
    
    # Perform detection
    results = model.predict(frame, conf=0.5)  # Run YOLO model on the current frame with confidence threshold

    # Check if any objects (potholes) were detected
    if len(results) > 0 and len(results[0].boxes) > 0:
        print(f"Detections: {len(results[0].boxes)} objects detected.")

    # Annotate and save the results
    annotated_frame = results[0].plot()  # Plot the YOLO output (annotations) on the frame
    out.write(annotated_frame)  # Save the annotated frame to the output video

    # Optionally display the results in a window (for visualization)
    cv2.imshow('Pothole Detection', annotated_frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video and file resources
cap.release()
out.release()  # Finalize and save the output video
cv2.destroyAllWindows()

print(f"Video processing complete. Output saved at {output_path}")
