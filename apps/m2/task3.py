from bs4 import BeautifulSoup, SoupStrainer
import argparse
import time
import lxml

def printAllTags(file_path):
    with open(file_path, encoding='utf-8') as file:
        if file_path.endswith(".html"):
            parser = "html.parser"
        else:
            parser = "lxml-xml"

        only_tags = SoupStrainer(True)
        soup = BeautifulSoup(file, parser, parse_only = only_tags)

        for tag in soup.find_all(True):
            print(tag)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help = "File to be processed")
    args = parser.parse_args()
    start_time = time.perf_counter()
    printAllTags(args.file_path)
    print(time.perf_counter() - start_time)