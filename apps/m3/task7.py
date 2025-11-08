from bs4 import BeautifulSoup, SoupReplacer
import argparse
import lxml
import time

def addAttribute(file_path):
    with open(file_path, encoding = 'utf-8') as file:
        if file_path.endswith(".html"):
            parser = "html.parser"
        else:
            parser = "lxml-xml"

        def add_class_attr(tag):
            # Add class = "test" to all <p> tags
            if tag.name == "p":
                tag.attrs["class"] = "test"
        
        replacer = SoupReplacer(xformer = add_class_attr)
        soup = BeautifulSoup(file, parser, replacer = replacer)

        with open("task7_output.html", "w", encoding = "utf-8") as out_file:
            out_file.write(str(soup))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help = "File to be processed")
    args = parser.parse_args()
    start_time = time.perf_counter()
    addAttribute(args.file_path)
    print(time.perf_counter() - start_time)