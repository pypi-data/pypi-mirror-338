# markdown-dom API Reference

This document provides detailed information about the classes and methods available in the markdown-dom library.

## Core Classes

### `MarkdownSectionTitle`

A class representing a Markdown section title.

```python
from markdown_dom import MarkdownSectionTitle

title = MarkdownSectionTitle("My Section")
```

#### Constructor

```python
MarkdownSectionTitle(title: str)
```

- **Parameters**:
  - `title`: The text of the section title.

#### Attributes

- `title`: The text of the section title.

### `MarkdownSection`

A class that represents a section in a Markdown document, which can contain text content and nested sections.

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle

section = MarkdownSection(
    MarkdownSectionTitle("My Section"),  
    "Content goes here"
)
```

#### Constructor

```python
MarkdownSection(
    markdown_title_or_element: MarkdownSectionTitle | MarkdownSection | str,
    *elements: MarkdownSection | str | None,
)
```

- **Parameters**:
  - `markdown_title_or_element`: Either a `MarkdownSectionTitle` object (for a section with a title) or the first content element.
  - `*elements`: Additional content elements (strings, nested `MarkdownSection` objects, or `None` values). `None` values will be filtered out.

#### Attributes

- `markdown_title`: The title text of the section (optional).
- `elements`: A list of content elements (strings or nested `MarkdownSection` objects).

#### Methods

##### `render(*, section_level: int = 2) -> str`

Renders the section as a Markdown string.

- **Parameters**:
  - `section_level`: The heading level to use for the section title (default: 2).
- **Returns**:
  - A string containing the rendered Markdown.

## Usage Patterns

### Basic Section with Title

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle

section = MarkdownSection(
    MarkdownSectionTitle("Hello World"),
    "This is a paragraph."
)

print(section.render())  # Default section_level is 2
```

Output:
```markdown
## Hello World
This is a paragraph.
```

### Section without Title

```python
from markdown_dom import MarkdownSection

section = MarkdownSection(
    "This is a paragraph without a title."
)

print(section.render())
```

Output:
```markdown
This is a paragraph without a title.
```

### Nested Sections

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle

section = MarkdownSection(
    MarkdownSectionTitle("Parent Section"),
    "Parent content.",
    MarkdownSection(
        MarkdownSectionTitle("Child Section"),
        "Child content."
    )
)

print(section.render(section_level=1))
```

Output:
```markdown
# Parent Section
Parent content.

## Child Section
Child content.
```

### Multiple Content Elements

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle

section = MarkdownSection(
    MarkdownSectionTitle("Multiple Elements"),
    "First paragraph.",
    "Second paragraph.",
    "- List item 1",
    "- List item 2"
)

print(section.render())
```

Output:
```markdown
## Multiple Elements
First paragraph.
Second paragraph.
- List item 1
- List item 2
```

### Handling None Values

Any `None` values passed as elements will be automatically filtered out:

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle

section = MarkdownSection(
    MarkdownSectionTitle("Filtered Elements"),
    "This stays.",
    None,  # This gets filtered out
    "This also stays."
)

print(section.render())
```

Output:
```markdown
## Filtered Elements
This stays.
This also stays.
```

## Advanced Use Cases

### Dynamic Content Generation

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle

def generate_content(items):
    content_list = []
    for i, item in enumerate(items, 1):
        content_list.append(f"{i}. {item}")
    
    return MarkdownSection(
        MarkdownSectionTitle("Generated Content"),
        *content_list
    )

items = ["Apple", "Banana", "Cherry"]
section = generate_content(items)
print(section.render())
```

Output:
```markdown
## Generated Content
1. Apple
2. Banana
3. Cherry
```

### Building Complex Documentation

See the examples in the `example.py` file for more complex use cases, including:
- Building LLM system prompts
- Creating project documentation
- Writing tutorials

## Implementation Details

The `markdown-dom` library uses Pydantic's `BaseModel` for data validation and provides a clean, object-oriented interface for building Markdown documents programmatically.

When rendering nested sections, proper spacing is added automatically, and section heading levels are incremented appropriately.