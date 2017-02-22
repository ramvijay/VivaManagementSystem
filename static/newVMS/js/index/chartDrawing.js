$(document).ready(function(){
    $.ajax({
        url: '/ajax/student_company_graph',
        type: 'GET',
        error: function (err) {
            alert("Get Student Location Graph Ajax Error " + err.responseText);
        },
        success: function (data) {
            jsonData = jQuery.parseJSON(data);
            window.studentCityDistribution = new Morris.Donut({
                // ID of the element in which to draw the chart.
                element: 'studentCompanyDist',
                data: jsonData
            });
        }
    });
    $.ajax({
        url: '/ajax/student_location_graph',
        type: 'GET',
        error: function (err) {
            alert("Get Student Location Graph Ajax Error " + err.responseText);
        },
        success: function (data) {
            jsonData = jQuery.parseJSON(data);
            window.studentCityDistribution = new Morris.Donut({
                // ID of the element in which to draw the chart.
                element: 'studentCityDistribution',
                data: jsonData
            });
        }
    });
    window.studentCompanyDist = new Morris.Donut({
        // ID of the element in which to draw the chart.
        element: 'studentVivaAllotStatus',
        data: [
            { label : "Report Submitted", value : 13},
            { label : "Report Not Submitted", value : 20},
            { label : "Viva Scheduled", value : 2},
            { label : "Viva Completed", value : 4}
        ]
    });
    // This is to fill the Tutor class details
    $.ajax({
        url: '/ajax/index_tutor_data',
        type: 'GET',
        error: function(err) {
            alert('Get Tutor Data AJAX Error : ' + err.responseText);
        },
        success: function(data) {
            var jsonData = JSON.parse(data);
            if (!jsonData.status) {
                alert(jsonData.msg);
                return;
            }
            // Parse the data and construct the table
            var htmlContent = '';
            for(var courseIter = 0; courseIter < jsonData.data.length; courseIter++) {
                htmlContent += '<tr>';
                htmlContent += '<td>' + jsonData.data[courseIter].course_name + '</td>';
                htmlContent += '<td>' + jsonData.data[courseIter].tutor_name + '</td>';
                htmlContent += '<td>' + jsonData.data[courseIter].strength + '</td>';
                htmlContent += '</tr>';
            }
            $('#tutor_data_container').html(htmlContent);
        }
    });
    // This is to fill the Guide Allotment details
    $.ajax({
        url: '/ajax/index_guide_data',
        type: 'GET',
        error: function(err) {
            alert('Get Guide Data AJAX Error : ' + err.responseText);
        },
        success: function(data) {
            var jsonData = JSON.parse(data);
            if (!jsonData.status) {
                alert(jsonData.msg);
                return;
            }
            // Parse the data and construct the table
            var htmlContent = '';
            for(data in jsonData.data) {
                var nameParts = data.split('##');
                htmlContent += '<tr>';
                htmlContent += '<td>' + nameParts[0] + '</td>';
                htmlContent += '<td>' + nameParts[1] + '</td>';
                htmlContent += '<td>' + jsonData.data[data] + '</td>';
                htmlContent += '</tr>';
            }
            $('#guide_data_container').html(htmlContent);
        }
    });
});