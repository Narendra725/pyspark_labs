from functions import *

report_structure = {
                    "Supplier": [ "FillPage" , "POs" , "OpenPOs","InventoryBalance" , "ShelfAvailability" , 
                                "Transactions" , "TransactionsData" , "Sales"] ,
                    "SupplierMetrics": [   "Data" , "IMF" ,"Return" ],
                    "SalesShare" : [ "Panel1"],
                    "FillRateDetails": ["Panel1"]

                   }


# "cards" : ["KPI","simpleCard"],
# "Tabular": ["Table","Matrix"],
# "P"


target_report_folder = r"C:\Nahdi-articrafts\01.MODEL_MIGRATION\Mydemo.Report"
base_folder = r"C:\Nahdi-articrafts\base_articrafts"


# basic setup 
initial_setup(target_report_folder,base_folder)

pages =target_report_folder+"\\definition\\pages"
# create a homepage 
create_homepage(report_structure,pages)

# create rest of the pages 

for chapter in report_structure.keys():
    chapter_button_visuals = get_chapter_button_visuals(report_structure)
    chapter_button_visuals = update_button_visuals_for_current_chapter(chapter_button_visuals,chapter)
    page_navigation_data = get_page_navigation_json(chapter,report_structure)
    for page in report_structure[chapter]:
        create_skeleton_for_page(page,pages)
        create_page_navigation(pages,page,page_navigation_data)
        create_chapter_buttons(chapter_button_visuals,pages,page)
        print(GREEN+f"page : {chapter}/{page} created successfully"+RESET)
    print(GREEN+f"chapter : {chapter} created successfully"+RESET)
        
