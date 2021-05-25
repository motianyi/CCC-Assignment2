/* jshint strict: false */

var adel_score_g = echarts.init(document.getElementById('adelaide-g'));
adel_score_g.showLoading();
$.getJSON('../data/has_geo_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    adel_score_g.hideLoading()
    var index = "3"
    var adel_score_g_option = {
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

    adel_score_g.setOption(adel_score_g_option);
});