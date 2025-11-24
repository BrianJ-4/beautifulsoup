import pytest

from bs4 import BeautifulSoup
from . import (
    SoupTest,
)

class TestIter(SoupTest):
    """Test Soup Iteration"""

    def test_iter_simple_tree(self):
        html = "<div><p>Hello</p></div>"
        soup = BeautifulSoup(html, "html.parser")

        nodes = list(soup)
        types = [type(n) for n in nodes]

        assert types[0].__name__ == "BeautifulSoup"
        assert str(nodes[1]) == "<div><p>Hello</p></div>"
        assert str(nodes[2]) == "<p>Hello</p>"
        assert nodes[3] == "Hello"

    def test_iter_empty_document(self):
        html = ""
        soup = BeautifulSoup(html, "html.parser")

        result = list(soup)
        print(result)

        # Yields the document root
        assert len(result) == 1
        assert result[0] is soup

    def test_iter_mixed_content(self):
        html = "<div>Text <b>bold</b> end</div>"
        soup = BeautifulSoup(html, "html.parser")

        result = [str(node) for node in soup]

        # Expected DFS order
        assert result == [
            str(soup),
            "<div>Text <b>bold</b> end</div>",
            "Text ",
            "<b>bold</b>",
            "bold",
            " end",
        ]

    def test_iter_deep_nested(self):
        html = "<a><b><c><d>Hi</d></c></b></a>"
        soup = BeautifulSoup(html, "html.parser")

        nodes = [str(n) for n in soup]

        assert nodes == [
            str(soup),
            "<a><b><c><d>Hi</d></c></b></a>",
            "<b><c><d>Hi</d></c></b>",
            "<c><d>Hi</d></c>",
            "<d>Hi</d>",
            "Hi"
        ]

    def test_iter_with_comment(self):
        html = "<div><!--comment--> text </div>"
        soup = BeautifulSoup(html, "html.parser")

        nodes = list(soup)

        # Find comment node
        comment_nodes = [n for n in nodes if type(n).__name__ == "Comment"]
        assert len(comment_nodes) == 1
        assert str(comment_nodes[0]) == "comment"