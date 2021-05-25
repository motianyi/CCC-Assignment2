/* jshint strict: false */

var beer = echarts.init(document.getElementById('beer'));

var beer_option = {
    title: {
        text: 'Beers',
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
            name: 'beer',
            type: 'pie',
            radius: '50%',
            data: [
                {value: 1048, name: 'Beer'},
                {value: 735, name: 'Others'},

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

beer.setOption(beer_option);