// var total_senti = '../data/all_senti_analysis.json';
// var senti_c = '../data/covid_senti_analysis.json';
// var senti_cv = '../data/covid_vaccine_senti_analysis.json';

var covid_ana = echarts.init(document.getElementById('covid-ana'))

var covid_ana_option = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    legend: {
        data: ['Infected Cases', 'Score in All Tweets', 'Score in Tweets with COVID', 'Score in Tweets with COVID and Vaccine']
    },
    xAxis: [
        {
            type: 'category',
            data: ['Greater Melbourne', 'Greater Sydney', 'Australian Capital Territory', 'Greater Brisbane', 'Greater Adelaide', 'Greater Perth'],
            axisPointer: {
                type: 'shadow'
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: 'Infected Cases',
            min: 0,
            max: 25000,
            interval: 5000,
            axisLabel: {
                formatter: '{value}'
            }
        },
        {
            type: 'value',
            name: 'Sentiment Score',
            min: -0.4,
            max: 1,
            interval: 0.2,
            axisLabel: {
                formatter: '{value}'
            }
        }
    ],
    series: [
        {
            name: 'Infected Cases',
            type: 'bar',
            data: [ 20549, 5572, 124, 1605, 748, 1016]
        },
        {
            name: 'Score in All Tweets',
            type: 'line',
            yAxisIndex: 1,
            data: [0.65, 0.60, 0.83, 0.66, 0.81, 0.67]
        },
        {
            name: 'Score in Tweets with COVID',
            type: 'line',
            yAxisIndex: 1,
            data: [0.50, 0.18, 0.30, 0.46, 0.28, -0.13]
        },
        {
            name: 'Score in Tweets with COVID and Vaccine',
            type: 'line',
            yAxisIndex: 1,
            data: [-0.32, -0.19, -0.35, -0.20, 0.13, -0.23]
        }
    ]
};

covid_ana.setOption(covid_ana_option);

