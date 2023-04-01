# -*- coding: utf-8 -*-
"""Plotly_Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bsKT-XW0IvkbxPW5tELHhjTeiJc-j5qE

Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
scatter plot for age and fare columns in the titanic dataset.
"""

import seaborn as sns

import plotly.express as px

titanic=sns.load_dataset('titanic')

titanic

px.scatter(titanic,x='age',y='fare',title="Age Vs Fare Scatter Plot")

"""Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express."""

tips=px.data.tips()

tips

px.box(tips,x='total_bill',title='Box Plot of Total Bills')

px.box(tips,x='tip',title='Box plot of Tips Given')

"""Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
column with the color parameter.
"""

px.histogram(tips,x='sex',y='total_bill',pattern_shape='smoker',color='day')



"""Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
the color parameter.
"""

iris=px.data.iris()

iris

px.scatter_matrix(iris,dimensions=['sepal_length','sepal_width','petal_length','petal_width'],color='species',symbol='species',title="Scatter Plot of Iris Species")



"""Q5. What is Distplot? Using Plotly express, plot a distplot."""

## Distplot is a distribution plot and show how the data is distributed and depicts variation in the dataset

px.histogram(iris,x='sepal_length',color='species')

