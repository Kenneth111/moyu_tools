# 摸鱼工具集

## stock.py 将股票信息插入代码中，让人以为你在看代码，实际上是在看股票。

# dependencies

1. tushare
2. windows-curses

提供了requirements.txt文件，可以用下面的方式安装依赖
```
pip install -r requirements.txt
```
# usage

```
python stock.py -f stocklist -i -s sourcefile -t time
```

-f stocklist: 股票代码文件。示例见stocklist.txt。

-i: 是否显示上证指数和深证综指。默认不显示。

-s: 要将股票信息插入哪个文本文件中。默认stock.py。

-t: 运行多长时间（分钟）。默认一分钟。

在显示股票信息时：**pre_close**或者**preclose**代表昨日收盘价, **volume**成交量，**amount**成交金额。别的英文含义应该比较清晰。

# 已知问题

1. 如果网络超时请求不到股票数据会报错。

2. 股票名称挤在一起显示。

3. 如果窗口宽度过小，最后股票信息会换行。

4. 不能在运行时随意调整窗口大小，否则会造成显示错位。