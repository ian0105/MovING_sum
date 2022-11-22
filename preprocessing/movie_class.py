import pandas as pd
import re
import os


class Movie():
    def __init__(self, name, path):
        self.moviename = name
        self.filename = path + name + '/script.txt'
        self.contents = self.getContents()
        self.lines = self.getLines()
        
        self.headingLocations, self.tailLocations = self.getHeadings_tails()
        
        self.scenes = self.getTextBetweenHeadings()
        self.numScenes = len(self.scenes)
        self.summary = self.getSummary()
        
    def getContents(self):
        with open(self.filename) as f:
            contents = f.read()
        return contents
    
    def getLines(self):
        return self.contents.split('\n')
    
    def getHeadings_tails(self):
        headings = []
        tails=  []
        start_list = ['INT.', 'EXT.', ' - DAY', ' - NIGHT']
        p = re.compile('\\b(?:'+ '|'.join(start_list) +')\\b')
        for i, line in enumerate(self.lines):
            if any(word in line for word in start_list):
                headings.append(i)
#                print(i)
                if len(headings) != 1:
                    tails.append(i-1)
        tails.append(i)
        return headings, tails
        
    def getTextBetweenHeadings(self):
        scenes = []
        lastHeading = len(self.headingLocations) - 1
        for i, (headingLocation, tailLocation) in enumerate(zip(self.headingLocations, self.tailLocations)):
            lines = self.lines[headingLocation+1:tailLocation]
            scene = []
            for line in lines:
                scene.append(line.strip())
            final = 0
            for s in scene:
                if not final:
                    final = s
                else:
                    if not s:
                        final += '\n'
                    elif s[0].islower():
                        while final[-1] =='\n':
                            fianl = final[:-1]
                        final += ' ' + s
                    else:
                        final += '\n' + s
            scenes.append(final)
        return scenes
    
    def getSummary(self):
        path = path + self.moviename + '/processed/wikiplot.txt'
        with open(path) as f:
            contents = f.read()
        return contents

