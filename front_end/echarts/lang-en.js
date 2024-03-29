/* jshint strict: false */

var lang1 = echarts.init(document.getElementById('lang1'));

lang1.showLoading();
$.getJSON('../data/language_count.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    lang1.hideLoading()
    var index = "1"
var lang1_option = {
    title: {
        text: 'English vs Others',
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
            name: 'Language',
            type: 'pie',
            radius: '50%',
            data: [
                {value: jsondata[index]["English"], name: 'English'},
                {value: 1-jsondata[index]["English"], name: 'Others'},
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

lang1.setOption(lang1_option);

});