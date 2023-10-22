import string
import json
import jieba

from pypinyin import lazy_pinyin

jieba.setLogLevel(jieba.logging.INFO)


def process_name(obj):
    """
    Recursively processes a JSON object, looks for the "name" key, and appends the pinyin version to its value.
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "name" and isinstance(value, str):
                # 删除 \r 以及 \r 后面的全部内容
                value = value.split('\r')[0]

                # 用 jieba 的搜索模式分词
                words = jieba.cut_for_search(value)
                words_with_space = ' '.join(words)

                # 转换成 pinyin
                pinyin_result = lazy_pinyin(words_with_space)
                pinyin_name = ''.join(pinyin_result)

                # pinyin_name 去除重复
                pinyin_name_list = pinyin_name.split()
                pinyin_name_list = list(set(pinyin_name_list))
                pinyin_name_list.sort(key=pinyin_name.index)

                if len(pinyin_name_list) > 0:
                    # 找到第一个 pinyin_name_list[0] 的位置（要求位置非 0）
                    first_position = value.find(pinyin_name_list[0])
                    if first_position == 0:
                        first_position = value.find(pinyin_name_list[0], 1)

                    if first_position != -1:
                        value = value[:first_position]
                    
                    # 拼接新的书签名
                    obj[key] = value + '\r' + pinyin_name
            else:
                # 递归处理
                process_name(value)
    elif isinstance(obj, list):
        for item in obj:
            process_name(item)


file_path = '/Users/ritsu/Library/Application Support/Google/Chrome/Default/Bookmarks'

# 以二进制模式读取JSON文件
with open(file_path, 'rb') as file:
    content = json.loads(file.read().decode('utf-8'))

# 处理内容
process_name(content)

# 以二进制模式将处理的内容写回到新文件
with open(file_path, 'wb') as file:
    file.write(json.dumps(content, ensure_ascii=False, indent=2).encode('utf-8'))
