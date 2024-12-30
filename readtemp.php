<?php
    //Koneksi ke database bro
    $koneksi = mysqli_connect("localhost", "root", "", "monitoringair");

    //Baca tabel sensor bro
    $sql = mysqli_query($koneksi, "SELECT * FROM tb_kualitas_air");

    //Ambil nilai dari tb_sensor bro (sensor)
    $data = mysqli_fetch_array($sql);

    //Ambil nilai field sensor
    $nilai_sensor =  $data['temperature'];
?>

<h1 style="font-size: 100px"><?php echo $nilai_sensor; ?></h1>