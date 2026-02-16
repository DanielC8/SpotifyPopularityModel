"""
Setup script for GitHub Pages deployment with Audio Analysis
"""
import os
import shutil
import subprocess

def setup_github_pages():
    """Prepare files for GitHub Pages deployment with audio features"""
    
    print("🚀 Setting up GitHub Pages with Audio Analysis...")
    
    # Create docs folder (GitHub Pages can serve from docs/)
    docs_dir = 'docs'
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.makedirs(docs_dir)
    
    # Copy the enhanced HTML file with audio features
    if os.path.exists('index_with_audio.html'):
        shutil.copy('index_with_audio.html', f'{docs_dir}/index.html')
        print(f"✓ Copied index_with_audio.html as main index.html")
    else:
        shutil.copy('index.html', f'{docs_dir}/index.html')
        print(f"✓ Copied basic index.html (audio version not found)")
    
    # Copy sample audio file if it exists
    if os.path.exists('skeletononthebeat.wav'):
        shutil.copy('skeletononthebeat.wav', f'{docs_dir}/skeletononthebeat.wav')
        print(f"✓ Copied sample audio file")
    else:
        print("⚠️  Sample audio file 'skeletononthebeat.wav' not found")
    
    # Try to export model data if possible
    try:
        if os.path.exists('export_model_data.py'):
            print("Exporting model data...")
            subprocess.run(['python', 'export_model_data.py'], check=True)
            if os.path.exists('model_data.json'):
                shutil.copy('model_data.json', f'{docs_dir}/model_data.json')
                print("Copied model_data.json")
            else:
                print("model_data.json not found, using sample data in HTML")
        else:
            print("export_model_data.py not found, using sample data in HTML")
    except Exception as e:
        print(f"Could not export model data: {e}")
        print("Using sample data embedded in HTML")
    
    # Create enhanced README for the docs folder
    readme_content = """# 🎵 Spotify Popularity Predictor

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
"""
    
    with open(f'{docs_dir}/README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ Created enhanced README.md")
    
    # Create .nojekyll file to prevent Jekyll processing
    with open(f'{docs_dir}/.nojekyll', 'w') as f:
        f.write('')
    print(f"✓ Created .nojekyll file")
    
    # Create a simple 404 page
    error_404_content = """<!DOCTYPE html>
<html>
<head>
    <title>404 - Page Not Found</title>
    <style>
        body { font-family: Arial, sans-serif; background: #191414; color: white; text-align: center; padding: 50px; }
        h1 { color: #1DB954; font-size: 3rem; }
        a { color: #1DB954; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>🎵 404 - Page Not Found</h1>
    <p>The page you're looking for doesn't exist.</p>
    <p><a href="/">← Back to Spotify Popularity Predictor</a></p>
</body>
</html>"""
    
    with open(f'{docs_dir}/404.html', 'w', encoding='utf-8') as f:
        f.write(error_404_content)
    print(f"✓ Created 404.html")
    
    print("\n🎉 GitHub Pages setup with Audio Analysis complete!")
    print("\n🌟 Enhanced Features Added:")
    print("  - Audio file upload simulation")
    print("  - Feature extraction visualization")
    print("  - Interactive audio controls")
    print("  - Real-time predictions")
    print("  - Mobile-responsive design")
    
    print("\n📋 Next steps:")
    print("1. Push this repository to GitHub")
    print("2. Go to Settings > Pages in your GitHub repo")
    print("3. Select 'Deploy from a branch'")
    print("4. Choose 'main' branch and '/docs' folder")
    print("5. Your enhanced site will be available at:")
    print("   https://danielc8.github.io/SpotifyPopularityModel/")
    
    print(f"\n📁 Files ready in '{docs_dir}/' folder:")
    for file in os.listdir(docs_dir):
        file_size = os.path.getsize(f'{docs_dir}/{file}')
        size_str = f"{file_size:,} bytes" if file_size < 1024 else f"{file_size//1024}KB"
        print(f"  - {file} ({size_str})")

if __name__ == "__main__":
    setup_github_pages()
