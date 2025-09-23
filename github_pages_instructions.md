# GitHub Pages Deployment Instructions

## 🚀 Quick Setup

1. **Prepare files for GitHub Pages:**
   ```bash
   python setup_github_pages.py
   ```

2. **Create a new GitHub repository:**
   - Go to GitHub.com
   - Click "New repository"
   - Name it something like "spotify-popularity-predictor"
   - Make it public
   - Don't initialize with README (we have our own)

3. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Spotify Popularity Predictor"
   git branch -M main
   git remote add origin https://github.com/yourusername/spotify-popularity-predictor.git
   git push -u origin main
   ```

4. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Click "Settings" tab
   - Scroll down to "Pages" in the left sidebar
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch and "/docs" folder
   - Click "Save"

5. **Access your site:**
   - Your site will be available at: `https://yourusername.github.io/spotify-popularity-predictor/`
   - It may take a few minutes to deploy

## 📁 File Structure

```
your-repo/
├── docs/                    # GitHub Pages files
│   ├── index.html          # Main website
│   ├── model_data.json     # Model data (if exported)
│   ├── .nojekyll          # Prevents Jekyll processing
│   └── README.md          # Documentation
├── index.html             # Standalone version
├── setup_github_pages.py  # Setup script
└── other files...
```

## 🎯 Features

Your deployed site will have:
- ✅ Song comparison (actual vs predicted popularity)
- ✅ Interactive audio feature sliders
- ✅ Real-time predictions
- ✅ Mobile-responsive design
- ✅ No server required (pure client-side)

## 🔧 How It Works

The website uses:
- **HTML/CSS/JavaScript** - No backend required
- **Client-side predictions** - Simplified model runs in browser
- **Sample data** - 500+ real songs for testing
- **Feature importance** - Weighted prediction algorithm

## 📱 Mobile Friendly

The site automatically adapts to mobile devices with:
- Responsive grid layout
- Touch-friendly controls
- Optimized font sizes

## 🎨 Customization

You can easily customize:
- Colors in the CSS section
- Sample songs in the JavaScript
- Feature weights for predictions
- Add more audio features

## 🚨 Troubleshooting

**Site not loading?**
- Check that GitHub Pages is enabled
- Ensure you selected "/docs" folder
- Wait 5-10 minutes for deployment

**Predictions seem off?**
- The model is simplified for browser use
- Real accuracy depends on the full Random Forest model
- This is a demonstration version

**Want better accuracy?**
- Run `python export_model_data.py` to export real model data
- This creates `model_data.json` with actual model parameters
