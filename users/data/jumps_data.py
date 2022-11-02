import time

#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#models
from neuro.models import SJ, CMJ, DROPS, Q

#utils
from .data_utils import update_plot

def jump_data(context):
    
    sj = SJ.objects.filter(athlete=context['user'].athlete).order_by('date')
    cmj = CMJ.objects.filter(athlete=context['user'].athlete)
    drops = DROPS.objects.filter(athlete=context['user'].athlete)
    q = Q.objects.filter(athlete=context['user'].athlete)

    jumps = []

    d = {
        'date':[],
        'jump':[],
        'score':[],
        'id':[],
    }

    def add_jump(name, jump):
        for item in jump:
            jumps.append(item)

            d['jump'].append(name)
            d['date'].append(item.date) 
            d['score'].append(item.score)
            d['id'].append(item.id)

    if len(sj) > 0:
        add_jump('SJ', sj)

    if len(cmj) > 0:  
        add_jump('CMJ', cmj)

    if len(drops) > 0:  
        add_jump('DROPS', drops)

    if len(q) > 0:  
        add_jump('Q', q)


    #df = pd.DataFrame(data=d, index=['Mes ' + str(x) for x in range(1, 3)])
    df = pd.DataFrame(data=d, index=d['date'])

    #Bar chart
    fig = px.bar(df, x= 'date', y = 'score', labels={'date':'Fecha', 'score': 'Salto en CM', 'color': 'Salto'}, color = d['jump'], barmode = 'group')
    update_plot(fig)

    #Line chart
    #fig = px.line(df, labels={'index':'Meses', 'value': 'Salto en CM'}, markers=True)

    context['fig'] = fig.to_html(include_plotlyjs="cdn", full_html=False)
    context['jumps'] = jumps
    context['df'] = df.to_html(justify='left')
