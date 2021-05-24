/* jshint strict: false */

var total_score = echarts.init(document.getElementById('total-senti'));
total_score.showLoading();
$.getJSON('../data/all_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    total_score.hideLoading()
    var index = "6"
    var total_score_option = {
        title: {
            text: "Total",
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
                name: 'tweets/total tweets(%)',
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

    total_score.setOption(total_score_option);
});