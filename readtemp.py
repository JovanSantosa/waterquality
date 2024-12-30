import mysql.connector
import streamlit as st

# Koneksi ke database
def get_temperature():
    try:
        # Menghubungkan ke database MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Ganti dengan username database Anda
            password="",  # Ganti dengan password database Anda
            database="monitoringair"  # Nama database
        )
        
        cursor = connection.cursor()
        
        # Menjalankan query untuk membaca nilai temperature dari tb_kualitas_air
        cursor.execute("SELECT temperature FROM tb_kualitas_air ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()  # Mengambil data terbaru
        
        if result:
            return result[0]  # Mengembalikan nilai temperature
        else:
            return "Data tidak tersedia"
    
    except mysql.connector.Error as err:
        return f"Terjadi kesalahan: {err}"
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Streamlit untuk antarmuka
st.title("Monitoring Kualitas Air")

# Ambil dan tampilkan nilai temperature
temperature = get_temperature()
st.header(f"Temperature: {temperature} °C")
