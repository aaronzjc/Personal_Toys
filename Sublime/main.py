import datetime
import random
from preference import Preference

setting = {
    'light':[
                {
                    "name":"SpacegrayLight",
                    "color_scheme": "Packages/User/SublimeLinter/Mac Classic (SL).tmTheme",
                    "theme": "Spacegray Light.sublime-theme",
                },
            ],
    'dark':[
        {
            "name":"SpacegrayDark",
            "color_scheme": "Packages/User/SublimeLinter/base16-eighties.dark (SL).tmTheme",
            "theme": "Spacegray.sublime-theme",
        }
    ]
}

# init sublime settings
preference = Preference()
# judge current time
sec = datetime.datetime.now().strftime('%H')
flag = 'dark' if int(sec) <= 17 else 'light'
# choose a random theme
theme = setting[flag][random.randrange(len(setting[flag]))]
theme.pop('name')
# set theme
preference.setAttr(theme)
preference.save()