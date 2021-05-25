/* jshint strict: false */

var fina = echarts.init(document.getElementById('fina'));

var fina_option = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    legend: {
        data: ['Employment Rates', 'Sentiment Score with "income"']
    },
    xAxis: [
        {
            type: 'category',
            data: ["Greater Melbourne", "Greater Sydney", "Greater Brisbane", "Greater Adelaide", "Greater Perth", "Australian Capital Territory"],
            axisPointer: {
                type: 'shadow'
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: 'Employment Rates',
            min: 50,
            max: 80,
            interval: 10,
            axisLabel: {
                formatter: '{value}%'
            }
        },
        {
            type: 'value',
            name: 'Sentiment Score',
            min: 0,
            max: 1.2,
            interval: 0.3,
            axisLabel: {
                formatter: '{value}'
            }
        }
    ],
    series: [
        {
            name: 'Employment Rates',
            type: 'bar',
            data: [65.9, 64.1, 63.2, 55.9, 55.7, 71.8]
        },
        {
            name: 'Sentiment Score with "income"',
            type: 'line',
            yAxisIndex: 1,
            data: [0.33393994, 0.52348995, 0.477707, 1.2881356, 0.15454546, 0.94017094]
        }
    ]
};

fina.setOption(fina_option)