from fastapi import APIRouter, FastAPI
from api.schemas.risk_schema import RISKPREDICTIONREQUEST
from api.services.predictor import predict_risk_result

router = APIRouter()

@router.post("/risk")
def risk_score(request: RISKPREDICTIONREQUEST):
    result = predict_risk_result(request.model_dump())
    return result

