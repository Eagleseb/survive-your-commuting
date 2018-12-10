# Survive your commuting

# Abstract
Road traffic safety is a major societal issue costing up to 4% of a country's GNP, while traffic crashes are said to become the fifth leading cause of death by 2030. The 2017 European Commission Fact sheet shows how the United Kingdom is a leader in road safety with 27 fatalities per millions of habitants while France stands slightly above average with 57. 
What’s more, the United Kingdom provides their traffic reports for the past 30 years, what can it tell about the implementation of road safety policies ? Can this data explain the gap between France and the UK ? While it is well known that the majority of road accidents happens while commuting, can the figures prove it ?
Therefore, our goal is to extract information from the UK dataset to put common road safety beliefs into perspectives whether it is about driving conditions or the likelihood of being a casualty.

# Research questions
- What are the major risk factors?
- Who is more likely to be a casualty ?
- To what extent is it more dangerous in urban areas compared to rural ones?
- When and where is it safer to drive?

# Dataset

We found three datasets consistent with our goal, and we decided to use the one provided by the United Kingdom. The three of them have a great list of features but only UK provides a massive amount of data for many different years.

- **UK dataset:**  From year 1979 to current year. Available at https://data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data
- **France dataset:** Only 60.000 entries, for 2015. But help on the website. Available at https://data.opendatasoft.com/explore/dataset/accidents-corporels-circulation-2015%40public/
- **Geneva canton dataset:** 22.000 entries from 2010 to december 2017. Available at https://ge.ch/sitg/fiche/8139

For each year, the entries are divided in three datasets, one for the accident, one for the casualties and a last one for the vehicles manufacturer and model. Those three datasets are linked by an Accident_index. For instance, the 2014 UK casualties dataset contains the following entries: Accident_Index, Location_Easting_OSGR, Location_Northing_OSGR, Longitude, Latitude, Police_Force, Accident_Severity, Number_of_Vehicles, Number_of_Casualties, Date, Day_of_Week,Time, Local_Authority_(District) Local_Authority_(Highway), 1st_Road_Class, 1st_Road_Number, Road_Type, Speed_limit, Junction_Detail, Junction_Control, 2nd_Road_Class, 2nd_Road_Number, Pedestrian_Crossing-Human_Control, Pedestrian_Crossing-Physical_Facilities, Light_Conditions, Weather_Conditions, Road_Surface_Conditions, Special_Conditions_at_Site, Carriageway_Hazards, Urban_or_Rural_Area, Did_Police_Officer_Attend_Scene_of_Accident, LSOA_of_Accident_Location. Most columns are categorical and all the data variables are coded rather than containing textual strings and a "lookup table" is provided. Thus, making the data science work much easier.

# A list of internal milestones up until project milestone 2
- **Clean** the UK dataset for the past 10 years.
- **Visualize** the data using plots and maps (_matplolib_ and _folium_) to get to know the data.
- **Detect** correlations and trends between features such as the frequency, the weather, the severity etc. 
- **Identify and quantify** the impact of several road safety related policies specific to the UK 

# A list of internal milestones up until project milestone 3
- **Characterize** road accidents and their casualties 
- **Compare** with the conclusions of the official Government Reports (see links)
- **Analyse** press article to extract a few "common beliefs"
- **Assess** to what extent common beliefs are true, according to the data: fact checking

Link to UK government reports : https://www.gov.uk/government/statistics/reported-road-casualties-great-britain-annual-report-2015?fbclid=IwAR3pGOaw-wCVJHvLYdKPJQ8bWmITUVCVZRVZ8xycxDIlqP5uOvoxXpra0Lg
Some recent press articles about road safety:
- https://www.theguardian.com/world/2018/nov/23/little-evidence-20mph-speed-limit-cuts-casualties-says-uk-report?fbclid=IwAR18ujDDTfoV-LRqQ_rkgVaZwrI4wspRmyoGDLPW9JxFda6j0TB94181L9o
- https://www.forbes.com/sites/carltonreid/2018/11/21/uk-government-rolls-out-new-road-safety-measures-ignores-will-of-the-people/?fbclid=IwAR1et22jgFkddCAcVfzO2zb8xzTclekQOytvWBJ5NhIbgq2r_UbFIms05L4#51d9ae7457fa
