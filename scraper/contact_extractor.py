import re

def extract_contacts(soup):
    # Search for mailto: links
    mailto_links = soup.select('a[href^=mailto]')
    if mailto_links:
        return mailto_links[0].get('href').replace('mailto:', '')

    # Fallback: Search for plain emails in text
    text = soup.get_text()
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return emails[0] if emails else "Not Found"
