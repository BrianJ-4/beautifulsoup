import pytest

from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer
from . import (
    SoupTest,
)

class TestReplacer(SoupTest):
    """Test SoupReplacer"""

    def test_replace_b_with_blockquote(self):
        html = "<html><body><b>Hello</b> <i>world</i>!</body></html>"
        b_to_blockquote = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html, "html.parser", replacer = b_to_blockquote)
        
        # There should be no <b> tags left
        assert soup.find("b") is None

    def test_replace_multiple_tags(self):
        html = """
            <body>
                <i>One</i>
                <i>Two</i>
                <i>Three</i>
            </body>
        """
        replacer = SoupReplacer("i", "em")
        soup = BeautifulSoup(html, "html.parser", replacer = replacer)
        
        # There should be no <i> tags left
        assert soup.find("i") is None
        
        # All replaced tags should now be <em>
        em_tags = soup.find_all("em")
        assert len(em_tags) == 3

        # Ensure text content is correct
        assert [tag.string for tag in em_tags] == ["One", "Two", "Three"]