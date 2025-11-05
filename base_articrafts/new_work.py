## Sample file to check if any manual formatting is applied in the dashboard.


## get the location of the definition folder for the dashboard

## iterate through all the pages and visuals and check for the objects in the jsons

import os
import json

visuals = ["pieChart",
           "barChart",
           "lineChart",
           "columnChart",
           "pivotTable",
           "tableEx",
           "card",
           "kpi",
           "slicer",
           "lineStackedColumnComboChart",
           "lineClusteredColumnComboChart",
           "donutChart",
           "scatterChart"]


def find_json_files(directory):
    json_files = []
    
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        # Filter out json files
        for file in files:
            if file == 'visual.json':
                with open(os.path.join(root,file),"r") as visual_json :
                    data = json.load(visual_json)
                if data["visual"]["visualType"] in visuals:
                    json_files.append(os.path.join(root, file))
    
    return json_files

# Define your folder path
folder_path = r"C:\Nahdi-articrafts\TEST_SAMPLE.Report\definition"

# Get the list of json files
json_files = find_json_files(folder_path)



# Print the found json files
for json_file in json_files:
    print(json_file)

