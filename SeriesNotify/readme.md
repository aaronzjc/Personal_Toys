## &lt;Silicon Valley&gt; Tracker

### why ?

《硅谷》更新第三季了，每周一更新英文版，星期二更新中文熟肉。但是我不知道具体是啥时候更新，所以，这就很尴尬了。我必须隔一段时间去瞅瞅更新了没有。所以，想到，能不能做一个系统提醒的工具，更新了，就在Mac右上角消息通知我。查了一下，解决了。整体解决的也很简单，代码写的不太清晰。

### how ?

把代码放到一个目录下，打开终端，建立一个定时任务

    crontab -e
    30 * * * * /usr/local/bin/python3 /Users/memosa/Coding/Crontabs/SeriesNotify/main.py