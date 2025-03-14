Image Classifier with CIFAR-10

Project Description
This project involves building a basic image classification model using the CIFAR-10 dataset. The goal is to create a model that can classify images into one of 10 categories using a Convolutional Neural Network (CNN). The model is trained using TensorFlow and evaluated on its accuracy with both training and validation datasets.

Setup
Prerequisites
Ensure you have the following Python packages installed:

TensorFlow
Matplotlib

You can install them using pip:
pip install tensorflow matplotlib

Project Structure
Image-classifier/
│
├── cifar-10-batches-py/          # CIFAR-10 dataset will be downloaded here
├── main.py                       # Main script to train the model
├── README.md                     # Project documentation
└── training_validation_accuracy.png  # Plot showing training and validation accuracy

Usage
Download CIFAR-10 Dataset
The CIFAR-10 dataset will be downloaded and extracted automatically when you run the script for the first time.
Run the Training Script
Execute the main.py script to train the model:
python main.py
The script will output the training progress for each epoch, including accuracy and loss for both training and validation datasets.

View Results
After training is complete, the script will generate a plot showing the training and validation accuracy over epochs.

Results

Training and Validation Accuracy

Final Test Accuracy
After 10 epochs of training, the final test accuracy achieved by the model is approximately 71.6%.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements

CIFAR-10 dataset: CIFAR-10
TensorFlow: TensorFlow
Matplotlib: Matplotlib

