# alfred-web-bookmarks-pinyin

## 介绍

[让 Alfred 自带的书签搜索支持拼音功能](https://kudoryafuka3.github.io/2023/08/13/%E8%AE%A9-Alfred-%E8%87%AA%E5%B8%A6%E7%9A%84%E4%B9%A6%E7%AD%BE%E6%90%9C%E7%B4%A2%E6%94%AF%E6%8C%81%E6%8B%BC%E9%9F%B3%E5%8A%9F%E8%83%BD/)

## 使用
### Python 脚本
修改 `bookmarks_pinyin.py` 中 `file_path = '{{your_bookmarks_file_path}}'`，改成你本地的书签路径即可。

#### 书签路径

Chrome: `/Users/{{user_name}}/Library/Application Support/Google/Chrome/Default/Bookmarks`

#### 用到的包

- pypinyin

### 定时任务
因为我们修改的书签文件会被 Chrome 更新覆盖，所以这边用 Mac 的定时任务，定时执行我们的 Python 脚本。在 macOS 上，可以使用 `launchd` 服务来创建定时任务。为了每 5 分钟执行一个 Python 脚本，需要创建一个 `launchd` plist 文件并将其放在 `~/Library/LaunchAgents/` 目录下。

#### 创建plist文件

首先，需要创建一个 `.plist` 文件。这里我们命名为 `com.mycompany.myscript.plist`。你可以更改 `mycompany` 和 `myscript` 为你自己喜欢的名字。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.mycompany.myscript</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/your/python/script.py</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

注意:

- 替换 `/path/to/your/python/script.py` 为你的 Python 脚本的完整路径。
- 这里使用了 `/usr/bin/python3` 作为 Python 3 的路径。如果你的 Python 安装在其他位置，需要相应地更改。

#### 保存plist文件

将上述内容保存为 `com.mycompany.myscript.plist` 文件，并将其放在 `~/Library/LaunchAgents/` 目录下。

#### 加载任务

打开终端并运行以下命令来加载你的任务：

```bash
launchctl load ~/Library/LaunchAgents/com.mycompany.myscript.plist
```

#### 验证

为了验证任务已经被正确地加载，你可以运行以下命令：

```bash
launchctl list | grep com.mycompany.myscript
```

如果你看到与 `com.mycompany.myscript` 相关的输出，那么任务已经被正确地加载。

#### 取消定时任务

如果你想在某个时候取消这个定时任务，只需运行以下命令：

```bash
launchctl unload ~/Library/LaunchAgents/com.mycompany.myscript.plist
```
