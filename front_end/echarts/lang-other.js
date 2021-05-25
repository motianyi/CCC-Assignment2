/* jshint strict: false */

var lang2 = echarts.init(document.getElementById('lang2'));

lang2.showLoading();
$.getJSON('../data/language_count.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    lang2.hideLoading()
    var index = "1"
var lang2_option = {
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
                {value: jsondata[index]["Indian"], name: 'Indian'},
                {value: jsondata[index]["Japanese"], name: 'Japanese'},
                {value: jsondata[index]["Spanish"], name: 'Spanish'},
                {value: jsondata[index]["Arabic"], name: 'Arabic'},
                {value: jsondata[index]["Tagalog"], name: 'Tagalog'},
                {value: jsondata[index]["Portuguese"], name: 'Portuguese'},
                {value: jsondata[index]["Chinese"], name: 'Chinese'},
                {value: jsondata[index]["Turkish"], name: 'Turkish'},
                {value: jsondata[index]["French"], name: 'French'},
                {value: 1-jsondata[index]["Indian"]-jsondata[index]["Japanese"]-jsondata[index]["Spanish"]-jsondata[index]["Arabic"]-jsondata[index]["Tagalog"]-jsondata[index]["Portuguese"]-jsondata[index]["Chinese"]-jsondata[index]["Turkish"]-jsondata[index]["French"], name: 'Others'},
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

lang2.setOption(lang2_option);

});