#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:15:35 2018

@author: mlt

Library to download three datasets into a single pd dataframe for each category: accidents, casualties and vehicules.
It download the data for each dataset, then clean it by removing the NaN values that could create issues for data handling.
It also turn numerical  categorical data into categorical data by attributing their legends to each feature.
"""

#import
import os
import datetime
import pandas as pd
import numpy as np
        
def categorical_labels(df, LEGENDS):
    for col in list(set(LEGENDS.keys() & df.columns)):
        try:
            df[col].replace( list(LEGENDS[col]['code']), LEGENDS[col]['label'], inplace = True)
        except KeyError:
            df[col].replace( list(LEGENDS[col]['Code']), LEGENDS[col]['Label'], inplace = True)
            pass
    
    return df


def dl():
    """
    Returns three dataframe: accidents, casualties and vehicules.
    
    """
    #Global
    DATA_FOLDER = [
                   './data/Stats19-Data1979-2004/', 
                   './data/Stats19_Data_2005-2014/', 
                   './data/RoadSafetyData_2015/']
    
    #columns we want to extract from each file
    use_cols = [[#Space and time context
                'Date','Time', 'Longitude', 'Latitude','Day_of_Week',
                #Identifier
                'Accident_Index', 
                #Police force related
                'Police_Force', 'Local_Authority_(District)', 'Local_Authority_(Highway)','Did_Police_Officer_Attend_Scene_of_Accident',
                #Casualties
                'Accident_Severity', 'Number_of_Casualties','Number_of_Vehicles',
                #Road conditions and traffic signalisations
                '1st_Road_Class', '1st_Road_Number', 'Road_Type', 'Speed_limit', 'Junction_Detail', 'Junction_Control',
                '2nd_Road_Class', '2nd_Road_Number',
                #Pedestrian 
                'Pedestrian_Crossing-Human_Control', 'Pedestrian_Crossing-Physical_Facilities', 
                #Visibility and road conditions
                'Light_Conditions', 'Weather_Conditions', 'Road_Surface_Conditions', 'Special_Conditions_at_Site', 'Carriageway_Hazards',
                'Urban_or_Rural_Area', 
                #'Location_Easting_OSGR','Location_Northing_OSGR', 'LSOA_of_Accident_Location',
               ],
                #casualties
                ['Accident_Index', 'Age_Band_of_Casualty',
                 #'Age_of_Casualty', 
                 'Bus_or_Coach_Passenger', 'Car_Passenger',
                 'Casualty_Class', 'Casualty_Home_Area_Type', 
                 #'Casualty_IMD_Decile',
                 'Casualty_Reference', 'Casualty_Severity', 'Casualty_Type',
                 'Pedestrian_Location', 'Pedestrian_Movement',
                 'Pedestrian_Road_Maintenance_Worker', 'Sex_of_Casualty',
                 'Vehicle_Reference'],
                #vehicules
                ['Accident_Index', '1st_Point_of_Impact',
                 'Age_Band_of_Driver', 
                 #'Age_of_Driver', 
                 'Age_of_Vehicle','Driver_Home_Area_Type', 'Driver_IMD_Decile', 'Engine_Capacity_(CC)',
                 'Hit_Object_in_Carriageway', 'Hit_Object_off_Carriageway',
                 'Journey_Purpose_of_Driver', 'Junction_Location', 'Propulsion_Code',
                 'Sex_of_Driver', 'Skidding_and_Overturning', 'Towing_and_Articulation',
                 #'Vehicle_IMD_Decile', 
                 'Vehicle_Leaving_Carriageway',
                 'Vehicle_Location-Restricted_Lane', 'Vehicle_Manoeuvre',
                 'Vehicle_Reference', 'Vehicle_Type', 'Was_Vehicle_Left_Hand_Drive?']
            ]
    
    
    
    df_list = [[] for i in range(3)]

    #for every period
    print("Begin download...")
    for file in DATA_FOLDER[1:]:
        
        #for every dataset (accidents, casualties, vehicules)
        files = sorted([doc for doc in os.listdir(file) if ".xls" not in doc and doc != '.DS_Store'])
        for doc in files:
            print(doc)
            index = files.index(doc)
            if index == 0:
                df_list[index].append(pd.read_csv(file + doc, 
                                                  index_col= "Accident_Index",
                                                  parse_dates=['Date'],
                                                  dayfirst=True,
                                                  infer_datetime_format=True,
                                                  usecols = use_cols[index],
                                       ))
            else:
                df_list[index].append(pd.read_csv(file + doc,
                                                  usecols = use_cols[index],
                                       ))
    
    accidents = pd.concat(df_list[0], axis = 0, ignore_index = True)

    casualties = pd.concat(df_list[1], axis = 0, ignore_index = True)

    vehicules = pd.concat(df_list[2], axis = 0, ignore_index = True)
    
    accidents.Time = pd.to_datetime(accidents.Time, format='%H:%M')
    
    
    print("Begin cleaning...")
    #clean the data
    accidents = accidents[accidents.Latitude.notnull() & accidents.Longitude.notnull()]
    
    
    #features legends
    LEGENDS = pd.read_excel(DATA_FOLDER[0] + 'Road-Accident-Safety-Data-Guide-1979-2004.xls',
                            sheet_name = None,
                           )
    #modify legend names to match with df features
    for k in [k for k in LEGENDS.keys()]:
        LEGENDS[k.replace(' ', '_')] = LEGENDS.pop(k)
        
        
        df_list = [[] for i in range(3)]

    #modify legend names to match with df features
    for k in [k for k in LEGENDS.keys()]:
        LEGENDS[k.replace(' ', '_')] = LEGENDS.pop(k)
    
    #some exceptions
    LEGENDS['Weather_Conditions'] = LEGENDS.pop('Weather')
    LEGENDS['Bus_or_Coach_Passenger'] = LEGENDS.pop('Bus_Passenger')
    LEGENDS['Casualty_Home_Area_Type'] = LEGENDS.pop('Home_Area_Type')
    LEGENDS['Age_Band_of_Casualty'] = LEGENDS.pop('Age_Band')
    
    #let's map categorical data to their label:
    accidents = categorical_labels(accidents, LEGENDS)
    casualties = categorical_labels(casualties, LEGENDS)
    vehicules = categorical_labels(vehicules, LEGENDS)
    
    return accidents, casualties, vehicules