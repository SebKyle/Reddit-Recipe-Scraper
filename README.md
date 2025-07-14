# Reddit Recipe Scraper

A Python script that extracts recipes from r/recipes subreddit and compiles them into a Microsoft Word document.

## Features

- Fetches the 30 hottest posts from r/recipes
- Skips pinned/stickied posts
- Extracts post title, author, and first comment (typically the recipe)
- Formats content into a structured Word document
- Separate image downloader for recipe images

## Prerequisites

- Python 3.6+
- Reddit API credentials (create at [Reddit Apps](https://www.reddit.com/prefs/apps))
- Required Python packages:
  ```bash
  pip install praw python-docx


[DEFAULT]
- client_id=your_client_id
- client_secret=your_client_secret
- user_agent=recipe_scraper/v1.0 by u/HorseActual


## Known Issues
- Recipe Identification: Not every first comment contains the actual recipe

- Image Handling:

- Not all recipes have images

- Some images may fail to download

- Images aren't automatically inserted into the Word document

- Formatting: Some recipes may have poor formatting in the Word document

## Future Improvements
- Implement better recipe detection (maybe look for keywords like "ingredients")

- Auto-insert images into the Word document

- Add better formatting for ingredients/instructions

- Create a table of contents

- Add error handling for missing API credentials

## Contributing
Pull requests are welcome! Please open an issue first to discuss what you'd like to change.
