#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#models
from bilateral.models import Bilateral

def bilateral_data(context):
    
    bilaterals = Bilateral.objects.filter(athlete=context['user'].athlete)


    d = {
        'date': [bilateral.date for bilateral in bilaterals],
        'deficit': [bilateral.deficit for bilateral in bilaterals],
    }

    df = pd.DataFrame(data=d)
    df.set_index('date', inplace=True)

    #Bar chart
    bi_fig = px.bar(df, labels={'value':'Deficit', 'date': 'Fecha'}, barmode = 'group')

    context['bilaterals'] = bilaterals
    context['ddf'] = df.to_html
    context['graph'] = bi_fig.to_html
