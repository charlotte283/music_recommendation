# 🎧 Song Recommender App

A simple **song recommendation system** that suggests similar songs based on **song titles**. Built using **TF-IDF vectorization** and **K-Nearest Neighbors**, with album covers fetched via the **Spotify API**.

---

## 🔍 Features

- 🎵 Recommends similar songs using only the song title
- ⚡ Fast and lightweight thanks to TF-IDF + Nearest Neighbors
- 🎨 Album covers fetched from Spotify for a rich UI
- 🖥️ Interactive interface with **Streamlit**

---

## 📦 Tech Stack

- **Python 3.10+**
- **Pandas** – Data processing
- **scikit-learn** – TF-IDF vectorizer and Nearest Neighbors model
- **Streamlit** – Web interface
- **Spotipy** – Spotify API wrapper

---

## 🛠 How It Works

1. Song titles are vectorized using `TfidfVectorizer`.
2. A `NearestNeighbors` model is trained to find similar titles.
3. The app searches for the input song and finds the top 5 most similar ones.
4. Album covers are retrieved from the Spotify API using `spotipy`.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/song-title-recommender.git
cd song-title-recommender
