import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
share = data.groupby(['Course Name'])['Rating'].count()

chart_def = """
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Number of ratings by course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'    
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f}%'
            }
        }
    },
    series: [
        {
            name: 'Percentage',
            colorByPoint: true,
            data: [
                {
                    name: 'Water',
                    y: 55.02
                },
                {
                    name: 'Fat',
                    sliced: true,
                    selected: true,
                    y: 26.71
                },
                {
                    name: 'Carbohydrates',
                    y: 1.09
                },
                {
                    name: 'Protein',
                    y: 15.5
                },
                {
                    name: 'Ash',
                    y: 1.68
                }
            ]
        }
    ]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews', classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analysis')

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc_data = [{'name': v1, 'y': v2} for v1, v2 in zip(share.index, share)]
    hc.options.series[0].data = hc_data

    return wp

jp.justpy(app)