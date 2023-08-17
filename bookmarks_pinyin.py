import string
import json
import jieba

from pypinyin import lazy_pinyin


def process_name(obj):
    """
    Recursively processes a JSON object, looks for the "name" key, and appends the pinyin version to its value.
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "name" and isinstance(value, str) and '\r' not in value:
                # Split the name value into words
                words = jieba.cut_for_search(value)
                words_with_space = ' '.join(words)

                # Convert the name value to pinyin
                pinyin_result = lazy_pinyin(words_with_space)
                pinyin_name = ''.join(pinyin_result)
                
                # Append the pinyin name to the original value
                obj[key] = f"{value}\r{pinyin_name}"
            else:
                # Recursively process the value
                process_name(value)
    elif isinstance(obj, list):
        for item in obj:
            process_name(item)


file_path = '{{your_bookmarks_file_path}}'

# Read the JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    content = json.load(file)

# Process the content
process_name(content)

# Write the processed content back to a new file
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(content, file, ensure_ascii=False, indent=2)
