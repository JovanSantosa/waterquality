import streamlit as st
from Respon import predict_quality_from_db
from readtemp import get_temperature
from readph import get_ph
from readtur import get_turbidity
from readcon import get_conductivity

# Custom CSS for modern minimalist style
st.markdown(
    """
    <style>
    .metric-box {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    .metric-header {
        font-size: 20px;
        font-weight: bold;
        color: #333333;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
    }
    .metric {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    .metric2 {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        margin-top: 30px;
        color: #666666;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(f"""<div class="metric2">Modern Water Quality Monitoring</div>""",
        unsafe_allow_html=True)

# Function to determine color based on value
def get_color(value, thresholds):
    if value < thresholds[0]:
        return "#007bff"  # Blue
    elif value < thresholds[1]:
        return "#ffc107"  # Yellow
    else:
        return "#dc3545"  # Red

# Thresholds for metrics
temperature_thresholds = [25, 35]  # Example thresholds for temperature
ph_thresholds = [6.5, 8.5]  # Example thresholds for pH
turbidity_thresholds = [5, 10]  # Example thresholds for turbidity
conductivity_thresholds = [500, 700]  # Example thresholds for conductivity

# Create a grid layout for metrics
col1, col2 = st.columns(2)

with col1:
    # Temperature
    temperature = get_temperature()
    temp_color = get_color(temperature if isinstance(temperature, (int, float)) else 0, temperature_thresholds)
    st.markdown(
        f"""
        <div class="metric-box" style="color: {temp_color};">
            <div class="metric-header">Temperature (°C)</div>
            <div class="metric-value">{temperature if isinstance(temperature, str) else f"{temperature} °C"}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # pH
    ph = get_ph()
    ph_color = get_color(ph if isinstance(ph, (int, float)) else 0, ph_thresholds)
    st.markdown(
        f"""
        <div class="metric-box" style="color: {ph_color};">
            <div class="metric-header">pH</div>
            <div class="metric-value">{ph}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    # Turbidity
    turbidity = get_turbidity()
    turb_color = get_color(turbidity if isinstance(turbidity, (int, float)) else 0, turbidity_thresholds)
    st.markdown(
        f"""
        <div class="metric-box" style="color: {turb_color};">
            <div class="metric-header">Turbidity (NTU)</div>
            <div class="metric-value">{turbidity}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Conductivity
    conductivity = get_conductivity()
    cond_color = get_color(conductivity if isinstance(conductivity, (int, float)) else 0, conductivity_thresholds)
    st.markdown(
        f"""
        <div class="metric-box" style="color: {cond_color};">
            <div class="metric-header">Conductivity (S/m)</div>
            <div class="metric-value">{conductivity}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Prediction Section
st.markdown(f"""<div class="metric">🔍 Predicted Water Quality</div>""",
        unsafe_allow_html=True)
prediction = predict_quality_from_db()
color = "#28a745" if prediction == "Bersih" else ("#dc3545" if prediction == "Kotor" else "#ffc107")
st.markdown(
    f"""
    <div class="metric-box" style="background-color: {color}20; border-left: 5px solid {color};">
        <div class="metric">Quality Prediction</div>
        <div class="metric-value" style="color: {color};">{prediction}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown(
    """
    <div class="footer">
        © 2025 Water Monitoring System | Data Mining Kel - 6
    </div>
    """,
    unsafe_allow_html=True
)
