import re

def extract_api_and_parameters(string):
    api_regex = r'\[(.*?)\]\[\[(.*?)\]\]'
    matches = re.findall(api_regex, string)
    if matches:
        apis = []
        for match in matches:
            api_name = match[0]
            api_params = match[1].split('][')
            apis.append((api_name, api_params))
        return apis
    else:
        return None

def is_api(string):
    return True if extract_api_and_parameters(string) else False

# 测试一下
test_str = '[led色][[1.0][2.0][3.00]]'
print(is_api(test_str))  # 应返回True
print(extract_api_and_parameters(test_str))  # 应返回[('led色', ['1.0', '2.0', '3.0'])]
