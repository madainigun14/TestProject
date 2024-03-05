import json

def recursive_single(json_obj):
    if isinstance(json_obj, dict):
        for k, v in json_obj.items():
            print(k)
            
            if isinstance(v, dict) or isinstance(v, list):
                recursive(v)
                
            if isinstance(v, str):
                print(v)
                
    if isinstance(json_obj, list):
        for i in range(len(json_obj)):
            value = json_obj[i]
            
            if isinstance(value, dict) or isinstance(value, list):
                recursive(value)
                
            if isinstance(value, str):
                print(value)
                
def call(value, method):
        if isinstance(value, dict) or isinstance(value, list):
            method(value)

        if isinstance(value, str):
            print(value)

                
                
def recursive(json_obj):
    if isinstance(json_obj, dict):
        for k, v in json_obj.items():
            print(k)
            
            call(v, recursive)
                
    if isinstance(json_obj, list):
        for i in range(len(json_obj)):
            value = json_obj[i]
            
            call(value, recursive)
            
            
            

def test():
    raw_str = '''
    {
        "姓名":"麻袋",
        "年龄":"18",
        "爱好":[
            "吃饭",
            "睡觉",
            "打游戏", 
            {
                "暴雪":"魔兽争霸",
                "网易":"梦幻西游",
                "金山":"封神榜",
            }
        ],
        "民族":"汉",
        "编号":"9527",
    }
    '''

    json_str = json.loads(raw_str.encode("utf-8"))  # 这里要encode一下，不然遇到中文字符就会出错
    recursive(json_str)


if __name__=="__main__":
    test()