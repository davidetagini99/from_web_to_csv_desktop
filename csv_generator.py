import os
from urllib.parse import urljoin
import requests
import csv
from bs4 import BeautifulSoup

def generate_csv(link, class_name):
    if not link or not class_name:
        print("Please fill in both fields.")
        return False

    # Define user-agent headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Make the request with headers
    response = requests.get(link, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all(class_=class_name)
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        csv_file_path = os.path.join(download_folder, 'scraped_data.csv')
        
        # Open the CSV file in append mode
        with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile: # I put a instead of w to let the csv file being overrided
            csv_writer = csv.writer(csvfile)
            for element in elements:
                # Get text content, escape special characters to prevent XSS
                text_content = BeautifulSoup(str(element), 'html.parser').text.strip()
                image_src = None
                # If the element is an image, get its source URL
                if element.name == 'img' and 'src' in element.attrs:
                    # If the image source is relative, convert it to absolute URL
                    if not element['src'].startswith('http'):
                        image_src = urljoin(link, element['src'])
                    else:
                        image_src = element['src']
                csv_writer.writerow([text_content, image_src])
        return True
    else:
        print("Failed to fetch the webpage. Please check the URL.")
        return False
