import glob,os,json
from abstract_utilities import *
from abstract_math import *
from abstract_webtools import *
from abstract_utilities.path_utils import get_files
from abstract_ocr import download_pdf
from PIL import Image
from pathlib import Path
remove=["is_web_link","is_video","is_spreadsheet","is_presentation","is_media","is_image","is_document","is_audio","image"]
obj = {"url":["og_url","original","url","href","URL"],
       "path":["file_path"],
       "title":["title"],
       "description":["description"],
       "keywords":["keywords"],
       "caption":["caption"],
       "alt":["alt"]}
media_types = {
        'image': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'},
        'video': {'.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm'},
        'audio': {'.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a'},
        'document': {'.pdf', '.doc', '.docx', '.txt', '.rtf'},
        'presentation': {'.ppt', '.pptx'},
        'spreadsheet': {'.xls', '.xlsx', '.csv'}
    }
TARGET_WIDTH = 1200
TARGET_HEIGHT = 627

def resize_and_convert_to_webp(input_path, output_path):
    """
    Resize an image to approximately 1200x627 while maintaining aspect ratio,
    and convert it to WebP format.
    
    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the output WebP image.
    
    Returns:
        tuple: (new_width, new_height) of the resized image, or None if an error occurs.
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Get the original dimensions
        original_width, original_height = img.size
        
        # Calculate the target aspect ratio
        target_ratio = TARGET_WIDTH / TARGET_HEIGHT
        original_ratio = original_width / original_height
        
        # Determine the new dimensions while maintaining aspect ratio
        if original_ratio > target_ratio:
            # Image is wider than the target ratio, fit to height
            new_height = TARGET_HEIGHT
            new_width = int(new_height * original_ratio)
        else:
            # Image is taller than the target ratio, fit to width
            new_width = TARGET_WIDTH
            new_height = int(new_width / original_ratio)
        
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # If the image is not in RGB mode, convert it (WebP requires RGB)
        if resized_img.mode != 'RGB':
            resized_img = resized_img.convert('RGB')
        
        # Save the image as WebP
        resized_img.save(output_path, 'WEBP', quality=80)
        print(f"Successfully processed: {input_path} -> {output_path}")
        
        return new_width, new_height
    
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return None

def get_file_size(file_path):
    """
    Get the file size in KB.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: File size in KB (e.g., "100KB").
    """
    try:
        size_bytes = os.path.getsize(file_path)
        size_kb = size_bytes / 1024  # Convert bytes to KB
        return f"{int(size_kb)}KB"
    except Exception as e:
        print(f"Error getting file size for {file_path}: {e}")
        return "Unknown"

def update_json_metadata(json_path, new_filename, new_ext, new_width, new_height, new_file_size):
    """
    Update the info.json file with the new WebP image details.
    
    Args:
        json_path (str): Path to the info.json file.
        new_filename (str): New filename for the WebP image.
        new_ext (str): New extension ("webp").
        new_width (int): New width of the resized image.
        new_height (int): New height of the resized image.
        new_file_size (str): New file size in KB.
    """
    try:
        # Read the existing JSON file
        with open(json_path, 'r') as f:
            metadata = json.load(f)
        BASE_DIR = os.path.split('imgs/')[-1].split('/')[0]
        # Update the relevant fields
        metadata['filename'] = new_filename
        metadata['ext'] = new_ext
        metadata['dimensions']['width'] = new_width
        metadata['dimensions']['height'] = new_height
        metadata['file_size'] = new_file_size
        
        # Update the schema URLs
        new_url = f"https://thedailydialectics.com/imgs/{BASE_DIR}/{os.path.basename(os.path.dirname(json_path))}/{new_filename}.{new_ext}"
        metadata['schema']['url'] = new_url
        metadata['schema']['contentUrl'] = new_url
        metadata['schema']['width'] = new_width
        metadata['schema']['height'] = new_height
        
        # Update the social media URLs
        metadata['social_meta']['og:image'] = new_url
        metadata['social_meta']['twitter:image'] = new_url
        
        # Write the updated JSON back to the file
        with open(json_path, 'w') as f:
            json.dump(metadata, f, indent=4)
        print(f"Updated JSON metadata: {json_path}")
    
    except Exception as e:
        print(f"Error updating JSON metadata for {json_path}: {e}")

def process_directory(directory):
    """
    Process a directory containing an image and info.json file.
    
    Args:
        directory (str): Name of the directory (e.g., "cannabinoids-synthesis").
    """
    try:
        # Construct the full directory path
        BASE_PATH = os.path.basename(directory)
        
        # Construct the image and JSON file paths
        image_path = os.path.join(directory, f"{BASE_PATH}.jpg")
        json_path = os.path.join(directory, "info.json")
        
        # Check if the image and JSON files exist
        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}")
            return
        if not os.path.exists(json_path):
            print(f"JSON file not found: {json_path}")
            return
        
        # Define the output WebP path
        new_filename = f"{BASE_PATH}_resized"
        output_path = os.path.join(directory, f"{new_filename}.webp")
        
        # Resize and convert the image to WebP
        result = resize_and_convert_to_webp(image_path, output_path)
        if result:
            new_width, new_height = result
            
            # Get the file size of the new WebP image
            new_file_size = get_file_size(output_path)
            
            # Update the JSON metadata
            update_json_metadata(json_path, new_filename, "webp", new_width, new_height, new_file_size)
        
    except Exception as e:
        print(f"Error processing directory {directory}: {e}")

def get_imgs_dir():
    return '/var/www/thedailydialectics/public/imgs'
def get_image_info_from_path(file_path):
    # Convert string path to Path object
    path = Path(file_path)
    
    # Get file size in bytes
    byte_size = path.stat().st_size
    byte_size = divide_it(byte_size,1000)
    # Get image dimensions
    with Image.open(file_path) as img:
        width, height = img.size
    
    return {
        'kbyte_size': byte_size,
        'width': width,
        'height': height
    }

def get_image_info_from_url(url):
    # Fetch the image from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request fails
    
    # Get byte size from the content
    kbyte_size = divide_it(len(response.content),1000)
    # Open the image from the bytes data
    img_bytes = io.BytesIO(response.content)
    with Image.open(img_bytes) as img:
        width, height = img.size
    
    return {
        'kbyte_size': kbyte_size ,
        'width': width,
        'height': height
    }
def get_image_path_from_url(url):
    dimensions={}
    og_file_path = os.path.join('/var/www/thedailydialectics/public/imgs/',url.split('imgs/')[-1])
    file_path = og_file_path
    if not os.path.isfile(og_file_path):
        dirname = os.path.dirname(og_file_path)
        basename = os.path.basename(og_file_path)
        filename,ext = os.path.splitext(basename)
        for basename_comp in os.listdir(dirname):
            filename_comp,ext_comp = os.path.splitext(basename_comp)
            if filename == filename_comp:
                file_path = os.path.join(dirname,basename_comp)
                return file_path
    if os.path.isfile(file_path):
        return file_path
def get_image_info(media,file_path,url=None):
    dimensions={}
    file_path = file_path or get_image_path_from_url(url)
    if file_path:
        dimensions = get_image_info_from_path(file_path)
    else:
        dimensions = get_image_info_from_url(url)
    image_info = {
        "alt": media.get('alt'),
        "caption": media.get('caption'),
        "keywords_str": ','.join(media.get('keywords') or []),
        "filename": media.get('filename'),
        "ext": media.get('ext'),
        "title": media.get('title'),
        "dimensions": {
            "width": dimensions.get('width'),
            "height": dimensions.get('height'),
        },
        "file_size": dimensions.get('kbyte_size'),
        "license": "CC BY-SA 4.0",
        "attribution": "Created by thedailydialectics for educational purposes",
        "longdesc": media.get('description'),
        "schema": {
            "@context": "https://schema.org",
            "@type": "ImageObject",
            "name": media.get('title'),
            "description": media.get('description'),
            "url": media.get('url'),
            "contentUrl": media.get('url'),
            "width": dimensions.get('width'),
            "height": dimensions.get('height'),
            "license": "https://creativecommons.org/licenses/by-sa/4.0/",
            "creator": {
                "@type": "Organization",
                "name": "thedailydialectics"
            },
            "datePublished": "2025-03-30"
        },
        "social_meta": {
            "og:image": media.get('url'),
            "og:image:alt": media.get('alt'),
            "twitter:card": "summary_large_image",
            "twitter:image": media.get('url')
        }
    }
    input(image_info)
    return image_info
def get_image_json(image_info, section=None):
    """
    Copy or download an image to a section directory and save its metadata as JSON.
    
    Args:
        image_info (dict): Dictionary with image metadata (url, filename, etc.).
        section (str, optional): Subdirectory under imgs (e.g., "sommerfeld-goubau").
    """
    try:
        # Base directory for images
        section_dir = get_imgs_dir()  # e.g., '/var/www/thedailydialectics/public/imgs'
        if section:
            section_dir = os.path.join(section_dir, section)
            os.makedirs(section_dir, exist_ok=True)
        
        # Get URL and original file path
        url = image_info.get('url')
        og_file_path = get_image_path_from_url(url) if url else None
        
        # Determine basename, filename, and extension
        basename = image_info.get('basename') or (os.path.basename(og_file_path) if og_file_path else os.path.basename(url))
        filename = image_info.get('filename') or os.path.splitext(basename)[0]
        ext = image_info.get('ext') or os.path.splitext(basename)[-1]
        
        # Contextualize numeric filenames
        if re.match(r'^\d+$', filename):
            dirname = os.path.dirname(og_file_path) if og_file_path else section or 'unknown'
            og_basename = os.path.basename(dirname)
            filename = f"{og_basename}_{filename}"
        
        # Create image directory and file path
        image_dir = os.path.join(section_dir, filename)
        os.makedirs(image_dir, exist_ok=True)
        basename = f"{filename}{ext}"
        image_file_path = os.path.join(image_dir, basename)
        
        # Copy or download the image
        if og_file_path and os.path.isfile(og_file_path) and not os.path.isfile(image_file_path):
            shutil.copy(og_file_path, image_file_path)
            print(f"Copied: {og_file_path} -> {image_file_path}")
        elif url and not os.path.isfile(image_file_path):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                with open(image_file_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {url} -> {image_file_path}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {url}: {e}")
                return
        
        # Generate and save image info JSON
        image_info_path = os.path.join(image_dir, 'info.json')
        image_info = get_image_info(image_info, image_file_path, url) or image_info
        safe_dump_to_file(image_info, image_info_path)
        
        # Process the directory (resize to WebP)
        process_directory(image_dir)
        return image_dir
    except Exception as e:
        print(f"Failed to process {image_info.get('url', 'unknown URL')}: {e}")
    
def get_only_type(list_objs,types):
    keeps = []
    exts = media_types.get(types)
    for list_obj in list_objs:
        for ext in exts:
            if list_obj.endswith(ext):
                keeps.append(list_obj)
    return keeps
def var_clean(obj):
    return eatAll(obj,[' ','"',"'",'“','” ','`'])
def get_content(soup, tag, attr_name, attr_values, content_key):
    """Extract content from a BeautifulSoup object based on tag and attributes."""
    if not soup:
        return None
    # Ensure attr_values is a list or single value
    attr_values = make_list(attr_values)
    for value in attr_values:
        # Find all tags matching the criteria
        elements = soup.find_all(tag, {attr_name: value})
        for element in elements:
            content = element.get(content_key)
            if content:
                return content
    return None
def analyze_text_for_keywords(soup: str, keywords: List[str], lines_per_section: int = 5):
    keywords = break_down_keywords(keywords)
    text = soup.text
    lines=[]
    # Split into individual lines
    if text:
        lines = text.replace('.','.\n').replace('\n\n','\n').split('\n')
        if not lines:
            return "", 0

    # Group lines into sections
    sections = []
    for i in range(0, len(lines), lines_per_section):
        section = '\n'.join(lines[i:i + lines_per_section])
        sections.append(section)

    def count_keywords(section: str) -> int:
        section_lower = section.lower()
        return sum(section_lower.count(kw) for kw in keywords)

    max_count = 0
    max_section_index = 0

    for i, section in enumerate(sections):
        if not section.strip():
            continue
        count = count_keywords(section)
        if count > max_count:
            max_count = count
            max_section_index = i

    if max_count == 0:
        return "", 0

    section_text = sections[max_section_index].strip()
    return section_text
def break_down_keyword(keyword):
    all_key_words = [keyword]
    if '-' in keyword:
        all_key_words.append(keyword.replace('-',''))
        all_key_words+=keyword.split('-')
    return all_key_words
def break_down_keywords(keywords):
    all_key_words=[]
    keywords = keywords or []
    if isinstance(keywords,str):
        keywords = [eatAll(keyword,[' ']) for keyword in keywords.splir(',') if keyword]
    for keyword in keywords:
        keyword_breakdown = break_down_keyword(keyword)
        keyword_break = make_list(keyword_breakdown)
        all_key_words+=keyword_break
    all_key_words = list(set(make_list(all_key_words)))
    return all_key_words
def combine_media(media,media_2):
    for key,value in media.items():
        media[key] = check_value(value) or check_value(media_2.get(key))
    return media
def check_value(value):
    if value in ['True','False','None',None,True,False,'None','True','false',['True'],['False'],['None'],[True],[None],[False]]:
        value = None
    return value
def get_abs_path():
    return os.path.abspath(__file__)
def get_abs_dir():
    abs_path = get_abs_path()
    return os.path.dirname(abs_path)
def get_json_directory():
    return '/var/www/thedailydialectics/src/json_pages'
def get_sections_dir():
    return '/var/www/thedailydialectics/collect_media/sections'
def get_gone_list_path():
    return '/var/www/thedailydialectics/collect_media/gone_list.json'
def add_to_gone_list(url):
    gone_list_path = get_gone_list_path()
    data = safe_read_from_json(gone_list_path)
    if url and url not in data:
        data.append(url)
        safe_dump_to_file(data,gone_list_path)
def get_json_directories():
    return get_dir_paths(get_json_directory())
def get_dir_paths(directory):
    json_dirs = [os.path.join(directory,item) for item in os.listdir(directory)]
    json_dirs = [json_dir for json_dir in json_dirs if os.path.isdir(json_dir)]
    return json_dirs
def get_cannabis_file():
    cannabis_path = os.path.join(get_abs_dir(),'cannabis_sources.json')
    return cannabis_path
def get_data(file_path):
    return safe_read_from_json(file_path)
def consolidate_media(file_path):
    data = safe_read_from_json(file_path)
    data = get_new_media(data)
    safe_dump_to_file(data,file_path)
    return data
def create_keys(titles):
    keywords = []
    for title in titles:
        keywords+=title.split(' ')
    keywords = list(set(keywords))
    all_valid = list('abcdefghijklmnopqrstuvwxyz1234567890'+'abcdefghijklmnopqrstuvwxyz'.upper())
    invalid = ['and','the','of','at']
    all_new_words = []
    for word in keywords:
        chars = ''
        for char in word:
            if char not in all_valid:
                char = ' '
            chars+=char
        chars_spl = chars.split(' ')
        chars = [char for char in chars_spl if char and char.lower() not in invalid] 
        all_new_words+=chars
    return all_new_words
def get_phrase(soup,string):
    soup = soup.find_all('head')
    text = str(soup)
    targets = []
    string_lower = string.lower()
    lines = text.replace('\n',' ').replace('> <','><').split('><')
    for line in lines:
        line_lower = line.lower()
        if string_lower in line_lower:
            target_text = ''
            if '>' in line_lower:
                target_text = line.split('>')[1].split('<')[0]
            elif '=' in line_lower:
                target_text = line.split(string)[0].split('=')[1].split(' ')
                target_text = ' '.join(target_text[:-1])
            if target_text:
                target_text = eatAll(target_text,[' ','\t','\n','',"'",'"'])
                targets.append(target_text)
    return list(set(targets))
image_exts = get_media_types(types='image').get('image')
def get_json_data(file_path):
    json_contents = safe_read_from_json(file_path)
    if not json_contents:
        raise ValueError(f"Failed to load JSON: {file_path}")
    return json_contents
def get_all_json_paths(directory):
    json_paths = glob.glob(os.path.join(directory, '**', '*.json'), recursive=True)
    return json_paths
def url_in_sources(media,sources):
    url = media.get('url')
    for i,source in enumerate(sources):
        source_url = source.get('url')
        if url == source_url:
            for key,value in media.items():
                sources[i][key] = source.get(key,value) or value
            return sources
    sources.append(media)
    return sources
def get_all_medias(directory):
    list_dir = os.listdir(directory)
    all_jsons = get_all_json_paths(directory)
    all_medias = []
    for file_path in all_jsons:
        if not file_path.endswith('sources.json') and not file_path.endswith('images.json'):
            json_data = get_json_data(file_path)
            all_medias+=json_data.get('media')
    return all_medias
def get_all_keywords(directory):
    list_dir = os.listdir(directory)
    all_jsons = get_all_json_paths(directory)
    all_keywords = []
    for file_path in all_jsons:
        if not file_path.endswith('sources.json') and not file_path.endswith('images.json'):
            json_data = get_json_data(file_path)
            keywords = json_data.get('keywords') or json_data.get('keywords_str') or []
            if isinstance(keywords,str):
                keywords = [eatAll(keyword,[' ','\n','\t','#',',']) for keyword in keywords.split(',') if keyword]
            
            all_keywords+=keywords
    return all_keywords
def get_images_others(media,images,others):
    url = media.get('url')
    if url:
        basename= os.path.basename(url)
        filename, ext = os.path.splitext(basename)
        if ext.lower() in image_exts:
            images = url_in_sources(media,images)
        else:
            others = url_in_sources(media,others)
    return images,others

def consolidate_medias(all_medias,images=None,others=None):
    images = images or []
    others=others or []
    for medias in all_medias:
        if isinstance(medias,list):
            for media in medias:    
               images,others = get_images_others(media,images,others)
        else:
            images,others = get_images_others(medias,images,others)
    
    return images,others
def get_youtube_info(url):
    print(url)
    info = downloadvideo(url)
    
    return info
def create_source_dirs():
    json_directories = get_json_directories()
    for json_directory in json_directories:
        print(json_directory)
        basename = os.path.basename(json_directory)
        filename,ext = os.path.splitext(basename)
        source_dir = os.path.join(get_sections_dir(),filename)
        os.makedirs(source_dir,exist_ok=True)
        all_medias = get_all_medias(json_directory)
        all_keywords = get_all_keywords(json_directory)
        sources_json = os.path.join(source_dir,'sources.json')
        if not os.path.isfile(sources_json):
            safe_dump_to_file([],sources_json)
        sources_data =safe_read_from_json(sources_json)
        images_json = os.path.join(source_dir,'images.json')
        if not os.path.isfile(sources_json):
            safe_dump_to_file([],images_json)    
        images_data =safe_read_from_json(images_json)
        
        keywords_json = os.path.join(source_dir,'keywords.json')
        if not os.path.isfile(keywords_json):
            safe_dump_to_file([],keywords_json)
        images_data,sources_data = consolidate_medias(all_medias,images=images_data,others=sources_data)
        safe_dump_to_file(sources_data,sources_json)
        safe_dump_to_file(images_data,images_json)
last_url = 'http://www.emediapress.com/go.php?offer=qiman&pid=36'
def get_consolidated_data(datas,all_keywords,consolidated_path,last_url_found = False):
    for j,data in enumerate(datas):
        og_data = data.copy()
        types = data.get('type')
        if types != 'image':
            url = data.get('url')
            if last_url_found == False and url == last_url:
                last_url_found=True
            if last_url_found == True:
                if "thedailydialectics" not in url:
                    if 'youtube' in url:
                        try:
                            if 'channel' not in url:
                                youtube_info = get_youtube_info(url)
                                print(youtube_info)
                        except:
                            print(f"bad youtube url {url}")
                    else:
                        try:
                            soup = soupManager(url).soup
                            try:
                                url_pieces = url_mgr.url_to_pieces(url)
                                protocol = url_pieces[0]
                                domain = url_pieces[1]
                                domain = f"{protocol}://{domain}"
                            except:
                                print(f"no url domain for {url}")
                            i=0
                            titles = get_phrase(soup,'title')
                            for title in titles:
                                i+=1
                                if i ==2:
                                    break
                            titles = titles[:i]
                            keywords = create_keys(titles) or []
                            icon = get_phrase(soup,'icon')
                            icon+=make_list(get_phrase(soup,'image') or [])
                            icon = get_only_type(icon,'image')
                            icons = [f"{domain}{ico}" if ico.startswith('/') else ico for ico in icon if ico]
                            description2 = get_phrase(soup,'description')
                            description = analyze_text_for_keywords(soup, all_keywords, 5)
                            js_meta = {"domain":domain,"url":url,"title":titles,"keywords":keywords,"image":icons,"description":description,"description2":description2}
                            combine_media(data,js_meta)
                            datas[j] = combine_media(datas[j],og_data)
                            safe_dump_to_file(datas,consolidated_path)
                        except:
                            add_to_gone_list(url)
    return datas,last_url_found
last_url_found = False
def get_media_from_source_dirs(get_urls=False):
    for section_dir in get_dir_paths(get_sections_dir()):
        section = os.path.basename(section_dir)
        images_path = os.path.join(section_dir,'images.json')
        images_datas = safe_read_from_json(images_path)
        for image_data in images_datas:
            get_image_json(image_data,section=section)
        if get_urls:
            if 'space' not in section_dir:
                sources_path = os.path.join(section_dir,'sources.json')
                keywords_path = os.path.join(section_dir,'keywords.json')
                sources_data = safe_read_from_json(sources_path)
                keywords = safe_read_from_json(keywords_path)
                sources_data,last_url_found = get_consolidated_data(sources_data,keywords,sources_path,last_url_found)
