import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import numpy as np



data=dict(
    number=[10000,7000,4000,2000,1000],
    stage=['browse','follow','download','consult','deal'])
fig=px.funnel(data,x='number',y='stage')
#fig.show()


fig1=px.funnel_area(names=['1st stage','2nd stage','3rd stage','4th stage','5th stage'],
                    values=[10000,7000,5000,2000,1000])
#fig1.show()


iris=px.data.iris()
fig2=px.density_contour(iris,x='sepal_width',y='sepal_length',color='species')
#fig2.write_image('./2.png2.png')
#fig2.show()


#plor coordinate

'''
def confirm_class(x):
    if x<=50000:
        y='1'
    if 50000<x<=
'''

data1=[30,80,75,80,90,110,120]
country_list=['France','Germany','China','Japan','Korea','Tailand','Italy']
fig3=px.bar_polar(data1,country_list)
#fig3=px.bar_polar(data1,country_list,color_discrete_sequence=px.colors.sequential.Blugrn)
fig3.show()

fig4=px.scatter_polar(data1,country_list)
fig4.show()

fig5=px.line_polar(data1,country_list)
fig5.show()
    
df1=px.data.wind()
fig6=px.line_polar(df1,r="frequency",theta="direction",color="strength",line_close=True,
                   color_discrete_sequence=px.colors.sequential.Plasma_r)
fig6.show()

'''
from skimage import io
ima=io.imread('./2.png')
fig7=px.imshow(img)

fig7.show()
'''

