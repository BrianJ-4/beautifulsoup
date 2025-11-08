# Milestone-3

## Milestone 3 Implementation Overview

Milestone 3 expands the existing SoupReplacer by allowing transformations to occur immediately as each tag is created during parsing. Now, the replacer can modify a tag’s name, alter or rebuild its attributes, and perform in-place edits directly within the parsing process.

The new SoupReplacer accepts three optional functions:
* name_xformer(tag) – returns a new tag name.
* attrs_xformer(tag) – returns a new attribute dictionary.
* xformer(tag) – modifies the tag directly, in place.

For example:
```
def remove_class(tag):
    tag.attrs.pop("class", None)

replacer = SoupReplacer(
    name_xformer=lambda t: "strong" if t.name == "b" else t.name,
    xformer=remove_class
)

html = "<b class='bold'>Hello</b>"
soup = BeautifulSoup(html, "html.parser", replacer=replacer)
print(soup)
```
Output:
```
<strong>Hello</strong>
```

## Comparison to Milestone 2

In Milestone 2, the SoupReplacer supported only a simple replacement model:
```
SoupReplacer("b", "blockquote")
```

This allowed one tag to be replaced by another but could not modify attributes, handle multiple tag types, or perform any kind of dynamic transformation. It worked well for basic renaming but was limited.

Milestone 3 improves this by introducing transformer functions that make the API far more powerful and extensible. Instead of being limited to static replacements, users can now define custom rules that can inspect and modify any part of a tag.

## Recommendation
The Milestone 3 design should be the foundation on which any new improvements should be built on. It unifies all forms of tag transformation under one consistent interface, and this is both easier for users and more efficient since transformations happen in a single pass during parsing rather than requiring a post-processing step.