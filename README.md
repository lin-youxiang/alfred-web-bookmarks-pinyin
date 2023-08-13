# alfred-web-bookmarks-pinyin
这是我的一个书签。

~~~json
{
	"date_added": "13298050222711550",
	"date_last_used": "0",
	"guid": "820a51f4-8ab1-49df-bc70-0cd29382eeb",
	"id": "885",
	"name": "Downie - 视频下载",
	"type": "url",
	"url": "https://software.charliemonroe.net/downie/"
}
~~~

搜索”视频下载“可以搜出来，但是搜索 “shipinxiazai” 搜不出来。

![image-20230812214758164](https://ritsurin-1309788983.cos.ap-guangzhou.myqcloud.com/img/20230812214758.png)

![image-20230812214842456](https://ritsurin-1309788983.cos.ap-guangzhou.myqcloud.com/img/20230812214842.png)

但是如果修改 `Bookmarks` 如下图所示。

~~~json
{
	"date_added": "13298050222711550",
	"date_last_used": "0",
	"guid": "820a51f4-8ab1-49df-bc70-0cd29382eeb",
	"id": "885",
	"name": "Downie - 视频下载\rshipinxiazai",
	"type": "url",
	"url": "https://software.charliemonroe.net/downie/"
}
~~~

那么又可以被拼音搜出来，并且不会把拼音内容显示在 Alfred 上。

![image-20230812215118069](https://ritsurin-1309788983.cos.ap-guangzhou.myqcloud.com/img/20230812215118.png)

可以用 Python 对所有书签做这样的批处理，但是只要 Chrome 更新了 `Bookmarks` 文件，就会覆盖掉我们 DIY 的内容。这要怎么解决呢？

- 定时任务？
  - 有延迟
  - 太频繁又没必要
- 监听 `Bookmarks` 的修改？ 
  - how？
