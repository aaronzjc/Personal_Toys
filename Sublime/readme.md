## Sublime Text3主题自动更换

### why ?

ST3中，我偏爱黑色主题。但是，前段时间发现眼睛瞅着这黑色的屏幕，分辨不清楚了。换个白色的就好了。但是ST3的配置有点不爽，得自己去编辑那个JSON文件，要输入一长串的名字等，所以，程序员思维就是写个程序搞定。于是，立马用Python写了这么个小东西。每天10:00-17:00为黑色主题，其他时间为白色。
### how ?

把代码放到一个目录下，打开终端，建立一个定时任务

    crontab -e
    0 * * * * /usr/local/bin/python3 /Users/memosa/Coding/Crontabs/Sublime/main.py
