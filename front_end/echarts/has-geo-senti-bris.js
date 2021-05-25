/* jshint strict: false */

var bris_score_g = echarts.init(document.getElementById('brisbane-g'));
bris_score_g.showLoading();
$.getJSON('../data/has_geo_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    bris_score_g.hideLoading()
    var index = "3"
    var bris_score_g_option = {
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

    bris_score_g.setOption(bris_score_g_option);
});