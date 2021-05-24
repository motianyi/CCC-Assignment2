var ec_map = echarts.init(document.getElementById('map-box'), 'dark');

var mapdata = [{'name':'Melbourne', 'positive':19870, 'neutral':5766, 'negative':6675}, {'name':'Perth', 'positive':12345, 'neutral':4332, 'negative':6543}]
//存为dict

var ec_map_option = {
	title:{
		text: '',
		subtext: '',
		x: 'left'
	},
	tooltip:{
		trigger: 'item'
	},
	//导航图标
	visualMap:{
		show: true,
		x: 'left',
		y: 'bottom',
		textStyle: {
			fontSize: 8,
		},
		splitList: [
			{start: 1, end: 9},
			{start: 10, end: 99},
			{start: 100, end: 999},
			{start: 1000, end: 9999},
			{start: 10000}],
		color: ['#D5DDDF', '#B2C5B2', '#6BBE4E', '#3C5148', '#1B2727']	
	},
	//配置属性
	series: [{
		name: 'Sentiment-Analysis',
		type: 'map',
		mapType: 'world',
		roam: true,
		itemStyle: {
			normal: {
				borderWidth: .5,
				borderColor:'A8D0DA',
				areaColor: 'FFEFD5',
			},
			emphasis:{//鼠标滑过地图高亮设置
				borderWidth: .5,
				borderColor: '#002452',
				areaColor: '#FFFFFF',
			}
		},
		label: {
			normal: {
				show: true,
				fontSize: 8,
			},
			emphasis: {
				show: true,
				fontSize: 8,
			}
		},
		data: mapdata
	}]
};
ec_map.setOption(ec_map_option);