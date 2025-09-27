# 🎵 Spotify Popularity Predictor

A machine learning web application that predicts Spotify song popularity with audio analysis capabilities.

## ✨ Features

- 🎧 **Audio Analysis**: Upload audio files and extract Spotify-like features (simulation)
- 🎯 **Song Comparison**: Compare actual vs predicted popularity for real songs
- 🎛️ **Interactive Controls**: Adjust audio features with sliders and see real-time predictions
- 📱 **Mobile Friendly**: Responsive design works on all devices
- ⚡ **No Server Required**: Pure client-side JavaScript implementation

## 🎮 How to Use

1. **Audio Analysis**:
   - Click "Simulate Audio Analysis" for a demo
   - Upload audio files to see simulated feature extraction
   - Features update automatically in the controls panel

2. **Song Comparison**:
   - Select songs from the dropdown to compare actual vs predicted popularity
   - Green = good prediction, Red = needs improvement

3. **Interactive Experimentation**:
   - Use sliders to adjust audio features
   - See how changes affect popularity predictions in real-time

## 🧠 How It Works

The web app uses a simplified version of a Random Forest model trained on 1M+ Spotify tracks:
- **Feature Importance**: Uses weights from the trained model
- **Client-Side Scaling**: Normalizes features in the browser
- **Audio Simulation**: Simulates feature extraction for demo purposes
- **Real-Time Predictions**: Instant updates as you adjust parameters

## 🎵 Audio Features

The system analyzes these Spotify-like features:
- Danceability, Energy, Valence, Acousticness
- Tempo, Loudness, Key, Mode, Time Signature
- Speechiness, Instrumentalness, Liveness

## 📊 Model Performance

- **Algorithm**: Random Forest Regressor
- **Dataset**: 1M+ Spotify tracks
- **Features**: 15 audio and metadata features
- **Validation**: Cross-validated with hyperparameter tuning

---

*Note: This is a demonstration version. Audio analysis is simulated for GitHub Pages compatibility.*
