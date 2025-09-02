from fastapi import FastAPI, HTTPException, Request
from automation import execute_trade
from telegram_signals import get_signals
from detection import detect_trade_result
from logger import setup_logger

logger = setup_logger("backend")
app = FastAPI()

@app.get("/signals")
def signals():
    try:
        return get_signals()
    except Exception as e:
        logger.error("Signal extraction failed: %s", e)
        raise HTTPException(status_code=500, detail="Error extracting signals")

@app.post("/trade")
async def trade(request: Request):
    data = await request.json()
    try:
        result = execute_trade(data)
        trade_outcome = detect_trade_result()
        result["trade_result"] = trade_outcome
        return result
    except Exception as e:
        logger.error("Trade execution failed: %s", e)
        raise HTTPException(status_code=500, detail="Error executing trade")
