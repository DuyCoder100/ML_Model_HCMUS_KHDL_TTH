#!/usr/bin/env python
# coding: utf-8

# In[331]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import style

sns.set(style = "darkgrid")

#Getting Data
mcp_df = pd.read_csv('D:/insurance.csv')


#Data exploration
mcp_df.info()
mcp_df.describe()

#Checking missing Data
mcp_df.isnull().sum()

mcp_df.head(10)

#Separate sex
male = mcp_df[mcp_df['sex']=='male']
female = mcp_df[mcp_df['sex']=='female']
mcp_df['sex'].value_counts()

#Checking region
mcp_df['region'].value_counts()

#Checking Children
mcp_df['children'].value_counts()

#Plotting
#1. Age
sns.displot(mcp_df['age'])
plt.title('Age')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()

#2. Sex distribution
sns.countplot(data = mcp_df, x = 'sex')
plt.title('Male vs Female')
plt.show()

#3. BMI
sns.displot(mcp_df['bmi'], kde = True)
plt.title('BMI')
plt.xlabel('BMI')
plt.ylabel('Density')
plt.show()

#4. Children distribution
sns.countplot(mcp_df['children'])
plt.title('Children distribution')
plt.xlabel('Children')
plt.ylabel('Density')
plt.show()

#5. Charges
sns.displot(mcp_df['charges'], bins = 30)
plt.title('Charges')
plt.xlabel('Charges')
plt.ylabel('Density')
plt.show()

#6. Regions distribution
labels = ['South East','North West','South West','North East']
plt.figure(figsize=(10,6))
plt.pie(mcp_df['region'].value_counts(),labels=labels, autopct = '%1.3f%%')
plt.title('Regions')
plt.show()

#7. BMI vs Age with 2 groups
plt.figure(figsize=(10,6))
sns.lineplot(data = mcp_df, x = 'age', y = 'bmi', hue = 'sex' )
plt.xlabel('Age')
plt.ylabel('BMI')
plt.title('BMI across Ages')
plt.show()

#8.1. BMI vs Charges with 2 groups of sex
plt.figure(figsize=(10,6))
sns.jointplot(data = mcp_df, x = 'bmi', y = 'charges', hue = 'sex')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.title('Charges across BMI')
plt.show()

#8.2. BMI vs Charges with 2 groups of smoker
plt.figure(figsize=(10,6))
sns.jointplot(data = mcp_df, x = 'bmi', y = 'charges', hue = 'smoker')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.title('Charges across BMI')
plt.show()

#9. Region vs Charges with 2 groups
plt.figure(figsize=(10,6))
sns.boxplot(data = mcp_df, x = 'region', y = 'charges', hue = 'sex')
plt.xlabel('Region')
plt.ylabel('Charges')
plt.title('Charges across Regions')
plt.show()

#10. Children vs Charges
plt.figure(figsize=(10,6))
sns.boxplot(data = mcp_df, x = 'children', y = 'charges')
plt.xlabel('Children')
plt.ylabel('Charges')
plt.title('Charges across Childrens per family have')
plt.show()

#11. Pair plot
fig = plt.figure(figsize = (10, 6))
sns.pairplot(mcp_df, height = 2.5, y_vars = ['charges']);
plt.show()





