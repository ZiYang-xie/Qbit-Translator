from jinja2 import Environment, FileSystemLoader
from Voice_Api import Voice

def Trans_main_html(LIST):
    #--------| 释义输出处理 |--------#
    # 主要释义 #
    main_trans = str(LIST[0])
    # 更多释义筛选 #
    if(LIST[1]!=''):
        try:
            pos = ['词性: ',LIST[2]]
            if(LIST[1][1]):pass
            if(LIST[1][0]==LIST[0]):
                detail = ['更多释义: ',','.join(term for term in LIST[1][1:])]
            else:
                detail = ['更多释义: ',','.join(term for term in LIST[1][:])]
        except IndexError:
            detail=['','']
    else:
        detail=['','']
        pos=['','']
        
    #--------------------| 模板传参 |-----------------------#
    if(len(main_trans)<=3):
        src='../temp_audio/'+main_trans+'.mp3'
    else:
        src='../temp_audio/'+main_trans[:4]+'.mp3'
    params = {
    'main_trans':'主要释义: ',
    'detail_trans':detail[0],
    'pos_str':pos[0],
    'main':main_trans,
    'detail':detail[1],
    'pos':pos[1],
    'src':src,
    }
    env = Environment(loader=FileSystemLoader('./', encoding='utf-8'))
    template = env.get_template('./Trans_html/qbit_template1.html')
    html_content = template.render(**params)
    with open('./Trans_html/qbit1.html','w',encoding='utf-8') as f:
        f.write(str(html_content))
    return main_trans

def sy_html(sy_str):
    trans_sy = '，'.join(sy for sy in sy_str)
    env = Environment(loader=FileSystemLoader('./', encoding='utf-8'))
    template = env.get_template('./Trans_html/qbit_template2.html')
    html_content = template.render(sy_str=trans_sy)
    with open('./Trans_html/qbit2.html','w',encoding='utf-8') as f:
        f.write(str(html_content))
    return 0