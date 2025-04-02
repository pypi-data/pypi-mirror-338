"""Contains the Document model for Dentrix API."""
from t_object import ThoughtfulObject
from typing import Optional


class Document(ThoughtfulObject):
    """Document model for easier Data handling."""

    id: int
    byte_size: Optional[int]
    date: Optional[int]
    name: Optional[str]
    pdf_page_count: Optional[int]
    tags: Optional[list]
    thumb_nail_id: Optional[str]
    type: Optional[str]
    payload: Optional[dict]

    @classmethod
    def from_payload(cls, payload: dict) -> "Document":
        """Generate a Document model from a Dentrix payload result."""
        return cls(
            id=payload.get("id"),
            byte_size=payload.get("byteSize"),
            date=payload.get("date"),
            name=payload.get("name"),
            pdf_page_count=payload.get("pdfPageCount"),
            tags=payload.get("tags"),
            thumb_nail_id=payload.get("thumbNailId"),
            type=payload.get("type"),
            payload=payload,
        )
