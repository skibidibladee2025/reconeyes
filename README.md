<div align="center">
<h1>👁️ OpenEyes 👁️<h1>

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/OpenEyes)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/OpenEyes)
![GitHub size](https://img.shields.io/github/languages/code-size/YOUR_USERNAME/OpenEyes)
![GitHub lastcommit](https://img.shields.io/github/last-commit/YOUR_USERNAME/OpenEyes)

<a href="https://twitter.com/intent/follow?screen_name=YOUR_TWITTER">

![Github twitter](https://img.shields.io/twitter/follow/YOUR_TWITTER?label=Follow%20%40%20Twitter&style=social)
</a>
</div>
<br>
Open IP Cameras, with default credentials - publicly accessible, scrapped from http://www.insecam.org/ and https://hacked.camera. Every camera is placed on a Google Map with live stream and information.

## 🚀 Quick Start

### Option 1: Netlify Static Site (Recommended - No Server Needed)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/OpenEyes.git
   cd OpenEyes
   ```

2. **Deploy to Netlify:**
   - Go to [Netlify](https://netlify.com) and sign up/login
   - Click "New site from Git"
   - Connect your GitHub repository
   - Set build command: (leave empty)
   - Set publish directory: `deploy`
   - Click "Deploy site"

3. **Your site is live!** The map will load with camera markers. Click "Refresh Cameras" to fetch new data from insecam.org.

### Option 2: Local Flask App
1. **Clone and setup:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/OpenEyes.git
   cd OpenEyes
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run the GUI (Windows):**
   ```bash
   python app/gui.py
   ```
   Or run the web version:
   ```bash
   python app/srv.py
   ```

3. **Open in browser:** Visit `http://127.0.0.1:5001`

## 📋 Prerequisites
- Python 3.8+ (for local development)
- Git
- Netlify account (for deployment)

## 🛠️ Features
- **Interactive Google Maps** with camera locations
- **Live camera streams** in popups
- **Dynamic data refresh** (Netlify version)
- **Cross-platform** GUI and web interfaces
- **Docker support** for containerized deployment

## 🌐 Netlify Deployment Details
The static version includes:
- Google Maps integration
- Camera markers with details
- Live stream iframes
- Refresh button that fetches new data via serverless functions

### Updating Camera Data:
- The "Refresh Cameras" button dynamically fetches from insecam.org
- Sample data is included for initial load
- No backend server required!

## 🐳 Docker Deployment
```bash
docker build -t openeyes .
docker run -p 5001:5001 openeyes
```

## 📁 Project Structure
```
OpenEyes/
├── app/                    # Flask application
│   ├── srv.py             # Main Flask server
│   ├── gui.py             # Tkinter GUI
│   ├── controllers.py     # Scraping logic
│   ├── config.py          # Configuration
│   └── templates/         # HTML templates
├── deploy/                # Static site for Netlify
│   ├── index.html
│   ├── static/
│   └── .netlify/functions/
├── requirements.txt       # Python dependencies
└── README.md
```

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License
This project is for educational purposes only. Use responsibly.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/YOUR_USERNAME)
