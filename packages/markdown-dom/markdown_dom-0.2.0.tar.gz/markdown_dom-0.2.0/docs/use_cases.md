# Use Cases for markdown-dom

This document outlines various practical use cases for the markdown-dom library.

## LLM System Prompts

One of the most powerful use cases for markdown-dom is building structured system prompts for Large Language Models (LLMs). With markdown-dom, you can:

- Define a consistent structure for your prompts
- Generate prompts dynamically based on user input or application state
- Create prompts with multiple nested sections for complex instructions

### Example: Building an AI Assistant Prompt

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle

def build_assistant_prompt(assistant_name: str, expertise: list[str], constraints: list[str]) -> str:
    """Generate a system prompt for an AI assistant with configurable parameters."""
    
    # Build expertise list
    expertise_items = []
    for area in expertise:
        expertise_items.append(f"- {area}")
    
    # Build constraints list
    constraint_items = []
    for constraint in constraints:
        constraint_items.append(f"- {constraint}")
    
    prompt = MarkdownSection(
        MarkdownSection(
            MarkdownSectionTitle("Role"),
            f"You are {assistant_name}, an AI assistant specialized in helping users with their questions and tasks.",
        ),
        MarkdownSection(
            MarkdownSectionTitle("Expertise"),
            "You have expertise in the following areas:",
            *expertise_items
        ),
        MarkdownSection(
            MarkdownSectionTitle("Instructions"),
            "When responding to users:",
            "- Be concise and direct",
            "- Use markdown formatting for code and structured content",
            "- Provide examples when helpful"
        ),
        MarkdownSection(
            MarkdownSectionTitle("Constraints"),
            "You must follow these constraints:",
            *constraint_items
        )
    )
    
    return prompt.render(section_level=1)

# Example usage
prompt = build_assistant_prompt(
    assistant_name="CodeHelper",
    expertise=["Python", "JavaScript", "SQL", "System Design"],
    constraints=["Never generate harmful code", "Cite sources when providing factual information"]
)

print(prompt)
```

## Dynamic Documentation Generation

markdown-dom is ideal for generating documentation dynamically:

- Generate API documentation from code annotations or schemas
- Create dynamic README files for repositories
- Build customized user guides based on feature flags or user roles

### Example: Generating API Documentation

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle
from typing import Dict, List, Any

def generate_api_docs(endpoints: Dict[str, Dict[str, Any]]) -> str:
    """Generate API documentation from an endpoints dictionary."""
    
    doc = MarkdownSection(
        MarkdownSectionTitle("API Reference"),
        "This document describes the available API endpoints."
    )
    
    for path, details in endpoints.items():
        endpoint_section = MarkdownSection(
            MarkdownSectionTitle(f"`{details['method']} {path}`"),
            details.get("description", "No description provided."),
            
            # Parameters subsection
            MarkdownSection(
                MarkdownSectionTitle("Parameters"),
                "| Name | Type | Required | Description |",
                "| ---- | ---- | -------- | ----------- |"
            )
        )
        
        # Add parameter rows
        for param in details.get("parameters", []):
            param_row = f"| {param['name']} | {param['type']} | {'Yes' if param.get('required') else 'No'} | {param.get('description', '')} |"
            endpoint_section.elements.append(param_row)
        
        # Add responses subsection
        responses_section = MarkdownSection(
            MarkdownSectionTitle("Responses"),
            "| Status | Description |",
            "| ------ | ----------- |"
        )
        
        for status, desc in details.get("responses", {}).items():
            responses_section.elements.append(f"| {status} | {desc} |")
        
        # Add responses to endpoint section
        endpoint_section.elements.append("")  # Add a blank line
        endpoint_section.elements.append(responses_section)
        
        # Add endpoint section to main doc
        doc.elements.append(endpoint_section)
    
    return doc.render(section_level=1)

# Example usage
endpoints = {
    "/users": {
        "method": "GET",
        "description": "Retrieve a list of users",
        "parameters": [
            {"name": "limit", "type": "integer", "required": False, "description": "Maximum number of results"},
            {"name": "offset", "type": "integer", "required": False, "description": "Pagination offset"}
        ],
        "responses": {
            "200": "List of users",
            "401": "Unauthorized",
            "500": "Server error"
        }
    },
    "/users/{id}": {
        "method": "GET",
        "description": "Retrieve a specific user",
        "parameters": [
            {"name": "id", "type": "string", "required": True, "description": "User ID"}
        ],
        "responses": {
            "200": "User details",
            "404": "User not found",
            "500": "Server error"
        }
    }
}

print(generate_api_docs(endpoints))
```

## Structured Report Generation

markdown-dom is perfect for generating structured reports:

- Analytical reports with hierarchical sections
- Status reports with standardized formatting
- Technical documentation with nested details

### Example: Building a Test Report

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle
from typing import Dict, List, Any
import datetime

def generate_test_report(test_results: Dict[str, List[Dict[str, Any]]]) -> str:
    """Generate a test report from test results."""
    
    # Calculate summary statistics
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    for module, tests in test_results.items():
        total_tests += len(tests)
        passed_tests += sum(1 for test in tests if test["status"] == "PASS")
        failed_tests += sum(1 for test in tests if test["status"] == "FAIL")
    
    # Create the report
    report = MarkdownSection(
        MarkdownSectionTitle("Test Report"),
        f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        MarkdownSection(
            MarkdownSectionTitle("Summary"),
            f"Total Tests: {total_tests}",
            f"Passed: {passed_tests}",
            f"Failed: {failed_tests}",
            f"Pass Rate: {(passed_tests / total_tests * 100):.2f}%"
        )
    )
    
    # Add sections for each module
    for module, tests in test_results.items():
        module_section = MarkdownSection(
            MarkdownSectionTitle(f"Module: {module}"),
            f"Tests: {len(tests)}",
            f"Passed: {sum(1 for test in tests if test['status'] == 'PASS')}",
            f"Failed: {sum(1 for test in tests if test['status'] == 'FAIL')}"
        )
        
        # Add failed tests details
        failed_tests = [test for test in tests if test["status"] == "FAIL"]
        if failed_tests:
            failed_section = MarkdownSection(
                MarkdownSectionTitle("Failed Tests"),
                "| Test | Error |",
                "| ---- | ----- |"
            )
            
            for test in failed_tests:
                failed_section.elements.append(f"| {test['name']} | {test['error']} |")
            
            module_section.elements.append("")
            module_section.elements.append(failed_section)
        
        report.elements.append(module_section)
    
    return report.render(section_level=1)

# Example usage
test_results = {
    "auth": [
        {"name": "test_login", "status": "PASS", "duration": 0.25},
        {"name": "test_logout", "status": "PASS", "duration": 0.12},
        {"name": "test_password_reset", "status": "FAIL", "duration": 0.31, "error": "Expected token but got None"}
    ],
    "api": [
        {"name": "test_get_users", "status": "PASS", "duration": 0.45},
        {"name": "test_create_user", "status": "FAIL", "duration": 0.52, "error": "Database connection error"},
        {"name": "test_delete_user", "status": "PASS", "duration": 0.28}
    ]
}

print(generate_test_report(test_results))
```

## Generating Complex Markdown Content

markdown-dom excels at creating complex markdown content like:

- Technical manuals with multiple levels of headings
- Knowledge base articles with consistent structure
- Educational content with hierarchical organization

### Example: Generating a Tutorial

```python
from markdown_dom import MarkdownSection, MarkdownSectionTitle

def generate_tutorial(title: str, sections: list[dict]) -> str:
    """Generate a tutorial with multiple sections."""
    
    tutorial = MarkdownSection(
        MarkdownSectionTitle(title),
        "This tutorial will guide you through the process step by step."
    )
    
    for i, section in enumerate(sections, 1):
        section_content = MarkdownSection(
            MarkdownSectionTitle(f"Step {i}: {section['title']}"),
            section["description"]
        )
        
        # Add code blocks if present
        if "code" in section:
            section_content.elements.append("")
            section_content.elements.append("```" + section.get("language", ""))
            section_content.elements.append(section["code"])
            section_content.elements.append("```")
        
        # Add notes if present
        if "notes" in section:
            notes_section = MarkdownSection(
                MarkdownSectionTitle("Notes"),
                *[f"- {note}" for note in section["notes"]]
            )
            section_content.elements.append("")
            section_content.elements.append(notes_section)
        
        tutorial.elements.append(section_content)
    
    # Add conclusion
    tutorial.elements.append(
        MarkdownSection(
            MarkdownSectionTitle("Conclusion"),
            "You have now completed all the steps in this tutorial!",
            "If you have any questions, please refer to the documentation or contact support."
        )
    )
    
    return tutorial.render(section_level=1)

# Example usage
tutorial_sections = [
    {
        "title": "Installation",
        "description": "First, install the package using pip:",
        "code": "pip install example-package",
        "language": "bash",
        "notes": ["Make sure you have Python 3.10+ installed", "You may need admin privileges"]
    },
    {
        "title": "Configuration",
        "description": "Create a configuration file:",
        "code": "API_KEY = 'your-key-here'\nDEBUG = True",
        "language": "python",
        "notes": ["Keep your API key secret", "Never commit your keys to version control"]
    },
    {
        "title": "Running the App",
        "description": "Now you can run the application:",
        "code": "python -m example_package.main",
        "language": "bash"
    }
]

print(generate_tutorial("Getting Started with Example Package", tutorial_sections))
```

## Conclusion

markdown-dom provides a flexible, object-oriented approach to generating Markdown content programmatically. Its hierarchical structure makes it easy to create complex, nested documents with consistent formatting, which is particularly valuable for:

- LLM system prompts
- Dynamic documentation
- Report generation
- Educational content
- API documentation
- Technical manuals

By leveraging the power of markdown-dom, you can standardize your Markdown generation process, making it more maintainable and scalable.