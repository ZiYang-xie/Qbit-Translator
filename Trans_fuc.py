from urllib import request,parse,error
import json
import os,sys

#-------------------------------|处理函数|------------------------------------------#
# 翻译处理 #
def Trans_Process(response):
    # 读取json #
    trans_json = json.load(response)
    # 获取释义 #
    trans = trans_json['sentences'][0]['trans']
    try: # 获取单词更多信息并输出 #
        #trans_orig = trans_json['sentences'][0]['orig']
        trans_pos = trans_json['dict'][0]['pos']
        trans_terms = trans_json['dict'][0]['terms']
        trans_sy = trans_json['dict'][0]['entry'][0]['reverse_translation']
        return [trans,trans_terms,trans_pos,trans_sy]
    except KeyError: # 如无或无法获取，直接显示释义 #
        return [trans,'','','']
    else: # 错误处理 #
        error_info = '错误信息:'+ trans_json +'json长度：'+str(len(trans_json))
        return 1

# 中文判断 #
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

# ----------|翻译API请求处理过程|--------------- #

def Main_Translate(sl,tl,text):
    params = {'sl': sl, 'tl': tl, 'hl': 'zh-CN','tk':'tk','q': text} # 参数字典 #
    url = "https://translate.google.cn/translate_a/single?client=gtx&dt=t&dt=bd&dt=rm&dj=1&ie=UTF-8&oe=UTF-8&"
    data = parse.urlencode(params)
    # request请求 #
    req = request.Request(url+data)
    browser = "Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3"
    req.add_header('User-agent', browser)
    # 尝试获取json #
    try:
        response = request.urlopen(req)
    except error.HTTPError as e: # HTTP错误信息处理 #
        print(e.reason)
        print(e.code)
        print(e.headers)
        return 1
    except error.URLError as e: # URL错误信息处理 #
        print(e.reason)
        return 1
    else:
        return Trans_Process(response) # 正常处理 #