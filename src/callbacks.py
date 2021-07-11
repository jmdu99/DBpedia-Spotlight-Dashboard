# -*- coding: utf-8 -*-
import dash
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import resources as R

def initialize_callbacks(app):                                                 
 # Comparison callback -> To be modified
     @app.callback(
        dash.dependencies.Output('metric', 'figure'),
        [dash.dependencies.Input('dropdown', 'value')])
     def update_metrics(value):
        fig = make_subplots(rows=1, cols=2, specs=[[{'type' : 'indicator'}, 
                                                {'type' : 'indicator'}]])
        if value == 'Precision':
            fig.add_trace(
                go.Indicator(
                    mode = "gauge+number",
                    value = float(R.es_stats[0]),
        title = {'text': "Precision of Spanish valid URLs"},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {'axis': {'range': [0, 1]}}
        ),
        row=1, col=1
        )
            fig.add_trace(
                go.Indicator(
                    mode = "gauge+number",
                    value = float(R.en_stats[0]),
                    title = {'text': "Precision of English valid URLs"},
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    gauge = {'axis': {'range': [0, 1]}}
                    ),
                row=1, col=2
                )
        
        elif value == 'Impact':
            fig.add_trace(
                go.Indicator(
                    mode = "gauge+number",
                    value = float(R.es_stats[1]),
                    title = {'text': "Impact of Spanish invalid types"},
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    gauge = {'axis': {'range': [0, 1]}, 'bar': {'color': "red"}}
                    ),
                row=1, col=1
                )
            fig.add_trace(
                go.Indicator(
                    mode = "gauge+number",
                    value = float(R.en_stats[1]),
                    title = {'text': "Impact of English invalid types"},
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    gauge = {'axis': {'range': [0, 1]}, 'bar': {'color': "red"}}
                    ),
                row=1, col=2
                )
        return fig

    # Spanish known types callback
     @app.callback(
            dash.dependencies.Output('es_known_types', 'figure'),
            [dash.dependencies.Input('ontology', 'clickData')]
            )
     def es_update_known_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.known_types_es
            ontology_df = R.get_ontology_df()
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
            figure.add_vline(x=float(R.es_stats[6]), line_width=4, line_color="#77C14C") # Mean
            figure.add_vline(x=float(R.es_stats[7]), line_width=4, line_color="#1FAFEE") # Median
            figure.add_vline(x=float(R.es_stats[9]), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
                go.Scatter(x=[float(R.es_stats[6])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.es_stats[6]], hoverinfo="text"),
                go.Scatter(x=[float(R.es_stats[7])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[7]], hoverinfo="text"),
                go.Scatter(x=[float(R.es_stats[9])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.es_stats[9]], hoverinfo="text")
                ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        
 # Spanish instance types callback
     @app.callback(
            dash.dependencies.Output('es_instance_types', 'figure'),
            [dash.dependencies.Input('ontologyy', 'clickData')]
            )
     def es_update_instance_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.get_instance_types_df(R.es_dashboard_directory)
            ontology_df = R.get_ontology_df()
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        

# Spanish uriCounts callback
     @app.callback(
        dash.dependencies.Output('uriCounts_graph', 'figure'),
        [dash.dependencies.Input('uriCounts_slider', 'value')])
     def update_uriCounts_figure(value):
        uriCounts_df = R.uriCounts_es
        filtered_df = uriCounts_df[(uriCounts_df['Count'] >= value[0]) & (uriCounts_df['Count'] <= value[1])].sample(n=20)	
        fig = go.Figure()
        fig.add_trace(go.Bar(x= filtered_df['Count'], y= filtered_df['DBpedia entity'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
        fig.add_vline(x=float(R.es_stats[35]), line_width=4, line_color="#77C14C") # Mean
        fig.add_vline(x=float(R.es_stats[36]), line_width=4, line_color="#1FAFEE") # Median
        fig.add_vline(x=float(R.es_stats[38]), line_width=4, line_color="#D53614") # Standard deviation
        fig.add_traces([
        go.Scatter(x=[float(R.es_stats[35])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.es_stats[35]], hoverinfo="text"),
        go.Scatter(x=[float(R.es_stats[36])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[36]], hoverinfo="text"),
        go.Scatter(x=[float(R.es_stats[38])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.es_stats[38]], hoverinfo="text")
        ])
        fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times appearing in Wikipedia dump", yaxis_title="DBpedia entity")
        return fig    
   

# Spanish pairCounts callback
     @app.callback(
        dash.dependencies.Output('pairCounts_graph', 'figure'),
        [dash.dependencies.Input('pairCounts_slider', 'value')])
     def update_pairCounts_figure(value):
        pairCounts_df = R.pairCounts_es
        filtered_df = pairCounts_df[(pairCounts_df['Times linked'] >= value[0]) & (pairCounts_df['Times linked'] <= value[1])].sample(n=20)	
        fig = go.Figure()
        fig.add_trace(go.Bar(x= filtered_df['Times linked'], y= filtered_df['Surface form'], orientation='h', marker_color='#A349A4', name = "Surface form"))
        fig.add_vline(x=float(R.es_stats[39]), line_width=4, line_color="#77C14C") # Mean
        fig.add_vline(x=float(R.es_stats[40]), line_width=4, line_color="#1FAFEE") # Median
        fig.add_vline(x=float(R.es_stats[42]), line_width=4, line_color="#D53614") # Standard deviation
        fig.add_traces([
        go.Scatter(x=[float(R.es_stats[39])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.es_stats[39]], hoverinfo="text"),
        go.Scatter(x=[float(R.es_stats[40])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[40]], hoverinfo="text"),
        go.Scatter(x=[float(R.es_stats[42])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.es_stats[42]], hoverinfo="text")
        ])
        fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times linked to a DBpedia entity", yaxis_title="Surface form")
        return fig           
      
# Spanish sfAndTotalCounts callback
     @app.callback(
        dash.dependencies.Output('sfAndTotalCounts_graph', 'figure'),
        [dash.dependencies.Input('sfAndTotalCounts_slider', 'value')])
     def update_sfAndTotalCounts_figure(value):
        sfAndTotalCounts_df = R.sfAndTotalCounts_es
        filtered_df = sfAndTotalCounts_df[(sfAndTotalCounts_df['Times linked'] >= value[0]) & (sfAndTotalCounts_df['Times linked'] <= value[1])].sample(n=20)	
        fig = go.Figure()
        fig.add_trace(go.Bar(x= filtered_df['Times linked'], y= filtered_df['Surface form'], orientation='h', marker_color='#A349A4', name = "Surface form"))
        fig.add_vline(x=float(R.es_stats[52]), line_width=4, line_color="#77C14C") # Mean
        fig.add_vline(x=float(R.es_stats[53]), line_width=4, line_color="#1FAFEE") # Median
        fig.add_vline(x=float(R.es_stats[55]), line_width=4, line_color="#D53614") # Standard deviation
        fig.add_traces([
        go.Scatter(x=[float(R.es_stats[52])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.es_stats[52]], hoverinfo="text"),
        go.Scatter(x=[float(R.es_stats[53])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[53]], hoverinfo="text"),
        go.Scatter(x=[float(R.es_stats[55])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.es_stats[55]], hoverinfo="text")
        ])
        fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times linked to a DBpedia entity", yaxis_title="Surface form")
        return fig


# Spanish tokenCounts callback
     @app.callback(
        dash.dependencies.Output('tokenCounts_graph', 'figure'),
        [dash.dependencies.Input('tokenCounts_slider', 'value')])
     def update_tokenCounts_figure(value):
        tokenCounts_df = R.tokenCounts_es
        filtered_df = tokenCounts_df[(tokenCounts_df['Nº tokens'] >= value[0]) & (tokenCounts_df['Nº tokens'] <= value[1])].sample(n=20)	
        fig = go.Figure()
        fig.add_trace(go.Bar(x= filtered_df['Nº tokens'], y= filtered_df['Wikipedia article'], orientation='h', marker_color='#A349A4', name = "Wikipedia article"))
        fig.add_vline(x=float(R.es_stats[44]), line_width=4, line_color="#77C14C") # Mean
        fig.add_vline(x=float(R.es_stats[45]), line_width=4, line_color="#1FAFEE") # Median
        fig.add_vline(x=float(R.es_stats[46]), line_width=4, line_color="#D53614") # Standard deviation
        fig.add_traces([
         go.Scatter(x=[float(R.es_stats[44])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.es_stats[44]], hoverinfo="text"),
         go.Scatter(x=[float(R.es_stats[45])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[45]], hoverinfo="text"),
         go.Scatter(x=[float(R.es_stats[46])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.es_stats[46]], hoverinfo="text")
         ])
        fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Number of tokens", yaxis_title="Wikipedia article")
        return fig                 

# Spanish known types position measures callback
     @app.callback(
            dash.dependencies.Output('es_known_types_pos', 'figure'),
            [dash.dependencies.Input('ontology_pos', 'clickData')]
            )
     def es_update_inits_bar_pos(clicked_data):
            if clicked_data is None:
                return dash.no_update
            selected_type = clicked_data['points'][0]['label'] 
            if selected_type in R.known_types_es["DBpedia type"].values:
                selected_row = R.known_types_es[R.known_types_es["DBpedia type"] == selected_type]
                fig = go.Figure(go.Bar(x = [selected_row.iloc[0]['Pos']], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            else:
                fig = go.Figure(go.Bar(x = [0], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            
            fig.add_vline(x=int(R.es_stats[14]), line_width=4, line_color="#77C14C") # 10th percentile
            fig.add_vline(x=int(R.es_stats[11]), line_width=4, line_color="#1FAFEE") # 1st quartile
            fig.add_vline(x=int(R.es_stats[22]), line_width=4, line_color="#D53614") # 50th percentile
            fig.add_vline(x=int(R.es_stats[12]), line_width=4, line_color="#D59D14") # 3rd quartile
            fig.add_vline(x=int(R.es_stats[30]), line_width=4, line_color="#FFA4F5") # 90th percentile
            fig.add_vline(x=int(R.es_stats[32]), line_width=4, line_color="#FFFB0B") # 95th percentile
    
            fig.add_traces([
            go.Scatter(x=[int(R.es_stats[14])], y= [" "], mode='lines', name='10th percentile', line=dict(color="#77C14C"), hovertext=[R.es_stats[14]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[11])], y= [" "], mode='lines', name='1st quartile', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[11]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[22])], y= [" "], mode='lines', name='50th percentile', line=dict(color="#D53614"), hovertext=[R.es_stats[22]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[12])], y= [" "], mode='lines', name='3rd quartile', line=dict(color="#D59D14"), hovertext=[R.es_stats[12]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[30])], y= [" "], mode='lines', name='90th percentile', line=dict(color="#FFA4F5"), hovertext=[R.es_stats[30]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[32])], y= [" "], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"), hovertext=[R.es_stats[32]], hoverinfo="text")
            ])
    
            fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=700, xaxis_title="Number of DBpedia types", yaxis_title="DBpedia type")
            return fig
        
# English known types callback
     @app.callback(
            dash.dependencies.Output('en_known_types', 'figure'),
            [dash.dependencies.Input('en_ontology', 'clickData')]
            )
     def en_update_known_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.known_types_en
            ontology_df = R.get_ontology_df()
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
            figure.add_vline(x=float(R.en_stats[6]), line_width=4, line_color="#77C14C") # Mean
            figure.add_vline(x=float(R.en_stats[7]), line_width=4, line_color="#1FAFEE") # Median
            figure.add_vline(x=float(R.en_stats[9]), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
                go.Scatter(x=[float(R.en_stats[6])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.en_stats[6]], hoverinfo="text"),
                go.Scatter(x=[float(R.en_stats[7])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[7]], hoverinfo="text"),
                go.Scatter(x=[float(R.en_stats[9])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.en_stats[9]], hoverinfo="text")
                ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        
 # English instance types callback
     @app.callback(
            dash.dependencies.Output('en_instance_types', 'figure'),
            [dash.dependencies.Input('en_ontologyy', 'clickData')]
            )
     def en_update_instance_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.get_instance_types_df(R.en_dashboard_directory)
            ontology_df = R.get_ontology_df()
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        

# English uriCounts callback
     @app.callback(
        dash.dependencies.Output('en_uriCounts_graph', 'figure'),
        [dash.dependencies.Input('en_uriCounts_slider', 'value')])
     def en_update_uriCounts_figure(value):
        uriCounts_df = R.uriCounts_en
        filtered_df = uriCounts_df[(uriCounts_df['Count'] >= value[0]) & (uriCounts_df['Count'] <= value[1])].sample(n=20)	
        fig = go.Figure()
        fig.add_trace(go.Bar(x= filtered_df['Count'], y= filtered_df['DBpedia entity'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
        fig.add_vline(x=float(R.en_stats[35]), line_width=4, line_color="#77C14C") # Mean
        fig.add_vline(x=float(R.en_stats[36]), line_width=4, line_color="#1FAFEE") # Median
        fig.add_vline(x=float(R.en_stats[38]), line_width=4, line_color="#D53614") # Standard deviation
        fig.add_traces([
        go.Scatter(x=[float(R.en_stats[35])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.en_stats[35]], hoverinfo="text"),
        go.Scatter(x=[float(R.en_stats[36])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[36]], hoverinfo="text"),
        go.Scatter(x=[float(R.en_stats[38])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.en_stats[38]], hoverinfo="text")
        ])
        fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times appearing in Wikipedia dump", yaxis_title="DBpedia entity")
        return fig    
   

# English pairCounts callback
     @app.callback(
        dash.dependencies.Output('en_pairCounts_graph', 'figure'),
        [dash.dependencies.Input('en_pairCounts_slider', 'value')])
     def en_update_pairCounts_figure(value):
        pairCounts_df = R.pairCounts_en
        filtered_df = pairCounts_df[(pairCounts_df['Times linked'] >= value[0]) & (pairCounts_df['Times linked'] <= value[1])].sample(n=20)	
        fig = go.Figure()
        fig.add_trace(go.Bar(x= filtered_df['Times linked'], y= filtered_df['Surface form'], orientation='h', marker_color='#A349A4', name = "Surface form"))
        fig.add_vline(x=float(R.en_stats[39]), line_width=4, line_color="#77C14C") # Mean
        fig.add_vline(x=float(R.en_stats[40]), line_width=4, line_color="#1FAFEE") # Median
        fig.add_vline(x=float(R.en_stats[42]), line_width=4, line_color="#D53614") # Standard deviation
        fig.add_traces([
       go.Scatter(x=[float(R.en_stats[39])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.en_stats[39]], hoverinfo="text"),
        go.Scatter(x=[float(R.en_stats[40])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[40]], hoverinfo="text"),
        go.Scatter(x=[float(R.en_stats[42])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.en_stats[42]], hoverinfo="text")
        ])
        fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times linked to a DBpedia entity", yaxis_title="Surface form")
        return fig           
      
# English sfAndTotalCounts callback
     @app.callback(
        dash.dependencies.Output('en_sfAndTotalCounts_graph', 'figure'),
        [dash.dependencies.Input('en_sfAndTotalCounts_slider', 'value')])
     def en_update_sfAndTotalCounts_figure(value):
        sfAndTotalCounts_df = R.sfAndTotalCounts_en
        filtered_df = sfAndTotalCounts_df[(sfAndTotalCounts_df['Times linked'] >= value[0]) & (sfAndTotalCounts_df['Times linked'] <= value[1])].sample(n=20)	
        fig = go.Figure()
        fig.add_trace(go.Bar(x= filtered_df['Times linked'], y= filtered_df['Surface form'], orientation='h', marker_color='#A349A4', name = "Surface form"))
        fig.add_vline(x=float(R.en_stats[52]), line_width=4, line_color="#77C14C") # Mean
        fig.add_vline(x=float(R.en_stats[53]), line_width=4, line_color="#1FAFEE") # Median
        fig.add_vline(x=float(R.en_stats[55]), line_width=4, line_color="#D53614") # Standard deviation
        fig.add_traces([
        go.Scatter(x=[float(R.en_stats[52])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.en_stats[52]], hoverinfo="text"),
        go.Scatter(x=[float(R.en_stats[53])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[53]], hoverinfo="text"),
        go.Scatter(x=[float(R.en_stats[55])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.en_stats[55]], hoverinfo="text")
        ])
        fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times linked to a DBpedia entity", yaxis_title="Surface form")
        return fig  

# English tokenCounts callback
     @app.callback(
        dash.dependencies.Output('en_tokenCounts_graph', 'figure'),
        [dash.dependencies.Input('en_tokenCounts_slider', 'value')])
     def en_update_tokenCounts_figure(value):
        tokenCounts_df = R.tokenCounts_en
        filtered_df = tokenCounts_df[(tokenCounts_df['Nº tokens'] >= value[0]) & (tokenCounts_df['Nº tokens'] <= value[1])].sample(n=20)	
        fig = go.Figure()
        fig.add_trace(go.Bar(x= filtered_df['Nº tokens'], y= filtered_df['Wikipedia article'], orientation='h', marker_color='#A349A4', name = "Wikipedia article"))
        fig.add_vline(x=float(R.en_stats[44]), line_width=4, line_color="#77C14C") # Mean
        fig.add_vline(x=float(R.en_stats[45]), line_width=4, line_color="#1FAFEE") # Median
        fig.add_vline(x=float(R.en_stats[46]), line_width=4, line_color="#D53614") # Standard deviation
        fig.add_traces([
         go.Scatter(x=[float(R.en_stats[44])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.en_stats[44]], hoverinfo="text"),
        go.Scatter(x=[float(R.en_stats[45])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[45]], hoverinfo="text"),
        go.Scatter(x=[float(R.en_stats[46])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.en_stats[46]], hoverinfo="text")
         ])
        fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Number of tokens", yaxis_title="Wikipedia article")
        return fig                         
    

# English known types position measures callback
     @app.callback(
            dash.dependencies.Output('en_known_types_pos', 'figure'),
            [dash.dependencies.Input('en_ontology_pos', 'clickData')]
            )
     def en_update_inits_bar_pos(clicked_data):
            if clicked_data is None:
                return dash.no_update
            selected_type = clicked_data['points'][0]['label'] 
            if selected_type in R.known_types_en["DBpedia type"].values:
                selected_row = R.known_types_en[R.known_types_en["DBpedia type"] == selected_type]
                fig = go.Figure(go.Bar(x = [selected_row.iloc[0]['Pos']], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            else:
                fig = go.Figure(go.Bar(x = [0], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            
            fig.add_vline(x=int(R.en_stats[14]), line_width=4, line_color="#77C14C") # 10th percentile
            fig.add_vline(x=int(R.en_stats[11]), line_width=4, line_color="#1FAFEE") # 1st quartile
            fig.add_vline(x=int(R.en_stats[22]), line_width=4, line_color="#D53614") # 50th percentile
            fig.add_vline(x=int(R.en_stats[12]), line_width=4, line_color="#D59D14") # 3rd quartile
            fig.add_vline(x=int(R.en_stats[30]), line_width=4, line_color="#FFA4F5") # 90th percentile
            fig.add_vline(x=int(R.en_stats[32]), line_width=4, line_color="#FFFB0B") # 95th percentile
    
            fig.add_traces([
            go.Scatter(x=[int(R.en_stats[14])], y= [" "], mode='lines', name='10th percentile', line=dict(color="#77C14C"), hovertext=[R.en_stats[14]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[11])], y= [" "], mode='lines', name='1st quartile', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[11]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[22])], y= [" "], mode='lines', name='50th percentile', line=dict(color="#D53614"), hovertext=[R.en_stats[22]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[12])], y= [" "], mode='lines', name='3rd quartile', line=dict(color="#D59D14"), hovertext=[R.en_stats[12]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[30])], y= [" "], mode='lines', name='90th percentile', line=dict(color="#FFA4F5"), hovertext=[R.en_stats[30]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[32])], y= [" "], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"), hovertext=[R.en_stats[32]], hoverinfo="text")
            ])
    
            fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=700, xaxis_title="Number of DBpedia types", yaxis_title="DBpedia type")
            return fig
        