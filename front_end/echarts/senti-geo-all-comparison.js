/* jshint strict: false */

var geo_senti = echarts.init(document.getElementById('geo-senti'));

    var geo_senti_option = {
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
            data: ['Rate of Tweets with location', 'Sentiment score in all tweets', 'Sentiment score in tweets with location']
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
                name: 'Rate of Tweets with location',
                min: 0,
                max: 0.1,
                interval: 0.02,
                axisLabel: {
                    formatter: '{value}'
                }
            },
            {
                type: 'value',
                name: 'Sentiment score',
                min: 0,
                max: 2.5,
                interval: 0.5,
                axisLabel: {
                    formatter: '{value}'
                }
            }
        ],
        // formatter: function(data) {
        //     let res = data[0].name + '<br/>'
        //     let val
        //     let length = data.length
        //     let i = 0 
        //     for (; i < length; i++){
        //         val = data[i].value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')
        //         res += '<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:' + data[i].color + ';"></span>' + data[i].seriesName + '：' + val + '<br/>'
        //       }
        //       return res
        // },
        series: [
            {
                name: 'Rate of Tweets with location',
                type: 'bar',
                data: [962/26092, 1194/25912, 43/2368, 315/8692, 167/4579, 189/7404],
                // data = data.toFixed(2)
            },
            {
                name: 'Sentiment score in all tweets',
                type: 'line',
                yAxisIndex: 1,
                data: [0.65, 0.60, 0.83, 0.66, 0.81, 0.67]
            },
            {
                name: 'Sentiment score in tweets with location',
                type: 'line',
                yAxisIndex: 1,
                data: [0.81, 0.77, 1.67, 0.84, 0.63, 1.15]
            }
        ]
    };

    geo_senti.setOption(geo_senti_option);
