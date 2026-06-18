import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('data/movies.csv')

def recommend_movies(movie_name, num_recommendations=3):
    if movie_name not in df['movie'].values:
        return f"Movie '{movie_name}' not found!"
    
    features = df[['action', 'scifi', 'drama', 'romance', 'thriller']]
    similarity = cosine_similarity(features)
    similarity_df = pd.DataFrame(similarity, index=df['movie'], columns=df['movie'])
    
    similar_movies = similarity_df[movie_name].sort_values(ascending=False)
    recommendations = similar_movies.drop(movie_name).head(num_recommendations)
    
    return recommendations.index.tolist()

if __name__ == "__main__":
    movie = input("Enter a movie name: ")
    results = recommend_movies(movie)
    print(f"\nMovies similar to '{movie}':")
    for i, m in enumerate(results, 1):
        print(f"{i}. {m}")