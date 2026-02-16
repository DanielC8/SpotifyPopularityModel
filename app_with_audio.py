from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import os
from werkzeug.utils import secure_filename
from audio_analyzer import SpotifyAudioAnalyzer

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads directory
os.makedirs('uploads', exist_ok=True)

# Allowed audio file extensions
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'flac', 'm4a', 'aac', 'ogg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load model and data
try:
    model = joblib.load('spotify_popularity_model.pkl')
    scaler = joblib.load('spotify_scaler.pkl')
    genre_encoder = joblib.load('spotify_genre_encoder.pkl')
    
    # Load data
    data = pd.read_csv('data/spotify_data.csv')
    data = data.dropna(subset=['artist_name', 'track_name'])
    data = data[data['popularity'] > 0]
    data['duration_min'] = data['duration_ms'] / 60000
    
    # Filter valid genres
    genre_counts = data['genre'].value_counts()
    valid_genres = genre_counts[genre_counts >= 1000].index.tolist()
    data = data[data['genre'].isin(valid_genres)]
    data['genre_encoded'] = genre_encoder.transform(data['genre'])
    
    print("Model and data loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = scaler = genre_encoder = data = None

# Initialize audio analyzer
audio_analyzer = SpotifyAudioAnalyzer()

@app.route('/')
def index():
    return render_template('index_with_audio.html')

@app.route('/api/songs')
def get_songs():
    if data is not None:
        songs = data.sample(50)[['artist_name', 'track_name', 'popularity', 'genre']].to_dict('records')
        return jsonify(songs)
    return jsonify([])

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        features = request.json
        feature_array = np.array([[
            features['year'], features['danceability'], features['energy'],
            features['key'], features['loudness'], features['mode'],
            features['speechiness'], features['acousticness'], 
            features['instrumentalness'], features['liveness'],
            features['valence'], features['tempo'], features['duration_min'],
            features['time_signature'], features['genre_encoded']
        ]])
        
        scaled = scaler.transform(feature_array)
        prediction = model.predict(scaled)[0]
        return jsonify({'prediction': max(0, min(100, prediction))})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/analyze_audio', methods=['POST'])
def analyze_audio():
    try:
        if 'audio_file' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        file = request.files['audio_file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Analyze the audio file
            features = audio_analyzer.analyze_audio_file(filepath)
            
            # Clean up uploaded file
            os.remove(filepath)
            
            if features:
                # Add default values for missing features
                features['year'] = 2023
                features['genre'] = 'pop'  # Default genre
                features['genre_encoded'] = 0  # Default to first genre
                
                # Make prediction
                feature_array = np.array([[
                    features['year'], features['danceability'], features['energy'],
                    features['key'], features['loudness'], features['mode'],
                    features['speechiness'], features['acousticness'], 
                    features['instrumentalness'], features['liveness'],
                    features['valence'], features['tempo'], features['duration_min'],
                    features['time_signature'], features['genre_encoded']
                ]])
                
                scaled = scaler.transform(feature_array)
                prediction = model.predict(scaled)[0]
                features['predicted_popularity'] = max(0, min(100, prediction))
                
                return jsonify(features)
            else:
                return jsonify({'error': 'Failed to analyze audio file'}), 500
        else:
            return jsonify({'error': 'Invalid file type. Supported: WAV, MP3, FLAC, M4A, AAC, OGG'}), 400
            
    except Exception as e:
        return jsonify({'error': f'Error processing audio: {str(e)}'}), 500

@app.route('/api/analyze_default')
def analyze_default():
    """Analyze the default sample file"""
    try:
        if os.path.exists('skeletononthebeat.wav'):
            features = audio_analyzer.analyze_audio_file('skeletononthebeat.wav')
            if features:
                # Add default values
                features['year'] = 2023
                features['genre'] = 'electronic'
                features['genre_encoded'] = 3  # Assuming electronic is index 3
                
                # Make prediction
                feature_array = np.array([[
                    features['year'], features['danceability'], features['energy'],
                    features['key'], features['loudness'], features['mode'],
                    features['speechiness'], features['acousticness'], 
                    features['instrumentalness'], features['liveness'],
                    features['valence'], features['tempo'], features['duration_min'],
                    features['time_signature'], features['genre_encoded']
                ]])
                
                scaled = scaler.transform(feature_array)
                prediction = model.predict(scaled)[0]
                features['predicted_popularity'] = max(0, min(100, prediction))
                
                return jsonify(features)
        
        return jsonify({'error': 'Default sample file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/song/<artist>/<track>')
def get_song(artist, track):
    if data is not None:
        song = data[(data['artist_name'] == artist) & (data['track_name'] == track)]
        if not song.empty:
            return jsonify(song.iloc[0].to_dict())
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(port=5001)
