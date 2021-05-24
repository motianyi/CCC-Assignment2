/* jshint strict: false */

var total_covid = echarts.init(document.getElementById('total-covid'));

total_covid.showLoading();

$.getJSON('../data/all_senti_analysis.json', function (jsondata) {
    console.log(JSON.stringify(jsondata));
    var city = []
    var value = []
    for (const key in jsondata){
        if(jsondata.hasOwnProperty(key)){
        //   console.log(`${key} : ${res[key]}`)
          city.push(jsondata[key]["gcc_name16"])
          value.push(jsondata[key]["senti_score"])
        }
    }
    console.log(city);

    total_covid.hideLoading();
    var total_covid_option = {
        xAxis: {
            type: 'category',
            data: city
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: value,
            type: 'bar',
            showBackground: true,
            backgroundStyle: {
                color: 'rgba(180, 180, 180, 0.2)'
            }
        }]
    };

    total_covid.setOption(total_covid_option);
});


// var total_covid = echarts.init(document.getElementById('total-covid'));

// total_covid.showLoading();

// $.getJSON('https://s3-us-west-2.amazonaws.com/s.cdpn.io/95368/obama_budget_proposal_2012.list.json', function (obama_budget_2012) {
//     total_covid.hideLoading();

//     option = {
        
//         xAxis: [
//             {
//                 type : 'category',
//                 data : obama_budget_2012.names
//             }
//         ],
//         yAxis: [
//             {
//                 type : 'value',
//                 name : 'Budget (million USD)',
//                 axisLabel: {
//                     formatter: function (a) {
//                         a = +a;
//                         return isFinite(a)
//                             ? echarts.format.addCommas(+a / 1000)
//                             : '';
//                     }
//                 }
//             }
//         ],
  
//         series : [
//             {
//                 name: 'Budget 2011',
//                 type: 'bar',
//                 data: obama_budget_2012.budget2011List
//             },
//             {
//                 name: 'Budget 2012',
//                 type: 'bar',
//                 data: obama_budget_2012.budget2012List
//             }
//         ]
//     };

//     total_covid.setOption(option);

// });
