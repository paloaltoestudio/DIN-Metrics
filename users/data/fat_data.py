#third party
import pandas as pd
import plotly.express as px

#models
from fat.models import Fat_rate, FatObservation

#utils
from .data_utils import update_plot

def fat_data(context):
    
    fat_rates = Fat_rate.objects.filter(athlete=context['user'].athlete).order_by('date')
    fat_observation = FatObservation.objects.filter(athlete=context['user'].athlete)

    if(fat_observation and len(fat_observation) > 0):
        fat_observation = fat_observation[0]
        context['fat_observation'] = fat_observation


    data = {
        'date': [],
        'rate': [],
    }

    if len(fat_rates) > 0:
        for fat in fat_rates:
                data['date'].append(fat.date)
                data['rate'].append(fat.fat_rate)


        df = pd.DataFrame(data=data, index=data['date'])
        context['df'] = df.to_html(justify='left')

        #Bar chart
        bi_fig = px.bar(df, x= 'date', y='rate', labels={'date':'Fecha', 'rate': 'Porcentaje'}, barmode = 'group')

        update_plot(bi_fig)

        context['fat_graph'] = bi_fig.to_html(include_plotlyjs="cdn", full_html=False)
        context['fat_graph_mobile'] = bi_fig.to_html(include_plotlyjs="cdn", full_html=False)

    context['fat_rates'] = fat_rates
