import joblib
import mysql.connector
import pandas as pd

# Fungsi untuk mengambil data dari database
def get_data_from_db():
    try:
        # Koneksi ke database MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # ganti dengan username database Anda
            password='',  # ganti dengan password Anda
            database='monitoringair'  # ganti dengan nama database Anda
        )

        cursor = connection.cursor()

        # Query untuk mengambil data pH, temperature, turbidity, dan conductivity dari database
        cursor.execute("SELECT pH, temperature, turbidity, conductivity FROM tb_kualitas_air ORDER BY id DESC LIMIT 1")  # mengambil data terbaru
        result = cursor.fetchone()

        if result:
            # Ambil nilai dari result (pastikan data ada)
            pH, temperature, turbidity, conductivity = result
            return [pH, temperature, turbidity, conductivity]
        else:
            print("Data tidak ditemukan.")
            return None

    except mysql.connector.Error as err:
        print(f"Terjadi kesalahan: {err}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Muat model yang telah dilatih
model = joblib.load('model_kualitas_air.pkl')

# Fungsi untuk melakukan prediksi kualitas air
def predict_quality_from_db():
    # Ambil data dari database
    input_data = get_data_from_db()

    if input_data:
        # Mengubah input menjadi DataFrame dengan kolom yang sesuai
        input_df = pd.DataFrame([input_data], columns=['pH', 'Temperature (°C)', 'Turbidity (NTU)', 'Conductivity (µS/cm)'])

        # Prediksi kualitas air
        prediction = model.predict(input_df)

        # Output hasil prediksi
        if prediction[0] == 'Baik':
            return "Bersih"
        elif prediction[0] == 'Buruk':
            return "Kotor"
        else:
            return "Keruh"
    else:
        return "Data tidak tersedia"

if __name__ == "__main__":
    # Menampilkan hasil prediksi agar dapat dibaca PHP
    print(predict_quality_from_db())
