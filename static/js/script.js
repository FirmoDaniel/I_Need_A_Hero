$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    /*$('.modal').modal();
    $('#modal1').hide();*/
    
    /*If session cookie / user exists update to check on doc change*/
    if(document.cookie.indexOf('session')){
        $('.session-exists-hide').hide();
    }
    

    
    let success=$('#test').text();
    if(success == "Registration Successful"){
        $('#test').addClass("green")
    } else if(success == "Username already exists"){
        $('#test').removeClass("green").addClass("red")
    } else if(success == "You've been logged out. #SadTimes! Come back soon"){
        $('#test').addClass("blue")
    }

    /* not wokring 
    $(document).on( "click", '#delete', function(){
        var instance = M.Modal.getInstance(elem);
        $('#modal1').show()

    });*/
    
    /*Taken from CI source code for form select:validation on create.html*/
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }

  });

  /*window resizing*/
    $( window ).resize(function(){
    if ((screen.width>425)) {
    // if screen size is 425px wide or larger
        $('#jq-valign').addClass('valign-wrapper'); 
        }
        else if ((screen.width<=425)){
            // if screen size width is less than 425px
           $('#jq-valign').removeClass('valign-wrapper'); 
    }});