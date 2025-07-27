# 🎬 Movie Recommendation System

A **Content-Based Recommender System** that suggests movies similar to a user’s input using **NLP, TF-IDF vectorization**, and **cosine similarity**. This system uses the [TMDB movie dataset](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies) and is deployed with a Streamlit web interface.

---

## 📌 Table of Contents

- [📙 Try on Google Colab](#-try-on-google-colab)
- [🚀 Demo (ngrok)](#-demo-ngrok)
- [✨ Features](#-features)
- [📦 Dataset](#-dataset)
- [⚙️ Installation](#-installation)
- [🔧 Kaggle API Setup in Colab](#-kaggle-api-setup-in-colab)
- [🧠 How It Works](#-how-it-works)
- [🖥️ Streamlit App + ngrok](#-streamlit-app--ngrok)
- [📁 Project Structure](#-project-structure)
- [📈 Results](#-results)
- [📜 License](#-license)

---

## 📙 Try on Google Colab

Run the complete project in your browser — no installation required!

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1LCRbboPyECuc079dxITUKsv3Qe8tuxlY?usp=sharing)

---

## 🚀 Demo (ngrok)

You can also deploy the app with ngrok for public access:


🔗 Live App: [ngrok public access](https://0cd83ec13ed7.ngrok-free.app/)


## ✨ Features

- Recommends similar movies using **text-based similarity**
- Uses combined metadata: `overview`, `genres`, `keywords`, `tagline`
- Fuzzy match for movie search (`difflib`)
- Lightweight interface with **Streamlit**
- Optionally deployable via **ngrok**

## 📦 Dataset

- **Source**: [TMDB 2023 Dataset (Kaggle)](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies)
- **Size**: 1.26 million movies
- **After cleaning**: 72,565 entries
- **License**: ODC Attribution License (ODC-By)

---

## ⚙️ Installation

### 1. Clone this Repository
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run demo.py
```

## 🔧 Kaggle API Setup in Colab

### Step-by-step:

#### 1. Download your `kaggle.json`

From [https://www.kaggle.com/account](https://www.kaggle.com/account) ➝ Create New API Token

#### 2. Upload in Colab:

* upload `kaggle.json` in colab

## 🧠 How It Works

### 1. **Data Cleaning**

* Removed nulls in key features (`overview`, `tagline`, etc.)
* Combined metadata into one string ("soup")
* Example:

  ```python
  df['soup'] = df['overview'] + ' ' + df['genres'] + ' ' + df['keywords'] + ' ' + df['tagline']
  ```

### 2. **Feature Extraction**

* TF-IDF Vectorizer:

  ```python
  from sklearn.feature_extraction.text import TfidfVectorizer
  tfidf = TfidfVectorizer(stop_words='english')
  tfidf_matrix = tfidf.fit_transform(df['soup'])
  ```

### 3. **Similarity Calculation**

* Cosine similarity matrix:

  ```python
  from sklearn.metrics.pairwise import cosine_similarity
  cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
  ```

### 4. **Recommendation Logic**

* Based on index of closest title
* Top K recommendations sorted by popularity

---

## 🖥️ Streamlit App + ngrok

### Requirements

```bash
pip install streamlit pyngrok
```

### Deploy Script (simplified):

```python
from pyngrok import ngrok
import os

ngrok.set_auth_token("YOUR_NGROK_TOKEN")
try:
    ngrok.kill()
except:
    pass
!nohup streamlit run demo.py &
ngrok_tunnel = ngrok.connect(addr='5011', proto='http', bind_tls=True)
print(' * Tunnel URL:', ngrok_tunnel.public_url)
```

---

## 📁 Project Structure

```
.
├── demo.py                 # Streamlit UI logic
├── movie_data/             # Dataset directory
├── consine_sim.pkl         # Precomputed similarity matrix (40+ GB)
├── movies.csv              # Cleaned movie data
├── requirements.txt        # Dependencies
├── LICENSE                 # MIT License
└── README.md               # This file
```

---

## 📈 Results

| Metric             | Value                 |
| ------------------ | --------------------- |
| Dataset Size       | 1.26 million          |
| Cleaned Rows       | 72,565                |
| TF-IDF Features    | \~97,000              |
| Cosine Matrix Size | \~40 GB               |
| Recommendations    | Top 10 similar movies |

✅ Runs efficiently on Colab
⚠️ Cosine matrix should be precomputed and saved as `.pkl` to avoid memory errors

---

## 📜 License

This project is licensed under the **MIT License**.
