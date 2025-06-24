from fastapi import APIRouter, HTTPException, Query
from app.service.currency import CurrencyConverter

router = APIRouter()
converter = CurrencyConverter()

@router.get("/convert")
async def convert_currency(
    from_currency: str = Query(..., min_length=3, max_length=3),
    to_currency: str = Query(..., min_length=3, max_length=3),
    amount: float = Query(..., gt=0)
):
    try:
        result = await converter.convert(from_currency, to_currency, amount)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/supported-currencies")
async def supported_currencies():
    try:
        codes = await converter.get_supported_currencies()
        return {"supported_currencies": codes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
