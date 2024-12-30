
<h1><?php
            // Menjalankan skrip Python untuk mendapatkan hasil prediksi kualitas air
            $output = shell_exec('python .\Respon.py');  // Sesuaikan path ke skrip Python Anda
            echo  $output ;
            ?></h1>