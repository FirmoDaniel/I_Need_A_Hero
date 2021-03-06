$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $(".modal").modal();

/* Thank you message on contact form submit. */
    $(".contactMessage").hide();
    $("#contactForm").submit(function(){
        $(".contactMessage").delay(1000).fadeIn(3000);
    });


/* Defensive hide/show and alerts for character deletion on characters.html */
    $(".characterDeleteButton").hide();
    $(".cancelButton").hide();
    
    $(".callDeleteCancelButtons").on("click", function(){
    $(".characterDeleteButton").show();
    $(".cancelButton").show();
    $(".fakeCharacaterDeleteButton").hide();
    $(".editRoleButton").hide();
    });

    $(".ifVisible").on("click", function(){
        if($(".characterDeleteButton").is(':visible') === $(".characterDeleteButton").is(':not(:hidden)')){
           $(".characterDeleteButton").hide();
           $(".cancelButton").hide();
           $(".fakeCharacaterDeleteButton").show();
        }
        
    });
    
    let profileCharacters = $('#profileCharacters').text();
        if(profileCharacters == ""){
            $('#profileCharactersNone').show();
            $('#profileHideCollapsible').hide();
            $('#ifProfileCharactersExist').hide();
        }else{
            $('#profileCharactersNone').hide();
            $('#ifProfileCharactersExist').show();

     }

/* Taken from CI source code for form select:validation on create_character.html */
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

/* Window resizing */
    if ((screen.width>536)) {
    // if screen size is larger
        $('#jq-valign').addClass('valign-wrapper');
        }
        
        else if ((screen.width<=536)){
            // if screen size width smaller or equal
            $('#jq-valign').removeClass('valign-wrapper');
            
    }

});

