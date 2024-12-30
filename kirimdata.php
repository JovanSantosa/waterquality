<?php
    //Koneksi ke database bro
    $koneksi = mysqli_connect("localhost", "root", "", "monitoringair");

    $nilai_sensor = $_GET['sensor'];

    //Update nilai sensor di tabel tb_sensor
    mysqli_query($koneksi, "UPDATE tb_sensor SET sensor='$nilai_sensor'");
?> 