#Django
from django.db.models import Sum, Count, Avg

#third party
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#models
from profile_fv.models import Profile_fv

def profile_data(context):
    
    profiles = Profile_fv.objects.filter(athlete=context['user'].athlete)

    d = {
        'Peso': [profile.weight for profile in profiles],
        'Velocidad 1': [profile.speed1 for profile in profiles],
        #'Velocidad 2': [profile.speed2 for profile in profiles],
        #'Velocidad 3': [profile.speed3 for profile in profiles],
        # 'Velocidad 3': [1.25, None, None, None, None],
        # 'speed4': [profile.speed4 for profile in profiles],
    }




    df = pd.DataFrame(data=d)
    df.set_index('Peso', inplace=True)

    df2 = pd.DataFrame(data=d)
    df2.set_index('Velocidad 1', inplace=True)

    #Bar chart
    #bi_fig = px.bar(df, labels={'weight':'Peso', 'value': 'Vel'}, barmode = 'group')
    bi_fig = px.scatter(df, title='Perfil F/V', labels={'Peso':'PESO(KG)', 'value': 'VEL(m/s'}, trendline="ols", trendline_scope="overall")
    bi_fig2 = px.scatter(df2, title='Perfil F/V', labels={'value':'PESO(KG)', 'Velocidad 1': 'VEL(m/s)'}, trendline="ols", trendline_scope="overall")
    
    model = px.get_trendline_results(bi_fig2)
    results = model.iloc[0]["px_fit_results"]
    
    rm = round(results.params[1]*0.3+results.params[0], 2)

    context['profiles'] = profiles
    context['df'] = df2.to_html
    context['pgraph'] = bi_fig.to_html
    context['pgraph2'] = bi_fig2.to_html
    context['rm'] = rm
