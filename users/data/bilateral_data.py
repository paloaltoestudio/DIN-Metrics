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

def bilateral_data(context):
    
    bilaterals = Bilateral.objects.filter(athlete=context['user'].athlete).order_by('date')
    bilaterals_total = Bilateral.objects.values('date').annotate(Sum('deficit')).filter(athlete=context['user'].athlete)

    is_limit = len(bilaterals) >= 10

    if len(bilaterals) > 0:
        d = {
            'date': [bilateral_total['date'] for bilateral_total in bilaterals_total],
            'deficit': [bilateral_total['deficit__sum'] for bilateral_total in bilaterals_total],
        }

        df = pd.DataFrame(data=d)
        df.set_index('date', inplace=True)

        #Bar chart
        bi_fig = px.bar(df, labels={'value':'Deficit', 'date': 'Fecha'}, barmode = 'group')
        update_plot(bi_fig)
        context['graph'] = bi_fig.to_html(include_plotlyjs="cdn", full_html=False)

    context['bilaterals'] = bilaterals
    context['is_limit'] = is_limit
