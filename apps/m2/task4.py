from bs4 import BeautifulSoup, SoupStrainer
import argparse
import time
import lxml

def printAllIDTags(file_path):
    with open(file_path, encoding='utf-8') as file:
        if file_path.endswith(".html"):
            parser = "html.parser"
        else:
            parser = "lxml-xml"

        only_id_tags = SoupStrainer(True, id = True)
        soup = BeautifulSoup(file, parser, parse_only = only_id_tags)
        
        tags = soup.find_all(True, id = True)
        for tag in tags:
            print(tag)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help = "File to be processed")
    args = parser.parse_args()
    start_time = time.perf_counter()
    printAllIDTags(args.file_path)
    print(time.perf_counter() - start_time)