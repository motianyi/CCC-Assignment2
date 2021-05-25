/* jshint strict: false */

var melb_score_g = echarts.init(document.getElementById('melbourne-g'));
melb_score_g.showLoading();
$.getJSON('../data/has_geo_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    melb_score_g.hideLoading()
    var index = "0"
    var melb_score_g_option = {
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

    melb_score_g.setOption(melb_score_g_option);
});