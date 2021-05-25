/* jshint strict: false */

var melb_score_c = echarts.init(document.getElementById('melbourne-c'));
melb_score_c.showLoading();
$.getJSON('../data/covid_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    melb_score_c.hideLoading()
    var index = "0"
    var melb_score_c_option = {
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
                name: 'Tweets Number',
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

    melb_score_c.setOption(melb_score_c_option);
});