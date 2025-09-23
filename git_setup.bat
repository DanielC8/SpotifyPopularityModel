@echo off
echo 🧹 Cleaning up project...
python final_cleanup.py

echo.
echo 📊 Setting up GitHub Pages...
python setup_github_pages.py

echo.
echo 🔧 Initializing Git repository...
git init

echo.
echo 📁 Adding files to Git...
git add .

echo.
echo 💾 Creating initial commit...
git commit -m "Initial commit: Spotify Popularity Predictor web app"

echo.
echo 🌐 Adding GitHub remote...
git remote add origin https://github.com/DanielC8/SpotifyPopularityModel.git

echo.
echo 🚀 Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo ✅ Done! Your repository is now on GitHub.
echo 🌐 Visit: https://github.com/DanielC8/SpotifyPopularityModel
echo 📱 Live site will be at: https://danielc8.github.io/SpotifyPopularityModel/
echo.
echo Next steps:
echo 1. Go to your GitHub repository
echo 2. Click Settings ^> Pages
echo 3. Select "Deploy from a branch"
echo 4. Choose "main" branch and "/docs" folder
echo 5. Your site will be live in a few minutes!

pause
