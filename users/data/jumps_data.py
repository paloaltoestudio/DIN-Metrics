#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#models
from neuro.models import SJ, CMJ, DROPS, Q

def jump_data(context):

    x = ['Mes ' + str(x) for x in range(1, 13)]
  
    fig2 = go.Figure(data=[go.Bar(
        name = 'SJ',
        x = x,
        y = [100, 200, 500, 673, 600, 500, 502, 405, 609, 700, 750, 760]
    ),
        go.Bar(
        name = 'CMJ',
        x = x,
        y = [56, 123, 982, 213, 500, 673, 600, 500, 502, 405, 300, 230]
    )
    ])

    jumps = {
        'SJ': {
            'm1': 56,
            'm2': 123,
        },
        'CMJ': {
            'm1': 34,
            'm2': 58,
        },
    }
    
    
    sj = SJ.objects.filter(athlete=context['user'].athlete)
    cmj = CMJ.objects.filter(athlete=context['user'].athlete)
    drops = DROPS.objects.filter(athlete=context['user'].athlete)
    q = Q.objects.filter(athlete=context['user'].athlete)

    d = {'SJ': [0,0,0,0,0,0,0,0,0,0,0,0], 
         'CMJ': [0,0,0,0,0,0,0,0,0,0,0,0], 
         'DROPS': [0,0,0,0,0,0,0,0,0,0,0,0], 
         'Q': [0,0,0,0,0,0,0,0,0,0,0,0]}

    if len(sj) > 0:
        sj = sj[0]
        d['SJ'] = [sj.month1, sj.month2, sj.month3, sj.month4, sj.month5, sj.month6,
                    sj.month7, sj.month8, sj.month9, sj.month10, sj.month11, sj.month12]

    if len(cmj) > 0:             
        cmj = cmj[0]
        d['CMJ'] = [cmj.month1, cmj.month2, cmj.month3, cmj.month4, cmj.month5, cmj.month6,
                    cmj.month7, cmj.month8, cmj.month9, cmj.month10, cmj.month11, cmj.month12]

    if len(drops) > 0:  
        drops = drops[0]
        d['DROPS'] = [drops.month1, drops.month2, drops.month3, drops.month4, drops.month5, drops.month6,
                    drops.month7, drops.month8, drops.month9, drops.month10, drops.month11, drops.month12]

    if len(q) > 0:  
        q = q[0]
        d['Q'] = [q.month1, q.month2, q.month3, q.month4, q.month5, q.month6,
                    q.month7, q.month8, q.month9, q.month10, q.month11, q.month12]

    df = pd.DataFrame(data=d, index=['Mes ' + str(x) for x in range(1, 13)])

    #Bar chart
    #fig = px.bar(df, labels={'index':'Meses', 'value': 'Salto en CM'}, barmode = 'group')

    #Line chart
    fig = px.line(df, labels={'index':'Meses', 'value': 'Salto en CM'}, markers=True)

    context['fig'] = fig.to_html()
    context['df'] = df.to_html()
    context['jumps'] = d
