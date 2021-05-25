
var obes_ana = echarts.init(document.getElementById('obes-ana'));

    var obes_ana_option = {
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
            data: ['Tweets with Beers', 'Tweets with Unhealthy Food', 'Obesity Rate']
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
                name: 'Rates of Tweets',
                min: 0,
                max: 0.18,
                interval: 0.06,
                axisLabel: {
                    formatter: '{value}'
                }
            },
            {
                type: 'value',
                name: 'Obesity Rate',
                min: 0,
                max: 40,
                interval: 5,
                axisLabel: {
                    formatter: '{value}%'
                }
            }
        ],
        series: [
            {
                name: 'Tweets with Beers',
                type: 'bar',
                data: [0.13835168, 0.076911636, 0.035554893, 0.022166021, 0.022909848, 0.013686403]
            },
            {
                name: 'Tweets with Unhealthy Food',
                type: 'bar',
                data: [0.115606934, 0.1683526, 0.061416186, 0.018063584, 0.031791907, 0.009393063]
            },
            {
                name: 'Obesity Rate',
                type: 'line',
                yAxisIndex: 1,
                data: [31.8, 30.8, 32.4, 32.6, 28.7, 26.4]
            }
        ]
    };
obes_ana.setOption(obes_ana_option)
