from pydantic import BaseModel


class Shipment(BaseModel):
    carrier: str
    delay_days: int


def compute_status(delay_days: int) -> str:
    """Determine the shipment status based on the number of delay days."""

    if delay_days <= 0:
        return "On Time"
    elif delay_days <= 2:
        return "Delayed"
    else:
        return "Severely Delayed"
