/* jshint strict: false */

var covid_perc = echarts.init(document.getElementById('covid-percentage'));
covid_perc.showLoading();
$.getJSON('../data/all_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    covid_perc.hideLoading()
    var index = "7"
    var covid_perc_option = {
    title: {
        text: 'Covid Related Topics',
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
            name: 'tweets proportion',
            type: 'pie',
            radius: '50%',
            data: [
                {value: 12, name: 'Covid'},
                {value: 88, name: 'Others'},
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

covid_perc.setOption(covid_perc_option);
});