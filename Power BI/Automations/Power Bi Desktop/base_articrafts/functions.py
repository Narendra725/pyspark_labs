# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

print("********** Initializing the script **********")

import os
import json
import shutil

def get_chapter_button_pos(report_struct):
    btn_pos= {}
    z=1000
    x=1150

    for chapter in list(report_struct.keys())[::-1]:
        pos = {
                "height": 40,
                "width": 120,
                "x": 1150,
                "y": 11,
                "z": 4,
                "tabOrder": 4
                }
        pos["x"]=x
        pos["z"]=pos["tabOrder"] = z
        btn_pos[chapter]=pos
        x = x - 135   # to recalculate the horizontal position
        z = z + 100   # to recalculate the tab/layer order
    return btn_pos



def get_home_btn_pos(report_struct,chapter_btn_pos):
    pos = {
            "x": 498,
            "y": 3,
            "z": 3,
            "width": 70,
            "height": 57,
            "tabOrder": 3
        }
    



def get_module_btn_pos(report_struct):
    def change(x,y,z):
        return (304,y+83,z+500)
    def right(x,y,z):
        return (703,y,z+100)
    mod_btn_pos = {}
    i = 0
    x= 304
    y= 360
    z= 4000
    for chapter in report_struct.keys():
        pos =  {
                "x": 304,
                "y": 360,
                "z": 4000,
                "width": 270,
                "height": 70,
                "tabOrder": 4000
               }
        pos["x"]= x
        pos["y"]= y
        pos["z"]=pos["tabOrder"]=z
        mod_btn_pos[chapter]=pos
        if i % 2 == 0:
            x,y,z=right(x,y,z)
        else:
            x,y,z=change(x,y,z)
        i+=1
    return mod_btn_pos



def create_folder(folder_path):
   
    try:
        os.makedirs(folder_path, exist_ok=True)  # Create the directory if it doesn't exist
        print(GREEN + f"Folder creation successful: {folder_path.split('\\')[-1]}"+RESET)
    except Exception as e:
        print(RED+f" Couldn't create the Folder{folder_path.split('\\')[-1]}: {e}"+ RESET)



def read_json(file_path):
    try:
         with open(file_path,"r") as file:
            data = json.load(file)
         return data
    except Exception as e:
         print(RED+f"error reading json {file_path.split('\\')[-1]}"+RESET)




def create_or_replace_file(file_path,data):
    try:
         with open(file_path ,"w") as file :
            json.dump(data,file,indent=2)
         print(GREEN+fr"successfully updated file {file_path.split('\\')[-1]}"+RESET)
    except Exception as e:
        print(RED+f"An error occured while updating the file {file_path.split('\\')[-1]}: {e}" + RESET)




def delete_directory(directory):
    if os.path.isdir(directory):
        try:
            shutil.rmtree(directory)
            print(RED+f"Directory '{directory.split('\\')[-1]}' has been deleted."+RESET)
        except Exception as e:
            print(RED+f"An error occurred while deleting the directory {directory.split('\\')[-1]}: {e}"+RESET)
    else:
        print(RED+f"Directory '{directory.split('\\')[-1]}' does not exist."+RESET)




def copy_folder(source_folder, destination_folder):
    try:
        # Check if source folder exists
        if not os.path.isdir(source_folder):
            print(RED+f"Source folder '{source_folder.split('\\')[-1]}' does not exist."+ RESET)
            return
        
        # Ensure destination folder does not already exist
        if os.path.isdir(destination_folder):
            print(YELLOW+f"Destination folder '{destination_folder.split('\\')[-1]}' already exists."+RESET)
            return
        
        # Copy the entire folder to the destination
        shutil.copytree(source_folder, destination_folder)
        print(GREEN+f"Folder '{source_folder.split('\\')[-1]}' has been successfully copied to '{destination_folder.split('\\')[-1]}'."+RESET)
    
    except Exception as e:
        print(f"An error occurred while copying the folder: {e}")




def initial_setup(dstn_folder,source_folder):
    RegisteredResources_src = f"{source_folder}\\RegisteredResources"
    RegisteredResources_des= f"{dstn_folder}\\StaticResources\\RegisteredResources"
    delete_directory(RegisteredResources_des)
    # create_folder(RegisteredResources_des)
    copy_folder(RegisteredResources_src,RegisteredResources_des)
    pages = dstn_folder+"\\definition\\pages"

    delete_directory(pages)
    pages_data  = read_json(f"{source_folder}\\pages.json")
    report_data = read_json(f"{source_folder}\\report.json")

    create_folder(pages)
    create_or_replace_file(f"{dstn_folder}\\definition\\pages\\pages.json",pages_data)
    create_or_replace_file(f"{dstn_folder}\\definition\\report.json",report_data)
    return 




def create_skeleton_for_page(page_name,pages_folder):

    
    create_folder( f"{pages_folder}\\{page_name}")


    #update page information in the pages.json
    pages_data = read_json(f"{pages_folder}\\pages.json")
    
    pages_data["pageOrder"].extend([page_name])
    create_or_replace_file(f"{pages_folder}\\pages.json",pages_data)

    # create the json file for the page and store it in page.json from base_page json
    page_data = read_json(r"C:\Nahdi-articrafts\base_articrafts\report_page_jsons\page.json")
    page_data["displayName"] = page_name
    page_data["name"]         = page_name
    create_or_replace_file(f"{pages_folder}\\{page_name}\\page.json",page_data)

    # creating a page visuals 
    page_base_visuals = r"C:\Nahdi-articrafts\base_articrafts\report_page_jsons\visuals"
    page_visuals = f"{pages_folder}\\{page_name}\\visuals"
    create_folder(page_visuals)

    visuals = [ "LOGO_visual",
                "chapter_header",
                "dossier_name_box",
                "Home_button",
                "sub_header_box",
                "PageNavigation",
                "divider_line"
                ]
    for item in visuals :
        data = read_json(f"{page_base_visuals}\\{item}\\visual.json")
        create_folder(f"{page_visuals}\\{item}")
        create_or_replace_file(f"{page_visuals}\\{item}\\visual.json",data)
    return 





def create_page_navigation(pages_folder,page_name,data):
    create_folder(f"{pages_folder}\\{page_name}\\visuals\\PageNavigation")
    create_or_replace_file(f"{pages_folder}\\{page_name}\\visuals\\PageNavigation\\visual.json",data)
    return




def get_chapter_button_json(data,is_current_chapter,dis_name,l_name,dstn ):

    normal ="'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"
    semi_bold = "'''Segoe UI Semibold'', wf_segoe-ui_semibold, helvetica, arial, sans-serif'"
    bold = "'''Segoe UI Bold'', wf_segoe-ui_bold, helvetica, arial, sans-serif'"

    # default state 
    def_color ="'#FFFFFF'"
    def_font = normal
    def_transparency  ="0D"
    active_chapter_color = "'#BAD3CE'"
    active_chapter_font  = semi_bold
    if is_current_chapter:
        def_color = active_chapter_color
        def_font = active_chapter_font
        def_transparency  ="0D"


        #font
        data["visual"]["objects"]["text"][1]["properties"]["fontFamily"]["expr"]["Literal"]["Value"] = def_font
        # is bold
        data["visual"]["objects"]["text"][1]["properties"]["bold"]["expr"]["Literal"]["Value"] = "false"
        # fill colour
        data["visual"]["objects"]["fill"][1]["properties"]["fillColor"]["solid"]["color"]["expr"]["Literal"]["Value"] = def_color
        data["visual"]["objects"]["fill"][1]["properties"]["transparency"]["expr"]["Literal"]["Value"] = def_transparency
        
        return data


    


    # hover state 
    hover_colour = "'#0F9797'"
    hov_transparency ="70D"

    # press state 
    press_colour = "'#0F9797'"
    pre_transparency ="0D"


    if l_name:
        data["name"] = l_name
    

    #font
    data["visual"]["objects"]["text"][1]["properties"]["fontFamily"]["expr"]["Literal"]["Value"] = def_font
    # is bold
    data["visual"]["objects"]["text"][1]["properties"]["bold"]["expr"]["Literal"]["Value"] = "false"
    # fill colour
    data["visual"]["objects"]["fill"][1]["properties"]["fillColor"]["solid"]["color"]["expr"]["Literal"]["Value"] = def_color
    data["visual"]["objects"]["fill"][1]["properties"]["transparency"]["expr"]["Literal"]["Value"] = def_transparency

    
    #font
    data["visual"]["objects"]["text"][2]["properties"]["fontFamily"]["expr"]["Literal"]["Value"] = semi_bold
    # is bold
    data["visual"]["objects"]["text"][2]["properties"]["bold"]["expr"]["Literal"]["Value"] = "false"
    # fill colour
    data["visual"]["objects"]["fill"][2]["properties"]["fillColor"]["solid"]["color"]["expr"]["Literal"]["Value"] = hover_colour
    data["visual"]["objects"]["fill"][2]["properties"]["transparency"]["expr"]["Literal"]["Value"] = hov_transparency

    
    #font
    data["visual"]["objects"]["text"][3]["properties"]["fontFamily"]["expr"]["Literal"]["Value"]= bold
    # is bold
    data["visual"]["objects"]["text"][3]["properties"]["bold"]["expr"]["Literal"]["Value"] = 'true'
    # fill colour
    data["visual"]["objects"]["fill"][3]["properties"]["fillColor"]["solid"]["color"]["expr"]["Literal"]["Value"] = press_colour
    data["visual"]["objects"]["fill"][3]["properties"]["transparency"]["expr"]["Literal"]["Value"] = pre_transparency


    if l_name:
        # layer_name
        data["visual"]["visualContainerObjects"]["title"][0]["properties"]["text"]["expr"]["Literal"]["Value"] = f"'{l_name}'"
    if dis_name:
        # display_name_for_button
        data["visual"]["objects"]["text"][1]["properties"]["text"]["expr"]["Literal"]["Value"] = f"'{dis_name}'"

    if dstn:
        # navigation to
        data["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["navigationSection"]["expr"]["Literal"]["Value"] = f"'{dstn}'"
    
    return data




def get_page_navigation_json(chapter_name,report_struct):
    base_page_navigation = r"C:\Nahdi-articrafts\base_articrafts\report_page_jsons\visuals\PageNavigation\visual.json"
    
    pages=[]
    # find the required pages 
    for page in report_struct[chapter_name]:
        page_schema = {
          "properties": {
            "showPage": {
              "expr": {
                "Literal": {
                  "Value": "true"
                }
              }
            }
          },
          "selector": {
            "id": ""
          }
        }
        page_schema["selector"]["id"]= page
        pages.append(page_schema)
    data=read_json(base_page_navigation)
    data["visual"]["objects"]["pages"].extend(pages)
    return data




def get_chapter_button_visuals(report_struct):
    chapter_button_visual_jsons = {}
    btn_pos = get_chapter_button_pos(report_struct)
    
    for chapter in report_struct.keys():
        base_chapter_button_json = read_json(r"C:\Nahdi-articrafts\base_articrafts\report_page_jsons\visuals\chapter_button\visual.json")
        data = get_chapter_button_json(base_chapter_button_json,False,chapter,chapter,report_struct[chapter][0])
        data["position"]=btn_pos[chapter]
        chapter_button_visual_jsons[chapter] = data
    return chapter_button_visual_jsons

def update_button_visuals_for_current_chapter(visuals_dict,chapter):
    visuals_dict[chapter] = get_chapter_button_json(visuals_dict[chapter],True,False,False,False)
    return visuals_dict

def create_chapter_buttons(visuals_dict,pages,page_name):
    for button in visuals_dict.keys():
        create_folder(f"{pages}\\{page_name}\\visuals\\{button}")
        create_or_replace_file(f"{pages}\\{page_name}\\visuals\\{button}\\visual.json",visuals_dict[button])

def create_homepage(report_struct,pages_folder):
    base_loc = r"C:\Nahdi-articrafts\base_articrafts\home_page_jsons"
    homepage_data = read_json(fr"{base_loc}\Home_page.json")
    
    # creating a homepage
    homepage = pages_folder+"\\Homepage"
    homepage_visuals = homepage +"\\visuals"
    create_folder(homepage)
    create_folder(homepage_visuals)
    create_or_replace_file(homepage + "\\page.json",homepage_data)

    # creting homepage visulas

    visuals = [ "background_box",
                "home_page_logo",
                "dossier_name",
                "select_module_line"
                ]
    for item in visuals :
        data = read_json(f"{base_loc}\\{item}.json")
        create_folder(f"{homepage_visuals}\\{item}")
        create_or_replace_file(f"{homepage_visuals}\\{item}\\visual.json",data)
    btn_pos = get_module_btn_pos(report_struct)
    for chapter in report_struct.keys():
        data= read_json(f"{base_loc}\\module_button.json")
        data["position"]=btn_pos[chapter]
        data["name"]=chapter
        data["visual"]["objects"]["text"][1]["properties"]["text"]["expr"]["Literal"]["Value"] = f"'{chapter}'"
        data["visual"]["visualContainerObjects"]["title"][0]["properties"]["text"]["expr"]["Literal"]["Value"] = f"'{chapter}'"
        data["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["navigationSection"]["expr"]["Literal"]["Value"]=f"'{report_struct[chapter][0]}'"
        create_folder(f"{homepage_visuals}\\{chapter}")
        create_or_replace_file(f"{homepage_visuals}\\{chapter}\\visual.json",data)
