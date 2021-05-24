/* jshint strict: false */

var heal_con = echarts.init(document.getElementById('heal-con'));

var heal_con_option = {
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
        data: ['cigratte', 'achohol', 'fastfood', 'mortality']
    },
    xAxis: [
        {
            type: 'category',
            data: [jsondata[index]["gcc_name16"]],
            axisPointer: {
                type: 'shadow'
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: 'sentiment-score',
            min: 0,
            max: 2,
            interval: 0.4,
            axisLabel: {
                formatter: '{value}'
            }
        },
        {
            type: 'value',
            name: 'mortality',
            min: 0,
            max: 20,
            interval: 5,
            axisLabel: {
                formatter: '{value} %'
            }
        }
    ],
    series: [
        {
            name: 'cigratte',
            type: 'bar',
            data: [1, 0.5, 0.1, 1.1, 0.3, 0.2]
        },
        {
            name: 'achohol',
            type: 'bar',
            data: [0.4, 0.6, 0.8, 1.2, 1.5, 0.3]
        },
        {
            name: 'fastfood',
            type: 'bar',
            data: [1.9, 1.1, 1, 0.2, 0.7, 0.4]
        },
        {
            name: 'mortality',
            type: 'line',
            yAxisIndex: 1,
            data: [12.0,8.2, 13.3, 14.5, 6.3, 10.2]
        }
    ]
};

heal_con.setOption(heal_con_option);