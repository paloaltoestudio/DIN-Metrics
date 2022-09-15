#Django
from django.db.models import Sum, Count, Avg

#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#models
from bilateral.models import Bilateral

def bilateral_data(context):
    
    bilaterals = Bilateral.objects.filter(athlete=context['user'].athlete)
    bilaterals_total = Bilateral.objects.values('date').annotate(Sum('deficit')).filter(athlete=context['user'].athlete)

    print([bilateral_total['date'] for bilateral_total in bilaterals_total])

    d = {
        'date': [bilateral_total['date'] for bilateral_total in bilaterals_total],
        'deficit': [bilateral_total['deficit__sum'] for bilateral_total in bilaterals_total],
    }

    df = pd.DataFrame(data=d)
    df.set_index('date', inplace=True)

    #Bar chart
    bi_fig = px.bar(df, labels={'value':'Deficit', 'date': 'Fecha'}, barmode = 'group')

    context['bilaterals'] = bilaterals
    context['ddf'] = df.to_html
    context['graph'] = bi_fig.to_html
