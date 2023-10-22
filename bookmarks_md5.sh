#!/bin/bash

# 被监控的文件路径，即书签路径
FILE_TO_WATCH="/Users/ritsu/Library/Application Support/Google/Chrome/Default/Bookmarks"

# 存储 MD5 值的文件路径
STORED_CHECKSUM_FILE="./stored_checksum.md5"

# Python 脚本的路径
PYTHON_SCRIPT="./bookmarks_pinyin.py"

# 确保要监视的文件存在
if [ ! -f "$FILE_TO_WATCH" ]; then
    echo "错误：${FILE_TO_WATCH} 不存在。"
    exit 1
fi

# 计算 MD5 校验和
CURRENT_CHECKSUM=$(md5 -q "$FILE_TO_WATCH" | awk '{print $1}')

# 检索存储的MD5校验和
if [ -f "$STORED_CHECKSUM_FILE" ]; then
    STORED_CHECKSUM=$(cat "$STORED_CHECKSUM_FILE")
else
    STORED_CHECKSUM=""
fi

# 比较校验和并检查非空
if [ "$CURRENT_CHECKSUM" != "$STORED_CHECKSUM" ] && [ -n "$CURRENT_CHECKSUM" ]; then
    
    # 检查Python脚本是否存在
    if [ ! -f "$PYTHON_SCRIPT" ]; then
        echo "错误：${PYTHON_SCRIPT} 不存在。"
        exit 1
    fi
    
    # 执行 Python 脚本
    /usr/bin/python3 "$PYTHON_SCRIPT"
    
    # 计算新的 MD5 校验和，因为 Python 脚本会修改 Bookmarks 文件
    CURRENT_CHECKSUM=$(md5 -q "$FILE_TO_WATCH" | awk '{print $1}')

    # 更新存储的校验和
    echo "$CURRENT_CHECKSUM" > "$STORED_CHECKSUM_FILE"
fi
