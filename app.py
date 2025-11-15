from flask import Flask, render_template, request
import pandas as pd
import joblib
import datetime

app = Flask(__name__)

# ✅ Load trained hybrid model
hybrid_models = joblib.load("hybrid_energy_model.pkl")
rf = hybrid_models['rf']
xgb = hybrid_models['xgb']
lgbm = hybrid_models['lgbm']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # User Inputs
    temp = float(request.form['temp'])
    humidity = float(request.form['humidity'])
    date_str = request.form['date']

    # Convert date → numeric features
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    day = date.weekday()
    is_weekend = 1 if day >= 5 else 0

    # Create input with all model-required features
    input_data = pd.DataFrame(columns=rf.feature_names_in_)
    input_data.loc[0] = 0  # initialize all to 0

    # Fill required user inputs
    input_data['Temperature'] = temp
    input_data['Humidity'] = humidity
    input_data['DayOfWeek'] = day
    input_data['IsWeekend'] = is_weekend

    # Default assumptions for remaining features
    if 'Global_active_power' in input_data:
        input_data['Global_active_power'] = 1.2
    if 'Global_reactive_power' in input_data:
        input_data['Global_reactive_power'] = 0.15
    if 'Voltage' in input_data:
        input_data['Voltage'] = 230
    if 'Global_intensity' in input_data:
        input_data['Global_intensity'] = 5.0
    if 'Sub_metering_1' in input_data:
        input_data['Sub_metering_1'] = 0
    if 'Sub_metering_2' in input_data:
        input_data['Sub_metering_2'] = 1
    if 'Sub_metering_3' in input_data:
        input_data['Sub_metering_3'] = 8
    if 'PrevDayPower' in input_data:
        input_data['PrevDayPower'] = 1.3
    if 'RollingMean_3' in input_data:
        input_data['RollingMean_3'] = 1.5

    # Predictions from 3 models
    rf_pred = rf.predict(input_data)[0]
    xgb_pred = xgb.predict(input_data)[0]
    lgbm_pred = lgbm.predict(input_data)[0]

    final_pred = (rf_pred + xgb_pred + lgbm_pred) / 3

    return render_template(
        'index.html',
        prediction_text=f"🔋 Predicted Energy Consumption: {round(final_pred, 3)} kW"
    )

# ✅ RUN APP
if __name__ == '__main__':
    app.run(debug=True)
