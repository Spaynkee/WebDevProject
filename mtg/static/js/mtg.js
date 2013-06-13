var currentEdition = 1;

$(function()
{
"use strict";
    $("#cardName").keypress(function(e){
        if(e.which === 13){
           $("#getCard").click(search_and_get());
        }
    });
   $("#getCard").click(search_and_get);
   $("#getRandom").click(get_random);     
   $("#cycleEditions").click(cycle_editions); 
   $("#searchList").click(results_change);                
});

function search_and_get() {
"use strict";
            $.ajax({
            url: "/search_cards/",
            data: { pyCardName: $("#cardName").val()},
            contentType: "application/json; charset=utf-8",
            success:
            function(cardString)
            {
                if (cardString !== "")
{
                $("#searchList").children().remove();
                while(cardString !== "")
                {
                var split = cardString.substring(0, (cardString.indexOf("~")));
                var opt = document.createElement("option");
                opt.text = split;
                opt.value = split;
                opt.innerHTML = split;
                $("#searchList").append("<option>"+split+"</option>");
                cardString = cardString.substring(split.length + 1);
                }
                }
                else
                {
                alert("No cards with that string found.");
                }
            }});

            $.ajax({
            url: "/get_card/",
            data: { pyCardName: $("#cardName").val()},
            contentType: "application/json; charset=utf-8",
            success:
            function(cardInfo)
            {
            fade_out(cardInfo);
            currentEdition = 1;
            change_info(cardInfo);
            $("#cardPic").fadeTo(1000, 1);
            }});
}

function get_random() {
"use strict";
        document.getElementById("searchList").options.length = 0;
          $.ajax({
            url: "/get_random/",
            contentType: "application/json; charset=utf-8",
            success:
            function(cardInfo)
            {
                fade_out(cardInfo);

            currentEdition = 1;
            change_info(cardInfo);
            $("#cardPic").fadeTo(1000, 1);
            }
                });              
                }    

function cycle_editions() {
"use strict";
          $.ajax({			
            url: "/cycle_editions/",
            data: { pyEdition: $("#spanEd").html(), pyName: $("#spanName").html()},
            contentType: "application/json; charset=utf-8",
            success:
            function(cardInfo)
            {
                currentEdition += 1;
                $("#spanEd").html(cardInfo.edition_id);	
                 if (parseInt($("#spanCurEd").html(), 10) >=(parseInt($("#spanMaxEd").html(), 10)))
                {
                    currentEdition = 1;
                }

            fade_out(cardInfo);
            change_info(cardInfo);
            $("#cardPic").fadeTo(1000, 1);
            }
       });
                
    }
        
function results_change() {
"use strict";
    if ($("#searchList").val() !== null)
    {
    $.ajax({
            url: "/get_card/",
            data: { pyCardName: $("#searchList").val()},
            contentType: "application/json; charset=utf-8",
            success:
            function(cardInfo){
            fade_out(cardInfo);
            change_info(cardInfo);
            currentEdition = 1;
            $("#cardPic").fadeTo(1000, 1);
            }
                });
    }
}

function change_info(cardInfo)
{
"use strict";
                $('#spanName').html(cardInfo.name);				
                $("#spanFlavor").html(cardInfo.flavor);				
                $("#spanIllustrator").html(cardInfo.illustrator);				
                $("#spanType").html(cardInfo.type);	
                $("#spanEd").html(cardInfo.edition_id);	
                $("#spanMaxEd").html(cardInfo.max_editions);		
                $("#spanCost").html(cardInfo.cost);	
                $("#spanAbilities").html(cardInfo.abilities);   
                $("#spanCurEd").html(currentEdition);
                
}

function fade_out(cardInfo)
{
"use strict";
 if ($("#cardPic").css("opacity") > 0)
                {
                    $("#cardPic").fadeTo(500, 0, function()
                    {
                    $("#cardPic").attr("src", cardInfo.graphic);	
                    }
                    );
                }
}