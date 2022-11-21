#Python
import datetime

#Django
from django.db.models import Sum, Count, Avg

#third party
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

#models
from bilateral.models import Bilateral, BilateralObservation

#utils
from .data_utils import update_plot

def bilateral_data(context, date):
    
    bilaterals = Bilateral.objects.filter(athlete=context['user'].athlete).order_by('date')
    #bilaterals_filter = Bilateral.objects.filter(athlete=context['user'].athlete, date=date).order_by('date')
    bilateral_observation = BilateralObservation.objects.filter(athlete=context['user'].athlete)

    if(bilateral_observation and len(bilateral_observation) > 0):
        bilateral_observation = bilateral_observation[0]
        context['bilateral_observation'] = bilateral_observation


    is_limit = len(bilaterals) >= 10

    data = {
        'date': [],
        'jump': [],
        'score_left': [],
        'score_right': [],
        'deficit': [],
    }

    if len(bilaterals) > 0:
        for bilateral in bilaterals:
                data['date'].append(bilateral.date)
                data['jump'].append(bilateral.jump)
                data['deficit'].append(bilateral.deficit)
                data['score_left'].append(bilateral.left)
                data['score_right'].append(bilateral.right)


        df = pd.DataFrame(data=data, index=data['date'])
        if date != '':
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            df = df[(pd.to_datetime(df['date']) == date)]
        else:
            date = pd.to_datetime(df['date']).max()
            df = df[(pd.to_datetime(df['date']) == date)]
        context['df'] = df.to_html(justify='left')

        #Bar chart
        # bi_fig = px.bar(df, x= 'jump', y='score', labels={'jump':'Salto', 'score': 'Salto en CM', 'foot': 'Pierna'}, color = df['foot'], barmode = 'group')

        bi_fig = make_subplots(specs=[[{"secondary_y": True}]])

        bi_fig.add_trace(
            go.Bar(x=df['jump'], y=df['score_left'], name="izquierdo"),
            secondary_y=False,
        )
        bi_fig.add_trace(
            go.Bar(x=df['jump'], y=df['score_right'], name="derecho"),
            secondary_y=False,
        )

        bi_fig.update_layout(
            barmode="group",
            xaxis_title='Tipo de salto',
        )

        bi_fig.add_trace(
            go.Scatter(x=df['jump'], 
                       y=df['deficit'], 
                       mode="markers+lines+text", 
                       name="deficit", 
                       text=df['deficit'], 
                       textposition="top center",
                       textfont=dict(
                            size=14,
                        )),
            secondary_y=True,
        )

        bi_fig.update_layout(
            margin=dict(t=50)
        )


        bi_fig['layout']['yaxis']['title']='Salto en cm'
        bi_fig['layout']['yaxis2']['title']='Déficit'

        update_plot(bi_fig)

        context['graph'] = bi_fig.to_html(include_plotlyjs="cdn", full_html=False)
        context['graph_mobile'] = bi_fig.to_html(include_plotlyjs="cdn", full_html=False)

    context['bilaterals'] = bilaterals
    context['date'] = date
    #context['is_limit'] = is_limit
