"""Train a demo risk model for BharatSustain AI.

Production deployments should replace the synthetic sample with TimescaleDB/PostGIS
features, satellite rasters, CPCB/IMD observations, Census indicators, and verified labels.
"""
from __future__ import annotations

from pathlib import Path
import joblib
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

MODEL_DIR = Path(__file__).resolve().parent / "models"
MODEL_DIR.mkdir(exist_ok=True)

rng = np.random.default_rng(42)
X = rng.uniform(0, 100, size=(1000, 8))
weights = np.array([0.18, 0.22, 0.16, 0.12, 0.10, 0.13, 0.06, -0.09])
y = np.clip(X @ weights + rng.normal(0, 4, size=1000), 0, 100)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)
mae = mean_absolute_error(y_test, model.predict(X_test))
joblib.dump(model, MODEL_DIR / "risk_gradient_boosting.joblib")
print(f"saved={MODEL_DIR / 'risk_gradient_boosting.joblib'} mae={mae:.2f}")
