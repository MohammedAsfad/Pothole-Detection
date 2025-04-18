# Pothole-Detection
Pothole Detection Using YOLOv8


Step 1: Setting Up the Environment
        1.Create a New Folder for the Project:
          Create a folder where you want to store the project files. For example, Pothole_Detection_YOLOv8.
        2. Open VS Code:
          Launch Visual Studio Code and open the newly created folder (Pothole_Detection_YOLOv8).
        3.Create a Python Virtual Environment:
                    python -m venv yolov8_env
          Activate the virtual environment:
            On Windows:
                    yolov8_env\Scripts\activate
        4. Install Necessary Dependencies:
          Install the required libraries including Ultralytics (for YOLOv8), OpenCV, and other necessary dependencies:
                    pip install ultralytics opencv-python matplotlib
Step 2: Preparing Pre-Segmented Images
        1. Prepare the Dataset:
          Ensure you have a dataset with pre-segmented images. These should include:
          Images of potholes that you’ve pre-segmented.
          Labels in YOLO format (text files where each line corresponds to a detected object in the image).
        2. Data Structure: Organize the dataset folder in the following structure:
        
                pothole_dataset/
                ├── images/
                │   ├── train/
                │   │   ├── image1.jpg
                │   │   ├── image2.jpg
                │   └── val/
                │       ├── image1.jpg
                ├── labels/
                │   ├── train/
                │   │   ├── image1.txt
                │   │   ├── image2.txt

          In each .txt file, the format follows:
            <class_id> <x_center> <y_center> <width> <height>
Step 3: Configuring YOLOv8 for Pothole Detection
        1.Create a YAML File for Dataset Configuration: In the Pothole_Detection_YOLOv8 folder, create a pothole_data.yaml file, which configures YOLOv8 to recognize the dataset:
          .yaml:
            path: pothole_dataset
            train: images/train
            val: images/val
            nc: 1
            names: ['pothole']
        2. Download YOLOv8 Pre-trained Weights: YOLOv8 is based on the Ultralytics YOLO framework, which allows you to use pre-trained weights.
          In your code, the model is loaded using pre-trained weights:

              from ultralytics import YOLO

              # Load a YOLOv8 model
              model = YOLO('yolov8n.pt')  # nano model; other options: yolov8s.pt, yolov8m.pt, yolov8l.pt, etc.

Step 4: Training YOLOv8 on Pothole Detection
        1. Train the Model:
          After setting up the dataset and model, you can train the model using the following script.
          Create a new Python file called train.py in the project folder:

            python
            from ultralytics import YOLO

            # Load the YOLOv8 model (e.g., yolov8n.pt for nano model)
            model = YOLO('yolov8n.pt')  # choose the model size as per your requirement

            # Train the model using the pre-segmented dataset
            model.train(data='pothole_data.yaml', epochs=50, imgsz=640, batch=16, name='pothole_detector')
  Run the Training: In your terminal, run the script:
            python train.py
  YOLOv8 will start training and save the results to the runs/detect/pothole_detector/ folder.

Step 5: Inference and Pothole Detection
        Use the code detect.py mentioned in the repository
        Run the code
            pyton detect.py
