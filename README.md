# Survive your commuting

# Abstract
Road traffic safety is a major societal issue costing up to 4% of a country's GNP, while traffic crashs are said to become the fifth leading cause of death by 2030. The 2017 European Commission Fact sheet  shows how the United Kingdom is a leader in road safety with 27 fatalities per millions of habitants while France stands slightly above average with 57. 
What’s more, the United Kingdom provides their traffic reports for the past 30 years, what can it tell about the implementation of road safety policies ? Can this data explain the gap between France and Uk ? While it is well known that the majority of road accidents happens while commuting, we strongly believe there is much more to know about the circumstances and the reasons of road accidents. 
Therefore, our goal is to extract information from the UK dataset to highlight the consequences of the implementation of several policies related to road safety, enabling us to provide directives to follow the lead of the UK.

# Research questions
- What are the major risk factors? 
- How could they be attenuated?
- To what extent is it more dangerous in urban areas?
- Can we predict the consequences of a car crash given its initial condition (speed, vehicles involved, type of road...)?
- What policies implemented in our role model country, the UK, could be implemented in France in order to decrease death casualties there?

# Dataset

We found three datasets consistent with our goal, and we decided to use the one provided by the United Kingdom. The three of them have a great list of features but only UK provides a massive amount of data for many different years.

- **UK dataset:**  From year 1979 to current. Available at https://data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data
- **France dataset:** Only 60.000 entries, for 2015. But help on the website. Available at https://data.opendatasoft.com/explore/dataset/accidents-corporels-circulation-2015%40public/
- **Geneva canton dataset:** 22.000 entries from 2010 to december 2017. Available at https://ge.ch/sitg/fiche/8139

For each year, the entries are divided in three datasets, one for the accident, one for the casualties and a last one for the vehicles make and model. Those three datasets are linked by an Accident_index. For instance, the 2014 UK casualties dataset contains the following entries: Accident_Index, Location_Easting_OSGR, Location_Northing_OSGR, Longitude, Latitude, Police_Force, Accident_Severity, Number_of_Vehicles, Number_of_Casualties, Date, Day_of_Week,Time, Local_Authority_(District) Local_Authority_(Highway), 1st_Road_Class, 1st_Road_Number, Road_Type, Speed_limit, Junction_Detail, Junction_Control, 2nd_Road_Class, 2nd_Road_Number, Pedestrian_Crossing-Human_Control, Pedestrian_Crossing-Physical_Facilities, Light_Conditions, Weather_Conditions, Road_Surface_Conditions, Special_Conditions_at_Site, Carriageway_Hazards, Urban_or_Rural_Area, Did_Police_Officer_Attend_Scene_of_Accident, LSOA_of_Accident_Location. Most columns are categorical and all the data variables are coded rather than containing textual strings and a "lookup table" is provided. Thus, making the data science work much easier.

# A list of internal milestones up until project milestone 2
- **Clean** the UK dataset for the past 10 years.
- **Visualize** the data using plots and maps (_matplolib_ and _folium_) to get to know the data.
- **Detect** correlations and trends between features such as the frequency, the weather the gravity etc. 
- **Identify and quantify** the impact of several road safety related policies specific to the UK.
