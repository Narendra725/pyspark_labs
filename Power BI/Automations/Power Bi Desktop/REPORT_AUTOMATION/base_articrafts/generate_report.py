from functions import *

report_structure = {
                    "Supplier": [ "FillPage" , "POs" , "OpenPOs","InventoryBalance" , "ShelfAvailability" , 
                                "Transactions" , "TransactionsData" , "Sales"] ,
                    "SupplierMetrics": [   "Data" , "IMF" ,"Return" ],
                    "SalesShare" : [ "Panel1"],
                    "FillRateDetails": ["Panel1"]
                   }

# Restructures the report chapters and pages. because the code fails if there are duplicate page names across chapters
# example : "FillPage" exists in both "Supplier" and "SupplierMetrics" chapters
display_names = { k: v[:] for k, v in report_structure.items() }

for key in report_structure.keys():
    for index,page in enumerate(report_structure[key]):
        occurrences = sum([1 for k in report_structure.keys() for p in report_structure[k] if p == page])
        if occurrences > 1:
            report_structure[key][index] = page + "_" + key


target_report_folder = r"C:\Nahdi-articrafts\REPORT_AUTOMATION\NewReport.Report"
base_folder = r"C:\Nahdi-articrafts\REPORT_AUTOMATION\base_articrafts"


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
        create_skeleton_for_page(page,display_names[chapter][report_structure[chapter].index(page)],pages)
        create_page_navigation(pages,page,page_navigation_data)
        create_chapter_buttons(chapter_button_visuals,pages,page)
        # print(GREEN+f"page : {chapter}/{page} created successfully"+RESET)
    # print(GREEN+f"chapter : {chapter} created successfully"+RESET)
    
        
