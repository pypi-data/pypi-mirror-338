"""Contains the ProcedureCode model for Dentrix API."""
from t_object import ThoughtfulObject
from typing import Optional


class ProcedureCode(ThoughtfulObject):
    """ProcedureCode model for easier Data handling."""

    id: int
    abbreviated_description: Optional[str]
    active: Optional[bool]
    ada_code: Optional[str]
    amount: Optional[float]
    bill_to_insurance: Optional[bool]
    category: Optional[str]
    category_description: Optional[str]
    charting_symbol: Optional[str]
    code_extension: Optional[str]
    description: Optional[str]
    favorite_name: Optional[str]
    has_prosthesis: Optional[bool]
    is_aoc_shown: Optional[bool]
    is_clinical_note_required: Optional[bool]
    is_favorite: Optional[bool]
    is_ortho_flag_complete: Optional[bool]
    is_treatment_info_required: Optional[bool]
    is_tx_plan_template: Optional[bool]
    ortho: Optional[bool]
    predetermined: Optional[bool]
    treatment_area: Optional[str]
    treatment_area_flag: Optional[str]
    visible: Optional[bool]
    payload: Optional[dict]

    @classmethod
    def from_payload(cls, payload: dict) -> "ProcedureCode":
        """Generate a ProcedureCode model from a Dentrix payload result."""
        return cls(
            id=payload.get("id"),
            abbreviated_description=payload.get("abbreviatedDescription"),
            active=payload.get("active"),
            ada_code=payload.get("adaCode"),
            amount=payload.get("amount"),
            bill_to_insurance=payload.get("billToInsurance"),
            category=payload.get("category"),
            category_description=payload.get("categoryDescription"),
            charting_symbol=payload.get("chartingSymbol"),
            code_extension=payload.get("codeExtension"),
            description=payload.get("description"),
            favorite_name=payload.get("favoriteName"),
            has_prosthesis=payload.get("hasProsthesis"),
            is_aoc_shown=payload.get("isAocShown"),
            is_clinical_note_required=payload.get("isClinicalNoteRequired"),
            is_favorite=payload.get("isFavorite"),
            is_ortho_flag_complete=payload.get("isOrthoFlagComplete"),
            is_treatment_info_required=payload.get("isTreatmentInfoRequired"),
            is_tx_plan_template=payload.get("isTxPlanTemplate"),
            ortho=payload.get("ortho"),
            predetermined=payload.get("predetermined"),
            treatment_area=payload.get("treatmentArea"),
            treatment_area_flag=payload.get("treatmentAreaFlag"),
            visible=payload.get("visible"),
            payload=payload,
        )
