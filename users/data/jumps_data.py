#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

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
    
    

    d = {'SJ': [30,31,29,30,33,32,34,35,34,33,32,35], 'CMJ': [31.7,33,31,32,32.5,32.7,33,33.2,33.5,33.6,33.7,33.9], 'DROPS': [21.5,23,23,23.5,23.6,23.7,24,24.3,24.3,24.5,24.7,24.8], 'Q': [1.3,1.6,1.4,1.5,1.6,1.7,1.4,1.8,1.8,1.9,2,2.1]}

    #d = [['Mes ' + str(x) for x in range(1, 13)], [56, 123, 982, 213, 500, 673, 600, 500, 502, 405, 300, 230]]

    df = pd.DataFrame(data=d, index=['Mes ' + str(x) for x in range(1, 13)])



    #Bar chart
    #fig = px.bar(df, labels={'index':'Meses', 'value': 'Salto en CM'}, barmode = 'group')

    #Line chart
    fig = px.line(df, labels={'index':'Meses', 'value': 'Salto en CM'}, markers=True)

    context['fig'] = fig.to_html()
    context['df'] = df.to_html()
    context['jumps'] = jumps
