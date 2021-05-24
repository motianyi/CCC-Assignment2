/* jshint strict: false */

var total_covid = echarts.init(document.getElementById('total-covid'));

var total_covid_option = {
    xAxis: {
        type: 'category',
        data: ['Melbourne', 'Sydney', 'Canberra', 'Adelaide', 'Brisbane', 'Perth']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [120, 200, 150, 80, 70, 110],
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
        }
    }]
};

total_covid.setOption(total_covid_option);