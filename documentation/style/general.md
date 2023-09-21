# General

This document contains general style information that can be applied to the
various content that this project creates. This can include:

* The top 10 entries themselves
* Infographics
* Technical diagrams
* Website content
* Other additional and supplemental documentation


## Language and Tone

* **Consistency:** Ensure the same tense and voice (active/passive) are maintained throughout.
* **Clarity:** Make sure to avoid jargon unless it's industry-standard. Always define terms when they're introduced.
* **International:** Since the team and the intended audience are both international, avoid using idioms or region-specific references. For spelling: content should use US English versions of words (e.g. `behavior` not `behaviour`, or `authorize` not `authorise`, etc.).


## Document Format

Whenever possible, the document should use Markdown formatting. Markdown allows
for simple formatting while keeping the content easy to read as plain text.

### Headings

Headings should use the Markdown ATX style headings, with the header text preceded
by 1-6 octothorpe `#` characters to indicate heading levels:

```
# Heading Level 1
## Heading Level 2
### Heading Level 3
#### Heading Level 4
##### Heading Level 5
###### Heading Level 6
```

When using heading levels, do not skip levels (e.g. don't jump from H2 to H4).
After the heading, leave an empty line before continuing with the content.

For specific sections within the documents, follow the guidelines below:

#### 1. Document Title:
Use a level 1 header for the document title.

```markdown
# Top 10 Security Risks for LLM Applications
```

#### 2. Section Headers:
Use level 2 headers for major sections.

```markdown
## Introduction
```

#### 3. Subsections:
Use level 3 headers for subsections.

```markdown
### 1.1 Background
```

### Lists

For bullet point lists, use the Markdown unordered list syntax by preceding each
list item with an `* ` (asterisk proceeded by a space):

```markdown
* Factor 1: Description
* Factor 2: Description
```

For sub-items, indent two spaces per division, and use a dash `-` to dmarc the
bulleted item:

```markdown
* Factor 1: Description
  - Factor 1.1: Description
    - Factor 1.1.2: Description
```

For numbered lists, use the Markdown ordered list syntax by preceding each list
item with a number followed by `. ` (period surrounded by space):

```
1. First item
2. Second item
3. Third item
```

In some renderers, ordered lists can have numbers automatically assigned if you
use the same number on each entry. However, this behavior is inconsistent.
Accordingly, content authors should ensure the numbers they use are listed as they
should appear in the rendered content.

### Emphasis

Use Markdown syntax to emphasize text:

- Italics: surround text with `*asterisks*` or `_underscores_`
- Bold: surround text with `**double asterisks**` or `__double underscores__`
- Bold italics: surround text with `***triple asterisks***` or `___triple underscores___`

### Code Blocks

If there's a need to display code or terminal commands, use code blocks.

For single-line code or commands, use backticks (`).

```markdown
Use `chmod 777 filename` cautiously.
```

For multi-line code, use triple backticks.

\```
def malicious_code():
    pass
\```

### Quotes and Citations:
If quoting experts or sources, use the blockquote syntax.

```markdown
> "This quote supports the claim made in the risk." - [Source Name](URL)
```

### Links

### 9. Hyperlinks:

To reference external sources or provide further reading, use inline links.

```markdown
For more details, refer to [this article](https://example.com).
```

### Images

If you need to include diagrams or images, use the following format:

```markdown
![Alt Text for Image](URL-of-the-image)
```


### Tables

Format tables using Markdown table syntax:

```
| Column 1 | Column 2 | Column 3 |
|-|-|-|
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |
```

### Page Breaks

Use 3 hyphens surrounded by blank lines to create a page break:

\`\`\`
---
\`\`\`