import plotly.express as px
import pandas as pd
import statsmodels.api

# This file contains code to read a log file and create scatter and histogram plots using plotly.express library. 
# The scatter plot shows the relationship between the completion size and the request duration for each region. 
# The histogram plots show the request duration and success/error count for each region. 
# The log file is read using pandas library and the plots are created using plotly.express library.

#variable to read the log file and its columns
df = pd.read_csv('./Logs/27-07-2023 14-40-35.log', 
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

#variable to create a scatter graph
scat = px.scatter(df, 
                 x='Completion Size', 
                 y='Response_openai_s', 
                 symbol='Region', 
                 color='Region', 
                 trendline='ols', 
                 title='OpenAI Completion Size vs Request Duration (s)', 
                 labels={'Completion Size':'Completion Size (tokens)', 'Response_openai_s':'Request Duration (s)'}
                 )
#plot the scatter
scat.show()

#variable to create a histogram graph
histg_avg = px.histogram(df, 
                    x='Region', 
                    y='Response_openai_s', 
                    color='Status', 
                    barmode='group', 
                    histfunc='avg', 
                    title='OpenAI Request Duration (s) by Region',
                    labels={'Response_openai_s':'Request Duration (s)'},
                    text_auto=True)
#Plot the histogram
histg_avg.show()

histg = px.histogram(df, 
                    x='Region', 
                    y='Status', 
                    color='Status', 
                    barmode='stack', 
                    histfunc='count', 
                    title='OpenAI Success and Error by Region',
                    text_auto=True)
                    
histg.show()        

#print the statistics of the dataframe
print(df.query('Status == "SUCCESS"')['Response_openai_s'].groupby(df['Region']).describe())