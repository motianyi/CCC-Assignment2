/* jshint strict: false */

var unhealf = echarts.init(document.getElementById('unhealf'));

var unhealf_option = {
    title: {
        text: 'Unhealthy Food',
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
            name: 'Unhealthy Food',
            type: 'pie',
            radius: '50%',
            data: [
                {value: 1048, name: 'Unhealthy Food'},
                {value: 735, name: 'Others'},

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

unhealf.setOption(unhealf_option);