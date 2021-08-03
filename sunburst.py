import plotly.express as px
import plotly
import pandas as pd 
import numpy as np
 
df= pd.read_csv("worldpop.csv")


Country = df["country"]
Pop = df["pop"]
Continent = df["continent"]
LifeExp = df["lifeExp"]
GdpPercap = df["gdpPercap"]

fig=px.sunburst(df,
				path=[Continent,Country,LifeExp],
				values=Pop,
				color=LifeExp,
				color_continuous_scale='RdBu',
				title="Interactive world Population sunburst",
				color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']),
				hover_name="lifeExp"
				)
fig.update_layout(
				title_font_family="Arial",
				title_font_size=42,
				margin = dict(t=50, l=25, r=25, b=25)
				)
plotly.offline.plot(fig,filename="chart.html")