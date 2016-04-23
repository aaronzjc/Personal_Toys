import os
import json

class Preference(object):
    path = '~/Library/Application Support/Sublime Text 3/Packages/User/Preferences.sublime-settings'
    settings = {}

    def __init__(self):
        with open(os.path.expanduser(self.path)) as preference:
            try:
                self.settings = json.load(preference)
            except:
                print('file convert error!')
        preference.close()

    def setAttr(self, attr):
        for x in attr:
            self.settings[x] = attr[x]

    def save(self):
        preference = open(os.path.expanduser(self.path), 'w')
        preference.write(json.dumps(self.settings, indent=4))
        preference.close()

