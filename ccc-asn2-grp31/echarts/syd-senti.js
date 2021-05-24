/* jshint strict: false */

var syd_score = echarts.init(document.getElementById('sydney'));

var syd_score_option = {
    title: {
        text: 'Sydney',
        left: 'center'
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        orient: 'vertical',
        left: 'left',
    },
    series: [
        {
            name: 'tweets/total tweets(%)',
            type: 'pie',
            radius: '50%',
            data: [
                {value: 12, name: 'positive'},
                {value: 67, name: 'negative'},
                {value: 21, name: 'neutral'}
            ],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};

syd_score.setOption(syd_score_option);
