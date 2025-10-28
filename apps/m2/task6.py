from bs4 import BeautifulSoup, SoupReplacer
import argparse
import lxml
import time

def replaceBTags(file_path):
    with open(file_path, encoding='utf-8') as file:
        if file_path.endswith(".html"):
            parser = "html.parser"
        else:
            parser = "lxml-xml"

        # Create replacer and pass to soup
        b_to_blockquote = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(file, parser, replacer = b_to_blockquote)
        
        with open("task6_output.html", "w", encoding="utf-8") as out_file:
            out_file.write(str(soup))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help = "File to be processed")
    args = parser.parse_args()
    start_time = time.perf_counter()
    replaceBTags(args.file_path)
    print(time.perf_counter() - start_time)