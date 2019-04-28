# 摸鱼工具集

## dependencies

1. tushare
2. windows-curses
3. wxpy

提供了requirements.txt文件，可以用下面的方式安装依赖
```
pip install -r requirements.txt
```

## stock.py 将股票信息插入代码中，让人以为你在看代码，实际上是在看股票。

### usage

```
python stock.py -f stocklist -i -s sourcefile -t time
```

-f stocklist: 股票代码文件。示例见stocklist.txt。

-i: 是否显示上证指数和深证综指。默认不显示。

-s: 要将股票信息插入哪个文本文件中。默认stock.py。

-t: 运行多长时间（分钟）。默认一分钟。

在显示股票信息时：**pre_close**或者**preclose**代表昨日收盘价, **volume**成交量，**amount**成交金额。别的英文含义应该比较清晰。

### 已知问题

1. 如果网络超时请求不到股票数据会报错。

2. 如果窗口宽度过小，最后股票信息会换行。

3. 不能在运行时随意调整窗口大小，否则会造成显示错位。

## news.py 将新闻信息插入代码中，让人以为你在看代码，实际在看新闻。

新闻从[中国新闻网](http://www.chinanews.com/importnews.html)抓取。

### usage

```
python news.py -s sourcefile -t time -n number
```

-s: 要将股票信息插入哪个文本文件中。默认news.py。

-t: 新闻显示多长时间（分钟）。默认一分钟。

-n: 显示多少条新闻。默认5条。

## wx_send.py 在指定时刻将一系列文件和文字在微信上发给某人或某个群

### usage

```
python wx_send.py -d 0 -h 10 -m 1 -f wxFileList.txt -t wxMessageList.txt -u 爱谁谁 -g 单人
```

-d: 0代表今天；1代码明天。

-h: 几点0-24，默认0零点。

-m：几分，默认16。

-f：一个文本文件，记录了要发送的文件列表。格式参见根目录下的wxFileList.txt。

-t：一个文本文件，记录了要发送哪些消息。格式参见根目录下的wxMessageList.txt。

-u：接收文件和消息的用户名。

-g：接收文件和消息的群名称。

### notice

实验发现如果要发送名称中带有中文的文件会导致一个错误。解决的办法是把https://github.com/littlecodersh/ItChat/tree/master/itchat 下载下来放在项目根目录下。