"""Contains Provider model."""

from typing import Optional
from t_object import ThoughtfulObject


class Provider(ThoughtfulObject):
    """Provider Data model for easier Data handling."""

    id: int
    active: bool
    blue_cross_number: Optional[str]
    clinician_registration_status_type: Optional[dict]
    color: Optional[str]
    date_of_birth: Optional[int]
    dea_expiration: Optional[int]
    dea_schedule2: Optional[bool]
    dea_schedule3: Optional[bool]
    dea_schedule4: Optional[bool]
    dea_schedule5: Optional[bool]
    e_prescribe_enabled: Optional[bool]
    e_trans_provider_location_registration_status: Optional[list]
    erx_id: Optional[str]
    first_name: Optional[str]
    has_signature: Optional[bool]
    is_icp8214_enabled: Optional[bool]
    is_locum_tenens: Optional[bool]
    is_non_person_entity: Optional[bool]
    is_onboarded_with_dose_spot: Optional[bool]
    is_onboarded_with_veradigm: Optional[bool]
    is_primary_provider: Optional[bool]
    is_scheduling_eligible: Optional[bool]
    last_name: Optional[str]
    medicaid_number: Optional[str]
    middle_name: Optional[str]
    npi: Optional[str]
    organization: Optional[dict]
    prov_id: Optional[str]
    provider_number: Optional[str]
    short_name: Optional[str]
    state_id: Optional[str]
    state_id_expiration: Optional[int]
    tin: Optional[str]
    user: Optional[dict]
    payload: Optional[dict]

    @classmethod
    def from_payload(cls, payload: dict):
        """Generate a Provider model from a Dentrix payload result."""
        return cls(
            id=payload.get("id"),
            active=payload.get("active"),
            blue_cross_number=payload.get("blueCrossNumber"),
            clinician_registration_status_type=payload.get("clinicianRegistrationStatusType"),
            color=payload.get("color"),
            date_of_birth=payload.get("dateOfBirth"),
            dea_expiration=payload.get("deaExpiration"),
            dea_schedule2=payload.get("deaSchedule2"),
            dea_schedule3=payload.get("deaSchedule3"),
            dea_schedule4=payload.get("deaSchedule4"),
            dea_schedule5=payload.get("deaSchedule5"),
            e_prescribe_enabled=payload.get("ePrescribeEnabled"),
            e_trans_provider_location_registration_status=payload.get("eTransProviderLocationRegistrationStatus"),
            erx_id=payload.get("erxId"),
            first_name=payload.get("firstName"),
            has_signature=payload.get("hasSignature"),
            is_icp8214_enabled=payload.get("isIcp8214Enabled"),
            is_locum_tenens=payload.get("isLocumTenens"),
            is_non_person_entity=payload.get("isNonPersonEntity"),
            is_onboarded_with_dose_spot=payload.get("isOnboardedWithDoseSpot"),
            is_onboarded_with_veradigm=payload.get("isOnboardedWithVeradigm"),
            is_primary_provider=payload.get("isPrimaryProvider"),
            is_scheduling_eligible=payload.get("isSchedulingEligible"),
            last_name=payload.get("lastName"),
            medicaid_number=payload.get("medicaidNumber"),
            middle_name=payload.get("middleName"),
            npi=payload.get("npi"),
            organization=payload.get("organization"),
            prov_id=payload.get("provId"),
            provider_number=payload.get("providerNumber"),
            short_name=payload.get("shortName"),
            state_id=payload.get("stateID"),
            state_id_expiration=payload.get("stateIDExpiration"),
            tin=payload.get("tin"),
            user=payload.get("user"),
            payload=payload,
        )
