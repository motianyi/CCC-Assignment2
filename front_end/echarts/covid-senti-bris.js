/* jshint strict: false */

var bris_score_c = echarts.init(document.getElementById('brisbane-c'));
bris_score_c.showLoading();
$.getJSON('../data/covid_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    bris_score_c.hideLoading()
    var index = "2"
    var bris_score_c_option = {
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

    bris_score_c.setOption(bris_score_c_option);
});