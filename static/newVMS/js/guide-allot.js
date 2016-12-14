/**
 * Created by PRASANNA on 12/13/2016.
 */


$("#guide-allot-form").submit(function(){
    var $inputs = $('#guide-allot-form :input');
    var values = {};
    $inputs.each(function() {
        if($(this).is(":checked")){
            values[this.name] = $(this).val();
            alert(values[this.name]);
        }
    });
    $( "div.content" ).replaceWith( "<p>Guide List</p>" );
});