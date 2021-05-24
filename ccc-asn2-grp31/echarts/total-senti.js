/* jshint strict: false */

var total_score = echarts.init(document.getElementById('total-senti'));

var total_score_option = {
    title: {
        text: 'Australia',
        left: 'center'
    },
    // tooltip: {
    //     trigger: 'item'
    // },
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
                {value: 34, name: 'positive'},
                {value: 22, name: 'negative'},
                {value: 44, name: 'neutral'}
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

total_score.setOption(total_score_option);
