def update_plot(fig):
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.update_layout({
            'plot_bgcolor': 'rgba(255,255,255,1)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
        })