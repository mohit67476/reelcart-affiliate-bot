
from fastapi import FastAPI, Request
from pydantic import BaseModel
from earnkaro_bot import generate_earnkaro_link
from meesho_bot import generate_meesho_link

app = FastAPI()

class AffiliateRequest(BaseModel):
    platform: str
    product_url: str

@app.post("/generate-affiliate")
async def generate_affiliate(data: AffiliateRequest):
    if data.platform.lower() in ["flipkart", "myntra", "shopsy"]:
        return {"affiliate_link": generate_earnkaro_link(data.product_url)}
    elif data.platform.lower() == "meesho":
        return {"affiliate_link": generate_meesho_link(data.product_url)}
    else:
        return {"error": "Platform not supported"}
