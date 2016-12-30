jQuery(document).ready(function ($) {

	//madmin.init();


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
	$("#logout").on('click',function() {
	     $.post('/logout/',function (response) {
             window.location = "/login";
         });
    });
});
