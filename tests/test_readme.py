import re
from pathlib import Path

def test_readme_table_of_contents():
    readme_path = Path(__file__).parent.parent / "README.md"
    assert readme_path.exists(), "README.md must exist"

    content = readme_path.read_text(encoding="utf-8")

    # Verify Table of Contents header exists
    assert "## Table of Contents" in content

    # Extract all TOC links [text](#anchor)
    toc_match = re.search(r"## Table of Contents\s*\n\n(.*?)\n---", content, re.DOTALL)
    assert toc_match is not None, "Table of Contents section must be defined"
    toc_text = toc_match.group(1)

    toc_links = re.findall(r"\[([^\]]+)\]\((#[^)]+)\)", toc_text)
    assert len(toc_links) >= 8, f"Expected at least 8 TOC entries, found {len(toc_links)}"

    # Collect all anchor targets from README
    # 1. HTML anchors: <a id="..."> or <a name="...">
    html_anchors = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', content))

    # 2. Markdown headings: ## Heading Text
    heading_lines = re.findall(r"^#+\s+(.+)$", content, re.MULTILINE)
    generated_slugs = set()
    for h in heading_lines:
        # Standard GFM slug: lowercase, strip punctuation except hyphen, replace space with hyphen
        s = h.lower()
        s = re.sub(r"[^\w\s-]", "", s)
        s = re.sub(r"\s+", "-", s.strip())
        generated_slugs.add(s)

    all_valid_targets = html_anchors | generated_slugs

    # Verify every TOC link has a target
    for title, anchor in toc_links:
        slug = anchor.lstrip("#")
        assert (
            slug in all_valid_targets
            or slug.replace("--", "-") in all_valid_targets
        ), f"TOC link '{title}' with anchor '{anchor}' does not resolve to an anchor or heading in README.md"
