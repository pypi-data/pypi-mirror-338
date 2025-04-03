# Getting Started with markdown-dom

This guide will help you get started with using the markdown-dom library to create structured Markdown documents programmatically.

## Installation

Install the library using pip:

```bash
pip install markdown-dom
```

The library requires Python 3.10 or higher.

## Basic Usage

First, import the main classes:

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle
```

### Creating a Simple Section

To create a simple section with a title and content:

```python
# Create a section with a title and some content
section = MarkdownSection(
    MarkdownSectionTitle("Hello World"),
    "This is some content."
)

# Render the section to a Markdown string
markdown = section.render()
print(markdown)
```

This will output:

```markdown
## Hello World
This is some content.
```

### Creating a Section without a Title

You can also create sections without titles:

```python
# Create a section with just content
section = MarkdownSection(
    "This is a paragraph without a title."
)

print(section.render())
```

This will output:

```markdown
This is a paragraph without a title.
```

### Multiple Content Elements

You can add multiple content elements to a section:

```python
section = MarkdownSection(
    MarkdownSectionTitle("Multiple Elements"),
    "First paragraph.",
    "Second paragraph.",
    "- List item 1",
    "- List item 2"
)

print(section.render())
```

This will output:

```markdown
## Multiple Elements
First paragraph.
Second paragraph.
- List item 1
- List item 2
```

## Creating Nested Sections

One of the key features of markdown-dom is the ability to nest sections:

```python
document = MarkdownSection(
    MarkdownSectionTitle("Main Document"),
    "This is the main content.",
    MarkdownSection(
        MarkdownSectionTitle("Section 1"),
        "Content for section 1.",
        MarkdownSection(
            MarkdownSectionTitle("Subsection 1.1"),
            "Content for subsection 1.1."
        )
    ),
    MarkdownSection(
        MarkdownSectionTitle("Section 2"),
        "Content for section 2."
    )
)

print(document.render(section_level=1))
```

This will output:

```markdown
# Main Document
This is the main content.

## Section 1
Content for section 1.

### Subsection 1.1
Content for subsection 1.1.

## Section 2
Content for section 2.
```

## Controlling Heading Levels

By default, sections start with level 2 headings (`##`). You can adjust this using the `section_level` parameter:

```python
section = MarkdownSection(
    MarkdownSectionTitle("Custom Level"),
    "Content with custom heading level."
)

# Render with level 1 heading
print(section.render(section_level=1))

# Render with level 4 heading
print(section.render(section_level=4))
```

This will output:

```markdown
# Custom Level
Content with custom heading level.
```

and

```markdown
#### Custom Level
Content with custom heading level.
```

## Practical Example: Building Documentation

Here's a practical example of building documentation:

```python
def build_documentation() -> str:
    doc = MarkdownSection(
        MarkdownSectionTitle("Project Documentation"),
        "Welcome to the project documentation.",
        MarkdownSection(
            MarkdownSectionTitle("Installation"),
            "Install the project using pip:",
            "```bash",
            "pip install my-project",
            "```"
        ),
        MarkdownSection(
            MarkdownSectionTitle("Usage"),
            "Import the main module:",
            "```python",
            "import my_project",
            "result = my_project.run()",
            "```"
        )
    )
    
    return doc.render(section_level=1)

# Print the documentation
print(build_documentation())
```

This will produce:

```markdown
# Project Documentation
Welcome to the project documentation.

## Installation
Install the project using pip:
```bash
pip install my-project
```

## Usage
Import the main module:
```python
import my_project
result = my_project.run()
```
```

## Next Steps

- See the [API Reference](api.md) for detailed information about the library's classes and methods
- Check the examples in `example.py` for more complex usage patterns
- Explore use cases like building LLM system prompts, dynamic documentation generation, and more