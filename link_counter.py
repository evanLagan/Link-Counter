import subprocess # Command Line function stuff
import re # For regex
import sys # System stuff
import requests

def fetch_website_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status() 
        # Ensure the content is decoded as UTF-8
        response.encoding = 'utf-8'
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None

def extract_links(html_content):
    # Regex to find all href links
    link_pattern = r'href="([^"]+)"'
    links = re.findall(link_pattern, html_content)
    return links

def main():
    # Get the website URL from the user
    website_url = input("Enter the website URL (e.g., https://example.com): ")
    if not website_url.startswith("http"):
        website_url = "https://" + website_url

    # Fetch the website content
    html_content = fetch_website_content(website_url)

    # Extract and count all of the links
    links = extract_links(html_content)

    for link in links:
        print(link)

    print(f"Number of links found: {len(links)}")

    

if __name__ == "__main__":
    main()
