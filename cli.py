import argparse
import pandas as pd
from scraper.basic_scraper import fetch_basic_info

def run_scraper(urls):
    results = [fetch_basic_info(url) for url in urls]
    df = pd.DataFrame(results)
    df.to_csv("data/output.csv", index=False)
    print(" Scraping done! Check: data/output.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--urls', nargs='+', help='List of website URLs')
    args = parser.parse_args()

    if args.urls:
        run_scraper(args.urls)
    else:
        print(" No URLs provided.")
