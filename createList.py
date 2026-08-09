import os
import json
from xml.dom import minidom
from urllib.parse import quote
from datetime import datetime, timezone

# Get the current time in UTC
current_datetime_utc = datetime.now(timezone.utc)

# Format to ISO 8601 string without microseconds
iso_format_string = current_datetime_utc.isoformat(timespec='seconds')

print(iso_format_string)

# Specify the directory you want to search for folders in
directory_path = './WebCodes'

# Function to get folder names in a directory along with unique IDs
def get_folders_with_ids(directory_path):
    folder_names = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]
    folders_with_ids = [{'id': i, 'folder_name': folder_name} for i, folder_name in enumerate(folder_names, start=1)]
    return folders_with_ids

# Get the folder names with unique IDs
folders = get_folders_with_ids(directory_path)

# Specify the JSON file where you want to store the data
json_file_path = './list.json'

# Write the data to the JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(folders, json_file, ensure_ascii=False, indent=4)

print(f"Folder data with unique IDs has been saved to {json_file_path}")

# Create Sitemap
root = minidom.Document()

xml = root.createElement('urlset') 
xml.setAttribute('xmlns', "http://www.sitemaps.org/schemas/sitemap/0.9")
xml.setAttribute('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
xml.setAttribute('xsi:schemaLocation', "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd")
root.appendChild(xml)

url = root.createElement('url')

loc = root.createElement('loc')
lastmod = root.createElement('lastmod')
priority = root.createElement('priority')

loc.appendChild(root.createTextNode(f"https://areebuzair.github.io/GameHUB/"))
priority.appendChild(root.createTextNode(f"1.0"))
lastmod.appendChild(root.createTextNode(iso_format_string))

url.appendChild(loc)
url.appendChild(lastmod)
url.appendChild(priority)

xml.appendChild(url)

for folder in folders:
    url = root.createElement('url')

    loc = root.createElement('loc')
    lastmod = root.createElement('lastmod')
    priority = root.createElement('priority')

    loc.appendChild(root.createTextNode(f"https://areebuzair.github.io/GameHUB/WebCodes/{quote(folder['folder_name'])}/"))
    priority.appendChild(root.createTextNode(f"0.8"))
    lastmod.appendChild(root.createTextNode(iso_format_string))
    
    url.appendChild(loc)
    url.appendChild(lastmod)
    url.appendChild(priority)

    xml.appendChild(url)


xml_str = root.toprettyxml(indent ="\t") 

save_path_file = "sitemap.xml"

with open(save_path_file, "w", encoding='utf-8') as f:
    f.write(xml_str) 
print("Sitemap generated")