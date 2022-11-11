#Django
from django.db.models import Sum, Count, Avg

#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#models
from profile_fv.models import FV

#utils
from .data_utils import update_plot

def profile_data(context):
    
    profiles = FV.objects.filter(athlete=context['user'].athlete).order_by('date')

    d = {
        'Fecha':[],
        'RM':[],
    }

    if len(profiles) > 1:
        for profile in profiles:
            d['Fecha'].append(profile.date)
            d['RM'].append(profile.rm)

        df = pd.DataFrame(data=d)
        df.set_index('Fecha', inplace=True)
        print(df)
        bi_fig = px.bar(df, title='Perfil F/V', color=d['RM'], color_continuous_scale=[(0, "red"), (0.4, "yellow"), (0.6, "orange"), (1, "blue")], labels={'value': 'RM'})
        update_plot(bi_fig)
        context['graph'] = bi_fig.to_html(include_plotlyjs="cdn", full_html=False)
        
    context['profiles'] = profiles
    # context['is_limit'] = is_limit
    
