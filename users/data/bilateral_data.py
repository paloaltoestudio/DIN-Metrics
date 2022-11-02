#Python
import datetime

#Django
from django.db.models import Sum, Count, Avg

#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#models
from bilateral.models import Bilateral

#utils
from .data_utils import update_plot

def bilateral_data(context, date):
    
    bilaterals = Bilateral.objects.filter(athlete=context['user'].athlete).order_by('date')
    #bilaterals_filter = Bilateral.objects.filter(athlete=context['user'].athlete, date=date).order_by('date')

    is_limit = len(bilaterals) >= 10

    data = {
        'date': [],
        'jump': [],
        'foot': [],
        'score': [],
    }

    if len(bilaterals) > 0:
        for bilateral in bilaterals:
            if(bilateral.left >= 0):
                data['date'].append(bilateral.date)
                data['jump'].append(bilateral.jump)
                data['foot'].append('Izquierda')
                data['score'].append(bilateral.left)
            
            if(bilateral.right >= 0):
                data['date'].append(bilateral.date)
                data['jump'].append(bilateral.jump)
                data['foot'].append('Derecha')
                data['score'].append(bilateral.right)


        df = pd.DataFrame(data=data, index=data['date'])
        if date != '':
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            df = df[(pd.to_datetime(df['date']) == date)]
        else:
            date = pd.to_datetime(df['date']).max()
            df = df[(pd.to_datetime(df['date']) == date)]

        #Bar chart
        bi_fig = px.bar(df, x= 'jump', y='score', labels={'jump':'Salto', 'score': 'Salto en CM', 'foot': 'Pierna'}, color = df['foot'], barmode = 'group')
        update_plot(bi_fig)
        context['graph'] = bi_fig.to_html(include_plotlyjs="cdn", full_html=False)

    context['bilaterals'] = bilaterals
    context['df'] = df.to_html(justify='left')
    context['date'] = date
    #context['is_limit'] = is_limit
