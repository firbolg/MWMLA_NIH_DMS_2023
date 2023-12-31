# -*- coding: utf-8 -*-
"""MWMLA_2023_NIH_DMS_Classes_Analysis

Code for creating visualizations included in lightning talk


"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")

df = pd.DataFrame([['1st','Overview',1,1,1],
                  ['2nd','Overview',12,1,2],

                   ['3rd','Overview',7,1,0],
                   ['4th','Overview',11,1,0],
                   ['1st','Workflow',15,1,0],

                   ['2nd','Workflow',4,1,0],

                   ['5th','Overview',.2,0,0],
                   ['3rd','Workflow',1,1,0],

                   ['4th','Workflow',.2,0,0],
                   ['5th','Workflow',8,1,0]],


                  columns=['#','interaction','people','time','demographic'])

# Draw a grouped barplot
g = sns.catplot(
    data=df, kind="bar",
    x="#", y="people", hue="interaction",
    errorbar="sd", palette="colorblind", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Class Sequence", "Total Number of Attendees")
g.legend.set_title("")

sns.set_theme(style="whitegrid")

df = pd.DataFrame([['1st','Overview',1,1,1,0,0,0],
                  ['2nd','Overview',12,1,6,5,0,1],

                   ['3rd','Overview',7,1,2,4,1,0],
                   ['4th','Overview',11,1,5,4,1,1],
                   ['1st','Workflow',15,1,8,4,1,2],

                   ['2nd','Workflow',4,1,1,3,0,0],

                   ['5th','Overview',.2,0,0,0,0,0],
                   ['3rd','Workflow',1,1,0,1,0,0],

                   ['4th','Workflow',.2,0,0,0,0,0],
                   ['5th','Workflow',8,1,5,2,0,1]],

#added .2 for zero attendee classes for visualization clarity
                  columns=['#','class','people','time','faculty', 'staff','students','other'])

# Draw a grouped barplot
g = sns.catplot(
    data=df, kind="bar",
    x="#", y="faculty", hue="class",
    errorbar="sd", palette="colorblind", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Class Sequence", "Number of Faculty Attendees")
g.legend.set_title("")

sns.set_theme(style="whitegrid")

df = pd.DataFrame([['1st','Overview',1,1,1,0,0,0],
                  ['2nd','Overview',12,1,6,5,0,1],

                   ['3rd','Overview',7,1,2,4,1,0],
                   ['4th','Overview',11,1,5,4,1,1],
                   ['1st','Workflow',15,1,8,4,1,2],

                   ['2nd','Workflow',4,1,1,3,0,0],

                   ['5th','Overview',.2,0,0,0,0,0],
                   ['3rd','Workflow',1,1,0,1,0,0],

                   ['4th','Workflow',.2,0,0,0,0,0],
                   ['5th','Workflow',8,1,5,2,0,1]],

#added .2 for zero attendee classes for visualization clarity
                  columns=['#','class','people','time','faculty', 'staff','students','other'])

# Draw a grouped barplot
g = sns.catplot(
    data=df, kind="bar",
    x="#", y="staff", hue="class",
    errorbar="sd", palette="colorblind", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Class Sequence", "Number of Staff Attendees")
g.legend.set_title("")

sns.set_theme(style="whitegrid")

df = pd.DataFrame([['1st','Overview',1,1,1,0,0,0],
                  ['2nd','Overview',12,1,6,5,0,1],

                   ['3rd','Overview',7,1,2,4,1,0],
                   ['4th','Overview',11,1,5,4,1,1],
                   ['1st','Workflow',15,1,8,4,1,2],

                   ['2nd','Workflow',4,1,1,3,0,0],

                   ['5th','Overview',.2,0,0,0,0,0],
                   ['3rd','Workflow',1,1,0,1,0,0],

                   ['4th','Workflow',.2,0,0,0,0,0],
                   ['5th','Workflow',8,1,5,2,0,1]],

                  #Added .2 for zero attendee classes for visualization clarity
                  columns=['#','class','people','time','faculty', 'staff','students','other'])

# Draw a nested barplot by species and sex
g = sns.catplot(
    data=df, kind="bar",
    x="#", y="students", hue="class",
    errorbar="sd", palette="colorblind", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Class Sequence", "Number of Student Attendees")
g.legend.set_title("")

df = pd.DataFrame({'Faculty': [1,6,2,5,8,1,0,0,0,5],
                   'Staff': [0,5,4,4,4,3,0,1,0,2],
                   'Students': [0,0,1,1,1,0,0,0,0,0],
                   'Other': [0,1,0,1,2,0,0,0,0,1]},
                  index=['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6',
                         'Class 7', 'Class 8', 'Class 9', 'Class 10'])


# create stacked bar chart for demographics
df.plot(kind='bar', stacked=True, color=['firebrick', 'skyblue', 'plum', 'darkgreen'])
# labels for x & y axis
plt.xlabel('RLML NIH DMS Classes Fall 2022-Summer 2023')
plt.ylabel('Total Number of Attendees')

# title of plot
plt.title('Demographics of Attendees')

# Make data
group_names=['>Half an Hour', '>One Hour', '>Two Hours']
group_size=[1,5,5]
subgroup_names=['', 'Review', 'Consult', 'Review', 'Consult', 'Review']
subgroup_size=[0,1,2,3,3,2]

# Create colors
a, b, c=[plt.cm.Blues, plt.cm.Greens, plt.cm.Purples]

# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.5, labels=group_names, colors=[a(0.8), b(0.8), c(0.8)] )
plt.setp( mypie, width=0.5, edgecolor='white')

# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.5-0.5, labels=subgroup_names, labeldistance=0.6,
                   colors=[a(0.5), a(0.5), b(0.3), b(0.5), c(0.5), c(0.3), a(0.5), a(0.4), a(0.3), b(0.2)])
plt.setp( mypie2, width=0.5, edgecolor='white')
plt.margins(0,0)

plt.show()

#BEFORE WORKFLOW CLASS ONLY
# Make data: I have 3 groups and 7 subgroups
group_names=['>Half an Hour (None)', '>One Hour', '>Two Hours']
group_size=[0,1,3]

# Create colors
a, b, c=[plt.cm.Blues, plt.cm.Greens, plt.cm.Purples]

# First Ring
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.5, labels=group_names, colors=[a(0.8), b(0.8), c(0.8)] )
plt.setp( mypie, width=1.0, edgecolor='white')


plt.show()

#AFTER WORKFLOW CLASS ONLY
# Make data: I have 3 groups and 7 subgroups
group_names=['>Half an Hour', '>One Hour', '>Two Hours']
group_size=[1,4,3]

# Create colors
a, b, c=[plt.cm.Blues, plt.cm.Greens, plt.cm.Purples]

# First Ring
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.5, labels=group_names, colors=[a(0.8), b(0.8), c(0.8)] )
plt.setp( mypie, width=1.0, edgecolor='white')


plt.show()

