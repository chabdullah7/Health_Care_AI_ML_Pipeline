from pydantic import BaseModel, Field


class RISKPREDICTIONREQUEST(BaseModel):
    age: int = Field(..., example=47)
    gender: str = Field(..., example="M")
    city: str = Field(..., example="Bangalore")
    insurance_provider: str = Field(..., example="CareOne")
    chronic_flag: int = Field(..., example=1)
    department: str = Field(..., example="Cardiology")
    visit_type: str = Field(..., example="ER")
    doctor_id: int = Field(..., example=107)
    length_of_stay_hours: float = Field(..., example=77)
    days_since_registration: int = Field(..., example=300)
    visit_frequency: int = Field(..., example=5)
    avg_los_per_patient: float = Field(..., example=37.7)
    visit_month: int = Field(..., example=3)
    visit_dayofweek: int = Field(..., example=7)