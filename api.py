import re
import zdy.config_db as db


class API:
    def __init__(self):
        self.db = db.ConfigDB()
        self.__api_dict={
            'get':{
            '语速':self.db.get_speech_speed,
            'led颜色':self.db.get_led_color
            },
            'set':{
            '语速':self.db.set_speech_speed,
            'led颜色':self.db.set_led_color
            }
            
        }


    def __parse_api_call(self, api_call):
        # 验证API调用格式
        match = re.findall(r'\[(set|get)\]\[(\w+)\](\[(.*)\])?', api_call, re.IGNORECASE)
        if match is None:
            return "无效的API调用"

        groups = match[0]
        print(groups)
        if len(groups) == 4:
            operation, api_name, _ , parameters_str = groups
        else:  # 对应的是无参数的情况
            operation, api_name = groups
            parameters_str = ""
        print(operation, api_name, parameters_str)
        # 提取参数，允许在括号和内容之间存在空格
        parameters = []
        if parameters_str:  # 确保参数字符串不为空
            parameters = re.findall(r'\[\s*([^\]]*?)\s*\]', parameters_str)
            parameters = [float(param) if param.replace('.', '', 1).isdigit() else param for param in parameters]

        return {
            'operation': operation,
            'api_name': api_name,
            'parameters': parameters
        }

    
    def is_api_call(self, response):
        try:
                # 验证API调用格式
                match = re.findall(r'\[(set|get)\]\[(\w+)\](\[(.*)\])?', response, re.IGNORECASE)
                if match is None:
                    return False
                else:
                    return match[0]
        except Exception as e:
            print(e)
            return False

    def __do_api(self,api):
    
        api = self.__parse_api_call(api)
        operation = api['operation']
        api_name = api['api_name']
        parameters = api['parameters']
        
        response ={
            'is_success':True,
            'result':None
        }
        try:
        # 调用API
            param = self.__api_dict[operation][api_name](*parameters)
            print(param)
        except Exception as e:
            response['is_success'] = False
            response['result'] = str(e)
            return response
        result = '成功:'+str(param) if response['is_success'] else '失败:'+str(param)
        response['result'] = result
        return response
    def do_api(self,api):
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.__do_api, api)
            return future.result()
        
        
if __name__ == '__main__':
    api = API()
    print(api.do_api('''[get][语速]'''))
    
    
    
    
    api_call = '[set][语速][[0.2]]'
    print(api.is_api_call(api_call))
    print(api.do_api(api_call))
    # api_call = '[get][语速]'
    # print(api.is_api_call(api_call))
    # print(api.do_api(api_call))
        
        