import os
from typing import Any, Dict
from dotenv import load_dotenv
from fastapi import FastAPI, Query, Body
from x402.fastapi.middleware import require_payment
from x402.types import EIP712Domain, TokenAmount, TokenAsset
from time_agent import WorldTimeAgent

# Load environment variables
load_dotenv()

app = FastAPI()
time_agent = WorldTimeAgent()

# Apply payment middleware to specific routes
app.middleware("http")(
    require_payment(
        path="/time",
        price="$0.001",
        pay_to_address="0x23b72f31bfa80069012dc36e30380cb34aecc8f4",
        network="base-sepolia", # for mainnet, see Running on Mainnet section
        # Optional: Add metadata for better discovery in x402 Bazaar
        description="Get current time for any location",
        input_schema={
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "Location name"}
            }
        },
        output_schema={
            "type": "object",
            "properties": {
                "city": {"type": "string"},
                "country": {"type": "string"},
                "time": {"type": "string"},
                "timezone": {"type": "string"},
                "date": {"type": "string"},
                "full_datetime": {"type": "string"},
                "coordinates": {"type": "object", "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"}
                }}
            }
        }
    )
)

@app.post("/time")
async def get_time(location: dict = Body(..., description="Location name")) -> Dict[str, Any]:
    return time_agent.get_time_for_city(location["location"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)