/* jshint strict: false */

var per_score_cv = echarts.init(document.getElementById('perth-cv'));
per_score_cv.showLoading();
$.getJSON('../data/covid_vaccine_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    per_score_cv.hideLoading()
    var index = "4"
    var per_score_cv_option = {
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

    per_score_cv.setOption(per_score_cv_option);
});