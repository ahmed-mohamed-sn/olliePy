
![OlliePy logo](./sphinxSource/source/_static/imgs/logo.png)
<br/>
<br/>
![TestReport](https://github.com/ahmed-mohamed-sn/olliePy/workflows/TestReport/badge.svg?branch=master)
![CI](https://github.com/ahmed-mohamed-sn/olliePy/workflows/CI/badge.svg)
[![Coverage](https://codecov.io/github/ahmed-mohamed-sn/olliepy/coverage.svg?branch=master)](https://codecov.io/gh/ahmed-mohamed-sn/olliepy)
<br/>
[![Downloads](https://pepy.tech/badge/olliepy)](https://pepy.tech/project/olliepy)
[![Downloads](https://pepy.tech/badge/olliepy/month)](https://pepy.tech/project/olliepy/month)
[![Downloads](https://pepy.tech/badge/olliepy/week)](https://pepy.tech/project/olliepy/week)
<br/>
[![PyPI Latest Release](https://img.shields.io/pypi/v/olliepy.svg)](https://pypi.org/project/olliepy/)
[![License](https://img.shields.io/pypi/l/olliepy.svg)](https://github.com/ahmed-mohamed-sn/olliepy/blob/master/LICENSE)
<br/>
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/olliepy.svg)](https://pypi.python.org/pypi/olliepy/)
<br/>
<br/>

<h3>
<a href="../../issues/new">:speech_balloon: Ask a question</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="../../issues?q=is%3Aissue+is%3Aclosed+sort%3Aupdated-desc">:book: Read questions</a>
</h3>

# OlliePy
> **OlliePy** is a python package which can help data scientists in
> exploring their data and evaluating and analysing their machine learning experiments by
> utilising the power and structure of modern web applications. 
> The data scientist only needs to provide the data and any required 
> information and OlliePy will generate the rest.

## <br/>Documentation
Get started by following the [guide](https://ahmed-mohamed-sn.github.io/olliePy/)

### Installation
`pip install -U olliepy`

### Examples
Get started using the provided [examples](https://github.com/ahmed-mohamed-sn/olliePy/tree/master/examples)

## Error analysis report for regression
**OlliePy** can support you in doing error analysis for regression problems.

### Features
- Compare different datasets
- Compare different groups of error in you data.
- Check for data shift by using the numerical and categorical features reports
- Check for concept shift by using the patterns report

![error analysis report demo](./sphinxSource/source/_static/imgs/error-analysis-regression-demo.gif)

## <br/> Interactive dashboard
**OlliePy** can also help you in creating an interactive dashboard in minutes.
The dashboard can be used for EDA or error analysis for classification or regression problems.
The performance of the dashboard depend on the size of the data, number of charts, and the specs of the machine used.

![interactive dashboard demo](./sphinxSource/source/_static/imgs/interactive-dashboard-demo.gif)

### Features
- Draggable and resizeable charts
- Cross filtering
- Choose from 14 different customizable charts
- Different aggregations can be applied
- Searchable charts
- Create new charts
- Edit existing charts
- Delete charts
- Dark mode
- Auto save functionality
- Charts can be locked in place
- Fullscreen
- Bin numerical features to be used in heatmaps, row charts, etc.


### Available charts 
|                                                                                                   |                                                                                                |
|:-------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------:|
|            **Bar chart** ![bar-chart](./sphinxSource/source/_static/gifs/bar-chart.gif)           |            **Box plot** ![box-plot](./sphinxSource/source/_static/gifs/box-plot.gif)           |
|          **Data table** ![data-table](./sphinxSource/source/_static/gifs/data-table.gif)          |            **Heat map** ![heat-map](./sphinxSource/source/_static/gifs/heatmap.gif)            |
|            **Histogram** ![histogram](./sphinxSource/source/_static/gifs/histogram.gif)           |       **Leaflet map** ![leaflet-map](./sphinxSource/source/_static/gifs/leaflet-map.gif)       |
| **Number display** <br/> ![number-display](./sphinxSource/source/_static/gifs/number-display.gif) |          **Pie chart** ![pie-chart](./sphinxSource/source/_static/gifs/pie-chart.gif)          |
|            **Row chart** ![row-chart](./sphinxSource/source/_static/gifs/row-chart.gif)           |      **Scatter plot** ![scatter-plot](./sphinxSource/source/_static/gifs/scatter-plot.gif)     |
|            **Sun burst** ![sun-burst](./sphinxSource/source/_static/gifs/sun-burst.gif)           |   **Time bar chart** ![time-bar-chart](./sphinxSource/source/_static/gifs/time-bar-chart.gif)  |
|      **Time box plot** ![time-box-plot](./sphinxSource/source/_static/gifs/time-box-plot.gif)     | **Time line chart** ![time-line-chart](./sphinxSource/source/_static/gifs/time-line-chart.gif) |


## OlliePy Roadmap
- [x] Error analysis report for regression
- [x] Interactive dashboard
- [ ] Embedded interactive dashboard
- [ ] ML models evaluation and comparison report which includes model interpretation and bias checking
- [ ] Error analysis report for classification
