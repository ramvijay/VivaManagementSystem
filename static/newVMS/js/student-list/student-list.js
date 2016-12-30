/**
 * Created by PRASANNA on 12/28/2016.
 */
function students_search() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  student_list = document.getElementById("student-list");
  rows = student_list.getElementsByTagName("header");
  divs = $(document.getElementById("student-list")).children()
  for (i = 0; i < rows.length; i++) {
    data = rows[i].getElementsByTagName("h3")[0];
    if (data) {
      if (data.innerHTML.toUpperCase().indexOf(filter) > -1) {
        divs[i].style.display = "";
      } else {
        divs[i].style.display = "none";
      }
    }
  }
}
$(document).ready(function(){
    $("#container").mCustomScrollbar({
        theme:"3d",
        scrollbarPosition: "inside"
    });

});

function UpdateStudentList(data){
    var student_record;
    $.each(data, function(i, item) {
        student_record = '<div class="w3-card-4" id="w3-card-4"><header class="w3-container w3-green"><h3>'+item.name+'</h3><h5>'+item.roll_no+'</h5></header>'+'<div class="w3-container">'+'<p class="organization-name">'+ item.organization_name+ '<br>'+ item.phone_number+ '<br>'+'</p></div></div>';
        $('#student-list').append(student_record);
    });
}
$(document).ready(function(){
   $.ajax({
       type: "POST",
       url: "/ajax/get_student_list/",
       data: {},
       dataType: "json",
       success: function(result) {
           UpdateStudentList(result["result"]);
       }
    });
});