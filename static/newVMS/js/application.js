jQuery(document).ready(function ($) {
	// Setup the Extruder
	$("#extruderLeft").buildMbExtruder({
		position:"left",
		width:250,
		extruderOpacity:.8,
		hidePanelsOnClose:true,
		accordionPanels:true,
		onExtOpen:function(){},
		onExtContentLoad:function(){},
		onExtClose:function(){}
	});
	// Click Listener
	$("#logout").on('click',function() {
	     $.post('/logout/',function (response) {
             window.location = "/login";
         });
    });
	if(navigator.onLine) {
		$("#online-status").html("&nbsp;&nbsp;(online)");
		$("#online-status").css("color", "lightgreen");
	} else {
		$("#online-status").html("&nbsp;&nbsp;(offline)");
		$("#online-status").css("color", "red");
	}
	$("#sync_data").click(function(){
		$.ajax({
		   url: '/ajax/sync_data',
		   error: function(err) {
			  alert("Error syncing data, try again");
		   },
		   success: function(data) {
		   	  if(data != null) {
				  alert("Data synced successfully");
              }
		   },
		   type: 'GET'
    	});
	});
});
