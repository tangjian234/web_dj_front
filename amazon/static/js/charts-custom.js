/*global $, document, LINECHARTEXMPLE*/
$(document).ready(function() {

    'use strict';

    var brandPrimary = 'rgba(51, 179, 90, 1)';

    var LINECHARTEXMPLE = $('#lineChartExample'),
        PIECHARTEXMPLE = $('#pieChartExample'),
        BARCHARTEXMPLE = $('#barChartExample'),
        RADARCHARTEXMPLE1 = $('#radarChartExample1'),
        //RADARCHARTFEATURE = $('#radarChartFeature'),
        RADARCHARTKEYPARAMETER = $('#radarChartKeyParameter'),
        POLARCHARTEXMPLE = $('#polarChartExample');


    var string_list = JSON.parse(document.getElementById('asin_list').textContent);
    //window.alert(string_list)


    var lineChartExample = new Chart(LINECHARTEXMPLE1, {
        type: 'line',
        data: {
            labels: ["January-1", "February", "March", "April", "May", "June", "July"],
            datasets: [{
                    label: "Data Set One",
                    fill: true,
                    lineTension: 0.3,
                    backgroundColor: "rgba(51, 179, 90, 0.38)",
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
                    pointHitRadius: 10,
                    data: [50, 20, 40, 31, 32, 22, 10],
                    spanGaps: false
                },
                {
                    label: "Data Set Two",
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
                    data: [65, 59, 30, 81, 56, 55, 40],
                    spanGaps: false
                }
            ]
        }
    });

    var pieChartExample = new Chart(PIECHARTEXMPLE, {
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

    var pieChartExample = {
        responsive: true
    };

    var barChartExample = new Chart(BARCHARTEXMPLE, {
        type: 'bar',
        data: {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [{
                    label: "Data Set 1",
                    backgroundColor: [
                        'rgba(51, 179, 90, 0.6)',
                        'rgba(51, 179, 90, 0.6)',
                        'rgba(51, 179, 90, 0.6)',
                        'rgba(51, 179, 90, 0.6)',
                        'rgba(51, 179, 90, 0.6)',
                        'rgba(51, 179, 90, 0.6)',
                        'rgba(51, 179, 90, 0.6)'
                    ],
                    borderColor: [
                        'rgba(51, 179, 90, 1)',
                        'rgba(51, 179, 90, 1)',
                        'rgba(51, 179, 90, 1)',
                        'rgba(51, 179, 90, 1)',
                        'rgba(51, 179, 90, 1)',
                        'rgba(51, 179, 90, 1)',
                        'rgba(51, 179, 90, 1)'
                    ],
                    borderWidth: 1,
                    data: [65, 59, 80, 81, 56, 55, 40],
                },
                {
                    label: "Data Set 2",
                    backgroundColor: [
                        'rgba(203, 203, 203, 0.6)',
                        'rgba(203, 203, 203, 0.6)',
                        'rgba(203, 203, 203, 0.6)',
                        'rgba(203, 203, 203, 0.6)',
                        'rgba(203, 203, 203, 0.6)',
                        'rgba(203, 203, 203, 0.6)',
                        'rgba(203, 203, 203, 0.6)'
                    ],
                    borderColor: [
                        'rgba(203, 203, 203, 1)',
                        'rgba(203, 203, 203, 1)',
                        'rgba(203, 203, 203, 1)',
                        'rgba(203, 203, 203, 1)',
                        'rgba(203, 203, 203, 1)',
                        'rgba(203, 203, 203, 1)',
                        'rgba(203, 203, 203, 1)'
                    ],
                    borderWidth: 1,
                    data: [35, 40, 60, 47, 88, 27, 30],
                }
            ]
        }
    });



    var polarChartExample = new Chart(POLARCHARTEXMPLE, {
        type: 'polarArea',
        data: {
            datasets: [{
                data: [
                    11,
                    16,
                    7
                ],
                backgroundColor: [
                    "rgba(51, 179, 90, 1)",
                    "#FF6384",
                    "#FFCE56"
                ],
                label: 'My dataset' // for legend
            }],
            labels: [
                "First",
                "Second",
                "Third"
            ]
        }
    });

    var polarChartExample = {
        responsive: true
    };



});