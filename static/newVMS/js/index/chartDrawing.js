/**
 * Required Parsing / Data set creation logics
 */
/**
 * Converts from RGB to hex color code for use in ChartJS
 */
function rgbToHex(red, green, blue) {
    return '#' + ('0' + parseInt(red).toString(16)).slice(-2) +
                 ('0' + parseInt(green).toString(16)).slice(-2) +
                 ('0' + parseInt(blue).toString(16)).slice(-2);
}

/**
 * Returns a number between 0 - 255
 */
function getRandomSingleColorValue() {
    return Math.floor(Math.random() * 255);
}

/**
 * Creates a list of random color combinations.
 */
function createRandomColors(numColors) {
    var colorList = [];
    for (var colorGenIter = 0; colorGenIter < numColors; colorGenIter++) {
        colorList.push(rgbToHex(getRandomSingleColorValue(), getRandomSingleColorValue(), getRandomSingleColorValue()));
    }
    return colorList;
}

/**
 * Parses the JSON data to the required format (accepted by ChartJS).
 */
function parseGenericJSONData(jsonData) {
    if (jsonData === undefined) { return undefined; }
    var labels = [];
    var values = [];
    jsonData.forEach(entry => {
        labels.push(entry.label);
        values.push(entry.value);
    });
    var totalCount = labels.length;
    var colorList = createRandomColors(totalCount);
    console.log(colorList);
    return {
        labels: labels,
        datasets: [
            {
                data: values,
                backgroundColor: colorList
            }
        ]
    }
}

// Turning of legend display
Chart.defaults.global.legend.position = 'bottom';

$(document).ready(function(){
    /**
     * Pie chart representing the Distribution of the Students based on the Company.
     */
    $.ajax({
        url: '/ajax/student_company_graph',
        type: 'GET',
        error: function (err) {
            alert("Get Student Location Graph Ajax Error " + err.responseText);
        },
        success: function (data) {
            var jsonData = jQuery.parseJSON(data);
            var canvas = document.getElementById('studentCompanyDistCanvas');
            var ctx = canvas.getContext('2d');
            var studentCompanyDistChart = new Chart(ctx, {
                type: 'pie',
                data: parseGenericJSONData(jsonData)
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
            var canvas = document.getElementById('studentCityDistCanvas');
            var ctx = canvas.getContext('2d');
            var studentLocationDistChart = new Chart(ctx, {
                type: 'pie',
                data: parseGenericJSONData(jsonData)
            });
        }
    });
    var canvas = document.getElementById('studentVivaAllotStatusCanvas');
    var ctx = canvas.getContext('2d');
    var studentVivaStatusChart = new Chart(ctx, {
        type: 'pie',
        data: parseGenericJSONData([
            { label : "Report Submitted", value : 13},
            { label : "Report Not Submitted", value : 20},
            { label : "Viva Scheduled", value : 2},
            { label : "Viva Completed", value : 4}
        ])
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