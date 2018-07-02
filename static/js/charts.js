window.onload = function () {
    var enterpriseAtlas = echarts.init(document.getElementById('enterpriseAtlas'));
    enterpriseAtlas.showLoading();
    $.get('/static/json/enterpriseAtlas.json', function (data) {
        enterpriseAtlas.hideLoading();

        enterpriseAtlas.setOption(option = {
            title: {
                text: '江苏星网软件有限公司',
                subtext: '企业图谱',
                left: 'center'
            },
            tooltip: {
                trigger: 'item',
                triggerOn: 'mousemove'
            },
            series: [
                {
                    type: 'tree',

                    data: [data],

                    top: '18%',
                    bottom: '14%',

                    layout: 'radial',

                    symbol: 'emptyCircle',

                    symbolSize: 14,

                    initialTreeDepth: 3,

                    animationDurationUpdate: 750,

                    itemStyle: {
                        shadowColor: 'rgba(0, 0, 0, 0.5)',
                        shadowBlur: 2
                    }

                }
            ]
        });
    });
};