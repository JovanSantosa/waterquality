import mysql.connector

def get_turbidity():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="monitorair"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT turbidity FROM tb_kualitas_air ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        return result[0] if result else "Data tidak tersedia"
    except mysql.connector.Error as err:
        return f"Terjadi kesalahan: {err}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
