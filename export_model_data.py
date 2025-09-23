"""
Export model data to JSON for client-side use
"""
import pandas as pd
import numpy as np
import joblib
import json

def export_model_data():
    """Export model coefficients and sample data to JSON"""
    
    # Load model components
    model = joblib.load('spotify_popularity_model.pkl')
    scaler = joblib.load('spotify_scaler.pkl')
    genre_encoder = joblib.load('spotify_genre_encoder.pkl')
    
    # Load and prepare data
    data = pd.read_csv('data/spotify_data.csv')
    data = data.dropna(subset=['artist_name', 'track_name'])
    data = data[data['popularity'] > 0]
    data['duration_min'] = data['duration_ms'] / 60000
    
    # Filter valid genres
    genre_counts = data['genre'].value_counts()
    valid_genres = genre_counts[genre_counts >= 1000].index.tolist()
    data = data[data['genre'].isin(valid_genres)]
    
    # Get sample songs (500 random songs)
    sample_songs = data.sample(500)[['artist_name', 'track_name', 'popularity', 'genre', 
                                    'year', 'danceability', 'energy', 'key', 'loudness', 
                                    'mode', 'speechiness', 'acousticness', 'instrumentalness', 
                                    'liveness', 'valence', 'tempo', 'duration_min', 'time_signature']].to_dict('records')
    
    # Extract Random Forest parameters (simplified prediction)
    # We'll use feature importance and create a simplified linear model
    feature_importance = model.feature_importances_
    
    # Get scaler parameters
    scaler_mean = scaler.mean_.tolist()
    scaler_scale = scaler.scale_.tolist()
    
    # Get genre mapping
    genre_mapping = {genre: idx for idx, genre in enumerate(genre_encoder.classes_)}
    
    # Create simplified model data
    model_data = {
        'feature_importance': feature_importance.tolist(),
        'scaler_mean': scaler_mean,
        'scaler_scale': scaler_scale,
        'genre_mapping': genre_mapping,
        'feature_names': ['year', 'danceability', 'energy', 'key', 'loudness', 'mode', 
                         'speechiness', 'acousticness', 'instrumentalness', 'liveness', 
                         'valence', 'tempo', 'duration_min', 'time_signature', 'genre_encoded'],
        'sample_songs': sample_songs,
        'base_popularity': 50  # Base prediction value
    }
    
    # Save to JSON
    with open('model_data.json', 'w') as f:
        json.dump(model_data, f, indent=2)
    
    print(f"Exported model data with {len(sample_songs)} sample songs")
    print(f"Available genres: {list(genre_mapping.keys())}")
    
    return model_data

if __name__ == "__main__":
    export_model_data()
