# Program obtains user input to provide a ranked list of universities, dependent
# on the users country preference, and which year they want the data from.

import pandas as pd


def GetData(fileName):
    return pd.read_csv(fileName, header=0, index_col="Name")


# Retrieving data from CSV
QSUniData = GetData("QSUniData.csv")

# Obtaining user university preferences
country_pref = input(
    "Which country would you like to go to university in? \nEnter nothing if you have no preference.\nPreference: ")
year_pref = int(input(
    "Enter which year's data you would like to use (2018-2022): "))

if year_pref not in range(2018, 2023):
    print("Invalid year, not in range of data. Try again.")
    vote_pref = input(
        "Enter which year's data you would like to use (2018-2022): ")

# Dealing with the case of no preference, printing top
# universities worldwide.
if country_pref == "":
    print("The top 5 universities in the world are:")
    num = 0
    for index, row in QSUniData.iterrows():
        if(row["Year"] == year_pref):
            num += 1
            print(num, index)
            if(num == 5):
                break

# Dealing with the case of there being no top-ranked univesities in
# preferred country.
# isin([country_pref,year_pref]):
elif country_pref not in (QSUniData["Country"].values):
    print("No top-ranked universities in your country")

# Searching for top universities in preferred country.
else:
    print("The top universities in your country are:")
    num = 0
    for index, row in QSUniData.iterrows():
        if(row["Country"] == country_pref and row["Year"] == year_pref):
            num += 1
            print(num, index)
