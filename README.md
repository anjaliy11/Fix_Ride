# 🚗 Fix_Ride – AI-Powered Mechanic Recommendation System

Fix_Ride is a machine learning–driven recommendation engine designed to match users with the most suitable mechanics based on real-world parameters like **service type**, **location (via Haversine distance)**, **user preferences**, and **interaction history**.

---

## 🧠 Built With

- [TensorFlow](https://www.tensorflow.org/) – Deep Learning Framework  
- [Keras](https://keras.io/) – Functional API for building recommendation models  
- [Pandas, NumPy] – Data manipulation and numerical operations  
- [Scikit-learn] – Data preprocessing and evaluation  
- [Haversine](https://pypi.org/project/haversine/) – Distance calculation between geolocations  

---

## 🔍 Features

- ✅ Personalized mechanic recommendations using learned embeddings  
- ✅ Service type filtering and geolocation-based ranking  
- ✅ Normalized numerical features: distance, ratings, cost, experience, response time  
- ✅ Built using a custom Neural Collaborative Filtering (NCF)-style architecture with Keras  

---

## 📊 Model Overview

Fix_Ride uses a **deep learning model with embedding layers** to learn user and mechanic preferences from interaction data. The model combines:

- **Categorical embeddings**:
  - `user_id`, `mechanic_id`, `service_type`

- **Numerical features**:
  - Haversine `distance_km`
  - `ratings`, `cost`, `experience_years`, `response_time`

These are concatenated and passed through dense layers to predict the likelihood of a good match.

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
git clone https://github.com/your-username/Fix_Ride.git
cd Fix_Ride
pip install -r requirements.txt
