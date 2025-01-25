' this needs to be installed pip install requests beautifulsoup4 google-api-python-client scikit-learn
import requests
import csv
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Function to scrape Google search results
def scrape_web(query, num_results=200):
    headers = {"User-Agent": "Mozilla/5.0"}
    results = []
    for start in range(0, num_results, 20):
        url = f"https://www.google.com/search?q={query}&start={start}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: Unable to fetch results from Google. Status code: {response.status_code}")
            break
        soup = BeautifulSoup(response.text, "html.parser")
        for g in soup.find_all("div", class_="tF2Cxc"):
            title = g.find("h3").text if g.find("h3") else "No title"
            link = g.find("a")["href"] if g.find("a") else "No link"
            description = g.find("div", class_="VwiC3b").text if g.find("div", class_="VwiC3b") else "No description"
            results.append({"title": title, "link": link, "description": description})
        if len(results) >= num_results:
            break
    return results

# Function to search YouTube videos using the YouTube Data API
def search_youtube(query, api_key, max_results=50):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(q=query, part="snippet", maxResults=max_results)
    response = request.execute()
    results = []
    for item in response["items"]:
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        video_link = f"https://www.youtube.com/watch?v={item['id']['videoId']}" if "videoId" in item["id"] else "No link"
        results.append({"title": title, "link": video_link, "description": description})
    return results

# Function to classify results into dynamic categories
def classify_results(results):
    if not results:
        print("No results to classify.")
        return {}
    descriptions = [res["title"] + " " + res["description"] for res in results]
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(descriptions)
    num_clusters = min(10, len(descriptions))  # Limit to 10 categories for manageability
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)

    categories = {}
    for i, res in enumerate(results):
        category = f"Category {kmeans.labels_[i]}"
        if category not in categories:
            categories[category] = []
        categories[category].append(res)

    return categories

# Function to save results to a CSV file
def save_to_csv(categories, filename="firstdata.csv"):
    if not categories:
        print("No data to save.")
        return
    all_columns = set(categories.keys())
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        header = ["Category", "Title", "Link", "Description"]
        writer.writerow(header)
        for category, items in categories.items():
            for item in items:
                writer.writerow([category, item["title"], item["link"], item["description"]])

# Main function
def main():
    query = input("Enter your search query: ")
    youtube_api_key = input("Enter your YouTube API key: ")

    print("Scraping the web for results...")
    web_results = scrape_web(query)
    if not web_results:
        print("No web results found. Exiting...")
        return

    print(f"Found {len(web_results)} web results.")
    print("Classifying web results...")
    web_categories = classify_results(web_results)

    print("Searching YouTube for videos...")
    youtube_results = search_youtube(query, youtube_api_key)
    if not youtube_results:
        print("No YouTube results found.")

    print("Classifying YouTube results...")
    youtube_categories = classify_results(youtube_results)

    print("Combining web and YouTube results...")
    combined_categories = {**web_categories, **youtube_categories}

    print("Saving results to CSV...")
    save_to_csv(combined_categories)
    print(f"Results saved to 'firstdata.csv'.")

if __name__ == "__main__":
    main()
