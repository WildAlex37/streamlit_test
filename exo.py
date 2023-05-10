import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import time

st.title("Voici le résultat de l'exercice d'analyse sur le dataset Cars :")

st.write("En premier lieu, ci dessous le DataFrame :")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

#Datetime year :

df['year'] = df['year'].replace(',','')
df['year'] = df['year'].apply(lambda x: pd.to_datetime(str(x), format='%Y'))


df['year'] = df['year'].dt.year
                                    
# Here we use "magic commands":

st.write("Ci dessous une matrice de correlation")

viz_correlation = sns.heatmap(df.corr(), 
center=0,
cmap = sns.color_palette("vlag", as_cmap=True))

st.write("Les variables les plus correlées positivement sont : MPG et Year, et MPG et time-to-60")
st.write("Les variables les plus correlées négativement sont : MPG et cylinders,MPG et cubininches, MPG et hp, MPG et weightlbs")

st.pyplot(viz_correlation.figure)

st.write("Evolution des Mpg par année :")

colorize = st.selectbox('Sélectionnez un continent', df['continent'].unique())
fig = px.scatter(df[df['continent'] == colorize], x='year', y='mpg', color='continent')
st.plotly_chart(fig)

st.markdown('**Conclusion** :')
st.markdown("l'évolution  : des MPG des véhicules s'est généralisée d'un continent à l'autre, avec une plus forte intensité pour le :red[**Japon**] et :red[**l'Europe**]")