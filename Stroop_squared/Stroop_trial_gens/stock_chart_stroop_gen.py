import sys
import numpy as np
import pandas as pd
import random
import math
from random import randint
sys.path.insert(0, '../')

def main(SbjId=0):
    col_names = ['trial', 'stimWord', 'stimColor', 'condition', 'leftWord', 'leftColor', 'rightWord', 'rightColor', 'response', "stimImage", "leftImage", "rightImage"]
    catList = ['red', 'blue']
    colorList = ['darkred', 'darkblue']
    odd_list = list(range(1, 16, 2)) #gain
    even_list = list(range(2, 18, 2)) #loss
    #odd_list = list(range(17, 32, 2)) #happy
    #even_list = list(range(18, 34, 2)) #angry
    
    
    M = pd.DataFrame(columns=col_names)
    M.stimColor = (["white"]*400)
    M.leftColor = (["white"]*400)
    M.rightColor = (["white"]*400)
    

    M.stimWord = (["GAIN"]*200+["LOSS"]*200)
    M.stimImage = (["gain"]*100+["loss"]*100+["gain"]*100+["loss"]*100)
    M.leftWord = (["GAIN"]*50+["LOSS"]*50+["GAIN"]*50+["LOSS"]*50+["GAIN"]*50+["LOSS"]*50+["GAIN"]*50+["LOSS"]*50)
    M.rightWord = (["LOSS"]*50+["GAIN"]*50+["LOSS"]*50+["GAIN"]*50+["LOSS"]*50+["GAIN"]*50+["LOSS"]*50+["GAIN"]*50)
    for i in range(len(M.stimWord)):
        currentOption = random.randint(0,1)
        if currentOption == 0:
            M.leftImage[i] = 'gain'
            M.rightImage[i] = 'loss'
        else:
            M.leftImage[i] = 'loss'
            M.rightImage[i] = 'gain'
            
    M.loc[(M.stimImage == 'gain') & (M.leftWord == 'GAIN'), 'response'] = 'buttonA'
    M.loc[(M.stimImage == 'loss') & (M.leftWord == 'LOSS'), 'response'] = 'buttonA'
    M.loc[(M.stimImage == 'gain') & (M.rightWord == 'GAIN'), 'response'] = 'buttonB'
    M.loc[(M.stimImage == 'loss') & (M.rightWord == 'LOSS'), 'response'] = 'buttonB' 
    
    
    M.condition = M.stimImage
    for i in range(len(M)):
        if M.stimImage[i] == 'gain':
            M.stimImage[i] = str(random.choice(odd_list)) + ".png"
        elif M.stimImage[i] == 'loss':
            M.stimImage[i] = str(random.choice(even_list)) + ".png"
        if M.leftImage[i] == 'gain':
            M.leftImage[i] = str(random.choice(odd_list)) + ".png"
            M.rightImage[i] = str(random.choice(even_list)) + ".png"
        elif M.leftImage[i] == 'loss':
            M.leftImage[i] = str(random.choice(even_list)) + ".png"
            M.rightImage[i] = str(random.choice(odd_list)) + ".png"
    
    for i in range(len(M)):
        if M.stimImage[i] == M.leftImage[i]:
            if M.condition[i] == 'gain':
                M.stimImage[i] = str(random.choice(odd_list)) + ".png"
            elif M.condition[i] == 'loss':
                M.stimImage[i] = str(random.choice(even_list)) + ".png"
        if M.stimImage[i] == M.rightImage[i]:
            if M.condition[i] == 'gain':
                M.stimImage[i] = str(random.choice(odd_list)) + ".png"
            elif M.condition[i] == 'loss':
                M.stimImage[i] = str(random.choice(even_list)) + ".png"
                
    for i in range(len(M)):
        if M.stimImage[i] == M.leftImage[i]:
            if M.condition[i] == 'gain':
                M.stimImage[i] = str(random.choice(odd_list)) + ".png"
            elif M.condition[i] == 'loss':
                M.stimImage[i] = str(random.choice(even_list)) + ".png"
        if M.stimImage[i] == M.rightImage[i]:
            if M.condition[i] == 'gain':
                M.stimImage[i] = str(random.choice(odd_list)) + ".png"
            elif M.condition[i] == 'loss':
                M.stimImage[i] = str(random.choice(even_list)) + ".png"
                
    for i in range(len(M)):
        if M.stimImage[i] == M.leftImage[i]:
            if M.condition[i] == 'gain':
                M.stimImage[i] = str(random.choice(odd_list)) + ".png"
            elif M.condition[i] == 'loss':
                M.stimImage[i] = str(random.choice(even_list)) + ".png"
        if M.stimImage[i] == M.rightImage[i]:
            if M.condition[i] == 'gain':
                M.stimImage[i] = str(random.choice(odd_list)) + ".png"
            elif M.condition[i] == 'loss':
                M.stimImage[i] = str(random.choice(even_list)) + ".png"
                
    M.to_csv('finance_trialPool_' + str(SbjId) + ".csv", index=False)

if __name__ == '__main__':
   for id in range(0,1):
        main(id)