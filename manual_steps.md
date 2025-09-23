# Manual Setup Steps

Since I can't run commands directly, here are the exact steps to clean up and commit to GitHub:

## 🧹 Step 1: Clean Up Files

Run this in your terminal:
```bash
python final_cleanup.py
```

This will remove all unnecessary files and keep only:
- `index.html` (main website)
- `Spotify.ipynb` (your analysis)
- `README.md` (documentation)
- `requirements.txt` (dependencies)
- `export_model_data.py` (model exporter)
- `setup_github_pages.py` (deployment helper)
- `.gitignore` (Git ignore rules)

## 📊 Step 2: Setup GitHub Pages

```bash
python setup_github_pages.py
```

This creates a `docs/` folder with your website files.

## 🔧 Step 3: Initialize Git and Commit

```bash
# Initialize Git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Spotify Popularity Predictor web app"

# Add your GitHub repository as remote
git remote add origin https://github.com/DanielC8/SpotifyPopularityModel.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 🌐 Step 4: Enable GitHub Pages

1. Go to https://github.com/DanielC8/SpotifyPopularityModel
2. Click **Settings** tab
3. Scroll to **Pages** in left sidebar
4. Under **Source**, select "Deploy from a branch"
5. Choose **main** branch and **/docs** folder
6. Click **Save**

## ✅ Final Result

Your website will be live at:
**https://danielc8.github.io/SpotifyPopularityModel/**

## 🚨 Alternative: Quick Setup

If you prefer, just run the batch file:
```bash
git_setup.bat
```

This will do all the steps automatically!

## 📁 Final File Structure

```
SpotifyPopularityModel/
├── docs/
│   ├── index.html          # GitHub Pages website
│   ├── model_data.json     # Exported model data
│   └── .nojekyll          # GitHub Pages config
├── index.html             # Standalone version
├── Spotify.ipynb          # Your analysis notebook
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── export_model_data.py   # Model data exporter
├── setup_github_pages.py  # Deployment helper
└── .gitignore            # Git ignore rules
```

## 🎯 What You'll Have

✅ Clean, professional GitHub repository  
✅ Live website on GitHub Pages  
✅ Mobile-friendly Spotify popularity predictor  
✅ Interactive audio feature controls  
✅ Song comparison functionality  
✅ Beautiful Spotify-themed design  

Your project will look amazing on GitHub and the live website will work perfectly!
