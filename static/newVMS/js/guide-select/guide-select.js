/**
 * Created by PRASANNA on 12/13/2016.
 */
function invSortRows(a, b){
    if ( $(a).find('td:first-Child').text() > $(b).find('td:first-Child').text() ) {
        return 1;
      }

      if ( $(a).find('td:first-Child').text() < $(b).find('td:first-Child').text() ) {
        return -1;
      }

      return 0;
}
function sortRows(a, b){
    if ( $(a).find('td:first-Child').text() < $(b).find('td:first-Child').text() ) {
        return 1;
      }

      if ( $(a).find('td:first-Child').text() > $(b).find('td:first-Child').text() ) {
        return -1;
      }

      return 0;
}
$('#alpha-sort').on('click', function(){
    //get the rows from the table
    rows = $('#table0 tbody').find('tr');
    //sort the rows as "sortedrows"
    sortedRows = rows.sort(sortRows);
    //replace the old rows with the new rows
    $('#table0 tbody').empty();
    //$('#table0 tbody').append(sortedRows);
    $.each(sortedRows, function(i, item){
       if(i % 2 == 0)
           $(this).removeClass($(this).className).addClass("odd");
        else
            $(this).removeClass($(this).className).addClass("even");
        $('#table0 tbody').append(this);
    });
});
$('#alpha-alt-sort').on('click', function(){
    //get the rows from the table
    rows = $('#table0 tbody').find('tr');
    //sort the rows as "sortedrows"
    sortedRows = rows.sort(invSortRows);
    //replace the old rows with the new rows
    $('#table0 tbody').empty();
    //$('#table0 tbody').append(sortedRows);
    $.each(sortedRows, function(i, item){
       if(i % 2 == 0)
           $(this).removeClass($(this).className).addClass("odd");
        else
            $(this).removeClass($(this).className).addClass("even");
        $('#table0 tbody').append(this);
    });
});
(function($){
    $(window).on('load',function(){
        $("#content").mCustomScrollbar({
            theme:"3d",
            scrollbarPosition: "inside"
        });
    });
})(jQuery);

function UpdateFacultyList(data){
    var faculty;
    $('#table0 tbody').empty()
    $.each(data, function(i, item){
        if(i % 2 == 0)
            faculty = '<tr class="odd" id = '+ item["pk"] + '><td>' + item["fields"]["title"] + ' ' + item["fields"]["name"] + '</td><td>' + item["fields"]["designation"] + '</td><td>' + item["fields"]["core_competency"] + '</td><td>' + item["fields"]["short_name"] + '</td> <td class="input"> <label class="switch"> <input type="checkbox" id ="'+item["pk"]+'" '+'value="'+item["pk"]+'"class="checkbox pull-right" > <div class="slider round"></div> </label> </td> </tr>'
        else
            faculty = '<tr class="even" id = '+ item["pk"] + '><td>' + item["fields"]["title"] + ' ' + item["fields"]["name"] + '</td><td>' + item["fields"]["designation"] + '</td><td>' + item["fields"]["core_competency"] + '</td><td>' + item["fields"]["short_name"] + '</td> <td class="input"> <label class="switch"> <input type="checkbox" id ="'+item["pk"]+'" ' +'value="'+item["pk"]+'"class="checkbox pull-right" > <div class="slider round"></div> </label> </td> </tr>'
        $('#table0 tbody').append(faculty);
    });
}

function UpdateGuideList(data){
    var guide;
    $('#table0 tbody').empty();
    $.each(data, function(i, item) {
        if(i % 2 == 0)
            guide = '<tr class="odd" id = '+ item["pk"] + '><td>' + item["fields"]["title"] + ' ' + item["fields"]["name"] + '</td><td>' + item["fields"]["designation"] + '</td><td>' + item["fields"]["core_competency"] + '</td><td>' + item["fields"]["short_name"] + '</td> <td class="input"> <input type="textbox" name ="count"> </td> <td style="padding-left: 5%">5</td></tr>';
        else
            guide = '<tr class="even" id = '+ item["pk"] + '><td>' + item["fields"]["title"] + ' ' + item["fields"]["name"] + '</td><td>' + item["fields"]["designation"] + '</td><td>' + item["fields"]["core_competency"] + '</td><td>' + item["fields"]["short_name"] + '</td> <td class="input"> <input type="textbox" name ="count"> </td><td style="padding-left: 5%">5</td></tr>';
        $('#table0 tbody').append(guide);
    });
}

function EditFacultyList(data){
    var faculty;
    $('#table0 tbody').empty();
    $(".heading").html("Faculty List");
    $("th.variable").html("Is Guide?");
    $("th.count").remove();
    $.each(data, function(i, item){
        if(i % 2 == 0)
            if(item["fields"]["is_guide"] == 1)
                faculty = '<tr class="odd" id = '+ item["pk"] + '><td>' + item["fields"]["title"] + ' ' + item["fields"]["name"] + '</td><td>' + item["fields"]["designation"] + '</td><td>' + item["fields"]["core_competency"] + '</td><td>' + item["fields"]["short_name"] + '</td> <td class="input"> <label class="switch"> <input type="checkbox" id ="'+item["pk"]+'" '+'value="'+item["pk"]+'"class="checkbox pull-right" checked> <div class="slider round"></div> </label> </td> </tr>'
            else
                faculty = '<tr class="odd" id = '+ item["pk"] + '><td>' + item["fields"]["title"] + ' ' + item["fields"]["name"] + '</td><td>' + item["fields"]["designation"] + '</td><td>' + item["fields"]["core_competency"] + '</td><td>' + item["fields"]["short_name"] + '</td> <td class="input"> <label class="switch"> <input type="checkbox" id ='+item["pk"]+'" '+'value="'+item["pk"]+'"class="checkbox pull-right" > <div class="slider round"></div> </label> </td> </tr>'
        else
            if(item["fields"]["is_guide"] == 1)
                faculty = '<tr class="even" id = '+ item["pk"] + '><td>' + item["fields"]["title"] + ' ' + item["fields"]["name"] + '</td><td>' + item["fields"]["designation"] + '</td><td>' + item["fields"]["core_competency"] + '</td><td>' + item["fields"]["short_name"] + '</td> <td class="input"> <label class="switch"> <input type="checkbox" id ='+item["pk"]+'" '+'value="'+item["pk"]+'"class="checkbox pull-right" checked> <div class="slider round"></div> </label> </td> </tr>'
            else
                faculty = '<tr class="even" id = '+ item["pk"] + '><td>' + item["fields"]["title"] + ' ' + item["fields"]["name"] + '</td><td>' + item["fields"]["designation"] + '</td><td>' + item["fields"]["core_competency"] + '</td><td>' + item["fields"]["short_name"] + '</td> <td class="input"> <label class="switch"> <input type="checkbox" id ='+item["pk"]+'" '+'value="'+item["pk"]+'"class="checkbox pull-right" > <div class="slider round"></div> </label> </td> </tr>'
        $('#table0 tbody').append(faculty);
    });
}

$("h1").on('click', '#edit-button', function(){
    $.ajax({
       type:"POST",
        url: "/ajax/get_faculty_list/",
        data:{},
        dataType: "json",
        success:function(result){
            EditFacultyList(result["result"]);
            $("a#submit-button").show();
            $("button#edit-button").remove();
        },
        error: function(){alert("error");}
    });
});
$(document).ready(function(){
    $.ajax({
        type: "POST",
        url: "/ajax/get_guide_list/",
        data: {},
        dataType: "json",
        success: function(result){
            console.log(result["result"][0]["fields"]);
            if(result["flag"] == 1){
                $(".heading").html("Eligible Guides");
                $("th.variable").html("Students allocated");
                $("#table0 thead tr").append('<th class="header count" style="width:8%">Recommended</th>');
                $("a#submit-button").hide();
                UpdateGuideList(result["result"]);
                $("h1#heading").append('<a href="#" id="edit-button"><span class="glyphicon glyphicon-edit"></span></a>');
                //$("h1#heading").append('<button type="submit" id="edit-button" style="margin-left: 20%" value="Submit"> Edit </button>');
            }
            else
                UpdateFacultyList(result["result"]);
        }
    });
});

$("#submit-button").click(function(){
    var allVals = [];
    var data;

    $('#content :checked').each(function() {
	    allVals.push($(this).val());
	});
    $.ajax({
         type:"POST",
         url:"/ajax/update_guides/",
         data: {"input[]": allVals},
         dataType: "json",
         success:function(result){
             data = (result);
             $('input:checkbox:not(:checked)').each(function() {
	            allVals.push($(this).val());
                $("tr#"+($(this).val())).remove();
	        });
            $(".heading").html("Eligible Guides");
            $('tbody tr').each(function(index) {
                $(this).append('<td style="padding-left: 5%">5</td>');
	            if(index % 2 == 0){$(this).removeClass().addClass("even");}
                else{$(this).removeClass().addClass("odd");}
	        });
            $("th.variable").html("Students allocated");
            $("td.input").html('<input type="text" name="count">');
            $("a#submit-button").hide();
            $("#table0 thead tr").append('<th class="header count" style="width:8%">Recommended</th>');
            $("h1#heading").append('<a href="#" id="edit-button"><span class="glyphicon glyphicon-edit"></span></a>');
            //$("h1#heading").append('<button type="submit" id="edit-button" style="margin-left: 20%" value="Submit"> Edit </button>');
         },
         error:function(jqXHR, textStatus, errorThrown) {
            console.log(errorThrown);
         }
    });
});