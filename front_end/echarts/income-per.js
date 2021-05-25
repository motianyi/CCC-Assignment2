/* jshint strict: false */

var income_perc = echarts.init(document.getElementById('income-percentage'));
income_perc.showLoading();
$.getJSON('../data/senario_percentage.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    income_perc.hideLoading()
    var index = "4"
    var income_perc_option = {
    title: {
        text: 'Income Related Tweets',
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
                {value: jsondata[index]['percentage'], name: 'Income'},
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

income_perc.setOption(income_perc_option);
});