import praw
import requests
import os
from urllib.parse import urlparse

# Initialize Reddit API
reddit = praw.Reddit(
    client_id="Ye0hGHYVPuuMe_eunUGvXQ",
    client_secret="B3uzhCj5s2ZzPGozTx2KX8lyOIpoVw",
    user_agent="ImageDownloader by u/HorseActual",
)

print(f"Connected to Reddit: {reddit.read_only}")

# Directory to save images
output_dir = "reddit_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Supported image extensions
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')

# Counter for image numbering
image_counter = 1

# Get top 30 posts from r/recipes
for submission in reddit.subreddit("recipes").hot(limit=30):
    if submission.stickied:
        continue  # Skip pinned posts
    
    url = submission.url
    parsed_url = urlparse(url)
    file_ext = os.path.splitext(parsed_url.path)[1].lower()
    
    # Check if URL is a direct image link
    if file_ext in IMAGE_EXTENSIONS:
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                # Extract file extension from URL
                ext = file_ext if file_ext else '.jpg'  # Default to .jpg if no extension
                
                # New filename: "1.jpg", "2.png", etc.
                new_filename = f"{image_counter}.jpg"
                save_path = os.path.join(output_dir, new_filename)
                
                # Save the image
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                
                print(f"Downloaded: {new_filename} (Original URL: {url})")
                image_counter += 1  # Increment counter
            else:
                print(f"Failed to download: {url} (Status: {response.status_code})")
        except Exception as e:
            print(f"Error downloading {url}: {e}")
    else:
        print(f"Skipping non-image post: {url}")

print(f"Download complete! Saved {image_counter - 1} images.")