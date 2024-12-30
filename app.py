import streamlit as st
from Respon import predict_quality_from_db  # Mengimpor fungsi prediksi
from readtemp import get_temperature  # Mengimpor fungsi untuk membaca temperature
from readph import get_ph
from readtur import get_turbidity
from readcon import get_conductivity
st.title("Monitoring Kualitas Air Data Mining")

# Bagian Pembacaan Suhu
# st.subheader("Data Suhu (Temperature)")
temperature = get_temperature()  # Mengambil data suhu dari database
if isinstance(temperature, str):  # Cek jika ada pesan error
    st.error(f"Error: {temperature}")
else:
    st.subheader(f"Temperature: {temperature} °C")

# Bagian Pembacaan pH
# st.subheader("Data pH ")
ph = get_ph()  # Mengambil data suhu dari database
if isinstance(ph, str):  # Cek jika ada pesan error
    st.error(f"Error: {ph}")
else:
    st.subheader(f"pH: {ph}")

# Bagian Pembacaan Suhu
# st.subheader("Data Turbidity ")
tur = get_turbidity()  # Mengambil data suhu dari database
if isinstance(tur, str):  # Cek jika ada pesan error
    st.error(f"Error: {tur}")
else:
    st.subheader(f"Turbidity: {tur} NTU")

# Bagian Pembacaan Suhu
# st.subheader("Data Conductivity ")
con = get_conductivity()  # Mengambil data suhu dari database
if isinstance(ph, str):  # Cek jika ada pesan error
    st.error(f"Error: {con}")
else:
    st.subheader(f"Conductivity: {con} S/m")

# Bagian Prediksi Kualitas Air
st.subheader("Hasil Prediksi Kualitas Air")
prediction = predict_quality_from_db()
st.subheader(f"Kualitas Air: {prediction}")

