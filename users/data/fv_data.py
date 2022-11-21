#Django
from django.db.models import Sum, Count, Avg

#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#models
from profile_fv.models import FV, FV_register

#utils
from .data_utils import update_plot


def fv_data(fv_id, context):
    
    # fv_id = self.request.GET['fv_id']
    fv = FV.objects.filter(id=fv_id)
    fv = fv[0]
    fv_registers = FV_register.objects.filter(profile_fv=fv).order_by('weight')
    

    rm = 0

    d = {
        'Peso': [],
        'Velocidad': [],
    }

    for fv_register in fv_registers:

        #Get the max speed per row
        speeds = [fv_register.speed1 if fv_register.speed1 is not None else 0, 
                  fv_register.speed2 if fv_register.speed2 is not None else 0,
                  fv_register.speed3 if fv_register.speed3 is not None else 0,
                  fv_register.speed4 if fv_register.speed4 is not None else 0,]

        d['Peso'].append(fv_register.weight)
        d['Velocidad'].append(max(speeds))

    if len(fv_registers) > 0:
        df = pd.DataFrame(data=d)
        df.set_index('Peso', inplace=True)
        context['df'] = df.to_html(justify='left')

        bi_fig2 = px.scatter(x=df['Velocidad'], y=df.index, title='Perfil F/V', labels={'y':'PESO(KG)', 'x': 'VEL(m/s)'}, trendline="ols", trendline_scope="overall")
        update_plot(bi_fig2)
        context['graph'] = bi_fig2.to_html(include_plotlyjs="cdn", full_html=False)

        #Get RM from graph model
        if len(fv_registers) > 1:
            model = px.get_trendline_results(bi_fig2)
            results = model.iloc[0]["px_fit_results"]

            try:
                rm = round(results.params[1]*0.3+results.params[0], 2)
                context['rm'] = rm
                
            except IndexError:
                print('RM params index error')

        print('df: ', df)

    print('rows: ', d)
        
    context['fv'] = fv
    context['fv_registers'] = fv_registers

    return rm

    
    
