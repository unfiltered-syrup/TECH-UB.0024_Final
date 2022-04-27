<?php
  $username = $_POST['uname'];
  $password = $_POST['psw'];
  $correct_password = "123456";
  $correct_username = "vent";
  if($username == $correct_username && $password == $correct_password){
    setcookie("usernames", $username);
    header('location: front_page.php');
    exit();
  }
  else{
    header('location: login_page.php?error=login_error');
    exit();
  }


?>
