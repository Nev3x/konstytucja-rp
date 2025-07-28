<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>konstytucja-rp.pl</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav><a href="/konstytucjarp/prawo">Prawo</a> i <a href="/konstytucjarp/konstytucja">Konstytucja</a></nav>
    <div class="wprowadzenie">
        <h2>Witaj obywatelu!</h2>
        <select name="arts" id="artykuly">
        <?php
        for ($i = 1; $i <= 243; $i++) {
            echo "<option value=\"Art.$i\">Art.$i</option>\n";
        }
        ?>
        </select><br><br>

        <h4 id="artText">Art. 1. Rzeczpospolita Polska jest dobrem wspólnym wszystkich obywateli. </h4>
    </div>
    <script src="script.js"></script>
</body>
</html>