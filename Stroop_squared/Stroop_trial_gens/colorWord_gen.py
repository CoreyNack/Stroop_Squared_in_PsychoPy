import sys
import numpy as np
import pandas as pd
import random
import math
from random import randint
sys.path.insert(0, '../')

def main(SbjId=0):
    col_names = ['trial', 'stimWord', 'stimColor', 'leftWord', 'leftColor', 'rightWord', 'rightColor', 'response', "stimImage", "leftImage", "rightImage"]
    catList = ['red', 'blue']
    colorList = ['darkred', 'darkblue']

    M = pd.DataFrame(columns=col_names)

    M.stimImage = (["transparent.png"]*400)
    M.leftColor = (["transparent.png"]*400)
    M.rightColor = (["transparent.png"]*400)
    
    M.stimWord = (["RED"]*200+["BLUE"]*200)
    M.stimColor = (["darkred"]*100+["darkblue"]*100+["darkred"]*100+["darkblue"]*100)
    M.leftWord = (["RED"]*50+["BLUE"]*50+["RED"]*50+["BLUE"]*50+["RED"]*50+["BLUE"]*50+["RED"]*50+["BLUE"]*50)
    M.rightWord = (["BLUE"]*50+["RED"]*50+["BLUE"]*50+["RED"]*50+["BLUE"]*50+["RED"]*50+["BLUE"]*50+["RED"]*50)
    for i in range(len(M.stimWord)):
        currentOption = random.randint(0,1)
        if currentOption == 0:
            M.leftColor[i] = 'darkred'
            M.rightColor[i] = 'darkblue'
        else:
            M.leftColor[i] = 'darkblue'
            M.rightColor[i] = 'darkred'
            
    M.loc[(M.stimColor == 'darkred') & (M.leftWord == 'RED'), 'response'] = 'buttonA'
    M.loc[(M.stimColor == 'darkblue') & (M.leftWord == 'BLUE'), 'response'] = 'buttonA'
    M.loc[(M.stimColor == 'darkred') & (M.rightWord == 'RED'), 'response'] = 'buttonB'
    M.loc[(M.stimColor == 'darkblue') & (M.rightWord == 'BLUE'), 'response'] = 'buttonB' 
    
    seq = np.random.permutation(len(M))
    M = M.loc[seq, :].reset_index(drop=True)



    M.to_csv('colorWorld_trialPool_' + str(SbjId) + ".csv", index=False)

if __name__ == '__main__':
   for id in range(0,1):
        main(id)