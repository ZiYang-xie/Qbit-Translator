import uuid
import sys
import json
IS_PY3 = sys.version_info.major == 3
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus

def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    return mac

API_KEY = ""
SECRET_KEY = ""

TTS_URL = "http://tsn.baidu.com/text2audio" # 语音合成API #
TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token' # 获取token-API #

#-----------------------| 自动获取Token |----------------------------#
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()


    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'audio_tts_post' in result['scope'].split(' '):
            print ('please ensure has check the tts ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()
#-------------------| 语音合成功能 |----------------------------#
token_key =fetch_token()
def Voice(TEXT,token=token_key):
    tex = quote_plus(TEXT)
    params = {'tok': token, 'tex': tex, 'cuid': str(get_mac_address()),'lan': 'zh', 'ctp': 1,'per': 106}
    data = urlencode(params)
    req = Request(TTS_URL, data.encode('utf-8'))
    try:
        f = urlopen(req)
        result_str = f.read()
        headers = dict((name.lower(), value) for name, value in f.headers.items())
        has_error = ('content-type' not in headers.keys() or headers['content-type'].find('audio/') < 0)
    except  URLError as err:
        print('http response http code : ' + str(err.code))
        result_str = err.read()
        has_error = True

    if has_error:
        save_file = "error.txt" 
    elif(len(TEXT)<=3):
       save_file = './temp_audio/'+TEXT+'.mp3'
    else:
       save_file = './temp_audio/'+TEXT[:4]+'.mp3'

    with open(save_file, 'wb') as of:
        of.write(result_str)

    if has_error:
        if (IS_PY3):
            result_str = str(result_str, 'utf-8')
        print("tts api  error:" + result_str)
        return False
    else:
        return True