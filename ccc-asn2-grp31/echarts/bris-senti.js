/* jshint strict: false */

var bris_score = echarts.init(document.getElementById('brisbane'));

var bris_score_option = {
    title: {
        text: 'Brisbane',
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

bris_score.setOption(bris_score_option);
