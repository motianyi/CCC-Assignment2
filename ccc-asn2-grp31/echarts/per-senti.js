/* jshint strict: false */

var per_score = echarts.init(document.getElementById('perth'));

var per_score_option = {
    title: {
        text: 'Perth',
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

per_score.setOption(per_score_option);
