import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load vectorizer, model, and song data
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
nn_model = pickle.load(open("nn_model.pkl", "rb"))
music = pickle.load(open("music_data.pkl", "rb"))

# Spotify setup
CLIENT_ID = "1cf93001684a4b6daf4d051f025565d9"
CLIENT_SECRET = "e2ccc7da808a44fd9e064c9d55f2da4b"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

def get_album_cover(song_name, artist_name):
    query = f"track:{song_name} artist:{artist_name}"
    result = sp.search(q=query, type="track", limit=1)
    if result["tracks"]["items"]:
        return result["tracks"]["items"][0]["album"]["images"][0]["url"]
    return "https://i.postimg.cc/0QNxYz4V/social.png"

def get_similar_songs(song_name):
    try:
        idx = music[music['name'].str.lower() == song_name.lower()].index[0]
    except IndexError:
        return pd.DataFrame()  # empty if not found
    vec = vectorizer.transform([song_name])
    distances, indices = nn_model.kneighbors(vec)
    return music.iloc[indices[0][1:]]  # skip self

# UI
st.title("🎧 Song Title-Based Recommender")

selected_song = st.selectbox("Pick a song", music['name'].values)

if st.button("Recommend"):
    recs = get_similar_songs(selected_song)
    if recs.empty:
        st.warning("Song not found.")
    else:
        cols = st.columns(5)
        for i, row in enumerate(recs.itertuples()):
            with cols[i]:
                st.text(row.name)
                st.image(get_album_cover(row.name, row.artists))
