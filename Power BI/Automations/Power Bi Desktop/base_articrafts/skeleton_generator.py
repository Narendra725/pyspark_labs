import json

file_path = r"C:\Nahdi-articrafts\base_articrafts\report_page_jsons\visuals\chapter_button\visual.json"
with open(file_path,"r") as file:
    data = json.load(file)
    
# default state 
default_colour ='#FFFFFF'
transparency  ='0D'
#font
print(data["visual"]["objects"]["text"][1]["properties"]["fontFamily"]["expr"]["Literal"]["Value"])
# is bold
print(data["visual"]["objects"]["text"][1]["properties"]["bold"]["expr"]["Literal"]["Value"])
# fill colour
print(data["visual"]["objects"]["fill"][1]["properties"]["fillColor"]["solid"]["color"]["expr"]["Literal"]["Value"])


# hover state 
hover_colour = '#0F9797'
transparency ='70D'
#font
print(data["visual"]["objects"]["text"][2]["properties"]["fontFamily"]["expr"]["Literal"]["Value"])
# is bold
print(data["visual"]["objects"]["text"][2]["properties"]["bold"]["expr"]["Literal"]["Value"])
# fill colour
print(data["visual"]["objects"]["fill"][2]["properties"]["fillColor"]["solid"]["color"]["expr"]["Literal"]["Value"])


# press state 
press_colour = '#0F9797'
transparency ='0D'
#font
print(data["visual"]["objects"]["text"][3]["properties"]["fontFamily"]["expr"]["Literal"]["Value"][0])
# is bold
print(data["visual"]["objects"]["text"][3]["properties"]["bold"]["expr"]["Literal"]["Value"])
# fill colour
print(data["visual"]["objects"]["fill"][3]["properties"]["fillColor"]["solid"]["color"]["expr"]["Literal"]["Value"])



# layer_name
print(data["visual"]["visualContainerObjects"]["title"][0]["properties"]["text"]["expr"]["Literal"]["Value"])

# display_name_for_button
print(data["visual"]["objects"]["text"][1]["properties"]["text"]["expr"]["Literal"]["Value"])


# navigation to
print(data["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["navigationSection"]["expr"]["Literal"]["Value"])