from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Prepare dataset
data = merged_df.copy()
target = 'Global_active_power'
X = data.drop(columns=[target])
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train models
xgb = XGBRegressor(n_estimators=200, learning_rate=0.05)
lgbm = LGBMRegressor(n_estimators=300)
rf = RandomForestRegressor(n_estimators=150)

xgb.fit(X_train, y_train)
lgbm.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Blend predictions
y_pred = (xgb.predict(X_test) + lgbm.predict(X_test) + rf.predict(X_test)) / 3

# Evaluate
r2 = r2_score(y_test, y_pred)
print(f"⚡ Hybrid ML Model R² Score: {r2:.3f}")
