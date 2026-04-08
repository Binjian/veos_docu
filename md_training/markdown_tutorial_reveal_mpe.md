---
title: Markdown Basics and Writing Workflow
presentation:
  theme: white.css
  width: 1280
  height: 720
  margin: 0.08
  controls: true
  progress: true
  slideNumber: true
  history: false
  keyboard: true
  overview: true
  center: true
  touch: true
  loop: false
  shuffle: false
  fragments: true
  embedded: false
  help: true
  showNotes: false
  autoSlide: 0
  autoSlideStoppable: true
  mouseWheel: false
  transition: slide
  transitionSpeed: default
  backgroundTransition: fade
  viewDistance: 3
  enableSpeakerNotes: false
---

<!-- slide -->

# Markdown Basics and Writing Workflow

### A practical 20-minute tutorial

**Goal:** learn the core rules of Markdown, how to structure a `.md` file, and which tools help you write better Markdown.

<!-- slide -->

## What you will learn

- What Markdown is and why people use it
- The **basic syntax rules** you need every day
- How to organize a clean Markdown document
- The **essential tools** for writing, previewing, linting, and publishing
- Common mistakes and how to avoid them

<!-- slide -->

## Why Markdown?

- **Plain text first**: readable even before rendering
- **Portable**: works across editors, platforms, and tools
- **Version-control friendly**: excellent for Git workflows
- **Fast to write**: minimal formatting overhead
- **Convertible**: can be turned into HTML, PDF, slides, docs, and more

<!-- slide -->

## The basic rule of Markdown

Markdown is mostly about **simple text patterns**.

- `#` starts headings
- `-` or `1.` starts lists
- `>` starts block quotes
- Backticks mark `code`
- Blank lines separate major blocks

### Best habit
Write for **clarity first**, then add lightweight formatting.

<!-- slide -->

## Headings

Use headings to create structure.

```md
# Title
## Section
### Subsection
```

### Tips

- Use **one** `#` heading for the document title
- Keep heading levels in order
- Make headings descriptive and short

<!-- slide -->

## Paragraphs, line breaks, and blank lines

### Paragraphs
A blank line creates a new paragraph.

```md
This is the first paragraph.

This is the second paragraph.
```

### Important habit
Do not rely on random line breaks for structure. Use **blank lines** intentionally.

<!-- slide -->

## Lists

### Unordered list

```md
- Item one
- Item two
  - Nested item
```

### Ordered list

```md
1. First step
2. Second step
3. Third step
```

### Rule of thumb
Indent nested items consistently.

<!-- slide -->

## Emphasis and inline elements

```md
*italic* or _italic_
**bold** or __bold__
`inline code`
[OpenAI](https://openai.com)
![Alt text](images/example.png)
```

### Use these for

- emphasis on key terms
- filenames, commands, and code snippets
- links to docs and references
- images with meaningful alt text

<!-- slide -->

## Block quotes and thematic breaks

### Block quote

```md
> Markdown is easiest to maintain when the source stays simple.
```

### Horizontal rule

```md
---
```

Use these sparingly to separate ideas and call out important guidance.

<!-- slide -->

## Code blocks

Use fenced code blocks for examples.

````md
```bash
npm install markdownlint-cli
```
````

### Why fenced blocks matter

- easier to read than inline code
- syntax highlighting often works automatically
- safer than indentation-based code blocks for most teams

<!-- slide -->

## Tables and task lists

### Table

```md
| Tool | Purpose |
| --- | --- |
| VS Code | Editing |
| Pandoc | Conversion |
```

### Task list

```md
- [x] Write draft
- [ ] Review links
- [ ] Publish file
```

### Reminder
Support for tables and task lists depends on the Markdown flavor.

<!-- slide -->

## A good Markdown file skeleton

```md
# Document title

Short introduction.

## Section one
Main content.

## Section two
- Key point
- Key point

## References
- Link or source
```

### Good documents are

- easy to scan
- logically grouped
- short in paragraphs
- consistent in style

<!-- slide -->

## Recommended writing workflow

1. **Draft** the idea in plain text
2. **Structure** it with headings and lists
3. **Preview** the rendered result
4. **Lint** for style and consistency
5. **Version** it with Git if it matters
6. **Publish or convert** when ready

<!-- slide -->

## Essential tools for writing Markdown

### Editors

- **VS Code**: strong extension ecosystem
- **Obsidian**: great for notes and linked knowledge
- **Typora**: smooth WYSIWYG-style Markdown writing

### Preview and presentation

- **Markdown Preview Enhanced** for rich preview and Reveal.js presentations

### Quality tools

- **markdownlint** for style checks
- spell checker extensions for typos

### Publishing

- **Pandoc** for exporting to HTML, PDF, DOCX, and more

<!-- slide -->

## Markdown flavors matter

Not every renderer supports the exact same features.

### Common examples

- **CommonMark**: clean core behavior
- **GitHub Flavored Markdown**: adds practical features like tables and task lists
- **Pandoc Markdown**: strong for publishing workflows

### Lesson
Test your file in the same environment where it will be used.

<!-- slide -->

## Common mistakes

- Missing blank lines around blocks
- Broken or unclosed code fences
- Inconsistent list indentation
- Using absolute machine-specific file paths
- Assuming every renderer supports every extension
- Writing very long paragraphs that are hard to scan

<!-- slide -->

## Mini demo: from rough notes to useful Markdown

### Rough notes

```md
meeting notes api changes auth issue fix later docs update
```

### Better version

```md
# API Meeting Notes

## Action items
- Fix authentication issue
- Update documentation
- Review deployment timing
```

### Improvement
The second version is easier to read, review, and share.

<!-- slide -->

## Writing rules that help immediately

- Prefer **short headings**
- Keep paragraphs **brief**
- Use lists for scannable points
- Put code in fenced blocks
- Use relative paths for project files
- Add alt text for images
- Preview before sharing

<!-- slide -->

## Using this file in Markdown Preview Enhanced

### Slide separator
This deck uses:

```md
<!-- slide -->
```

### Presentation settings
Configured in YAML front matter under:

```md
presentation:
  theme: white.css
  transition: slide
```

### Practical tip
Open the Markdown Preview Enhanced preview, then switch to presentation mode.

<!-- slide -->

## Practice exercise

Create a file named `notes.md` with:

- one title
- one paragraph
- one list
- one link
- one fenced code block

Then preview it and fix anything that looks wrong.

<!-- slide -->

## Final takeaways

- Markdown is **simple, portable, and practical**
- The basics cover most real-world writing
- Good Markdown depends on **clear structure**
- Preview, lint, and test in the target renderer
- A small set of tools can dramatically improve quality

### Thank you
Questions?
