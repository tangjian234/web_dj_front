/*global $, document, Chart, LINECHART, data, options, window*/

$(document).ready(function() {



    'use strict';



    // Main Template Color"
    var brandPrimary = '#33b35a';
    // ------------------------------------------------------- //
    // Line Chart 
    // ------------------------------------------------------ //

    // Get data from django show_asin_task.html 
    // asin_list and asin_dict_list
    var asin_list = JSON.parse(document.getElementById('asin_list').textContent);
    var product_name_list = JSON.parse(document.getElementById('product_name_list').textContent);

    var data_from_django = JSON.parse(document.getElementById('asin_dict_list').textContent);



    // Price data 


    // x_axis : time line  
    var x_axis = JSON.parse(document.getElementById('x_axis').textContent);
    var x_axis = x_axis.split(',')

    // var data_from_django_1 = JSON.parse("{{asin_dict_list_sterilized|escapejs}}");
    // window.alert("jer")
    var data_from_django_1 = JSON.parse(document.getElementById('data').textContent);
    //window.alert(typeof(data_from_django_1));
    //var k = JSON.parse(data_from_django_1)
    // window.alert(data_from_django_1["Laugh"]["Cry"]);
    //var data = JSON.parse("{{data|escapejs}}");
    //for (var x in data) {
    //     window.alert(x)
    // }
    var d_price = [];
    var d_comment = [];
    var price_data = [];
    var first_price = [];
    var comment_data = [];
    var color_list = []

    for (var i = 0, l = asin_list.length; i < l; i++) {
        var d_template = {
            //ASIN id 
            //label: "template",
            //label: "First dataset - 1 ",
            fill: true,
            lineTension: 0.3,
            backgroundColor: "rgba(77, 193, 75, 0.4)",
            borderColor: brandPrimary,
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            borderWidth: 1,
            // points 
            pointBorderColor: brandPrimary,
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: brandPrimary,
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 5,
            pointHitRadius: 0,
            //   data: [50, 50.3, 49, 48, 52, 51,47],
            //Price line 1
            //data: [],
            spanGaps: false
        };
        var d = (data_from_django[asin_list[i]]["price"]);
        price_data[i] = d.split(',').map(Number);

        var s = (data_from_django[asin_list[i]]["no_of_comments"]);
        comment_data[i] = s.split(',').map(Number);

        // d1[i] = d_template;
        d_price[i] = d_template
        d_comment[i] = d_template

        d_price[i]['label'] = product_name_list[i]
        d_price[i]['data'] = price_data[i]

        d_comment[i]['label'] = product_name_list[i]
        d_comment[i]['data'] = comment_data[i]

    }

    for (var i = 0, l = asin_list.length; i < l; i++) {
        first_price[i] = parseFloat(price_data[i][0])
    }

    var price_max = Math.max(...first_price);

    var first_price_normal = [];
    var radar_d = [];

    for (var i = 0, l = asin_list.length; i < l; i++) {
        first_price_normal[i] = Math.round(first_price[i] / price_max * 100)
    }
    var radar_d1 = [first_price_normal[1]];
    radar_d1 = radar_d1.concat([48, 40, 19, 96, 27])


    var LINECHART = $('#Product_Price_Comparision');

    var myLineChart = new Chart(LINECHART, {
        /*

            Function: read data and plot line chart 
            
            Parameters:  
            
            */
        type: 'line',
        options: {
            legend: {
                display: true
            }
        },
        data: {
            //            labels: ["Jan1", "Feb", "Mar", "Apr", "May", "June", "July"],
            //labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],

            //x_axis : time line 
            labels: x_axis,
            datasets: d_price,
        }
    });

    var LINECHART_COMMENT = $('#2_Product_Comment_Comparision');

    var myLineChart = new Chart(LINECHART_COMMENT, {

        /*

             Function: 2_Product_Comment_Comparision : 
             
             Parameters:  
             
        */
        type: 'line',
        options: {
            legend: {
                display: true
            }
        },
        data: {
            //            labels: ["Jan1", "Feb", "Mar", "Apr", "May", "June", "July"],
            //labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            labels: x_axis,
            datasets: d_comment,
        }
    });



    // ------------------------------------------------------- //
    // Pie Chart
    // ------------------------------------------------------ //
    var PIECHART = $('#pieChart');
    var myPieChart = new Chart(PIECHART, {
        type: 'doughnut',
        data: {
            labels: [
                "First",
                "Second",
                "Third"
            ],
            datasets: [{
                data: [300, 50, 100],
                borderWidth: [1, 1, 1],
                backgroundColor: [
                    brandPrimary,
                    "rgba(75,192,192,1)",
                    "#FFCE56"
                ],
                hoverBackgroundColor: [
                    brandPrimary,
                    "rgba(75,192,192,1)",
                    "#FFCE56"
                ]
            }]
        }
    });



    // ------------------------------------------------------- //
    // Line Chart old
    // ------------------------------------------------------ //
    var LINECHART = $('#lineCahrt2');
    var myLineChart = new Chart(LINECHART, {
        type: 'line',
        options: {
            legend: {
                display: false
            }
        },
        data: {
            labels: ["F1", "Feb", "Mar", "Apr", "May", "June", "July"],
            datasets: [{
                    label: "",
                    fill: true,
                    lineTension: 0.3,
                    backgroundColor: "rgba(77, 193, 75, 0.4)",
                    borderColor: brandPrimary,
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    borderWidth: 1,
                    pointBorderColor: brandPrimary,
                    pointBackgroundColor: "#fff",
                    pointBorderWidth: 1,
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: brandPrimary,
                    pointHoverBorderColor: "rgba(220,220,220,1)",
                    pointHoverBorderWidth: 2,
                    pointRadius: 1,
                    pointHitRadius: 0,
                    data: [70, 20, 60, 31, 52, 22, 40],
                    spanGaps: false
                },
                {
                    label: "My First dataset",
                    fill: true,
                    lineTension: 0.3,
                    backgroundColor: "rgba(75,192,192,0.4)",
                    borderColor: "rgba(75,192,192,1)",
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    borderWidth: 1,
                    pointBorderColor: "rgba(75,192,192,1)",
                    pointBackgroundColor: "#fff",
                    pointBorderWidth: 1,
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: "rgba(75,192,192,1)",
                    pointHoverBorderColor: "rgba(220,220,220,1)",
                    pointHoverBorderWidth: 2,
                    pointRadius: 1,
                    pointHitRadius: 10,
                    data: [65, 59, 30, 81, 46, 55, 30],
                    spanGaps: false
                }
            ]
        }
    });

    var R = $('#radarChartFeature');
    var radarChartFeature = new Chart(R, {
        type: 'radar',
        data: {

            labels: ["Battery Life-", "Quality", "BT Range", "Weight", "Bass", "Pair Speed"],
            datasets: [{
                    label: product_name_list[0],
                    backgroundColor: "rgba(179,181,198,0.2)",
                    borderWidth: 2,
                    borderColor: "rgba(179,181,198,1)",
                    pointBackgroundColor: "rgba(179,181,198,1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(179,181,198,1)",
                    data: [95, 59, 90, 81, 56, 55]
                },
                {
                    label: product_name_list[1],
                    backgroundColor: "rgba(51, 179, 90, 0.2)",
                    borderWidth: 2,
                    borderColor: "rgba(51, 179, 90, 1)",
                    pointBackgroundColor: "rgba(51, 179, 90, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(51, 179, 90, 1)",
                    data: [88, 48, 40, 19, 96, 27]
                }
            ]
        }
    });
    var radarChartFeature = {
        responsive: true
    };

    var R1 = $('#radarChartParameter');
    var radarChartParameter = new Chart(R1, {
        type: 'radar',
        data: {

            labels: ["Price", "No_of_comment", "BT Range", "Weight", "Bass", "Pair Speed"],
            datasets: [{
                    label: product_name_list[0],
                    backgroundColor: "rgba(179,181,198,0.2)",
                    borderWidth: 2,
                    borderColor: "rgba(179,181,198,1)",
                    pointBackgroundColor: "rgba(179,181,198,1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(179,181,198,1)",
                    data: [100, 48, 40, 19, 96, 27]
                },
                {

                    label: product_name_list[1],
                    backgroundColor: "rgba(51, 179, 90, 0.2)",
                    borderWidth: 2,
                    borderColor: "rgba(51, 179, 90, 1)",
                    pointBackgroundColor: "rgba(51, 179, 90, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(51, 179, 90, 1)",
                    data: radar_d1
                }
            ]
        }
    });
    var radarChartParameter = {
        responsive: true
    };



});