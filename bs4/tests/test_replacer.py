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

    def test_remove_class_attr(self):
        def remove_class_attr(tag):
            if "class" in tag.attrs:
                print(f"Removing class from <{tag.name}>")
                del tag.attrs["class"]

        html = "<html><body><p class='text'>Hello</p><div id='main' class='container'>World</div></body></html>"
        class_deleter = SoupReplacer(xformer = remove_class_attr)
        soup = BeautifulSoup(html, "html.parser", replacer = class_deleter)

        for tag in soup.find_all(True):
            assert "class" not in tag.attrs

    def test_attrs_xformer_add_attribute(self):
        # Add the tag type as a attribute
        def add_data_attr(tag):
            attrs = dict(tag.attrs)
            attrs["data-tag"] = tag.name
            return attrs

        html = "<html><body><p>Hello</p><div>World</div></body></html>"
        replacer = SoupReplacer(attrs_xformer = add_data_attr)
        soup = BeautifulSoup(html, "html.parser", replacer = replacer)

        for tag in soup.find_all(True):
            assert "data-tag" in tag.attrs
            assert tag.attrs["data-tag"] == tag.name

    def test_xformer_in_place_removal(self):
        # Remove style attribute
        def remove_style(tag):
            if "style" in tag.attrs:
                del tag.attrs["style"]

        html = "<p style='color:red;'>Hello</p><span>No style</span>"
        replacer = SoupReplacer(xformer = remove_style)
        soup = BeautifulSoup(html, "html.parser", replacer = replacer)

        for tag in soup.find_all(True):
            assert "style" not in tag.attrs

    def test_non_matching_tags_unchanged(self):
        def rename_bold(tag):
            if tag.name == "b":
                return "strong"
            return tag.name

        html = "<i>italic</i><u>underline</u>"
        replacer = SoupReplacer(name_xformer = rename_bold)
        soup = BeautifulSoup(html, "html.parser", replacer = replacer)

        # No tags should have changed since no <b> tags in input
        assert str(soup) == html

    def test_multiple_replacers(self):
        # First replacer: rename <b> tag to <strong>
        replacer1 = SoupReplacer("b", "strong")

        # Second replacer: remove class attributes
        def remove_class(tag):
            tag.attrs.pop("class", None)
        replacer2 = SoupReplacer(xformer = remove_class)

        html = "<b class='bold'>Hello</b>"
        soup = BeautifulSoup(html, "html.parser", replacer = replacer1)
        soup = BeautifulSoup(str(soup), "html.parser", replacer = replacer2)

        tag = soup.find("strong")
        assert tag is not None
        assert "class" not in tag.attrs

    def test_combined_transformations(self):
        # Replace <a> with <button>
        def rename_links(tag):
            return "button" if tag.name == "a" else tag.name

        # Rename href to data-href
        def rebuild_attrs(tag):
            attrs = {}
            if "href" in tag.attrs:
                attrs["data-href"] = tag.attrs["href"]
            return attrs

        # Add new class
        def add_class(tag):
            tag.attrs["class"] = ["link-button"]

        html = "<a href='page.html'>Click</a>"
        replacer = SoupReplacer(
            name_xformer = rename_links,
            attrs_xformer = rebuild_attrs,
            xformer = add_class,
        )

        soup = BeautifulSoup(html, "html.parser", replacer = replacer)
        tag = soup.find("button")

        assert tag is not None
        assert "data-href" in tag.attrs
        assert tag.attrs["class"] == ["link-button"]