/*Global Variables*/
var guide_dict = {};
var stud_dict = {};
var map_dict = {};
var green_bound = 0;
var orange_bound = 6;
var tutor_id;

var rollno_detail_map = {}
var empid_detail_map = {}

jQuery(document).ready(function ($) {
    tutor_id = $("#tutor-id").val();
    $.ajax({
       url: '/ajax/get_student_list',

       error: function(err) {
          alert("Get Student List Ajax Error " +err.responseText);
       },
       success: function(data) {
            UpdateStudentList(data)
            $("#student-list").mCustomScrollbar({theme:"3d"});

       },
       type: 'GET'
    });
    $.ajax({
       url: '/ajax/get_guide_list',

       error: function(err) {
          alert("Get Faculty List Ajax Error " +err.responseText);
       },
       success: function(data) {

           data = jQuery.parseJSON(data);
           if(data.flag == 0){
                //alert("No guides have been selected, Select guides and come back again");
           }
            $.ajax({
               url: '/ajax/get_allotted_guide_list',
               error: function(err) {
                  alert("Get Student List Ajax Error " +err.responseText);
               },
               success: function(map_data) {
                   map_data = jQuery.parseJSON(map_data);
                   if(map_data.map_data == "no data"){
                       return;
                   }

                   map_data.map_data = jQuery.parseJSON(map_data.map_data);
                   data = $.extend(data,map_data)
                   UpdateFacultyList(data)
                   $("#faculty-list").mCustomScrollbar({theme:"3d"});

               },
                type: 'GET'
            });

       },
       type: 'GET'
    });
    $(document).ajaxStop(function () {
        $.each(map_dict,function(i,item){
            $.each(item,function(j,inner_item){
                if(inner_item.tutor == tutor_id){
                    stud = $("#"+inner_item.student).parent();
                    stud.hide();
                    stud_dict[inner_item.student] = stud;
                }
            })
        });
    });
    $("#confirm-allot").on("click",function(){

        alert("Are you sure this is the final guide allotment ");
        print_array= [];
        $.map(map_dict,function (value,key) {
            if (value.length > 0) {
                $.each(value, function (i, item) {

                    print_array.push({roll_no:item.student,stud_name:rollno_detail_map[item.student].name,
                        organization:rollno_detail_map[item.student].organization_name,guide_name:empid_detail_map[key].name,
                        guide_short_name:empid_detail_map[key].short_name});
                });
            }
        });
        console.log(print_array)
    });
});


function UpdateStudentList(data){
    var student;
    data = jQuery.parseJSON(data);
    $.each(data.result, function(i, item) {
          rollno_detail_map[item.roll_no] = item;
          student = '<div class="w3-card-4 card-margin  draggable "> <header id ='+item.roll_no+' class="w3-container w3-green"> <h4 class="student-roll">'+item.roll_no+'</h4> </header> <div class="w3-container custom-color-cream"> <div class="pull-left"> <strong>'+item.name+'</strong> </div><div class="pull-left organization-name">'+item.organization_name+'</div> <div class="area-of-interest pull-left"> <small>'+item.domain_key_word+'</small> </div> </div> </div>'
          $('#student-list').append(student);


    });
    $(".draggable").draggable({
        helper: 'clone',
        revert: 'invalid',
        appendTo: 'body',
        cursor: 'pointer',
    });
}


function UpdateFacultyList(data){
    var faculty;
    recommended_count = data.rc;
    orange_bound = recommended_count;
    $.each(data.result, function(i, item) {
        empid_detail_map[item.pk] = item.fields;
        if(item.fields.areas_of_interest.length > 63){
            item.fields.areas_of_interest = item.fields.areas_of_interest.substr(0,60)+'...';
        }
        no_of_allocated = Object.keys(data.map_data[item.pk]).length;
        w3_class = "w3-green";
        map_dict[item.pk] = data.map_data[item.pk];


        if(no_of_allocated > green_bound && no_of_allocated <= orange_bound){
            w3_class = "custom-color-warning";
        }
        else if(no_of_allocated > orange_bound){
            w3_class = "custom-color-danger";

        }
        faculty = '<div class="custom-card-margin" style="display: table "> <div class="w3-card-4" style="display: table-row"> <div class="faculty-detail "> <input type="hidden" class="emp-id" value='+item.pk+'><header class="w3-container '+w3_class+'"> <h4><span class="short-name">'+item.fields.short_name.toUpperCase()+'</span><span class="allot-status"> <span class="alloted-count">'+no_of_allocated+'</span>/ <span class="recommended-count">'+recommended_count+'</span> </span> </h4> </header> <div class="w3-container custom-color-cream padding-bottom-10"> <div class="core-competency pull-left"> <strong>'+item.fields.core_competency+'</strong> </div> <div class="area-of-interest pull-left"> <small>'+item.fields.areas_of_interest+'</small> </div> </div> </div> <div class="allot-now-div table-cell" > <span class="vertical-text">ALLOT NOW</span>  </div> </div> </div>';
        $('#faculty-list').append(faculty);
    });

    $("#faculty-list").on('click', '.allot-now-div', function(){
         AddFacultyToMappingPane($(this));
    });
}


$("#mapping-list").on('click','button',function () {
    var emp_id = $(this).parent().find('.emp-id').val();
    var alloted_count = $(this).parent().find('.alloted-count').text();
    guide_dict[emp_id].find('.alloted-count').text(alloted_count);
    guide_dict[emp_id].show();
    guide_dict[emp_id].find('header').removeClass('w3-green');
    guide_dict[emp_id].find('header').removeClass('custom-color-warning');
    guide_dict[emp_id].find('header').removeClass('custom-color-danger');
    if(alloted_count<=green_bound) {
        guide_dict[emp_id].find('header').addClass('w3-green');
    }else if(alloted_count>green_bound && alloted_count<=orange_bound){
        guide_dict[emp_id].find('header').addClass('custom-color-warning');
    }else{
        guide_dict[emp_id].find('header').addClass('custom-color-danger');
    }
    $(this).parent().hide();
});

$("#mapping-list").on('click','span',function () {
    var strVal = $(this).parent().html();
    rollNo = jQuery.trim(strVal.substr(0, strVal.indexOf('<span')));
    emp_id = $(this).parent().parent().parent().find('.emp-id').val();
    stud_dict[rollNo].show();
    index = map_dict[emp_id].map(function(e) { return e.student; }).indexOf(rollNo);
    map_dict[emp_id].splice(index,1);

    if($(this).parent().parent().children().length==1){
        $(this).parent().parent().addClass("empty-container");
    }
    var alloted_count = parseInt($(this).parent().parent().parent().find('.alloted-count').text().trim(),10)-1;
    if(alloted_count<=green_bound) {
        $(this).parent().parent().parent().find('header').addClass('w3-green');
        $(this).parent().parent().parent().find('header').removeClass('custom-color-danger');
        $(this).parent().parent().parent().find('header').removeClass('custom-color-warning');
    }
    else if((alloted_count>green_bound)&&(alloted_count<=orange_bound)){
        $(this).parent().parent().parent().find('header').removeClass('w3-green');
        $(this).parent().parent().parent().find('header').removeClass('custom-color-danger');
        $(this).parent().parent().parent().find('header').addClass('custom-color-warning');
    }
    else if((alloted_count>orange_bound)){
        $(this).parent().parent().parent().find('header').removeClass('w3-green');
        $(this).parent().parent().parent().find('header').addClass('custom-color-danger');
        $(this).parent().parent().parent().find('header').removeClass('custom-color-warning');
    }

    $(this).parent().parent().parent().find('.alloted-count').text(alloted_count);
    $(this).parent().remove();
    $.ajax({
       type:"POST",
       url: '/ajax/delete_allotted_guide_list/',
       data: {"delete_input":JSON.stringify({"roll":rollNo,"emp_id":emp_id})},
       dataType: "json",
       error: function(err) {
          alert("delete mapping List Ajax Error " +err.responseText);
       },
       success: function(data) {
           // console.log(data);
       }
    });
});
function AddFacultyToMappingPane(cmp){
        var short_name = cmp.parent().find('.short-name').text().trim();
        var alloted_count =  cmp.parent().find('.alloted-count').text().trim();
        var recommended_count = cmp.parent().find('.recommended-count').text().trim();
        var emp_id = cmp.parent().find('.emp-id').val();


        var w3_class = "";
        if(cmp.parent().find('header').hasClass("w3-green")){
            w3_class = "w3-green";
        }else if(cmp.parent().find('header').hasClass("custom-color-warning")){
            w3_class = "custom-color-warning";
        }else{
            w3_class = "custom-color-danger";
        }

        var faculty = '<div class="w3-card-4 card-margin droppable"> <header class="w3-container '+w3_class+'"><input type="hidden" class="emp-id" value='+emp_id+'> <h4>'+short_name+'<span class="allot-status"><span class="alloted-count">'+alloted_count+'</span>/<span class="recommended-count">'+recommended_count+'</span></span> </h4> </header> <div class="w3-container custom-color-cream empty-container mapped-stud-list"></div> <hr class="dash-line" style="display: none"/> <div class="w3-container custom-color-cream extra-stud-list"> </div> <button class="w3-btn-block w3-dark-grey"><- Done Alloting</button> </div>'
        $('#mapping-list').children().first().children().first().append(faculty);

        $.each(map_dict[emp_id], function(i, item) {
            if(item.tutor == tutor_id) {
                $('#mapping-list').children().first().children().first().children().last().find('.mapped-stud-list').removeClass("empty-container");
                $('#mapping-list').children().first().children().first().children().last().find('.mapped-stud-list').append('<div class="stud-grid">' + item.student + '<span class="close-btn">X</span></div>');
            } else{
                $('#mapping-list').children().first().children().first().children().last().find('.dash-line').show();
                $('#mapping-list').children().first().children().first().children().last().find('.extra-stud-list').append('<div class="stud-grid">' + item.student + '</div>');
            }
        });

        cmp.parent().parent().hide();
        guide_dict[emp_id] = cmp.parent().parent();
        $(".droppable").droppable({
            hoverClass: "cell-highlght",
            tolerance: "pointer",
            drop: function(event, ui) {
                var rollNo= jQuery.trim((ui.draggable).children(":first").text());
                var emp_id = $(this).find('.emp-id').val();
                $(this).find('.mapped-stud-list').append('<div class="stud-grid">'+rollNo+'<span class="close-btn">X</span></div>');
                alloted_count = parseInt($(this).find('.alloted-count').text().trim(),10)+1;
                map_dict[emp_id].push({student:rollNo,tutor:tutor_id});
                $(this).find('.mapped-stud-list').removeClass("empty-container");
                map_dict_string = JSON.stringify({guide:emp_id,student:rollNo,tutor:tutor_id});
                var faculty_element = $(this);

                $.ajax({
                   type:"POST",
                   url: '/ajax/update_allotted_guide_list/',
                   data: {"map_data": map_dict_string},
                   dataType: "json",
                   error: function(err) {
                      alert("update mapping List Ajax Error " +err.responseText);
                   },
                   success: function(data) {
                        new_count=0;
                        if(data["result"]!="no_data") {
                            json_data = JSON.parse(data.result);
                            faculty_element.find('.extra-stud-list').children().remove();

                            $.each(json_data, function (i, item) {
                                faculty_element.find('.extra-stud-list').append('<div class="stud-grid">' + item.fields.student + '</div>');
                                new_count++;
                            });
                        }
                        alloted_count = alloted_count + new_count;
                        if(alloted_count<=green_bound){
                            faculty_element.find('header').addClass('w3-green');
                            faculty_element.find('header').removeClass('custom-color-danger');
                            faculty_element.find('header').removeClass('custom-color-warning');
                        }
                        if((alloted_count>green_bound)&&(alloted_count<orange_bound)){
                            faculty_element.find('header').removeClass('w3-green');
                            faculty_element.find('header').removeClass('custom-color-danger');
                            faculty_element.find('header').addClass('custom-color-warning');
                        }
                        if((alloted_count>orange_bound)){
                            faculty_element.find('header').removeClass('w3-green');
                            faculty_element.find('header').addClass('custom-color-danger');
                            faculty_element.find('header').removeClass('custom-color-warning');
                        }
                        faculty_element.find('.alloted-count').text(alloted_count);
                        stud_dict[rollNo] = ui.draggable;
                        (ui.draggable).hide();

                   }
                });
            }
        });
}