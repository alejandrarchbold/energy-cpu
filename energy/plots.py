import pandas as pd
import plotly.express as px

df = pd.read_csv('output.csv')
df.info()
fig = px.line(df, x='TIME+', y="Energy", title='Energy vs time')
fig.show()
