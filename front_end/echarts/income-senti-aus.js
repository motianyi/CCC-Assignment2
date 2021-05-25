/* jshint strict: false */

var total_score_i = echarts.init(document.getElementById('total-senti-i'));
total_score_i.showLoading();

$.getJSON('../data/income_analysis.json', function (jsondata) {

    console.log(JSON.stringify(jsondata));

    total_score_i.hideLoading()

    var index = "1"
    var total_score_i_option = {
        title: {
            text: jsondata[index]["gcc_name16"],
            left: 'center'
        },
        tooltip: {
            trigger: 'item',
            confine: true
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
                // emphasis: {
                //     itemStyle: {
                //         shadowBlur: 10,
                //         shadowOffsetX: 0,
                //         shadowColor: 'rgba(0, 0, 0, 0.5)'
                //     }
                // }
            }
        ]
    };

    total_score_i.setOption(total_score_i_option);
});