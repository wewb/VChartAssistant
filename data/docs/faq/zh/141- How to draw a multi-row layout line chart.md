---
title: 8. 如何绘制多行布局的折线图</br>
---
## 问题标题

如何绘制多行布局的折线图</br>


## 问题描述

折线图可以实现如下多行布局的分组折线图吗？</br>
<img src='https://cdn.jsdelivr.net/gh/xuanhun/articles/visactor/img/Q0WVbWWQeoH0qVxCfTjcJIobnEb.gif' alt='' width='1732' height='754'>



## 解决方案 

VChart 中可以结合组合图和 grid 布局实现，参考 demo: https://visactor.io/vchart/demo/combination/col-line。</br>


## 代码示例  

```
const regionStyle = {
  stroke: 'rgb(201,205,212)',
  lineWidth: 1,
  strokeTop: true,
  strokeBottom: false,
  strokeLeft: false,
  strokeRight: false
};
const leftAxesCommonSpec = {
  expand: { max: 0.2 },
  label: { flush: true, visible: true },
  tick: { visible: false },
  forceTickCount: 3
};
const spec = {
  type: 'common',
  layout: {
    type: 'grid',
    col: 2,
    row: 6,
    elements: [
      {
        modelId: 'legend',
        col: 0,
        colSpan: 2,
        row: 5
      },
      {
        modelId: 'Social Penetration',
        col: 1,
        row: 0
      },
      {
        modelId: 'Engagement - Socialization',
        col: 1,
        row: 1
      },
      {
        modelId: 'Penetration of Private Messages',
        col: 1,
        row: 2
      },
      {
        modelId: 'Number of Private Messages per User',
        col: 1,
        row: 3
      },
      {
        modelId: 'Social Penetrationleft',
        col: 0,
        row: 0
      },
      {
        modelId: 'Engagement - Socialization-left',
        col: 0,
        row: 1
      },
      {
        modelId: 'Penetration of Private Messagesleft',
        col: 0,
        row: 2
      },
      {
        modelId: 'Number of Private Messages per Userleft',
        col: 0,
        row: 3
      },
      {
        modelId: 'Number of Private Messages per User-bottom',
        col: 1,
        row: 4
      }
    ]
  },
  region: [
    {
      id: 'Social Penetration',
      style: {
        ...regionStyle,
        strokeTop: false
      }
    },
    {
      id: 'Engagement - Socialization',
      style: regionStyle
    },
    {
      id: 'Penetration of Private Messages',
      style: regionStyle
    },
    {
      id: 'Number of Private Messages per User',
      style: regionStyle
    }
  ],
  legends: {
    padding: {
      top: 10
    },
    visible: true,
    orient: 'bottom',
    id: 'legend',
    regionId: [
      'Social Penetration',
      'Engagement - Socialization',
      'Penetration of Private Messages',
      'Number of Private Messages per User'
    ]
  },
  seriesField: 'type',
  tooltip: {
    dimension: {
      title: {
        value: datum => {
          return `第 ${datum.x} 天`;
        }
      },
      content: [
        {
          key: datum => datum.type,
          value: datum => datum.y
        }
      ]
    }
  },
  series: [
    {
      id: 'Social Penetrationseries0',
      regionId: 'Social Penetration',
      type: 'line',
      data: { id: 'Social Penetration' },
      xField: 'x',
      yField: 'y'
    },
    {
      id: 'Engagement - Socialization-series0',
      regionId: 'Engagement - Socialization',
      type: 'line',
      data: { id: 'Engagement - Socialization' },
      xField: 'x',
      yField: 'y'
    },
    {
      id: 'Penetration of Private Messagesseries0',
      regionId: 'Penetration of Private Messages',
      type: 'line',
      data: { id: 'Penetration of Private Messages' },
      xField: 'x',
      yField: 'y'
    },
    {
      id: 'Number of Private Messages per Userseries0',
      regionId: 'Number of Private Messages per User',
      type: 'line',
      data: { id: 'Number of Private Messages per User' },
      xField: 'x',
      yField: 'y'
    }
  ],
  axes: [
    {
      id: 'Social Penetrationleft',
      regionId: 'Social Penetration',
      orient: 'left',
      title: { visible: true, text: 'SP' },
      ...leftAxesCommonSpec
    },
    {
      id: 'Engagement - Socialization-left',
      regionId: 'Engagement - Socialization',
      orient: 'left',
      title: { visible: true, text: 'ES' },
      ...leftAxesCommonSpec
    },
    {
      id: 'Penetration of Private Messagesleft',
      regionId: 'Penetration of Private Messages',
      orient: 'left',
      title: { visible: true, text: 'Penetration of PM' },
      ...leftAxesCommonSpec
    },
    {
      id: 'Number of Private Messages per Userleft',
      regionId: 'Number of Private Messages per User',
      orient: 'left',
      title: { visible: true, text: 'PM per User' },
      ...leftAxesCommonSpec
    },
    {
      id: 'Number of Private Messages per User-bottom',
      regionId: [
        'Social Penetration',
        'Engagement - Socialization',
        'Penetration of Private Messages',
        'Number of Private Messages per User'
      ],
      orient: 'bottom',
      label: {
        firstVisible: true,
        lastVisible: true,
        visible: true
      },
      tick: { visible: false },
      paddingInner: 0.99,
      paddingOuter: 0
    }
  ]
};

fetch('https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/vchart/tutorials/col-line-data.json').then(res => {
  res.json().then(dataJson => {
    spec.series.forEach(s => {
      s.data.values = dataJson[s.data.id];
    });
    const vchart = new VChart(spec, { dom: CONTAINER_ID });
    vchart.renderSync();

    // Just for the convenience of console debugging, DO NOT COPY!
    window['vchart'] = vchart;
  });
});</br>
```
## 结果展示 

https://visactor.io/vchart/demo/combination/col-line</br>
## 相关文档

Demo：https://visactor.io/vchart/demo/combination/col-line</br>
教程：</br>
*  组合图： https://visactor.io/vchart/guide/tutorial_docs/Chart_Types/Combination</br>
*  Grid 布局：https://visactor.io/vchart/guide/tutorial_docs/Layout/Layout_Cases/example-grid</br>
API：</br>
*  组合图：https://visactor.io/vchart/option/commonChart</br>
*  Grid 布局：https://visactor.io/vchart/option/commonChart#layout.type</br>
Github：https://github.com/VisActor/VChart/</br>



