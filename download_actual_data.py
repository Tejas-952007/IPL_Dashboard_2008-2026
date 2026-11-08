import urllib.request
import os

def download_file(url, filename):
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}. Error: {e}")

if __name__ == "__main__":
    # URLs to a popular GitHub repo containing the IPL dataset (2008-2020/2022)
    matches_url = "https://raw.githubusercontent.com/genieincodebottle/generative-ai/main/docs/ipl-dataset/matches.csv"
    deliveries_url = "https://raw.githubusercontent.com/genieincodebottle/generative-ai/main/docs/ipl-dataset/deliveries.csv"
    
    download_file(matches_url, "matches.csv")
    download_file(deliveries_url, "deliveries.csv")
    
    print("\nData download complete! You can now run the dashboard using: streamlit run app.py")
