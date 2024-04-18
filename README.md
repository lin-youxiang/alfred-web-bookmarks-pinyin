# alfred-web-bookmarks-pinyin

## 介绍

[让 Alfred 自带的书签搜索支持拼音功能](https://kudoryafuka3.github.io/2023/08/13/%E8%AE%A9-Alfred-%E8%87%AA%E5%B8%A6%E7%9A%84%E4%B9%A6%E7%AD%BE%E6%90%9C%E7%B4%A2%E6%94%AF%E6%8C%81%E6%8B%BC%E9%9F%B3%E5%8A%9F%E8%83%BD/)

原生 Alfred 的书签搜索有点呆呆的，对中文不太友好。比如一个书签叫做“明日方舟”，你搜索“方舟”就有可能搜索不到。所以这里加入了 jieba 分词，采用 jieba 分词搜索模式，先分词再做拼音化，搜索书签体验 🆙🆙🆙

## 使用教程

### 前情提要


#### 书签路径

Chrome: `~/Library/Application Support/Google/Chrome/Default/Bookmarks`

#### 用到的包

- pypinyin
- jieba

### 具体步骤

1. clone 项目到本地

2. 给 `bookmarks_md5.sh` 执行权限

   ~~~sh
   chmod +x ./bookmarks_md5.sh
   ~~~

3. 修改 `com.mycompany.myscript.plist`

   ![image-20231022154148018](https://ritsurin-1309788983.cos.ap-guangzhou.myqcloud.com/img/20240319230301.png)

4. 复制 `com.mycompany.myscript.plist` 文件到 `~/Library/LaunchAgents`

5. 加载定时任务

   ~~~sh
   launchctl load ~/Library/LaunchAgents/com.mycompany.myscript.plist
   ~~~

6. 为了验证任务已经被正确地加载，你可以运行以下命令：

   ~~~sh
   launchctl list | grep com.mycompany.myscript
   ~~~

   如果你看到与 `com.mycompany.myscript` 相关的输出，那么任务已经被正确地加载。


## 其他问题

### 每次打开都会看到通知 "xxx.sh 已在后台运行"

解决办法：执行 `sudo sfltool resetbtm`

参考链接：[后台项目已添加的通知如何关闭](https://discussionschinese.apple.com/thread/254470532)

### 取消定时任务

如果你想在某个时候取消这个定时任务，只需运行以下命令：

```bash
launchctl unload ~/Library/LaunchAgents/com.mycompany.myscript.plist
```