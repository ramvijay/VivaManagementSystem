$(document).ready(function(){
    $("#loginButton").on('click', function()  {
        var username = $('#username').val();
        var password = $('#password').val();
        $.post('ajax/login.php', {username : username, password : password}, function(response){
            var jsonData = JSON.parse(response);
            if(jsonData.status == 'Ok') {
                //Redirect the user
                window.location = "index.php";
            } else {
                $('#statusMsg').html(jsonData.status);
            }
        });
    });
});