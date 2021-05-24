/* jshint strict: false */

var lang1 = echarts.init(document.getElementById('lang1'));

var lang1_option = {
    title: {
        text: 'English vs Others',
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
            name: 'Language',
            type: 'pie',
            radius: '50%',
            data: [
                {value: 24223, name: 'Others'},
                {value: 150829, name: 'English'},
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

lang1.setOption(lang1_option);