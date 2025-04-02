from abstract_utilities import *
import os,glob
from abstract_webserver import get_image_json
BASE_URL= "https://thedailydialectics.com",
IMGS_DIR = '/var/www/thedailydialectics/public/imgs'
sample = {"BASE_URL": BASE_URL,
    "href": "/mems/micro-fluidics.json",
    "title": "Micro Fluidics System Diagram | The Daily Dialectics",
    "content_file": "contents/mems/micro-fluidics.md",
    "share_url": "https://thedailydialectics.com/mems/micro-fluidics",
    "description": "A detailed illustration of a micro fluidics system showcasing various components and their functions, highlighting the intricacies of fluid dynamics in miniatur",
    "keywords_str": "Micro Fluidics,Fluid Dynamics,Lab-on-a-Chip,Microfluidic Systems,CO2 Emissions Solutions",
    "thumbnail":"/var/www/thedailydialectics/public/imgs/mems/micro-fluidics"}
def clean_var(obj):
    obj = eatAll(obj,['#',' ','/','-',',','\t','\n'])
    return obj
def sanitize_dir_filename(directory,filename):
    basename = eatAll(os.path.basename(directory),'/')
    filename = eatAll(os.path.splitext(filename)[0],'/')
    return basename,filename
def get_href(directory,filename,data):
    basename,filename = sanitize_dir_filename(directory,filename)
    return f"/{basename}/{filename}.json"
def get_content_file(directory,filename,data):
    basename,filename = sanitize_dir_filename(directory,filename)
    return f"/{basename}/{filename}.md"
def get_share_url(directory,filename,data):
    basename,filename = sanitize_dir_filename(directory,filename)
    return f"{BASE_URL}/{basename}/{filename}"
def convert_keyword_to_string(keywords):
    if isinstance(keywords,list):
        keywords = [clean_var(keyword) for keyword in keywords if clean_var(keyword)]
        keywords = ','.join(keywords)
    return keywords or ''
def get_keywords(dirname,filename,data):
    keywords = convert_keyword_to_string(data.get('keyword_str') or [])
    keywords += ','+convert_keyword_to_string(data.get('keyword') or [])
    keywords = eatAll(keywords,',') 
    return keywords
def clear_all_thumbs(data):
    data_copy = data.copy()
    for key,value in data_copy.items():
        if 'thumbnail' in key:
            del data[key]
    return data
def get_thumbnail(directory,filename,data):
    for key,value in data.items():
        if 'thumbnail' in key:
            if os.path.isfile(value):
                for media in image_info.get('media'):
                    url = media.get('url')
                    href = media.get('href')
                    if value in [url,href]:
                        thumbnail = get_image_json(media, value,section=value)
                        if thumbnail:
                            data = clear_all_thumbs(data)
                            data['thumbnail'] = thumbnail
                            return data
            elif os.path.isdir(value):
                info_path = os.path.join(value,'info.json')
                if os.path.isfile(info_path):
                    image_info = safe_read_from_file(info_path)
                    thumbnail = get_image_json(image_info, section=directory)
                    if thumbnail:
                        data = clear_all_thumbs(data)
                        data['thumbnail'] = thumbnail
                        return data
    for media in data.get('media'):
        for media in image_info.get('media'):
            url = media.get('url')
            href = media.get('href')
            if value in [url,href]:
                thumbnail = get_image_json(media, value,section=value)
                if thumbnail:
                    data = clear_all_thumbs(data)
                    data['thumbnail'] = thumbnail
                    return data
    return data
    
def get_json_directory():
    return '/var/www/thedailydialectics/src/json_pages'
def get_all_json_paths(directory):
    return glob.glob(os.path.join(directory, '**', '*.json'), recursive=True)
def conventionalize_jsons(directory):
    json_paths = get_all_json_paths(directory)
    for json_path in json_paths:
        dirname = os.path.dirname(json_path)
        dirname = os.path.basename(dirname)
        basename = os.path.basename(json_path)
        filename,ext = os.path.splitext(basename)
        json_data  = get_json_data(json_path)
        new_data = {"BASE_URL": BASE_URL,'title':json_data.get('title'),'description':json_data.get('description')}
        new_data['href'] = get_href(dirname,filename,json_data)
        new_data['get_content_file'] = get_content_file(dirname,filename,json_data)
        new_data['share_url'] = get_share_url(dirname,filename,json_data)
        new_data['keyword_str'] = get_keywords(dirname,filename,json_data)
        new_data['thumbnail'] = get_thumbnail(directory,filename,json_data)
        new_data['media'] = json_data
        
