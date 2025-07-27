import streamlit as st
import pandas as pd
import difflib
import pickle as pkl

print("Started....")

df = pd.read_csv('movies.csv')
print("Loaded df")

with open('consine_sim.pkl', 'rb') as f:
    consine_sim = pkl.load(f)
print("Loaded cosine sim")

indices = pd.Series(df.index, index=df['title_lower']).drop_duplicates()
list_of_all_titles = df['title_lower'].tolist()

def search_result(title):
  title = difflib.get_close_matches(title, list_of_all_titles)
  if len(title) == 0:
    return 'Movie not found'
  search_result = [indices[i] for i in title]
  return search_result

# Function to get movie recommendations based on index
def recommend(idx, df=df, consine_sim=consine_sim, k=5):
  sim_scores = list(enumerate(consine_sim[idx]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[1:k+1]
  movie_indices = [i[0] for i in sim_scores]
  recommended_df = df.iloc[movie_indices][['title', 'vote_average', 'popularity', 'overview', 'poster_path', 'runtime', 'release_date']]
  return recommended_df.sort_values(by='popularity', ascending=False)

st.set_page_config(
    page_title="Movie Recommender",
    layout="wide",
    page_icon="🎬"
)
st.title("Movie Recommendation System")
movie = st.text_input("Enter name of movie", placeholder="Type a movie name...")

sr_idx = search_result(movie)
if sr_idx == 'Movie not found':
    st.error("Movie not found. Please try another title.")
else:
  st.success(f"Found {len(sr_idx)} results for '{movie}':")
  st.subheader("Click on a movie to get recommendations:")

  cols = st.columns(3)
  for i, idx in enumerate(sr_idx):
      with cols[i]:
          name = df.iloc[idx]['title']
          poster_url = df.iloc[idx]['poster_path']
          st.image(poster_url, caption=name, use_container_width=True)

          if st.button(f"Get Recommendations for {name}", key=i):
              st.success(f"You selected: {name}")
              recommendations = recommend(idx, k=10)
              st.subheader("Recommended Movies:")

              for j, (_, row) in enumerate(recommendations.iterrows()):
                  st.image(row['poster_path'], caption=row['title'], use_container_width=True)
                  st.markdown(f"**Rating**: {row['vote_average']} | **Popularity**: {row['popularity']} | **Runtime** : {row['runtime']} | **Release Date** : {row['release_date']}")
                  st.write(row['overview'])
