# 🎵 Spotify Popularity Predictor

A machine learning web application that predicts Spotify song popularity and allows interactive experimentation with audio features.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen)](https://danielc8.github.io/SpotifyPopularityModel/)

## ✨ Features

- 🎯 **Song Comparison**: Compare actual vs predicted popularity for real songs
- 🎛️ **Interactive Controls**: Adjust audio features with sliders and see real-time predictions
- 📱 **Mobile Friendly**: Responsive design works on all devices
- ⚡ **No Server Required**: Pure client-side JavaScript implementation
- 🎨 **Modern UI**: Beautiful Spotify-themed interface

## 🚀 Live Demo

Visit the live website: **[https://danielc8.github.io/SpotifyPopularityModel/](https://danielc8.github.io/SpotifyPopularityModel/)**

## 📊 Model Details

- **Algorithm**: Random Forest Regressor
- **Dataset**: 1M+ Spotify tracks
- **Features**: Year, danceability, energy, valence, acousticness, loudness, tempo, duration, genre
- **Validation**: Cross-validated with hyperparameter tuning

## 🛠️ Local Development

### Option 1: View the Website
Simply open `index.html` in your browser - no installation required!

### Option 2: Export Real Model Data
```bash
# Install dependencies
pip install -r requirements.txt

# Export your trained model data
python export_model_data.py

# Setup GitHub Pages files
python setup_github_pages.py
```

## 📁 Project Structure

```
├── index.html                    # Main website (standalone)
├── Spotify.ipynb               # Jupyter notebook with full analysis
├── export_model_data.py        # Export model to JSON for web use
├── setup_github_pages.py       # GitHub Pages deployment helper
├── requirements.txt             # Python dependencies
├── docs/                        # GitHub Pages deployment files
└── data/                        # Dataset (not included in repo)
```

## 🎮 How to Use

1. **Song Comparison**:
   - Select a song from the dropdown
   - See actual vs predicted popularity
   - Green = good prediction, Red = needs improvement

2. **Interactive Experimentation**:
   - Use sliders to adjust audio features
   - See how changes affect popularity predictions
   - Experiment with different combinations

3. **Custom Predictions**:
   - Set your own values for all audio features
   - Get instant popularity predictions
   - Understand what makes songs popular

## 🧠 How It Works

The web app uses a simplified version of the Random Forest model:
1. **Feature Importance**: Uses weights from the trained model
2. **Client-Side Scaling**: Normalizes features in the browser
3. **Weighted Prediction**: Calculates popularity using feature importance
4. **Real-Time Updates**: Instant predictions as you adjust sliders

## 📈 Model Performance

- **Training Accuracy**: High R² score on validation set
- **Feature Importance**: Year, danceability, and energy are top predictors
- **Cross-Validation**: Robust performance across different data splits

## 🤝 Contributing

Feel free to:
- Report bugs or suggest features
- Improve the prediction algorithm
- Enhance the user interface
- Add more audio features

## 📄 License

This project is open source and available under the MIT License.