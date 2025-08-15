# Chest X-Ray Lung Disease Classification

## Project Overview
This project aims to classify chest X-ray images as either **Normal** (healthy lungs) or **Diseased** (indicating lung disease) using **deep learning models**.  

We use two types of models for educational comparison:

- **Convolutional Neural Networks (CNNs)**: Excellent for image feature extraction.
- **Recurrent Neural Networks (RNNs)**: Typically for sequential data, adapted here by treating image rows as time steps.

> **Note:** This project is for demonstration purposes only and **not intended for medical diagnosis**.

---

## Dataset
- Kaggle Chest X-ray Dataset  
- [Link to Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)  
- Dataset contains labeled X-ray images: **Normal** vs **Pneumonia/Diseased**

---

## Features
- Upload and classify chest X-ray images
- Train and evaluate **CNN** and **RNN** models
- Display **training, validation, and test accuracy**
- Compare model performance
- Web interface (optional) for image upload and prediction using Django

---

## Requirements
- Python 3.8+
- Libraries:
  ```bash
  pip install torch torchvision pillow numpy matplotlib pandas scikit-learn jupyter
  pip install django
