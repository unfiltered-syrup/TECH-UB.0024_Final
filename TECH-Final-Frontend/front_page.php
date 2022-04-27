<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  @font-face {
    font-family: laviossa;
    src: url("jehoo-creative-laviossa-medium.otf") format("opentype");
  }
  html {
  background: url(background.jpg) no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
  body{
    font-family: laviossa;
    margin-top: 10%;
    background-repeat: no-repeat;
    background-attachment: fixed;
    height: 100%;
}
h1{
  font-family: laviossa;
  font-size: 30px;
  font-weight: normal;
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: beige;
  color: rgba(2, 26, 62, 0.98);
}
.flip-card {
  background-color: transparent;
  width: 300px;
  height: 300px;
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  font-family: laviossa;

}
.container{
    top: 100;
    margin: auto;
    width: 15%;
}
#side-1 {
    transform: rotateY( 0deg );
}

#side-2 {
    transform: rotateY( 180deg );
}
.flip {
    backface-visibility: hidden;
    height: 352px;
    position: absolute;
    transform-origin: 50% 50% 0px;
    transition: all 3s;
    width: 231px;
}
.flip-side-1 {
    transform: rotateY( 0deg ) !important;
}

.flip-side-2 {
    transform: rotateY( 180deg ) !important;
}

#submit{
    width: 180px;
    height: 70px;
    positon: relative;
    border-width: 5px;
    border-color: rgba(13, 19, 56, 0.98);
    border-radius: 12px;
    background-color: rgba(13, 19, 56, 0.98);
    font-family: laviossa;
    font-size: 20px;
    font-weight: normal;
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: rgba(45, 39, 178, 0.8);
    color: beige;
}
#f{
    top: 20px;
    height: 240px;
    outline: none;
    border: none;
    margin-left: 10%;
    margin-right: 10%;
}
#text_input{
  font-family: laviossa;
  position: relative;
  background-color: rgba(0, 0, 0, 0);
  border: none transparent;
  outline: none;
  height: 150px;
  width: 180px;
  font-size: 18px;
  padding-left: 10px;
  padding-top: 10px;
  font-weight: 100;
  padding-right: 50px;
}
#text_box{
  position: absolute;
  height: 150px;
  width: 180px;
  background-color: white;
  opacity: 0.6;
  border-radius: 13px;

}
.slidein {
  animation-duration: 3s;
  animation-name: slidein;
  animation-iteration-count: 1;
  animation-direction: alternate;
}

@keyframes slidein {
  from {
    margin-top:50%;
  }

  to {
    margin-top:0%;
  }
}
#login{
  border-radius: 10px;
}
</style>
</head>
<body>
<button id="login">Login</button>
<div class="container">
  <div class="flip-card-inner">
    <div id = 'side-1' class='flip' style="background-image: url('cardbacks/card2.png');">
        <br><br>
        <h1>Vent to me!</h1>
        <form id="f" action="string_process.php" method="POST">
        <div id="text_box"></div>
        <textarea  id="text_input" type="text" placeholder="Enter your text"></textarea>
      </form>
      <button id="submit" onclick="flipping()">Hand Over the Card</button>
    </div>
    <div class="flip" id='side-2'>
      <img src="cardbacks/card1.png" alt="Avatar" style="width:231px;height:352px;">
    </div>
  </div>
</div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
<script>
  var card = document.querySelector('.container');
  var login_button = document.getElementById('login');
  function flipping(){
    event.preventDefault();
    document.getElementById( 'side-2' ).className = 'flip flip-side-1';
    document.getElementById( 'side-1' ).className = 'flip flip-side-2';
    setTimeout(function(){
    card.classList.add("slidein");
    },5000);
  }
  function user_login(){
    window.location.replace('login_page.php');
  }
  login_button.addEventListener("click",user_login);
  
</script>
</body>
</html>
