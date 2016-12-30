/**
 * Created by Admin on 12/16/2016.
 */
//Page for the AJAX to get the config values
var _AJAX_CONFIG_PAGE = '/ajax/get_config/';
var _AJAX_CONFIG_SET_PAGE = '/ajax/set_configs/';

var _CreateCourseDOM = function(course_name) {
    /**
     * Creates a proper DOM structure using the name.
     */
    var data =  '<div class="config_course"><div class="config_course_name">';
    data += course_name;
    data += '</div><div class="config_course_close">';
    data += '<i class="fa fa-close"></i></div><div class="clearfix"></div></div>';
    return data;
};

var _AddCourseDOM = function(course_dom) {
    /**
     * Adds the HTML to the required DIV
     */
    var existing_data = $('#config_course_container').html();
    $('#config_course_container').html( existing_data + course_dom);
};

var _LoadCourses = function() {
    /**
     * Method for loading the courses into the DIV
     */
    /*$.post('/ajax/get_config/', { config_key : 'Courses' }, function(data)  {
        var jsonCourseData = JSON.parse(data);
        $.post('/ajax/get_config/', { config_key : 'ShortNames' }, function(data) {
            var jsonShortNamesData = JSON.parse(data);
            $.each(jsonCourseData.result, function( i, item ){
                _AddCourseDOM(_CreateCourseDOM(item + ' ( ' + jsonShortNamesData.result[item] + ' )'));
            });
        });
    });*/
    $.ajax({
        url: '/ajax/get_course_list',
        type: 'GET',
        error: function (err) {
            alert("Get Course List Ajax Error " + err.responseText);
        },
        success: function (data) {
           data = jQuery.parseJSON(data);
            $.each(data.result,function(i,item){
                full_name = item.fields.course_name + " ( "+ item.fields.short_name+" )"
                 _AddCourseDOM(_CreateCourseDOM(full_name))
            });
        }
    });
};

var _SetPageOpenStatus = function() {
    /**
     * Sets the open / closed status of the various pages in the configuration
     */
    if (window.config_page_open_status != undefined) {
        for( var pageIter = 0; pageIter < window.config_pages; pageIter++) {
            if (window.config_page_open_status[pageIter] != undefined) {
                if (window.config_page_open_status[pageIter]) {
                    window.config_accordion.enable(pageIter + 1);
                } else {
                    window.config_accordion.disable(pageIter + 1);
                }
            }
        }
    }
};

var _LoadConfigPageSettings = function() {
    /**
     * Disable the pages based on the data already filled. Needs server configuration.
     */
    $.post('/ajax/config_page_open_status/', {}, function(data){
        var jsonData = JSON.parse(data);
        window.config_page_open_status = jsonData.page_status;
        _SetPageOpenStatus();
        _LoadConfigPageData(0);
    });
};

var _LoadConfigPageData = function(selected_page) {
    /**
     * Loads the configurations for the selected page.
     */
    if (!window.config_page_data_loaded[selected_page]) {
        window.config_page_data_load_func[selected_page]();
        window.config_page_data_loaded[selected_page] = true;
    }
};

/**
 * Used to store the data loaded settings.
 */
window.config_page_data_loaded = [false, false, false, false, false];
window.config_page_data_load_func = [];
window.config_page_open_status = [];
window.config_pages = 6;

/**
 * Custom data loaders for each of the various pages
 */
window.config_page_data_load_func[0] = function() {
    //Get the current session and semester.
    /*$.post(_AJAX_CONFIG_PAGE, {config_key : 'Session_Year'}, function(data){
        var jsonData = JSON.parse(data);
        console.log(jsonData);
        if(jsonData.result != 'None') {
            $('#session_year').val(jsonData.result);
        }
    });
    $.post(_AJAX_CONFIG_PAGE, {config_key : 'Session_Semester'}, function(data){
        var jsonData = JSON.parse(data);
        if(jsonData.result != 'None') {
            if(jsonData.result == 'even') {
                $('#session_sem').val('Even Semester');
            } else {
                $('#session_sem').val('Odd Semester');
            }
        }
    });*/

      $.post('/ajax/vms_session/',{action:'get',session_year:'',session_sem:''},function(data){
            var jsonData = JSON.parse(data);
            if(jsonData.result!='none'){
                jsonData = JSON.parse(jsonData.result);
                $('#session_year').val(jsonData[0].fields.session_year);
                if(jsonData[0].fields.session_sem == 'even') {

                     $('#session_sem').val('even')
                }else{
                     $('#session_sem').val('odd')

                }
           }
        });



};

update_course_page_2 = function() {
    //Loads the Table setting the Tutors
    $.ajax({
        url: '/ajax/get_course_list/',
        type: 'GET',
        success: function (data) {
            var jsonData = JSON.parse(data);
            window.current_tutor_table_contents = jsonData.result;
            $.each(jsonData.result, function (i, item) {
                var currentHtml = $('#class-tutor-alloc-data').html();
                var newHtml = '<tr>';
                newHtml += '<td>' + item.fields.course_name + '</td>';
                newHtml += '<td><input type="text" class="input-group" id="' + i + '_student_count"></td>';
                newHtml += '<td><input type="text" class="input-group" id="' + i + '_tutor"></td>';
                newHtml += '<td><input type="text" class="input-group" id="' + i + '_group_mail"></td>';
                $('#class-tutor-alloc-data').html(currentHtml + newHtml);
            });
            $.ajax({
               url:'/ajax/tutor_setup_config'
            });
        }
    });
}

window.config_page_data_load_func[1] = update_course_page_2;


$(document).ready(function(){
    window.config_accordion = $('#config-accordion').accordionjs();
    _LoadConfigPageSettings();
    $('#config-accordion > li').on('click', '.accordionjs-select', function() {
        /**
         * Used for loading the data for the first time.
         */
        var selected_index = $(this).val();
        _LoadConfigPageData(selected_index);

    });

    // START PAGE 1
    //Load the initial courses from the DB.
    _LoadCourses();

    $('#config_course_container').on('click', '.config_course_close', function(event){
        /**
         * Deals with removing a course from the Course List
         */
        var course_to_remove = $(this).parent();
        var courseName = course_to_remove.text();
        //TODO Change it to the required format
        courseName = courseName.substr(0, courseName.indexOf(' ('));
        var course_dom = this;
        $.post('/ajax/course_modification/', {action: 'remove', course: courseName, shortName : '',degree:''}, function (data) {
            var jsonData = JSON.parse(data);
            if(jsonData.result == 'fail') {
                toastr.warn("Something went wrong. Try again.");
                return;
            }
            toastr.info("Course Removed");
            $(course_dom).parent().remove();
        });
    });

    $('#config_add_course').on('click', function(event){
        /**
         * Deals with the Add Course button in the First Config tab.
         */
        event.preventDefault();
        var course = $('#config_add_course_name').val();
        var courseShortName = $('#config_add_course_short_name').val();
        var degree = $('#config_add_degree').val();
        if(jQuery.trim(course).length <= 1) {
            toastr.error("Course name is too short.");
            return;
        }
        $.post('/ajax/course_modification/', { action: 'add', course: course, shortName : courseShortName,degree:degree}, function (data) {
            var jsonData = JSON.parse(data);
            if(jsonData.status == 'fail') {
                toastr.error('Error occurred. Try again.');
            } else {
                toastr.success('Course Added');
                full_course = degree + " "+course
                _AddCourseDOM(_CreateCourseDOM(full_course + ' ( ' + courseShortName + ' )'));
                $('#config_add_course_name').val('');
                $('#config_add_course_short_name').val('');
                $('#config_add_degree').val('');
            }
        });
    });

    $('#config_page_1_submit').on('click', function(){
        /**
         * Submits the contents of the first Configuration Page
         * Session_Year
         * Session_Sem
         */
        var session_year = $('#session_year').val();
        var session_sem = $('#session_sem').val();
        //Lets do some sanity checks first.
        /*
        //Send the data so that it can be registered
        var configs = [];
        configs[0] = { config_key : 'Session_Year', config_value : session_year };
        configs[1] = { config_key : 'Session_Sem', config_value : session_sem };
        $.post(_AJAX_CONFIG_SET_PAGE, {'configs' : JSON.stringify(configs)}, function(data){
            var jsonData = JSON.parse(data);
            if(jsonData.status == 'success') {
                toastr.success("Configuration settings changed.");
            } else {
                toastr.error("Something went wrong. Try again.");
            }
        });*/
        if(session_year == ''||session_sem==''){
            toastr.error("Session year and semester must be entered . Try Again !");
            return;
        }
        $.post('/ajax/vms_session/',{action:'add',session_year:session_year,session_sem:session_sem},function(data){
            var jsonData = JSON.parse(data);
            console.log(jsonData)
            if(jsonData.result == 'success') {
                toastr.success("Configuration settings changed.");
            } else {
                toastr.error("Something went wrong. Try again.");
            }
        });

    });
    // END PAGE 1
    // START PAGE 2
    $('#config-2').click(function () {

    });



    $('#config_page_2_submit').on('click', function(){

        var tbl = $('#config-2-table tr').get().map(function(row) {
              return $(row).find('td').get().map(function(cell) {
                    if($(cell).find('input').val()==null){
                        return ($(cell).text());
                    }
                    return $(cell).find('input').val();
              });
        });
        tbl.shift();
        mydata=[];
        record={}
        $.each(tbl,function(i,item){
            record = {course:item[0],no_of_students:item[1],tutor:item[2],mail:item[3]}
            mydata.push(record);
        });
        final_data = JSON.stringify(mydata);
        console.log(final_data)
        $.ajax({
            url:'/ajax/set_tutor_setup_config/',
            type:'POST',
            data: {action:'SET',result:final_data},
            success: function(data) {
                console.log(data);
            }
        });
    });
    // END PAGE 2

});