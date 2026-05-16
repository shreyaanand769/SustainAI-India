"""Reference event loop for adaptive recalculation.

This local script emits an example observation to the API. In production the same
contract can be implemented with Kafka, Redis Streams, Pub/Sub, or Kinesis.
"""
from __future__ import annotations

from datetime import datetime, timezone
import requests

API_URL = "http://localhost:8000/ingest"

payload = {
    "source": "demo.imd.anomaly",
    "region_id": "KA-BLRU",
    "metric": "water",
    "value": 96,
    "unit": "risk_index",
    "observed_at": datetime.now(timezone.utc).isoformat(),
}

if __name__ == "__main__":
    response = requests.post(API_URL, json=payload, timeout=10)
    response.raise_for_status()
    print(response.json())
