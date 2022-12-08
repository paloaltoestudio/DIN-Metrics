#third party
import pandas as pd
import plotly.express as px

#models
from fat.models import Fat_rate

#utils
from .data_utils import update_plot

def fat_data(context):
    
    fat_rates = Fat_rate.objects.filter(athlete=context['user'].athlete).order_by('date')
    #bilateral_observation = BilateralObservation.objects.filter(athlete=context['user'].athlete)

    # if(bilateral_observation and len(bilateral_observation) > 0):
    #     bilateral_observation = bilateral_observation[0]
    #     context['bilateral_observation'] = bilateral_observation


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

    context['fat_rates'] = fat_rates
