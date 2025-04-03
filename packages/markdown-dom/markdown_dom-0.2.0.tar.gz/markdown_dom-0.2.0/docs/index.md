# markdown-dom Documentation

Welcome to the documentation for markdown-dom, an elegant Python library for handling Markdown with a DOM-like structure.

## 📚 Documentation Sections

- [Getting Started](getting_started.md) - How to install and use markdown-dom
- [API Reference](api.md) - Detailed information about the library's classes and methods
- [Use Cases](use_cases.md) - Examples of practical applications

## 🌟 Features

- 🎯 Handle Markdown with a hierarchical DOM-like structure
- 🔄 Dynamic Markdown generation and management
- 🧩 Modular structure for high reusability
- 🎨 Intuitive and easy-to-use API
- 📝 Programmatically create structured Markdown documents

## 🚀 Quick Start

Install the library:

```bash
pip install markdown-dom
```

Basic usage:

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle

# Create a simple section with title
section = MarkdownSection(
    MarkdownSectionTitle("Hello World"),
    "This is some content."
)

# Render the section as Markdown
print(section.render())
```

Output:
```markdown
## Hello World
This is some content.
```

For more detailed examples and usage patterns, please see the [Getting Started Guide](getting_started.md).

## 🛠️ Requirements

- Python 3.10 or higher
- pydantic >= 2.10.3

## 📜 License

Released under the MIT License. See [LICENSE](../LICENSE) for details.