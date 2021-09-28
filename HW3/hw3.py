"""Place such code in jupyter notebook"""

import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
url_death = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_deaths.csv"

url_age = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_deaths_age.csv"

url_inc = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_inc.csv"

table1 = pd.read_csv(url_death)

table2 = pd.read_csv(url_age)

table3 = pd.read_csv(url_inc)

#table1:
# data sets preparation:
# The names of column: "death malaria sex blablaxxxx" is too long....
#We add new column:"value", which stores the same values in "death malaria xxx ...rate". 
table1["value"] = table1["Deaths - Malaria - Sex: Both - Age: Age-standardized (Rate) (per 100,000 people)"]

table1 = table1.dropna()
table1.drop(table1[table1["value"]==0].index, inplace = True) 

#add a new column to store the means of values in each year among all entities: mean_rate
df_mean = table1.groupby("Year")["value"].mean()
year_list = [*range(1990, 2017)]

df_mean = list(df_mean)
dicy = dict(zip(year_list, df_mean))


mean_rate = []
for i in range(0, len(table1)):
    Y = list(table1["Year"])[i]
    mean_rate.append(dicy[Y])
mean_rate
table1["mean_rate"] = mean_rate

#data visulization:
def create_plot(entity):
    
    with plt.style.context("ggplot"):
        fig = plt.figure(figsize=(8,6))
        
        plt.plot(table1[table1.Entity == entity].Year,
                 table1[table1.Entity == entity].value,
                 'o-',
                 color = 'black'
                   )
        plt.plot(table1[table1.Entity == entity].Year,
                 table1[table1.Entity == entity].mean_rate,
                 'o-',
                 color = 'red'
                   )
        plt.legend([f"{entity}", "Average of DeathRate for all entities"], title = "Entity vs Average")
        plt.xlabel("Year")
        plt.ylabel("Death rate/100,000 People")
        plt.title(f"The Death Rate of Malaria vs Year in {entity}")
        
widgets.interact(create_plot, entity=sorted(set(table1.Entity)));

#table2:
table2= table2.drop(columns= ["Unnamed: 0"])

#preparing the data frame
table2 = table2.dropna()
table2.drop(table2[table2["deaths"]==0].index, inplace = True) 

#reording the factor value:age
age = list(set(table2["age_group"]))
age = ['Under 5', '5-14', '15-49', '50-69', '70 or older']

#data visulization:
def create_plot2(entity):
    
    with plt.style.context("ggplot"):
        fig = plt.figure(figsize=(10,6))
        for i in range(0, len(age)):
            plt.plot(table2[(table2["entity"] == entity) & (table2["age_group"] == age[i])].year,
                     table2[(table2["entity"] == entity) & (table2["age_group"] == age[i])].deaths,
                     'o-')
        plt.grid(ls='--')
        plt.xlabel("Year")
        plt.ylabel("Death Cases")
        plt.legend(age, title = "Age Groups", loc='best')

        plt.title(f"The Death cases v.s. Year in {entity} for different age groups")
widgets.interact(create_plot2, entity=sorted(set(table2.entity)));

#table3:
# The names of column: "Incidence of malaria (per 1,000 population at risk) 
#(per 1,000 population at risk)" is too long....
#We add new column:"value", which stores the same values in that column. 
table3["value"] = table3["Incidence of malaria (per 1,000 population at risk) (per 1,000 population at risk)"]

table3 = table3.dropna()
#remove all the rows contain 0 in value column.
table3.drop(table3[table3["value"]==0].index, inplace = True) 

#add a new column to store the means of values in each year among all entities: mean_INCIDENCErate
df3_mean = table3.groupby("Year")["value"].mean()
year_list3 = [*range(1990, 2017)]

df3_mean = list(df3_mean)
dicy3 = dict(zip(year_list3, df3_mean))


mean_INCrate = []
for i in range(0, len(table3)):
    Y = list(table3["Year"])[i]
    mean_INCrate.append(dicy[Y])
mean_INCrate
table3["mean_INCIDENCErate"] = mean_INCrate

# data visulization:
def create_plot3(entity):
    
    with plt.style.context("ggplot"):
        fig = plt.figure(figsize=(8,6))
        
        plt.plot(table3[table3.Entity == entity].Year,
                 table3[table3.Entity == entity].value,
                 'o-',
                 color = 'black'
                   )
        plt.plot(table3[table3.Entity == entity].Year,
                 table3[table3.Entity == entity].mean_INCIDENCErate,
                 'o-',
                 color = 'red'
                   )
        plt.legend([f"{entity}", "Average of INCIDENCErate for all entities"], title = "Entity vs Average")
        plt.xlabel("Year")
        plt.ylabel("Incdidence rate/100,000 People")
        plt.title(f"The Death Rate of Malaria vs Year in {entity}")
        
widgets.interact(create_plot3, entity=sorted(set(table3.Entity)));