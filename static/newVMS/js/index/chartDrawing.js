$(document).ready(function(){
    window.studentCompanyDist = new Morris.Donut({
        // ID of the element in which to draw the chart.
        element: 'studentCompanyDist',
        data: [
            { label : "KLA Tencor", value : 6},
            { label : "Goldman Sachs", value : 3},
            { label : "Zoho", value : 4},
            { label : "CISCO", value : 5},
            { label : "Micro Focus", value : 5},
            { label : "PayPal", value : 5},
            { label : "Skava", value : 4},
        ]
    });
    window.studentCompanyDist = new Morris.Donut({
        // ID of the element in which to draw the chart.
        element: 'studentCityDistribution',
        data: [
            { label : "Chennai", value : 13},
            { label : "Bangalore", value : 20},
            { label : "Pune", value : 2},
            { label : "Coimbatore", value : 4}
        ]
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