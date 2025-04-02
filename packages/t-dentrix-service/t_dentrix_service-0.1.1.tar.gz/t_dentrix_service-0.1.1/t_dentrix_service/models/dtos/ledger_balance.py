"""Data Transfer Object (DTO) for Ledger Balance information within Dentrix."""

from t_object import ThoughtfulObject
from typing import Optional


class LedgerBalance(ThoughtfulObject):
    """Model representing a Ledger Balance information."""

    first_month: Optional[float]
    second_month: Optional[float]
    third_month: Optional[float]
    over_three_months: Optional[float]
    insurance_portion: Optional[float]
    write_off_adjustments: Optional[float]
    patient_portion: Optional[float]
    balance: Optional[float]
    unapplied_credits: Optional[float]
    please_pay_amount: Optional[float]
    closeable_payment_plan_state: Optional[bool]
    has_coverage_gap: Optional[bool]
    has_updated_portions: Optional[bool]
    updated_insurance_portion: Optional[float]
    updated_write_off_adjustments: Optional[float]
    updated_patient_portion: Optional[float]
    payload: Optional[dict]

    @classmethod
    def from_payload(cls, payload: dict):
        """Generates LedgerBalance from payload."""
        return cls(
            first_month=payload.get("firstMonth"),
            second_month=payload.get("secondMonth"),
            third_month=payload.get("thirdMonth"),
            over_three_months=payload.get("overThreeMonths"),
            insurance_portion=payload.get("insurancePortion"),
            write_off_adjustments=payload.get("writeOffAdjustments"),
            patient_portion=payload.get("patientPortion"),
            balance=payload.get("balance"),
            unapplied_credits=payload.get("unappliedCredits"),
            please_pay_amount=payload.get("pleasePayAmount"),
            closeable_payment_plan_state=payload.get("closeablePaymentPlanState"),
            has_coverage_gap=payload.get("hasCoverageGap"),
            has_updated_portions=payload.get("hasUpdatedPortions"),
            updated_insurance_portion=payload.get("updatedInsurancePortion"),
            updated_write_off_adjustments=payload.get("updatedWriteOffAdjustments"),
            updated_patient_portion=payload.get("updatedPatientPortion"),
            payload=payload,
        )
