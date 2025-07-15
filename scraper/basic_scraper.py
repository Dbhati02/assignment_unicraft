import requests
from bs4 import BeautifulSoup
import re

def extract_contacts(soup):
    text = soup.get_text()
    emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    return emails[0] if emails else "Not Found"

def extract_social_links(soup):
    links = soup.find_all('a', href=True)
    socials = []
    for link in links:
        href = link['href']
        if any(platform in href for platform in ["linkedin.com", "twitter.com", "facebook.com", "instagram.com"]):
            socials.append(href)
    return ", ".join(set(socials)) if socials else "Not Found"

def extract_description(soup):
    meta_desc = soup.find("meta", attrs={"name": "description"})
    og_desc = soup.find("meta", attrs={"property": "og:description"})
    if meta_desc and meta_desc.get("content"):
        return meta_desc["content"]
    elif og_desc and og_desc.get("content"):
        return og_desc["content"]
    return "Not Found"

def fetch_basic_info(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, timeout=10, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        if not soup:
            return {
                "Company Name": "Not Found",
                "Website URL": url,
                "Contact Info": "No HTML Content",
                "Social Links": "",
                "Description": ""
            }

        title = soup.title.string.strip() if soup.title and soup.title.string else "N/A"
        contact = extract_contacts(soup)
        socials = extract_social_links(soup)
        description = extract_description(soup)

        return {
            "Company Name": title,
            "Website URL": url,
            "Contact Info": contact,
            "Social Links": socials,
            "Description": description
        }

    except Exception as e:
        return {
            "Company Name": "Error",
            "Website URL": url,
            "Contact Info": str(e),
            "Social Links": "",
            "Description": ""
        }
