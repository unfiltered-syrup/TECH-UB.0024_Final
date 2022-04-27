<html>
<head>
  <style>
  body{
    margin:160px;
  }
  html {
  background: url(background.jpg) no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
form {
  border: 3px solid #f1f1f1;
}

/* Full-width inputs */
input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
  background-color: #b6cbdb;
}

/* Set a style for all buttons */
button {
  background-color: #064575;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

/* Add a hover effect for buttons */
button:hover {
  opacity: 0.8;
}

/* Extra style for the cancel button (red) */
.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

/* Center the avatar image inside this container */
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

/* Avatar image */
img.avatar {
  width: 40%;
  border-radius: 50%;
}

/* Add padding to containers */
.container {
  padding: 16px;
}

/* The "Forgot password" text */
span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
    display: block;
    float: none;
  }
  .cancelbtn {
    width: 100%;
  }
}
form{
  background-color: black;
  border-radius: 50px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom:15px;
  margin-left: 20%;
  margin-right: 20%;
}
h1{
  color: #c3d9eb;
  font-family: laviossa;
  font-size: 40px;
}
@font-face {
  font-family: laviossa;
  src: url("jehoo-creative-laviossa-medium.otf") format("opentype");
}
</style>
</head>
<body>
  <form action="login_process.php" method="post">
  <div class="imgcontainer">
    <h1>Login</h1>
  </div>

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
  </div>
</form>
  <?php
    if(isset($_GET['error'])){
      $errors=$_GET['error'];
      if($errors=="login_error"){
        echo '<script> alert("Try Again")</script>';
      }
    }
  ?>
</body>
</html>
