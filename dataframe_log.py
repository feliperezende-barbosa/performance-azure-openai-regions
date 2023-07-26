import plotly.express as px
import pandas as pd
import statsmodels.api

df = pd.read_csv('./Logs/25-07-2023 21-09-42.log', 
                 delimiter=';', 
                 names = ['Status', 
                          'Region', 
                          'Sample', 
                          'Response_openai_s', 
                          'Request_Duration_s', 
                          'Prompt Size', 
                          'Completion Size'
                          ], 
                 header=1
                 )

df.head()

scat = px.scatter(df, 
                 x='Completion Size', 
                 y='Response_openai_s', 
                 symbol='Region', 
                 color='Region', 
                 trendline='ols', 
                 title='OpenAI Completion Size vs Request Duration (s)', 
                 labels={'Completion Size':'Completion Size (tokens)', 'Response_openai_s':'Request Duration (s)'}
                 )

scat.show()

histg1 = px.histogram(df, 
                    x='Region', 
                    y='Response_openai_s', 
                    color='Status', 
                    barmode='group', 
                    histfunc='avg', 
                    title='OpenAI Request Duration (s) by Region',
                    text_auto=True)
histg1.show()

histg = px.histogram(df, 
                    x='Region', 
                    y='Status', 
                    color='Status', 
                    barmode='stack', 
                    histfunc='count', 
                    title='OpenAI Success and Error by Region',
                    text_auto=True)
                    
histg.show()        


print(df.query('Status == "SUCCESS"')['Response_openai_s'].groupby(df['Region']).describe())
