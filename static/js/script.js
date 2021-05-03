$(document).ready(function(){
    $('.sidenav').sidenav();
    
    let success=$('#test').text();
    if(success == "Registration Successful"){
        $('#test').addClass("green")
    } if(success == "Username already exists"){
        $('#test').removeClass("green").addClass("red")
    } 

  });