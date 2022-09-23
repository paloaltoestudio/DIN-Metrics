#Django
from django.db.models import Sum, Count, Avg

#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#models
from profile_fv.models import Profile_fv

#utils
from .data_utils import update_plot

def profile_data(context):
    
    profiles = Profile_fv.objects.filter(athlete=context['user'].athlete)

    is_limit = len(profiles) >= 5

    d = {
        'Peso': [profile.weight for profile in profiles],
    }

    for i in range(1,5):
        current_speed = 'speed'+str(i)
        speed = [getattr(profile, current_speed) for profile in profiles]

        if any(type(value) == float for value in speed if value is not None):
            d['Velocidad '+str(i)] = speed

    #Get the max speed per row
    max_speeds = []
    for p in profiles:
        max_speed = [p.speed1 if p.speed1 is not None else 0, 
                     p.speed2 if p.speed2 is not None else 0,
                     p.speed3 if p.speed3 is not None else 0,
                     p.speed4 if p.speed4 is not None else 0,]

        max_speeds.append(max(max_speed))


    if len(profiles) < 1:
        d = {
            'Peso': [0, 0],
            'Velocidad 1': [0, 0],
        }
        max_speeds = [0, 0] 

    df = pd.DataFrame(data=d)
    df.set_index('Peso', inplace=True)

    df2 = pd.DataFrame(data=d)
    df2.set_index('Velocidad 1', inplace=True)


    if len(profiles) > 1:
        bi_fig = px.scatter(df, title='Perfil F/V', labels={'Peso':'PESO(KG)', 'value': 'VEL(m/s'}, trendline="ols", trendline_scope="overall")
        update_plot(bi_fig)
        
        bi_fig2 = px.scatter(x=max_speeds, y=d['Peso'], title='Perfil F/V', labels={'value':'PESO(KG)', 'Velocidad 1': 'VEL(m/s)'}, trendline="ols", trendline_scope="overall")
        update_plot(bi_fig2)

        model = px.get_trendline_results(bi_fig2)
        results = model.iloc[0]["px_fit_results"]
        
        rm = round(results.params[1]*0.3+results.params[0], 2)

        context['graph'] = bi_fig.to_html
        context['rm'] = rm
    else:
        bi_fig = px.scatter(x=[0,], y=[0,], title='Perfil F/V', labels={'Peso':'PESO(KG)', 'value': 'VEL(m/s)'}, trendline="ols", trendline_scope="overall")        
        update_plot(bi_fig)
        context['graph'] = bi_fig.to_html
        
    context['profiles'] = profiles
    context['is_limit'] = is_limit
    
