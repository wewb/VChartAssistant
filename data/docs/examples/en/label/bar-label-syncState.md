---
category: examples
group: label
title: Bar Label SyncState
keywords: label
order: 35-1
cover: /vchart/preview/label-syncState_1.9.0.gif
option: barChart#label
---

# Bar Label SyncState

If the data graphics have specific styles for interaction, it is generally expected that the corresponding labels also highlight or blur accordingly based on the interaction state.

## Key Configuration

To achieve this, configure the following properties for synchronization on the graphic elements:

- `label`: Label configuration.
  - `visible`: Display the label.
  - `syncState`: Synchronize with the state of the data element.

## Demo source

```javascript livedemo
const spec = {
  type: 'bar',
  data: [
    {
      id: 'barData',
      values: [
        {
          State: 'WY',
          Age: 'Under 5 Years',
          Population: 25635
        },
        {
          State: 'WY',
          Age: '5 to 13 Years',
          Population: 1890
        },
        {
          State: 'WY',
          Age: '14 to 17 Years',
          Population: 9314
        },
        {
          State: 'DC',
          Age: 'Under 5 Years',
          Population: 30352
        },
        {
          State: 'DC',
          Age: '5 to 13 Years',
          Population: 20439
        },
        {
          State: 'DC',
          Age: '14 to 17 Years',
          Population: 10225
        },
        {
          State: 'VT',
          Age: 'Under 5 Years',
          Population: 38253
        },
        {
          State: 'VT',
          Age: '5 to 13 Years',
          Population: 42538
        },
        {
          State: 'VT',
          Age: '14 to 17 Years',
          Population: 15757
        },
        {
          State: 'ND',
          Age: 'Under 5 Years',
          Population: 51896
        },
        {
          State: 'ND',
          Age: '5 to 13 Years',
          Population: 67358
        },
        {
          State: 'ND',
          Age: '14 to 17 Years',
          Population: 18794
        },
        {
          State: 'AK',
          Age: 'Under 5 Years',
          Population: 72083
        },
        {
          State: 'AK',
          Age: '5 to 13 Years',
          Population: 85640
        },
        {
          State: 'AK',
          Age: '14 to 17 Years',
          Population: 22153
        }
      ]
    }
  ],
  yField: 'State',
  xField: 'Population',
  seriesField: 'Age',
  direction: 'horizontal',
  stack: true,
  percent: true,
  legends: {
    visible: true
  },
  label: {
    visible: true,
    position: 'center',
    smartInvert: true,
    syncState: true,
    style: {
      fill: '#222'
    },
    state: {
      hover_series: {
        opacity: 1
      },
      unHover_series: {
        opacity: 0.1
      }
    }
  },
  bar: {
    state: {
      hover_series: {
        opacity: 1
      },
      unHover_series: {
        opacity: 0.2
      }
    }
  },
  tooltip: false,
  axes: [
    {
      orient: 'top',
      label: {
        formatMethod: val => {
          return `${(val * 100).toFixed(2)}%`;
        }
      }
    }
  ]
};

const vchart = new VChart(spec, { dom: CONTAINER_ID });

vchart.on('pointerover', { level: 'mark' }, ({ datum, mark }) => {
  if (mark?.name === 'bar' && datum) {
    const series = datum.Age;
    vchart.updateState({
      hover_series: {
        filter: datum => datum.Age === series
      },
      unHover_series: {
        filter: datum => datum.Age !== series
      }
    });
  }
});

vchart.on('pointerout', { level: 'mark' }, ({ datum, mark }) => {
  if (mark?.name === 'bar' && datum) {
    vchart.updateState({
      hover_series: {
        filter: () => false
      },
      unHover_series: {
        filter: () => false
      }
    });
  }
});

vchart.renderSync();

// Just for the convenience of console debugging, DO NOT COPY!
window['vchart'] = vchart;
```

## Related Tutorial

[Scatter Chart](link)
