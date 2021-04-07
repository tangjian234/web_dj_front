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
    var data_from_django = JSON.parse(document.getElementById('asin_dict_list').textContent);



    // Price data 
    var d = (data_from_django[asin_list[0]]["price"]);
    var price_data_1 = d.split(',').map(Number);
    //window.alert(asin_list[0]);
    //window.alert(d);
    //var string_1 = JSON.parse(document.getElementById('asin_string_1').textContent);
    //var data_from_django_1 = JSON.parse(document.getElementById('price_line_1').textContent);

    var d = data_from_django[asin_list[1]]["price"];
    var price_data_2 = d.split(',').map(Number);
    //        var string_2 = JSON.parse(document.getElementById('asin_string_2').textContent);

    // Comment data 
    var data_from_django_1 = (data_from_django[asin_list[0]]["no_of_comments"]);
    var c_data_1 = data_from_django_1.split(',').map(Number);
    var data_from_django_2 = (data_from_django[asin_list[1]]["no_of_comments"]);
    var c_data_2 = data_from_django_2.split(',').map(Number);

    // x_axis : time line  
    var x_axis = JSON.parse(document.getElementById('x_axis').textContent);
    var x_axis = x_axis.split(',')

    // var data_from_django_1 = JSON.parse("{{asin_dict_list_sterilized|escapejs}}");
    // window.alert("jer")
    var data_from_django_1 = JSON.parse(document.getElementById('data').textContent);
    //window.alert(typeof(data_from_django_1));
    //var k = JSON.parse(data_from_django_1)
    // window.alert(data_from_django_1["S3"]["M1"]);
    // window.alert(data_from_django_1["Laugh"]["Cry"]);
    //var data = JSON.parse("{{data|escapejs}}");
    //for (var x in data) {
    //     window.alert(x)
    // }


    var LINECHART = $('#2_Product_Price_Comparision');
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

            datasets: [{
                    //ASIN id 
                    label: asin_list[0],
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
                    pointBorderColor: brandPrimary,
                    pointBackgroundColor: "#fff",
                    pointBorderWidth: 1,
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: brandPrimary,
                    pointHoverBorderColor: "rgba(220,220,220,1)",
                    pointHoverBorderWidth: 2,
                    pointRadius: 1,
                    pointHitRadius: 0,
                    //   data: [50, 50.3, 49, 48, 52, 51,47],
                    //Price line 1
                    data: price_data_1,
                    spanGaps: false
                },
                {
                    label: asin_list[1],
                    //"My Second dataset",
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
                    //   data: [65, 59, 30, 81, 46, 55, 30],
                    //Price line 2

                    data: price_data_2,
                    spanGaps: false
                }
            ]
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
            datasets: [{
                    label: asin_list[0],
                    //"My First dataset-1",
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
                    //   data: [50, 50.3, 49, 48, 52, 51,47],
                    data: c_data_1,
                    spanGaps: false
                },
                {

                    label: asin_list[1],
                    //"My Second dataset",
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
                    //   data: [65, 59, 30, 81, 46, 55, 30],
                    data: c_data_2,
                    spanGaps: false
                }
            ]
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
                    data: [50, 20, 60, 31, 52, 22, 40],
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

    RADARCHARTEXMPLE = $('#radarChartExample');
    var radarChartExample = new Chart(RADARCHARTEXMPLE, {

        /*
      
              Function: read data and plot radar chart .  
              
              Parameters:  
              
              */

        type: 'radar',
        data: {
            labels: ["Battery Life", "Quality", "BT Range", "Weight", "Bass", "Pair Speed"],
            datasets: [{
                    label: string_list[0],
                    backgroundColor: "rgba(179,181,198,0.2)",
                    borderWidth: 2,
                    borderColor: "rgba(179,181,198,1)",
                    pointBackgroundColor: "rgba(179,181,198,1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(179,181,198,1)",
                    data: [65, 59, 90, 81, 56, 55]
                },
                {
                    label: string_list[1],
                    backgroundColor: "rgba(51, 179, 90, 0.2)",
                    borderWidth: 2,
                    borderColor: "rgba(51, 179, 90, 1)",
                    pointBackgroundColor: "rgba(51, 179, 90, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(51, 179, 90, 1)",
                    data: [28, 48, 40, 19, 96, 27]
                }
            ]
        }
    });


});