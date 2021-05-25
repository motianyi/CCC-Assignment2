/* jshint strict: false */

var syd_score = echarts.init(document.getElementById('sydney'));
syd_score.showLoading();
$.getJSON('../data/all_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    syd_score.hideLoading()
    var index = "1"
    var syd_score_option = {
        title: {
            text: jsondata[index]["gcc_name16"],
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
                name: 'total tweets',
                type: 'pie',
                radius: '50%',
                data: [
                    {value: jsondata[index]["num_posi"], name: 'positive'},
                    {value: jsondata[index]["num_neg"], name: 'negative'},
                    {value: jsondata[index]["num_neu"], name: 'neutral'}
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

    syd_score.setOption(syd_score_option);
});