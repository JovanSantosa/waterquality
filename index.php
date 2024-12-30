<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Monitoring Air</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  
    <script type="text/javascript" src="jquery/jquery.min.js"></script>

    <!-- Proses Realtime masbro -->
    <script type="text/javascript">
        $(document).ready( function(){
            //interval refresh / realtime = 1 detik = 1000 milidetik
            setInterval( function(){
                $("#ph").load("readph.php");
                $("#temp").load("readtemp.php");
                $("#tur").load("readturbidity.php");
                $("#con").load("readconductivity.php");
                $("#ph").load("readph.php");
                $("#res").load("result.php");
                $("#status").load("bacastatus.php");
            }, 1000);
        });
    </script>

    <!-- Akhir Proses Realtime masbro -->

</head>
  <body>
    <div class="container" style="text-align: center; margin-top: 100px;">
        <img src="img/Logo UDINUS.png" style="width:100px">
        <h2>Sistem Monitoring Kekeruhan Air <br>Secara Realtime Melalui Halaman Website <br>Kelompok 5 Data Mining <br>Aqua Insight</h2>
        <p style="font-size:24px">-DFRobot Turbidity Sensor, SENSOR PH METER MODULE PH-4502C, DHT11-</p>
        <!-- Kolom Tampilan Nilai Sensor masbro -->
        <div class="container text-center">
        <div class="row align-items-start">
            <div class="col">
                
            <!-- Kotak Nilai Sensor masbro -->
            <div class="card">
            <div class="card-header" style="background-color: red; color: white">
                <h3>Temperature</h3>
            </div>
            <div class="card-body" id="temp">
            </div>
            </div>

            <div class="card">
            <div class="card-header" style="background-color: red; color: white">
                <h3>pH</h3>
            </div>
            <div class="card-body" id="ph">
            </div>
            </div>
            
            


            <!-- Akhir Kotak Nilai Sensor masbro -->
            </div>
            <div class="col">
            <div class="card">
            <div class="card-header" style="background-color: red; color: white">
                <h3>Turbidity</h3>
            </div>
            <div class="card-body" id="tur">
            </div>
            </div>

            <div class="card">
            <div class="card-header" style="background-color: red; color: white">
                <h3>Conductivity</h3>
            </div>
            <div class="card-body" id="con">
            </div>
            </div>
            </div>
            <div class="col">

           <!-- Kotak Status Air masbro -->
           <div class="card">
            <div class="card-header" style="background-color: blue; color: white">
                <h3>STATUS AIR</h3>
            </div>
            <div id="res">

            </div>
            
            </div>
            </div
            <!-- Akhir Kotak Status Air masbro -->
            </div>
            
        </div>
        </div>
         <!-- Akhir Kolom Tampilan Nilai Sensor masbro -->
          <br>
          <img src="img/Aqua Insight.png" style="width:200px">
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>