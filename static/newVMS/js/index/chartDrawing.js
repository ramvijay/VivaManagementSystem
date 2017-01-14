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
});