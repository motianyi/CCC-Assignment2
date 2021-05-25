/* jshint strict: false */

var unhealthy_perc = echarts.init(document.getElementById('unhealthy-percentage'));
unhealthy_perc.showLoading();
$.getJSON('../data/senario_percentage.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    unhealthy_perc.hideLoading()
    var index = "2"
    var unhealthy_perc_option = {
    title: {
        text: 'Unhealthy Food Related Tweets',
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
            name: 'Tweets Proportion',
            type: 'pie',
            radius: '50%',
            data: [
                {value: jsondata[index]['percentage'], name: 'Unhealthy Food'},
                {value: 1-jsondata[index]['percentage'], name: 'Others'},
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

unhealthy_perc.setOption(unhealthy_perc_option);
});