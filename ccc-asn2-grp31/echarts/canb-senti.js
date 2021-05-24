/* jshint strict: false */

var canb_score = echarts.init(document.getElementById('canberra'));

var canb_score_option = {
    title: {
        text: 'Canberra',
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

canb_score.setOption(canb_score_option);
