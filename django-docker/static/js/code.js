$(document).ready(function(){
  
    $("#nav-toggle").click(function(){
        $("#nav-toggle").toggleClass('Open');
        $(".hide-menu").toggleClass('Open');
  
    })
    $("#nav-toggle").bind("click", function(){
        return false;
    })
        
    })