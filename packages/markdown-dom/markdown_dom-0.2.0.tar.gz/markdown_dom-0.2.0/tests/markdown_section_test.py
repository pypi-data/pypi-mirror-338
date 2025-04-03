from markdown_dom import markdown_section, markdown_section_title


def test_markdown_section() -> None:
    markdown = markdown_section("test")
    assert markdown.render(section_level=1) == "test"


def test_markdown_section_with_title() -> None:
    markdown = markdown_section(markdown_section_title("test"), "description")
    assert (
        markdown.render(section_level=1)
        == """# test
description"""
    )


def test_markdown_section_with_multiple_elements() -> None:
    markdown = markdown_section(
        markdown_section_title("test"),
        "description1",
        "description2",
    )
    assert (
        markdown.render(section_level=1)
        == """# test
description1
description2"""
    )


def test_markdown_section_with_none_elements() -> None:
    markdown = markdown_section(
        markdown_section_title("test"),
        None,
        "description",
    )
    assert (
        markdown.render(section_level=1)
        == """# test
description"""
    )


def test_markdown_section_nested() -> None:
    markdown = markdown_section(
        markdown_section_title("test"),
        markdown_section(
            markdown_section_title("nested"),
            "description",
        ),
        markdown_section(
            markdown_section_title("nested2"),
            "description2",
        ),
    )
    assert (
        markdown.render(section_level=2)
        == """## test
### nested
description

### nested2
description2"""
    )
