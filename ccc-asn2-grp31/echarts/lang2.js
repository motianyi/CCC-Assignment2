/* jshint strict: false */

var lang2 = echarts.init(document.getElementById('lang2'));

var lang2_option = {
    title: {
        text: 'Other Languages',
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
            name: 'Other Languages',
            type: 'pie',
            radius: '50%',
            data: [
                {value: 7339, name: 'Indian'},
                {value: 2209, name: 'Japanese'},
                {value: 2042, name: 'Spanish'},
                {value: 1715, name: 'Arabic'},
                {value: 1225, name: 'Portuguese'},
                {value: 1147, name: 'Chinese'},
                {value: 734, name: 'Turkish'},
                {value: 639, name: 'French'},
                {value: 7173, name: 'Rest'},
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

lang2.setOption(lang2_option);