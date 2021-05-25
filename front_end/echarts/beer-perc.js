/* jshint strict: false */

var beer_perc = echarts.init(document.getElementById('beer-percentage'));
beer_perc.showLoading();
$.getJSON('../data/senario_percentage.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    beer_perc.hideLoading()
    var index = "3"
    var beer_perc_option = {
    title: {
        text: 'Beer Related Tweets',
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
                {value: jsondata[index]['percentage'], name: 'Beer'},
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

beer_perc.setOption(beer_perc_option);
});