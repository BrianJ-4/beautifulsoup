from bs4 import BeautifulSoup, SoupStrainer
import argparse
import lxml
import time

def printHyperlinks(file_path):
    with open(file_path, encoding='utf-8') as file:
        if file_path.endswith(".html"):
            parser = "html.parser"
        else:
            parser = "lxml-xml"

        only_a_tags = SoupStrainer("a")
        soup = BeautifulSoup(file, parser, parse_only = only_a_tags)
        
        links = soup.find_all("a")
        for link in links:
            print(link)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help = "File to be processed")
    args = parser.parse_args()
    start_time = time.perf_counter()
    printHyperlinks(args.file_path)
    print(time.perf_counter() - start_time)

print("HELLO")