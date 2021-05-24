/* jshint strict: false */

var covid_ana = echarts.init(document.getElementById('covid-ana'));
covid_ana.showLoading();
$.getJSON('../data/all_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    var city = []
    var value = []
    for (const key in jsondata){
        if(jsondata.hasOwnProperty(key)){
        //   console.log(`${key} : ${res[key]}`)
          city.push(jsondata[key]["gcc_name16"])
          value.push(jsondata[key]["senti_score"])
          tweets.push(jsondata[key]["tweets_count"])
        }
    }
    console.log(city);

    covid_ana.hideLoading()
    var covid_ana_option = {
    title: {
        text: 'Sentiment Score'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['total tweets', 'covid tweets', 'covid & vaccine tweets']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: city
    },
    yAxis: {
        type: value
    },
    series: [
        {
            name: 'total tweets',
            type: 'line',
            stack: 'score',
            data: tweets
        },
        {
            name: 'covid tweets',
            type: 'line',
            stack: 'score',
            data: [220, 182, 191, 234, 290, 330, 310]
        },
        {
            name: 'covid & vaccine tweets',
            type: 'line',
            stack: 'score',
            data: [150, 232, 201, 154, 190, 330, 410]
        },
    ]
};

    covid_ana.setOption(covid_ana_option);
});