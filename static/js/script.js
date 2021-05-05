$(document).ready(function(){
    $('.sidenav').sidenav();
    
    let success=$('#test').text();
    if(success == "Registration Successful"){
        $('#test').addClass("green")
    } else if(success == "Username already exists"){
        $('#test').removeClass("green").addClass("red")
    } else if(success == "You've been logged out. #SadTimes! Come back soon"){
        $('#test').addClass("blue")
    } 

  });