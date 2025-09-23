"""
Setup script for GitHub Pages deployment
"""
import os
import shutil
import json

def setup_github_pages():
    """Prepare files for GitHub Pages deployment"""
    
    print("🚀 Setting up for GitHub Pages deployment...")
    
    # Create docs folder (GitHub Pages can serve from docs/)
    docs_dir = 'docs'
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.makedirs(docs_dir)
    
    # Copy the main HTML file
    shutil.copy('index.html', f'{docs_dir}/index.html')
    print(f"✓ Copied index.html to {docs_dir}/")
    
    # Try to export model data if possible
    try:
        if os.path.exists('export_model_data.py'):
            print("📊 Exporting model data...")
            exec(open('export_model_data.py').read())
            if os.path.exists('model_data.json'):
                shutil.copy('model_data.json', f'{docs_dir}/model_data.json')
                print("✓ Copied model_data.json")
            else:
                print("⚠️  model_data.json not found, using sample data in HTML")
        else:
            print("⚠️  export_model_data.py not found, using sample data in HTML")
    except Exception as e:
        print(f"⚠️  Could not export model data: {e}")
        print("   Using sample data embedded in HTML")
    
    # Create README for the docs folder
    readme_content = """# Spotify Popularity Predictor

This is a static web application that predicts Spotify song popularity using machine learning.

## Features
- Compare actual vs predicted song popularity
- Interactive audio feature controls
- Real-time predictions
- Mobile-friendly design

## Usage
Visit the deployed site or open `index.html` in your browser.

## How it works
The app uses a simplified version of a Random Forest model trained on Spotify data. 
Predictions are made client-side using JavaScript.
"""
    
    with open(f'{docs_dir}/README.md', 'w') as f:
        f.write(readme_content)
    
    print(f"✓ Created README.md in {docs_dir}/")
    
    # Create .nojekyll file to prevent Jekyll processing
    with open(f'{docs_dir}/.nojekyll', 'w') as f:
        f.write('')
    print(f"✓ Created .nojekyll file")
    
    print("\n🎉 GitHub Pages setup complete!")
    print("\nNext steps:")
    print("1. Push this repository to GitHub")
    print("2. Go to Settings > Pages in your GitHub repo")
    print("3. Select 'Deploy from a branch'")
    print("4. Choose 'main' branch and '/docs' folder")
    print("5. Your site will be available at: https://yourusername.github.io/yourreponame/")
    print(f"\nFiles ready in '{docs_dir}/' folder:")
    
    for file in os.listdir(docs_dir):
        print(f"  - {file}")

if __name__ == "__main__":
    setup_github_pages()
