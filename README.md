# Image Scraper

This Python script scrapes images from the [Digital Commonwealth](https://www.digitalcommonwealth.org) website using a list of image IDs. It extracts both the image and its name from the webpage and saves them in the `../downloads/` folder.

## Features
- Reads image IDs from the `imageids` file.
- Constructs URLs using `https://www.digitalcommonwealth.org/search/<id>`.
- Scrapes the image URL from `<img class="img_show">`.
- Extracts the image name from the `<h1>` tag.
- Downloads and saves the image with its extracted name.
- Ensures filenames are clean and valid.

## Requirements

Make sure you have Python installed. Install the necessary dependencies using:
```sh
pip install -r requirements.txt
```

## Usage

1. **Prepare the Image IDs**: Ensure `imageids` file contains one image ID per line.
2. **Run the script**:
   ```sh
   python script.py
   ```
3. **Downloaded Images**: Images will be saved in the `../downloads/` folder with their respective names.

## File Structure
```
project_folder/
│-- script.py             # Main script
│-- requirements.txt      # Dependencies
│-- README.md             # Documentation
│-- imageids              # File with list of IDs
│-- ./downloads/         # Folder where images are saved
```

## Notes
- If the `../downloads/` folder does not exist, the script will create it.
- The script uses `User-Agent` headers to avoid request blocking.
- If an image or name is not found, the script will skip that ID.

## License
This project is open-source and free to use. Feel free to modify and enhance it!

