# Milestone-4

## Milestone 4 Technical Brief

Milestone 4 introduces the ability to iterate directly over a BeautifulSoup object. Instead of traversing the document manually, users can now write:
```
for node in soup:
    # Do something
```

This feature treats the parsed HTML document as a sequence of nodes and produces them one at a time in a predictable order.

## How it Works 

The Soup object implements the Python iterator by returning a generator that performs a DFS traversal of the parse tree. Each node is yielded in preorder (parent before children).

The generator yields:
* The document root
* Every Tag node
* Text nodes (NavigableString)
* Comments and other types