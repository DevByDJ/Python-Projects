<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Zen+Tokyo+Zoo&display=swap" rel="stylesheet">
    <title>D&D Analogs</title>
</head>
<body>
    <div class="container">
       
        <nav>
            <img src="images/logo.png" class="logo">
            <div class="nav-icons">
                <img src="images/search.png">
                <img src="images/cart.png">
                <img src="images/menu.png">
                
            </div>
        </nav>
        <div class="row">
            <div class="col-1">
                <h1>Nike<br>Sports Air</h1>
                <p>The Nike Air Zoom 15 Is Back Upfated Cushioning<br> And A Tough Outsole for Traction</p>
                <h2>$150</h2>
                <button type="button">ADD TO CART</button>
            </div>
            <div class="col-2">
                <div class="feature-img">
                    <img src="images/nike.png">
            </div>
        <div class="small-img-row">
            <div class="small-img">
               <img src="images/nike-b.png" >
            </div>
            <div class="small-img">
                <img src="images/nike-s.png" >   
            </div>
            <div class="small-img">
                <img src="images/nike-b.png" >
            </div>
            <div class="small-img">
                <img src="images/nike-g.png" id="icon" >
            </div>
        </div>
        <script src="main.js"></script>
        </div>
        
      </div>
        <script type="text/javascript">
           
           function change(){
               var image = document.getElementById("small-img");
               image.src = "images/nike-b.png"
           }

        </script>
</body>
</html>