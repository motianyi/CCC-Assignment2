/* jshint strict: false */

var adel_score_cv = echarts.init(document.getElementById('adelaide-cv'));
adel_score_cv.showLoading();
$.getJSON('../data/covid_vaccine_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    adel_score_cv.hideLoading()
    var index = "3"
    var adel_score_cv_option = {
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

    adel_score_cv.setOption(adel_score_cv_option);
});