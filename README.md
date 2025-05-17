## 🚗 Fix_Ride – AI-Powered Mechanic Recommendation System

Fix_Ride is a machine learning–driven recommendation engine designed to match users with the most suitable mechanics based on real-world parameters like **service type**, **location (via Haversine distance)**, **user preferences**, and **interaction history**.

---

## 🛠️ FIX_Ride Overview

FIX_Ride is a smart recommendation system that connects users with the most suitable mechanics based on service type, user preferences, and location. It uses a machine learning model built with **Keras** and **TensorFlow**, incorporating features like distance, ratings, cost, experience, and response time to personalize mechanic recommendations.

---

## 🔧 Backend

The backend of FIX_Ride is written in **Python** and includes:

- A **recommendation engine** that predicts the most suitable mechanics for users.
- **Preprocessed datasets** of users, mechanics, and service requests.
- Distance calculation using the **Haversine formula** to find geographic proximity.
- Label encoding and feature scaling for categorical and numerical data.
- A neural network built using **Keras** and **TensorFlow** to learn user-mechanic-service interactions.

---

## 🧠 Built With

- [TensorFlow](https://www.tensorflow.org/) – Deep Learning Framework  
- [Keras](https://keras.io/) – Functional API for building recommendation models  
- [Pandas, NumPy] – Data manipulation and numerical operations  
- [Scikit-learn](https://scikit-learn.org/) – Data preprocessing and evaluation  
- [Haversine](https://pypi.org/project/haversine/) – Distance calculation between geolocations  

---

## 🔍 Features

- ✅ Personalized mechanic recommendations using learned embeddings  
- ✅ Service type filtering and geolocation-based ranking  
- ✅ Normalized numerical features: distance, ratings, cost, experience, response time  
- ✅ Built using a custom Neural Collaborative Filtering (NCF)-style architecture with Keras  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- TensorFlow 2.x
- Pandas
- NumPy
- scikit-learn
- haversine

### Installation

```bash
git clone https://github.com/anjaliy11/Fix_Ride.git
cd Fix_Ride
pip install -r requirements.txt
