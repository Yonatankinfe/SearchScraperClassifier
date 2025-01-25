# SearchScraperClassifier
🌐📹 Automated search result aggregation and categorization tool combining web scraping and YouTube API integration with ML-powered clustering.

---

## Description  
A comprehensive Python pipeline that aggregates and categorizes search results from both web pages and YouTube videos using TF-IDF vectorization and K-Means clustering. Ideal for content analysis, market research, and trend monitoring.

```python
# Key Features
- Google Search scraping (200+ results)
- YouTube Data API integration
- Dynamic category generation based on content
- TF-IDF text vectorization
- Automatic cluster optimization
- Cross-platform results merging
- CSV export with category labels
```

---

# 📂 SearchScraperClassifier

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-requests%20|%20scikit--learn%20|%20beautifulsoup4-orange)

Multi-source intelligence aggregator for web and video content analysis.

## 🚀 Overview
This tool combines three powerful capabilities:
1. **Web Scraping** - Extracts Google search results (titles, URLs, snippets)
2. **YouTube Integration** - Fetches video data through official API
3. **AI Categorization** - Groups results into dynamic categories using:
   - Natural Language Processing (TF-IDF)
   - Machine Learning (K-Means clustering)

## 🛠️ Installation
```bash
git clone https://github.com/Yonatankinfe/SearchScraperClassifier.git
cd SearchScraperClassifier
pip install -r requirements.txt
```

## 📋 Requirements File
```text
requests==2.31.0
beautifulsoup4==4.12.3
google-api-python-client==2.104.0
scikit-learn==1.3.2
pandas==2.1.4
```

## 🔑 Configuration
1. Get YouTube API Key from [Google Cloud Console](https://console.cloud.google.com/)
2. Enable YouTube Data API v3 for your project

## 🖥️ Usage
```bash
python search_classifier.py
```
Follow the interactive prompts:
1. Enter search query (e.g., "Alex Pereira UFC")
2. Provide YouTube API key
3. Let the script automatically:
   - Scrape web results
   - Fetch YouTube videos
   - Classify into categories
   - Generate output file

## 📊 Output Structure
`firstdata.csv` columns:
| Category | Title | Link | Description |
|----------|-------|------|-------------|
| Category 0 | Article Title | https://... | Text snippet |
| Category 1 | Video Title | https://... | Video description |

## ⚙️ Technical Details

### Web Scraper
- Bypasses basic anti-scraping measures with User-Agent rotation
- Handles pagination for deep result extraction
- Error handling for failed requests

### YouTube Integration
- Official API integration for reliable video data
- Returns full video descriptions
- Handles missing video IDs gracefully

### Smart Clustering
```python
# Dynamic cluster calculation
num_clusters = min(10, len(descriptions))  # Auto-adjusts to data size
# Combined text processing
descriptions = [res["title"] + " " + res["description"] for res in results]
```

## ⚠️ Important Notes
- Google may block scrapers - use proxies for heavy usage
- YouTube API has daily quota limits
- Cluster quality improves with more results

## 🔧 Customization
```python
# Adjust these parameters:
SCRAPE_RESULTS = 200  # Web results to collect
YOUTUBE_MAX = 50      # Video results to fetch
STOP_WORDS = "english" # Add custom stopwords
CLUSTER_LIMIT = 10    # Max categories to create
```

## 🤝 Contributing
Contribution guidelines:
1. Fork the repository
2. Create feature branch
3. Add tests for new features
4. Submit pull request

## 📜 License
MIT License - see [LICENSE](LICENSE) for details
```
