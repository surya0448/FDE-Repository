from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from shipment_model import Shipment, compute_status  # <-- add this line

app = FastAPI()

# In-memory store: shipment_id -> Shipment
shipments_db: dict[str, Shipment] = {}


class ShipmentIn(BaseModel):
    carrier: str
    delay_days: int


@app.get("/shipments/{shipment_id}")
def get_shipment(shipment_id: str):
    if shipment_id not in shipments_db:
        raise HTTPException(status_code=404, detail="Shipment not found")
    shipment = shipments_db[shipment_id]
    return {
        "shipment_id": shipment.shipment_id,
        "carrier": shipment.carrier,
        "delay_days": shipment.delay_days,
        "status": shipment.status(),
    }


@app.post("/shipments/{shipment_id}", status_code=201)
def create_shipment(shipment_id: str, shipment: ShipmentIn):
    if shipment_id in shipments_db:
        raise HTTPException(status_code=409, detail="Shipment already exists")
    new_shipment = Shipment(
        shipment_id=shipment_id,
        carrier=shipment.carrier,
        delay_days=shipment.delay_days,
    )
    shipments_db[shipment_id] = new_shipment
    return {
        "shipment_id": new_shipment.shipment_id,
        "carrier": new_shipment.carrier,
        "delay_days": new_shipment.delay_days,
        "status": new_shipment.status(),
    }


@app.get("/")
def root():
    return {
        "service": "Shipment Status API",
        "docs": "/docs",
        "endpoints": [
            "GET  /shipments/{shipment_id}",
            "POST /shipments/{shipment_id}",
        ],
    }
