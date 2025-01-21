# K-Nearest Neighbors (KNN) Classifier

## Project Overview
This project implements the **K-Nearest Neighbors (KNN)** algorithm as part of an **Introduction to AI** course. The goal was to introduce preliminary AI concepts and provide hands-on experience with fundamental machine learning algorithms.

## Features
- **KNN Classification:** Implements the basic KNN algorithm for supervised learning.
- **Distance Metrics:** Supports **Euclidean, Chebyshev, and Manhattan distances** for nearest neighbor computation.
- **Customizable `k` Value:** Allows users to specify the number of nearest neighbors.
- **Data Preprocessing:** Handles data normalization and feature scaling.
- **Automated Hyperparameter Tuning:** Finds the best `k` value through pre-testing.

## Technologies Used
- **Python**
- **CSV Data Handling** (for dataset processing)
- **Randomization** (for training data shuffling)

## How KNN Works
1. **Load Dataset:** Read and preprocess the dataset from a CSV file.
2. **Choose `k`:** Select the number of neighbors (optimized through pre-testing).
3. **Compute Distances:** Calculate distances using Manhattan, Chebyshev, or Euclidean methods.
4. **Find Nearest Neighbors:** Select the `k` closest data points.
5. **Predict Label:** Assign the most common class label among the neighbors.

## Implementation Details
- **Dataset Loading:** Reads data from `dataset(1).csv`, `pretest.csv`, and `finaltest.csv`.
- **Pre-testing:** Determines the best `k` value by running the model on a pretest dataset.
- **Final Predictions:** Generates predictions for unseen data and writes them to an output file. (for coourse evaluation purposes)

## Evaluation Metrics
- **Accuracy Score** (calculated from pre-test dataset)
- **Optimized `k` Selection**


## License
This project was developed for educational purposes as part of an **Intro to AI** course with my team mate Roya Aliyeva.


