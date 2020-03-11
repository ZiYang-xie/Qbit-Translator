from urllib import request,parse,error
import json
import os,sys

#################################处理函数#######################################
def Word_Process(response):
    #print("reqeust successfully")
    trans_json = json.load(response)
    #print(trans_json)
    #print(url+data)
    trans = trans_json['sentences'][0]['trans']
    if(trans.find(' ')<0):
        try:
            trans_orig = trans_json['sentences'][0]['orig']
            trans_pos = trans_json['dict'][0]['pos']
            trans_terms = trans_json['dict'][0]['terms']
            trans_sy = trans_json['dict'][0]['entry'][0]['reverse_translation']
            output_mean = '释义: '+ trans +'\n'+'词性：'+ trans_pos
            sywords = '，'.join(sy for sy in trans_sy)
            return[str(output_mean),str(sywords)]
        except KeyError:
            output = '释义： '+trans
            return output
        else:
            error_info = '错误信息:'+ trans_json +'json长度：'+str(len(trans_json))
            return ['可能输入不正确！',error_info]
    else:
        output = '句子释义: '+trans
        return str(output)

def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

def Scentence_Trans(response):
    trans_json = json.load(response)
    trans = trans_json['sentences'][0]['trans']
    output = '句子释义: '+trans
    return str(output)

def Main_Translate(sl,tl,text):
    params = {'sl': sl, 'tl': tl, 'hl': 'zh-CN','tk':'tk','q': text}
    url = "https://translate.google.cn/translate_a/single?client=gtx&dt=t&dt=bd&dt=rm&dj=1&ie=UTF-8&oe=UTF-8&"
    data = parse.urlencode(params)
    #print('data内容:\n'+ str(data) +'\n')
    req = request.Request(url+data)
    browser = "Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3"
    req.add_header('User-agent', browser)
    try:
        response = request.urlopen(req)
        #print(trans_json)
    except error.HTTPError as e:
        print(e.reason)
        print(e.code)
        print(e.headers)
        return 1
    except error.URLError as e:
        print(e.reason)
        return 1
    else:
        return Word_Process(response)