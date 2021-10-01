"""Place such code in jupyter notebook"""

import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets

%matplotlib widget

url_death = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_deaths.csv"

url_age = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_deaths_age.csv"

url_inc = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_inc.csv"

table1 = pd.read_csv(url_death)

table2 = pd.read_csv(url_age)

table3 = pd.read_csv(url_inc)



# The names of column: "death malaria sex blablaxxxx" is too long....
#We add new column:"value", which stores the same values in "death malaria xxx ...rate". 
table1["value"] = table1["Deaths - Malaria - Sex: Both - Age: Age-standardized (Rate) (per 100,000 people)"]

#preparing the dataframe, removing all NAs and value = 0 observations
table1 = table1.dropna()
table1.drop(table1[table1["value"]==0].index, inplace = True) 

#add a new column to store the means of values in each year among all entities in different years: mean_rate
df_mean = table1.groupby("Year")["value"].mean()
year_list = [*range(1990, 2017)]

df_mean = list(df_mean)
dicy = dict(zip(year_list, df_mean))#store the year:values in dictionary


mean_rate = []
for i in range(0, len(table1)):
    j = list(table1["Year"])[i]
    mean_rate.append(dicy[j])
table1["year_mean_rate"] = mean_rate


#draw the plot, if two input entities are same, only output the second one:

def create_plot(entity1, entity2):
    if (entity1 == entity2):
            print("The two input entities are the same, only showing the second input entity")
    
    with plt.style.context("ggplot"):
        fig = plt.figure(figsize=(8,6))
        fig.clear()
        plt.plot(table1[table1.Entity == entity1].Year,
                 table1[table1.Entity == entity1].value,
                 'o-',
                 color = 'black'
                   )
        plt.plot(table1[table1.Entity == entity1].Year,
                 table1[table1.Entity == entity1].year_mean_rate,
                 'o-',
                 color = 'red')
        plt.plot(table1[table1.Entity == entity2].Year,
                 table1[table1.Entity == entity2].value,
                 'o-',
                 color = 'yellow'
                   )
        
        plt.legend([f"{entity1}", "Avg of DeathRate for all entities",\
                    f"{entity2}"], \
                   title = "CurrentEntity vs AvgForAll vs AvgInContinent")
        plt.xlabel("Year")
        plt.ylabel("Death rate/100,000 People")
        plt.title(f"The Death Rate of Malaria during Years")
        
widgets.interact(create_plot, entity1=sorted(set(table1.Entity)), entity2=sorted(set(table1.Entity)));



# table2  malaria_deaths_age.csv
#preparing the data frame
#removing all NAs and value = 0 observations
table2 = table2.dropna()
table2.drop(table2[table2["deaths"]==0].index, inplace = True) 

#reording the factor value, "age_group"
age = list(set(table2["age_group"]))
age = ['Under 5', '5-14', '15-49', '50-69', '70 or older']

# draw the plot
def create_plot2(entity):
    
    with plt.style.context("ggplot"):
        fig = plt.figure(figsize=(10,6))
        fig.clear()
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


#table3 /malaria_inc.csv
# The names of column: "Incidence of malaria (per 1,000 population at risk) 
#(per 1,000 population at risk)" is too long....
#We add new column:"value", which stores the same values in that column. 
table3["value"] = table3["Incidence of malaria (per 1,000 population at risk) (per 1,000 population at risk)"]

table3 = table3.dropna()
#remove all the rows contain 0 in value column.
table3.drop(table3[table3["value"]==0].index, inplace = True) 

#add a new column to store the means of values in each year among all entities: mean_INCIDENCErate
df3_mean = table3.groupby("Year")["value"].mean()
year_list3 = [2000, 2005, 2010, 2015]

df3_mean = list(df3_mean)
dicy3 = dict(zip(year_list3, df3_mean))



mean_INCrate = []
for i in range(0, len(table3)):
    Y = list(table3["Year"])[i]
    mean_INCrate.append(dicy3[Y])
table3["mean_INCIDENCErate"] = mean_INCrate

#adding new column: to store continent info
continent = []
for index,row in table3.iterrows():
    #indicate some special country name:
    if row["Entity"] == "Cote d'Ivoire":
        country_code = pc.country_name_to_country_alpha2('Ivory Coast', cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        continent.append(continent_name)
    elif row["Entity"] == "Democratic Republic of Congo":
        country_code = pc.country_name_to_country_alpha2('Congo', cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        continent.append(continent_name)
    elif row["Entity"] == "Timor":
        continent.append("AS")
    elif row["Entity"] == "World":
        continent.append("World")
    else:
        country_code = pc.country_name_to_country_alpha2(row["Entity"], cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        continent.append(continent_name)
table3["Conti"] = continent
table3

#draw the plot:
import pycountry_convert as pc

def create_plot4(year, continent):
    #set pic size
    fig = plt.figure(figsize=(8,8))
    fig.clear()
    
    #store the xlabel and ylabel values:
    country = []
    country_value = []
    for index,row in table3.iterrows():
        if row["Year"] == year and row["Conti"] == continent:
            country.append(row["Code"])
            country_value.append(row["value"])
    colors = np.random.rand(len(country),3)
    
    x = plt.barh(range(len(country_value)), country_value, tick_label=country, color = colors)
    plt.ylabel("Country Code")
    plt.xlabel("Incidence rate/100,000 People")
    plt.title(f"The Incidence Rate in conti{continent} and in year{year}")
    
    # add number for each bar:
    for rect in x:
        w = rect.get_width()
        plt.text(w, rect.get_y()+rect.get_height()/2, '%d' % int(w), ha='left', va='center')


#remove world conti:
cont = list(sorted(set(table3.Conti)))
cont.remove("World")

widgets.interact(create_plot4, year=sorted(set(table3.Year)), continent=cont);
