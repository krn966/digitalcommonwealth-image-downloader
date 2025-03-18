import os
import requests
from bs4 import BeautifulSoup

# Set folder paths
DOWNLOAD_FOLDER = "./downloads"
IMAGEIDS_FILE = "imageids"  # Adjust if the file is in a different location

# Ensure the download folder exists
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def get_image_details(url):
    """Scrape the image URL and name from the given page URL."""
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find image src from img tag with class "img_show"
        img_tag = soup.find('img', class_='img_show')
        image_src = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None

        # Find the image name from h1 tag
        h1_tag = soup.find('h1')
        image_name = h1_tag.text.strip() if h1_tag else "unnamed_image"

        return image_src, image_name
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None, None

def download_image(image_url, image_name):
    """Download the image and save it with the extracted name."""
    try:
        if not image_url:
            print("No image URL found, skipping download.")
            return

        response = requests.get(image_url, headers={'User-Agent': 'Mozilla/5.0'}, stream=True)
        response.raise_for_status()

        # Clean filename (remove invalid characters)
        safe_name = "".join(c for c in image_name if c.isalnum() or c in " _-").strip()
        file_path = os.path.join(DOWNLOAD_FOLDER, f"{safe_name}.jpg")

        # Save the image
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Downloaded: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {image_url}: {e}")

def main():
    """Read IDs from the file and process each one."""
    if not os.path.exists(IMAGEIDS_FILE):
        print(f"File '{IMAGEIDS_FILE}' not found!")
        return

    with open(IMAGEIDS_FILE, 'r') as file:
        ids = [line.strip() for line in file if line.strip()]

    for img_id in ids:
        page_url = f"https://www.digitalcommonwealth.org/search/commonwealth:{img_id}"
        print(f"Processing: {page_url}")

        image_url, image_name = get_image_details(page_url)
        
        if image_url and image_name:
            download_image(image_url, image_name)
        else:
            print(f"Skipping {img_id}, no valid image found.")

if __name__ == "__main__":
    main()
