# Pydantic models for DOM structure with type checking and validation
from typing import List, Optional
from pydantic import BaseModel, Field, validator
import base64
import pypandoc

# Base class for elements with an optional summary
class Element(BaseModel):
    summary: Optional[str] = None

# Figure element with base64-encoded image data and validation
class Figure(Element):
    rawdata: str = Field(..., description="Base64-encoded image data")

    @validator('rawdata')
    def validate_base64(cls, v):
        # Ensure the rawdata is valid base64
        try:
            base64.b64decode(v)
        except Exception:
            raise ValueError('rawdata must be valid base64')
        return v

# Cell represents a single cell in a table
class Cell(BaseModel):
    c: str

# Column contains a list of cells
class Column(BaseModel):
    cells: List[Cell]

# Row contains a list of columns
class Row(BaseModel):
    cols: List[Column]

# Table element with rows, inherits summary from Element
class Table(Element):
    rows: List[Row]

# A class to represent and manipulate Markdown documents using pypandoc (Pandoc's Python API).
class Markdown(BaseModel):
    content: str = ""

    def to_markdown(self) -> str:
        """Return the markdown content as a string."""
        return self.content

    def to_html(self) -> str:
        """Convert the markdown content to HTML using pypandoc."""
        return pypandoc.convert_text(self.content, 'md', 'html')

    def to_latex(self) -> str:
        """Convert the markdown content to LaTeX using pypandoc."""
        return pypandoc.convert_text(self.content, 'md', 'latex')

    def walk(self, action):
        """
        Recursively apply an action to each element and subelement in the Pandoc AST.
        The action should accept and return a dict (AST node).
        """
        import json
        # Convert markdown to Pandoc JSON AST
        ast_json = pypandoc.convert_text(self.content, 'md', 'json')
        ast = json.loads(ast_json)

        def walk_node(node):
            node = action(node)
            if isinstance(node, dict):
                for key, value in node.items():
                    if isinstance(value, list):
                        node[key] = [walk_node(child) if isinstance(child, (dict, list)) else child for child in value]
                    elif isinstance(value, dict):
                        node[key] = walk_node(value)
            elif isinstance(node, list):
                node = [walk_node(child) if isinstance(child, (dict, list)) else child for child in node]
            return node

        ast = walk_node(ast)
        # Convert AST back to markdown
        new_json = json.dumps(ast)
        self.content = pypandoc.convert_text(new_json, 'json', 'md')

    @staticmethod
    def from_file(filepath: str):
        """Create a Markdown object from a file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return Markdown(content=content)

# Section can contain paragraphs, figures, tables, and nested subsections
class Section(BaseModel):
    summary: Optional[str] = None
    paragraphs: List[str] = Field(default_factory=list)
    figures: List[Figure] = Field(default_factory=list)
    tables: List[Table] = Field(default_factory=list)
    subsections: List['Section'] = Field(default_factory=list)

    def __init__(self, summary: Optional[str] = None, paragraphs: Optional[List[str]] = None,
                 figures: Optional[List[Figure]] = None, tables: Optional[List[Table]] = None,
                 subsections: Optional[List['Section']] = None):
        super().__init__(
            summary=summary,
            paragraphs=paragraphs or [],
            figures=figures or [],
            tables=tables or [],
            subsections=subsections or []
        )

    @classmethod
    def init(cls, md: Markdown):
        # Placeholder for initialization from Markdown
        return cls()

# Support for recursive Section references
Section.update_forward_refs()
