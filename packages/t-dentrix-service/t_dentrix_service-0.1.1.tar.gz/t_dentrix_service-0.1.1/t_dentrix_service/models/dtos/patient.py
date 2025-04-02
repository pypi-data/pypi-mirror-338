"""Contains Patient Models."""

from datetime import date
from typing import Optional

from t_object import ThoughtfulObject

from t_dentrix_service.models.activity_status import Status
from t_dentrix_service.utils.converters import convert_timestamp_to_date


class Patient(ThoughtfulObject):
    """Patient Data model for easier Data handling."""

    id: int
    first_name: str
    last_name: str
    preferred_name: Optional[str]
    primary_provider_id: Optional[int]
    name: Optional[str]
    date_of_birth: Optional[date]
    date_of_birth_timestamp: Optional[int]
    chart_number: Optional[str]
    phone_number: Optional[str]
    activity_status: Optional[Status | str]
    is_ortho: Optional[bool]
    preferred_location_id: Optional[int]
    payload: Optional[dict]

    @classmethod
    def from_payload(cls, payload: dict) -> "Patient":
        """Generate a Patient model from a Dentrix payload result."""
        return cls(
            id=payload.get("id"),
            first_name=payload.get("firstName"),
            last_name=payload.get("lastName"),
            preferred_name=payload.get("preferredName"),
            primary_provider_id=payload.get("primaryProviderId"),
            name=payload.get("name"),
            date_of_birth=convert_timestamp_to_date(payload.get("dateOfBirth")) if payload.get("dateOfBirth") else None,
            date_of_birth_timestamp=payload.get("dateOfBirth"),
            chart_number=payload.get("chartNumber"),
            phone_number=payload.get("phone"),
            activity_status=payload.get("status"),
            is_ortho=payload.get("isOrtho"),
            preferred_location_id=payload.get("preferredLocation")["id"] if payload.get("preferredLocation") else None,
            payload=payload,
        )


class PatientInfo(ThoughtfulObject):
    """Patient Info Data model for easier Data handling."""

    age: Optional[int]
    billing_type: Optional[dict[str, int]]
    chart_number: Optional[str]
    contact_method: Optional[str]
    created: Optional[int]
    date_of_birth: Optional[int]
    discount_plan: Optional[dict[str, int]]
    discount_plan_expiration_date: Optional[int]
    discount_type: Optional[str]
    display_full_name: Optional[str]
    display_name_by_last: Optional[str]
    emails: Optional[list[dict[str, any]]]
    emergency_contact: Optional[str]
    ethnicity: Optional[str]
    external_id: Optional[str]
    family_size: Optional[int]
    first_name: Optional[str]
    first_visit_date: Optional[int]
    gender: Optional[str]
    guarantored_patients: Optional[list[dict[str, any]]]
    has_alerts: Optional[bool]
    has_pending_changes: Optional[bool]
    id: int
    income: Optional[int]
    is_orthodontia_patient: Optional[bool]
    is_self_guarantored: Optional[bool]
    language_type: Optional[str]
    last_missed_appointment_date: Optional[int]
    last_name: Optional[str]
    last_visit_date: Optional[int]
    middle_name: Optional[str]
    name_suffix: Optional[str]
    organization: Optional[dict[str, int]]
    patient_address: Optional[dict[str, any]]
    patient_connection_notes: Optional[list[dict[str, any]]]
    patient_forms: Optional[list[dict[str, any]]]
    patient_insurance_plans: Optional[list[dict[str, any]]]
    patient_medical_alerts: Optional[list[dict[str, any]]]
    patient_payment_plans: Optional[list[dict[str, any]]]
    patient_picture: Optional[str]
    patient_sms_thread: Optional[int]
    phones: Optional[list[dict[str, any]]]
    preferred_days: Optional[dict[str, bool]]
    preferred_location: Optional[dict[str, int]]
    preferred_name: Optional[str]
    preferred_times: Optional[dict[str, bool]]
    primary_email: Optional[dict[str, any]]
    procedures: Optional[list[dict[str, any]]]
    races: Optional[list[dict[str, any]]]
    referred_patients: Optional[list[dict[str, any]]]
    related_patients: Optional[list[dict[str, any]]]
    relationships: Optional[dict[str, dict[str, int]]]
    status: Optional[str]
    third_party_external_ids: Optional[list[dict[str, str]]]
    title: Optional[str]
    tooth_codes: Optional[list[dict[str, any]]]
    total_missed_appointments: Optional[int]
    payload: Optional[dict]

    @classmethod
    def from_payload(cls, payload: dict) -> "PatientInfo":
        """Generate a PatientInfo model from a Dentrix payload result."""
        return cls(
            age=payload.get("age"),
            billing_type=payload.get("billingType"),
            chart_number=payload.get("chartNumber"),
            contact_method=payload.get("contactMethod"),
            created=payload.get("created"),
            date_of_birth=payload.get("dateOfBirth"),
            discount_plan=payload.get("discountPlan"),
            discount_plan_expiration_date=payload.get("discountPlanExpirationDate"),
            discount_type=payload.get("discountType"),
            display_full_name=payload.get("displayFullName"),
            display_name_by_last=payload.get("displayNameByLast"),
            emails=payload.get("emails"),
            emergency_contact=payload.get("emergencyContact"),
            ethnicity=payload.get("ethnicity"),
            external_id=payload.get("externalID"),
            family_size=payload.get("familySize"),
            first_name=payload.get("firstName"),
            first_visit_date=payload.get("firstVisitDate"),
            gender=payload.get("gender"),
            guarantored_patients=payload.get("guarantoredPatients"),
            has_alerts=payload.get("hasAlerts"),
            has_pending_changes=payload.get("hasPendingChanges"),
            id=payload.get("id"),
            income=payload.get("income"),
            is_orthodontia_patient=payload.get("isOrthodontiaPatient"),
            is_self_guarantored=payload.get("isSelfGuarantored"),
            language_type=payload.get("languageType"),
            last_missed_appointment_date=payload.get("lastMissedAppointmentDate"),
            last_name=payload.get("lastName"),
            last_visit_date=payload.get("lastVisitDate"),
            middle_name=payload.get("middleName"),
            name_suffix=payload.get("nameSuffix"),
            organization=payload.get("organization"),
            patient_address=payload.get("patientAddress"),
            patient_connection_notes=payload.get("patientConnectionNotes"),
            patient_forms=payload.get("patientForms"),
            patient_insurance_plans=payload.get("patientInsurancePlans"),
            patient_medical_alerts=payload.get("patientMedicalAlerts"),
            patient_payment_plans=payload.get("patientPaymentPlans"),
            patient_picture=payload.get("patientPicture"),
            patient_sms_thread=payload.get("patientSmsThread"),
            phones=payload.get("phones"),
            preferred_days=payload.get("preferredDays"),
            preferred_location=payload.get("preferredLocation"),
            preferred_name=payload.get("preferredName"),
            preferred_times=payload.get("preferredTimes"),
            primary_email=payload.get("primaryEmail"),
            procedures=payload.get("procedures"),
            races=payload.get("races"),
            referred_patients=payload.get("referredPatients"),
            related_patients=payload.get("relatedPatients"),
            relationships=payload.get("relationships"),
            status=payload.get("status"),
            third_party_external_ids=payload.get("thirdPartyExternalIds"),
            title=payload.get("title"),
            tooth_codes=payload.get("toothCodes"),
            total_missed_appointments=payload.get("totalMissedAppointments"),
            payload=payload,
        )
