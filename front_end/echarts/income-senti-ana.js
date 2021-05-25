/* jshint strict: false */

var income_ana = echarts.init(document.getElementById('income-ana'));

var income_ana_option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['Sentiment Score in All Tweets', 'Sentiment Score with "income"']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['Greater Melbourne', 'Greater Sydney', 'Greater Brisbane', 'Greater Adelaide', 'Greater Perth', 'Australian Capital Territory']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: 'Sentiment Score in All Tweets',
            type: 'line',
            stack: 'score',
            data: [0.6512724, 0.5969821, 0.6560055, 0.8082551, 0.67274445, 0.8348818]
        },
        {
            name: 'Sentiment Score with "income"',
            type: 'line',
            stack: 'score',
            data: [0.33393994, 0.52348995, 0.477707, 1.2881356, 0.15454546, 0.94017094]
        }
    ]
};

income_ana.setOption(income_ana_option)