/* jshint strict: false */

var ec_score = echarts.init(document.getElementById('sentiment-score'));

var ec_score_option = {
    series: [{
        type: 'gauge',
        startAngle: 180,
        endAngle: 0,
        min: -1,
        max: 1,
        splitNumber: 5,
        axisLine: {
            lineStyle: {
                width: 6,
                color: [
                    [0.25, '#C0A3A3'],
                    [0.5, '#C1E7EE'],
                    [0.75, '#FDD7EA'],
                    [1, '#ACCDF0']
                ]
            }
        },
        pointer: {
            icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
            length: '10%',
            width: 12,
            offsetCenter: [0, '-50%'],
            itemStyle: {
                color: '#F4F4D0'
            }
        },
        axisTick: {
            length: 12,
            lineStyle: {
                color: 'auto',
                width: 2
            }
        },
        splitLine: {
            length: 20,
            lineStyle: {
                color: 'auto',
                width: 5
            }
        },
        title: {
            offsetCenter: [0, '30%'],
            fontSize: 16,
			color: '#002452',
        },
        detail: {
            fontSize: 28,
            offsetCenter: [0, '0%'],
            valueAnimation: true,
            formatter: function (value) {
                return value;
            },
            color: 'auto'
        },
        data: [{
            value: 0.70,
            name: 'Sentiment-Score'
        }]
    }]
};
ec_score.setOption(ec_score_option);
