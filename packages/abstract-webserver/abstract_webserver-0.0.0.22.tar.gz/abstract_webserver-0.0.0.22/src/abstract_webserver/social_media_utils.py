import urllib.parse
SOCIAL_SHARE_PARAMS={
    "x":{
        "url":"https://twitter.com/intent/tweet",
        "params":{
            "text":{"alias":["text","post","content","tweet","thread","body"],"description":"The main tweet text."},
            "url":{"alias":["url","u","link","site","domain","intentUrl"],"description":"A URL to include in the tweet."},
            "via":{"alias":["via","username","user","@","uploader","author"],"description":"A Twitter username to attribute the tweet to."},
            "hashtags"{"alias":["hashtags","hashtag","tag","tags"],"description":"Comma-separated hashtags (without the # symbol)."},
            "related":{"alias":["related","contributor","credit","cc","bcc"],"description":"Comma-separated related accounts."}
            },
        "characters":{"limit":280,"optimal":100,"mobile_cutoff":150},
        "alias":["x","twitter","x.com","tweet","twitter.com"]
        },
     "facebook":{
         "url":"http://facebook.com/sharer.php",
         "params":{
             "u":{"alias":["url","u","link","site","domain","intentUrl"],"description":"The URL you want to share."}
             },
         "characters":{"limit":63206,"optimal":50,"mobile_cutoff":150},
         "alias":["facebook","fb","facebook.com","meta","meta.com"]
         },
    
     "threads":{
         "url":"https://www.threads.net/intent/post",
         "params":{
             "text":{"alias":["text","post","content","tweet","thread","body"],"description":"The content you want to post."}
             },
        "characters":{"limit":500,"optimal":150,"mobile_cutoff":150},
         "alias":["threads","@","threads.com","@.com"]
         },
    "mailto":{
        "url":"mailto:",
        "params":{
             "subject":{"alias":["title","subject","heading","header"],"description":"The email subject."},
             "body":{"alias":["text","post","content","tweet","thread","body"],"description":"The email body."},
             "cc":{"alias":["related","contributor","credit","cc","bcc"],"description":"Additional email addresses."},
             "bcc":{"alias":["related","contributor","credit","cc","bcc"],"description":"Additional email addresses."}
             },
        "characters":{"limit":None,"optimal":None,"mobile_cutoff":None},
         "alias":["mailto","mail","email","email.com","mail.com"]
        },
    "minds":{
        "url":"https://www.minds.com/newsfeed/subscriptions/latest",
        "params":{
            "intentUrl":{"alias":["url","u","link","site","domain","intentUrl"],"description":"A URL to include in the post."}
            },
        "characters":{"limit":500,"optimal":125,"mobile_cutoff":150},
         "alias":["minds","mindscollective","collective"]
        }
             
    }
def clean_var(var):
    return eatAll(var,['/',',','"',"'",'#','\t','\n'])
def capitalize_util(string):
    if not string:
        return string
    cap = string[0].upper()
    if len(string)>1:
        ital = string[1:].upper()
        cap = f"{cap}{ital}"
    return cap
def capitalize(string,all=True):
    strings = string.replace('_',' ').replace('-',' ').replace(',',' ').split(' ')
    strings = [capitalize_util(string) for string in strings]
    strings = ''.join(strings)
    return strings
def generate_hashtags(keywords: str,hash_symbol=True) -> str:
    keywords = keywords or []
    if isinstance(hash_symbol,bool):
        if hash_symbol:
            hash_symbol = ' #'
        else:
            hash_symbol = ','
    if isinstance(keywords,tuple) or isinstance(keywords,set):
        keywords = list(keywords)
    if isinstance(keywords,str):
        keywords = keywords.replace('#',',').split(',')
        keywords = [clean_var(keyword) for keyword in keywords if keyword]
    if isinstance(keywords,list):
        keywords = [clean_var(keyword) for keyword in keywords if keyword]
    keywords = hash_symbol.join(keywords)
    if keywords:
        keywords = eatAll(keywords,[' '])
    return keywords
def encode_uri(string):
    if string == None:
        return None
    string = str(string)
    encoded_string = urllib.parse.urlencode(string)
    return encoded_string
def get_share_params(platform):
    params = SOCIAL_SHARE_PARAMS.get(platform)
    if params:
        return params
    platform_lower = platform.lower()
    first_key = None
    for key,values in SOCIAL_SHARE_PARAMS.items():
        alias = values.get("alias")
        if platform_lower in alias:
            return values
        if first_values == None:
            first_values=values
    return first_values
def get_precise_param(params,input_params):
    alias = params.get('alias')
    input_params_copy = input_params.copy()
    for key,value in input_params_copy.items():
        if key in alias:
            del input_params[key]
            return value,input_params
    return None,input_params
def create_output_text(input_params):
    text_output = ''
    for key,value in input_params.items():
        if value:
            if key == 'text':
                text_output+=value
            elif key == 'via':
                if text_output:
                    text_output+='\n'
                text_output+="@{value}"
            elif key == 'hashtags':
                if text_output:
                    text_output+='\n'
                value = generate_hashtags(value,hash_symbol=True)
                text_output+=value
            elif key == 'url':
                if text_output:
                    text_output+='\n'
                text_output+=value
    return text_output
def create_output_url(output_params,share_url):
    url = None
    for key,value in output_params.items():
        if value:
            value = encode_uri(value)
            if url == None:
                url = f"{share_url}?{key}={value}"
            else:
               url += f"{url}&{key}={value}"
    return url
def create_post(platform,text=None,url=None,via=None,hashtags=None):
    hashtags = generate_hashtags(hashtags,hash_symbol=False)
    text = text or ''
    url = url or ''
    input_params = {"text":text,"via":via,"hashtags":hashtags,"url":url}
    share_params = get_share_params(platform)
    share_url = share_params.get('url')
    params = share_params.get('params')
    output_params = {}
    for param,values in params.items():
        value,input_params = get_precise_param(params,input_params)
        output_params[param] = value
    text_output = create_output_text(input_params)
    output_params['text'] +=text_output
    output_url = create_output_url(output_params,share_url)
    return output_url

