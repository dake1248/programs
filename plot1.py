import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import numpy as np


dates=pd.date_range('20111117',periods=10)
df=pd.DataFrame(np.random.randn(10,6),index=dates,columns=list('ABCDEF'))
print(df)
df1=pd.DataFrame(np.random.randn(10,1),index=dates)
fig=px.line(df1,x=df1.index,y='confirmed')
fig.show()
