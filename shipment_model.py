from dataclasses import dataclass


def compute_status(delay_days: int) -> str:
    """
    Pure function: maps delay_days to a status string.
    Does not need access to the Shipment class.
    """
    if delay_days <= 0:
        return "on_time"
    elif delay_days <= 2:
        return "minor_delay"
    else:
        return "major_delay"


class Shipment:
    def __init__(self, shipment_id: str, carrier: str, delay_days: int):
        self.shipment_id = shipment_id
        self.carrier = carrier
        self.delay_days = delay_days

    def status(self) -> str:
        return compute_status(self.delay_days)


# ---- Quick self-test (runs only when this file is executed directly) ----
if __name__ == "__main__":
    test_shipments = [
        Shipment("SHP-001", "FastFreight", 0),
        Shipment("SHP-002", "FastFreight", 2),
        Shipment("SHP-003", "SlowHaul", 5),
        Shipment("SHP-004", "MidMove", -1),  # early arrival
    ]

    for s in test_shipments:
        print(
            f"{s.shipment_id} | {s.carrier:<12} | "
            f"delay={s.delay_days:>3} | status={s.status()}"
        )
