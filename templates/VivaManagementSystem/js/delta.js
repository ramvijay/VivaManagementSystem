$(document).ready(function(){
    $("#LogoutUser").on('click', function(){
        $.post('ajax/logout.php', {}, function(response){
            window.location = "index.php";
        });
    });
});