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
    #odd_list = list(range(1, 16, 2))
    #even_list = list(range(2, 18, 2))
    odd_list = list(range(17, 32, 2)) #happy
    even_list = list(range(18, 34, 2)) #angry
    M = pd.DataFrame(columns=col_names)
    
    M.stimColor = (["white"]*400)
    M.leftColor = (["white"]*400)
    M.rightColor = (["white"]*400)
    
    M.stimWord = (["HAPPY"]*200+["ANGRY"]*200)
    M.stimImage = (["happy"]*100+["angry"]*100+["happy"]*100+["angry"]*100)
    M.leftWord = (["HAPPY"]*50+["ANGRY"]*50+["HAPPY"]*50+["ANGRY"]*50+["HAPPY"]*50+["ANGRY"]*50+["HAPPY"]*50+["ANGRY"]*50)
    M.rightWord = (["ANGRY"]*50+["HAPPY"]*50+["ANGRY"]*50+["HAPPY"]*50+["ANGRY"]*50+["HAPPY"]*50+["ANGRY"]*50+["HAPPY"]*50)
    for i in range(len(M.stimWord)):
        currentOption = random.randint(0,1)
        if currentOption == 0:
            M.leftImage[i] = 'happy'
            M.rightImage[i] = 'angry'
        else:
            M.leftImage[i] = 'angry'
            M.rightImage[i] = 'happy'
            
    M.loc[(M.stimImage == 'happy') & (M.leftWord == 'HAPPY'), 'response'] = 'buttonA'
    M.loc[(M.stimImage == 'angry') & (M.leftWord == 'ANGRY'), 'response'] = 'buttonA'
    M.loc[(M.stimImage == 'happy') & (M.rightWord == 'HAPPY'), 'response'] = 'buttonB'
    M.loc[(M.stimImage == 'angry') & (M.rightWord == 'ANGRY'), 'response'] = 'buttonB' 
    
    
    M.condition = M.stimImage
    for i in range(len(M)):
        if M.stimImage[i] == 'happy':
            M.stimImage[i] = str(random.choice(odd_list)) +".png"
        elif M.stimImage[i] == 'angry':
            M.stimImage[i] = str(random.choice(even_list)) +".png"
        if M.leftImage[i] == 'happy':
            M.leftImage[i] = str(random.choice(odd_list)) +".png"
            M.rightImage[i] = str(random.choice(even_list)) +".png"
        elif M.leftImage[i] == 'angry':
            M.leftImage[i] = str(random.choice(even_list)) +".png"
            M.rightImage[i] = str(random.choice(odd_list)) +".png"
    
    for i in range(len(M)):
        if M.stimImage[i] == M.leftImage[i]:
            if M.condition[i] == 'happy':
                M.stimImage[i] = str(random.choice(odd_list)) +".png"
            elif M.condition[i] == 'angry':
                M.stimImage[i] = str(random.choice(even_list)) +".png"
        if M.stimImage[i] == M.rightImage[i]:
            if M.condition[i] == 'happy':
                M.stimImage[i] = str(random.choice(odd_list)) +".png"
            elif M.condition[i] == 'angry':
                M.stimImage[i] = str(random.choice(even_list)) +".png"
                
    for i in range(len(M)):
        if M.stimImage[i] == M.leftImage[i]:
            if M.condition[i] == 'happy':
                M.stimImage[i] = str(random.choice(odd_list)) +".png"
            elif M.condition[i] == 'angry':
                M.stimImage[i] = str(random.choice(even_list)) +".png"
        if M.stimImage[i] == M.rightImage[i]:
            if M.condition[i] == 'happy':
                M.stimImage[i] = str(random.choice(odd_list)) +".png"
            elif M.condition[i] == 'angry':
                M.stimImage[i] = str(random.choice(even_list)) +".png"
    for i in range(len(M)):
        if M.stimImage[i] == M.leftImage[i]:
            if M.condition[i] == 'happy':
                M.stimImage[i] = str(random.choice(odd_list)) +".png"
            elif M.condition[i] == 'angry':
                M.stimImage[i] = str(random.choice(even_list)) +".png"
        if M.stimImage[i] == M.rightImage[i]:
            if M.condition[i] == 'happy':
                M.stimImage[i] = str(random.choice(odd_list)) +".png"
            elif M.condition[i] == 'angry':
                M.stimImage[i] = str(random.choice(even_list)) +".png"
        





    M.to_csv('emotion_trialPool_' + str(SbjId) + ".csv", index=False)

if __name__ == '__main__':
   for id in range(0,1):
        main(id)