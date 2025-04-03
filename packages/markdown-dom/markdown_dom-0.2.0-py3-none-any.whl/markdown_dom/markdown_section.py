from __future__ import annotations

from pydantic import BaseModel


class MarkdownSectionTitle(BaseModel):
    title: str


class MarkdownSection(BaseModel):
    markdown_title: str | None = None
    elements: list[MarkdownSection | str]

    def render(self, *, section_level: int = 2) -> str:
        rendered_elements = []
        if self.markdown_title is not None:
            rendered_elements.append(f"{'#' * section_level} {self.markdown_title}")

        for i, element in enumerate(self.elements):
            if isinstance(element, str):
                rendered_elements.append(element)
                continue

            # MarkdownSection element
            if i > 0:
                rendered_elements.append("")
            rendered_elements.append(element.render(section_level=section_level + 1))

        return "\n".join(rendered_elements)


def markdown_section_title(title: str) -> MarkdownSectionTitle:
    return MarkdownSectionTitle(title=title)


def markdown_section(
    markdown_title_or_element: MarkdownSectionTitle | MarkdownSection | str = "",
    *elements: MarkdownSection | str | None,
) -> MarkdownSection:
    match markdown_title_or_element:
        case MarkdownSectionTitle():
            markdown_title = markdown_title_or_element.title
            elements_filtered: list[MarkdownSection | str] = []
        case MarkdownSection() | str():
            markdown_title = None
            elements_filtered = [markdown_title_or_element]

    # filter None elements
    elements_filtered.extend(
        [element for element in elements if element is not None],
    )

    return MarkdownSection(markdown_title=markdown_title, elements=elements_filtered)
