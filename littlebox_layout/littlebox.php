<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Littlebox</title>
    <link href="style_basic.css" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
  </head>
  <body>
  <div id="timeline">
    <header>
      <h1 id="titre"><i class="fas fa-archive"></i> Littlebox</h1>
      <!-- <i class="fas fa-cog fa-3x"></i> -->
      <i class="fas fa-sliders-h fa-3x" id="config"></i>
    </header>
  </div>

  <!-- Les templates de la page de bd -->
    <?php
      // etape 1 : recuperer les datas (file ou Mysql)
      $timeline = file_get_contents('timeline.json');
    ?>

    <script type="text/javascript">
      // etape 2 : passer les datas dans js
       var timeline = <?php echo $timeline; ?>;
    </script>

    <!-- development version, includes helpful console warnings -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <!-- app timeline_reader -->
    <script src="js/timeline_reader.js" charset="utf-8"></script>


  </body>
</html>
