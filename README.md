# [Spotify Popularity Predictor](https://danielc8.github.io/SpotifyPopularityModel/)

This project predicts Spotify song popularity (0-100) based on audio features using a Random Forest Regressor trained on 1M+ tracks. It includes a Jupyter notebook for the full ML pipeline, a Flask server with audio file analysis, and a standalone client-side web interface deployed via GitHub Pages.

## Features
- Predict song popularity from 15 audio and metadata features.
- Interactive web interface with sliders for real-time prediction adjustments.
- Song comparison: view actual vs predicted popularity for real Spotify tracks.
- Audio file upload and feature extraction using librosa (Flask server mode).
- Client-side prediction via exported model weights (no server required).

## Project Workflow
1. **Data Collection**: 1,159,764 Spotify tracks sourced from the [Spotify 1 Million Tracks](https://www.kaggle.com/datasets/amitanshjoshi/spotify-1million-tracks) Kaggle dataset via spotipy.
2. **Data Preparation**:
   - Removed 158,391 songs with 0 popularity.
   - Dropped rows with missing artist/track names.
   - Filtered genres with fewer than 1,000 songs (kept 81 genres).
   - Converted duration from milliseconds to minutes.
   - Encoded genre labels with LabelEncoder.
   - Final cleaned dataset: 1,000,768 rows, 15 features.
3. **Model Development**: Tested four models on an 80/20 train/test split:
   - Linear Regression: RMSE 13.81, R² 0.17
   - Decision Tree: RMSE 0.42, R² 0.99 (overfitting)
   - Random Forest: RMSE 3.52, R² 0.95 (selected)
   - SVR: not evaluated (import error in notebook)
4. **Hyperparameter Tuning**: RandomizedSearchCV with 100 iterations over number of estimators, max depth, min samples split/leaf, max features, and bootstrap.
5. **Final Model Performance** (test set):
   - RMSE: 9.33
   - R²: 0.6232
   - Best params: 421 estimators, max depth 19, min samples leaf 6, min samples split 6
6. **Deployment**: Model weights exported to JSON for client-side prediction. Web interface hosted on GitHub Pages.

## Feature Importance
| Feature | Importance |
|---|---|
| Genre | 51.6% |
| Year | 19.6% |
| Duration | 4.5% |
| Instrumentalness | 3.9% |
| Speechiness | 3.5% |
| Danceability | 3.4% |
| Loudness | 2.7% |
| Acousticness | 2.5% |
| Valence | 2.0% |
| Energy | 2.0% |

## Project Structure
```
├── Spotify.ipynb              # Full ML pipeline (EDA, training, tuning, evaluation)
├── app_with_audio.py          # Flask server with audio upload and prediction endpoints
├── audio_analyzer.py          # Extracts Spotify-like features from audio files using librosa
├── export_model_data.py       # Exports trained model weights and sample songs to JSON
├── setup_github_pages.py      # Prepares /docs folder for GitHub Pages deployment
├── index.html                 # Standalone web interface (no server needed)
├── index_with_audio.html      # Enhanced web interface with audio upload simulation
├── requirements.txt           # Python dependencies
├── templates/
│   └── index_with_audio.html  # Flask template for server mode
├── docs/                      # GitHub Pages deployment files
└── data/                      # Dataset directory (not included in repo)
```

## Setup Instructions
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/amitanshjoshi/spotify-1million-tracks) and place it in `data/spotify_data.csv`.

## Usage

### Client-Side Only (No Server)
Open `index.html` in a browser. Model weights are embedded in the page. Use sliders to adjust features and see predictions.

### Flask Server (With Audio Analysis)
```bash
python app_with_audio.py
```
The server runs on `localhost:5001` and provides:
- `GET /` — Web interface
- `GET /api/songs` — 50 random sample songs
- `POST /api/predict` — Predict from feature values
- `POST /api/analyze_audio` — Upload audio file, extract features, predict popularity
- `GET /api/analyze_default` — Analyze included sample audio file

Supported audio formats: WAV, MP3, FLAC, M4A, AAC, OGG.

### Export Model Data
```bash
python export_model_data.py
```
Exports model weights, scaler parameters, genre mapping, and 500 sample songs to `model_data.json` for client-side use.

## Limitations
- Genre accounts for 51.6% of feature importance, so predictions are heavily genre-dependent.
- Audio feature extraction via librosa approximates Spotify's proprietary analysis and is not identical.
- R² of 0.6232 on the test set indicates the model explains about 62% of popularity variance. Factors like artist fame, marketing, and playlist placement are not captured.
- The client-side web interface uses a simplified weighted prediction rather than the full Random Forest model.

## Requirements
- Python 3.x
- flask 2.3.3
- pandas 2.0.3
- numpy 1.24.3
- scikit-learn 1.3.0
- joblib 1.3.2
- librosa 0.10.1
- soundfile 0.12.1
- scipy 1.11.1
