#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 02, 2024, at 13:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

ins_reps = 0
phase='prac'
trial_count = 0
points = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Stroop_Squared_all_3'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\cnack\\Desktop\\Stroop_squared\\Stroop_Squared_color_only_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "stroop_square_welcome"
stroop_square_welcomeClock = core.Clock()
stroop_block = 0 #needs to be 0 before running
stroop_intro = 0
stroop_welcome_text = visual.TextStim(win=win, name='stroop_welcome_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "ColorWordIns"
ColorWordInsClock = core.Clock()
resp_B_2_image = visual.ImageStim(
    win=win,
    name='resp_B_2_image', 
    image='sin', mask=None,
    ori=0.0, pos=(.5, -.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
resp_A_2_image = visual.ImageStim(
    win=win,
    name='resp_A_2_image', 
    image='sin', mask=None,
    ori=0.0, pos=(-.5, -.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Stim_2_image = visual.ImageStim(
    win=win,
    name='Stim_2_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.1), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
colorWord_ins_txt_maker = visual.TextStim(win=win, name='colorWord_ins_txt_maker',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Stim_2 = visual.TextStim(win=win, name='Stim_2',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
resp_A_2 = visual.TextStim(win=win, name='resp_A_2',
    text='',
    font='Open Sans',
    pos=(-.5, -.2), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
resp_B_2 = visual.TextStim(win=win, name='resp_B_2',
    text='',
    font='Open Sans',
    pos=(.5, -.2), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
buttonA_2 = visual.Rect(
    win=win, name='buttonA_2',
    width=(0.45, 0.25)[0], height=(0.45, 0.25)[1],
    ori=0.0, pos=(-.5, -.2),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-8.0, interpolate=True)
buttonB_2 = visual.Rect(
    win=win, name='buttonB_2',
    width=(0.45, 0.25)[0], height=(0.45, 0.25)[1],
    ori=0.0, pos=(.5, -.2),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-9.0, interpolate=True)
button = visual.ButtonStim(win, 
    text='', font='areal',
    pos=(0, -.35),
    letterHeight=0.03,
    size=(0.40, 0.1), borderWidth=0.0,
    fillColor='white', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button'
)
button.buttonClock = core.Clock()
ins_cue = visual.TextStim(win=win, name='ins_cue',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
checkmark = visual.ImageStim(
    win=win,
    name='checkmark', 
    image='1200px-Green-checkmark.svg.png', mask=None,
    ori=0.0, pos=(.5, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
xmark = visual.ImageStim(
    win=win,
    name='xmark', 
    image='Red_X.svg.png', mask=None,
    ori=0.0, pos=(-0.48, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
correct_txt = visual.TextStim(win=win, name='correct_txt',
    text='(right answer)',
    font='Open Sans',
    pos=(0.5, -0.27), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
wrong_txt = visual.TextStim(win=win, name='wrong_txt',
    text='(wrong answer)',
    font='Open Sans',
    pos=(-0.5, -0.27), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank_text = visual.TextStim(win=win, name='blank_text',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "wait"
waitClock = core.Clock()
timer_image_2 = visual.ImageStim(
    win=win,
    name='timer_image_2', 
    image='Timer.png', mask=None,
    ori=0.0, pos=(0, 0.4), size=[1.2, .03],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
time_left_2 = visual.TextStim(win=win, name='time_left_2',
    text='Time left',
    font='Open Sans',
    pos=(-.67, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
score_lable_2 = visual.TextStim(win=win, name='score_lable_2',
    text='Score',
    font='Open Sans',
    pos=(.67, 0.46), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
score_presenter_2 = visual.TextStim(win=win, name='score_presenter_2',
    text='0',
    font='Open Sans',
    pos=(.67, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ins_again = visual.TextStim(win=win, name='ins_again',
    text='Review instructions again',
    font='Open Sans',
    pos=(-.3, -.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
again_button = visual.Rect(
    win=win, name='again_button',
    width=(.4,.08)[0], height=(.4,.08)[1],
    ori=0.0, pos=(-.3, -.3),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-5.0, interpolate=True)
start_txt = visual.TextStim(win=win, name='start_txt',
    text='',
    font='Open Sans',
    pos=(.3, -.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
start_button = visual.Rect(
    win=win, name='start_button',
    width=(.4,.08)[0], height=(.4,.08)[1],
    ori=0.0, pos=(.3, -.3),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-7.0, interpolate=True)
wait_mouse = event.Mouse(win=win)
x, y = [None, None]
wait_mouse.mouseClock = core.Clock()

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank_text = visual.TextStim(win=win, name='blank_text',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ColorWordIns"
ColorWordInsClock = core.Clock()
resp_B_2_image = visual.ImageStim(
    win=win,
    name='resp_B_2_image', 
    image='sin', mask=None,
    ori=0.0, pos=(.5, -.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
resp_A_2_image = visual.ImageStim(
    win=win,
    name='resp_A_2_image', 
    image='sin', mask=None,
    ori=0.0, pos=(-.5, -.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Stim_2_image = visual.ImageStim(
    win=win,
    name='Stim_2_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.1), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
colorWord_ins_txt_maker = visual.TextStim(win=win, name='colorWord_ins_txt_maker',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Stim_2 = visual.TextStim(win=win, name='Stim_2',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
resp_A_2 = visual.TextStim(win=win, name='resp_A_2',
    text='',
    font='Open Sans',
    pos=(-.5, -.2), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
resp_B_2 = visual.TextStim(win=win, name='resp_B_2',
    text='',
    font='Open Sans',
    pos=(.5, -.2), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
buttonA_2 = visual.Rect(
    win=win, name='buttonA_2',
    width=(0.45, 0.25)[0], height=(0.45, 0.25)[1],
    ori=0.0, pos=(-.5, -.2),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-8.0, interpolate=True)
buttonB_2 = visual.Rect(
    win=win, name='buttonB_2',
    width=(0.45, 0.25)[0], height=(0.45, 0.25)[1],
    ori=0.0, pos=(.5, -.2),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-9.0, interpolate=True)
button = visual.ButtonStim(win, 
    text='', font='areal',
    pos=(0, -.35),
    letterHeight=0.03,
    size=(0.40, 0.1), borderWidth=0.0,
    fillColor='white', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button'
)
button.buttonClock = core.Clock()
ins_cue = visual.TextStim(win=win, name='ins_cue',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
checkmark = visual.ImageStim(
    win=win,
    name='checkmark', 
    image='1200px-Green-checkmark.svg.png', mask=None,
    ori=0.0, pos=(.5, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
xmark = visual.ImageStim(
    win=win,
    name='xmark', 
    image='Red_X.svg.png', mask=None,
    ori=0.0, pos=(-0.48, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
correct_txt = visual.TextStim(win=win, name='correct_txt',
    text='(right answer)',
    font='Open Sans',
    pos=(0.5, -0.27), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
wrong_txt = visual.TextStim(win=win, name='wrong_txt',
    text='(wrong answer)',
    font='Open Sans',
    pos=(-0.5, -0.27), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank_text = visual.TextStim(win=win, name='blank_text',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "wait_2"
wait_2Clock = core.Clock()
timer_image_3 = visual.ImageStim(
    win=win,
    name='timer_image_3', 
    image='Timer.png', mask=None,
    ori=0.0, pos=(0, 0.4), size=[1.2, .03],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
time_left_3 = visual.TextStim(win=win, name='time_left_3',
    text='Time left',
    font='Open Sans',
    pos=(-.67, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
score_lable_3 = visual.TextStim(win=win, name='score_lable_3',
    text='Score',
    font='Open Sans',
    pos=(.67, 0.46), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
score_presenter_3 = visual.TextStim(win=win, name='score_presenter_3',
    text='0',
    font='Open Sans',
    pos=(.67, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
start_txt_2 = visual.TextStim(win=win, name='start_txt_2',
    text='Start practice trials',
    font='Open Sans',
    pos=(.3, -.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
start_button_2 = visual.Rect(
    win=win, name='start_button_2',
    width=(.4,.08)[0], height=(.4,.08)[1],
    ori=0.0, pos=(.3, -.3),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-5.0, interpolate=True)
wait_mouse_2 = event.Mouse(win=win)
x, y = [None, None]
wait_mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "stroop_square_trials"
stroop_square_trialsClock = core.Clock()
stim_image = visual.ImageStim(
    win=win,
    name='stim_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.1), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
resp_A_image = visual.ImageStim(
    win=win,
    name='resp_A_image', 
    image='sin', mask=None,
    ori=0.0, pos=(-.5, -.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
resp_B_image = visual.ImageStim(
    win=win,
    name='resp_B_image', 
    image='sin', mask=None,
    ori=0.0, pos=(.5, -.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
timer_image = visual.ImageStim(
    win=win,
    name='timer_image', 
    image='Timer.png', mask=None,
    ori=0.0, pos=(0, 0.4), size=[1.2, .03],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
timer_mask = visual.Rect(
    win=win, name='timer_mask',
    width=[1.2, .03][0], height=[1.2, .03][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='gray', fillColor='gray',
    opacity=None, depth=-5.0, interpolate=True)
time_left = visual.TextStim(win=win, name='time_left',
    text='Time left',
    font='Open Sans',
    pos=(-.67, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
score_lable = visual.TextStim(win=win, name='score_lable',
    text='Score',
    font='Open Sans',
    pos=(.67, 0.46), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
score_presenter = visual.TextStim(win=win, name='score_presenter',
    text='',
    font='Open Sans',
    pos=(.67, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Stim = visual.TextStim(win=win, name='Stim',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
resp_A = visual.TextStim(win=win, name='resp_A',
    text='',
    font='Open Sans',
    pos=(-.5, -.2), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
resp_B = visual.TextStim(win=win, name='resp_B',
    text='',
    font='Open Sans',
    pos=(.5, -.2), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Stroop_mouse = event.Mouse(win=win)
x, y = [None, None]
Stroop_mouse.mouseClock = core.Clock()
buttonA = visual.Rect(
    win=win, name='buttonA',
    width=(0.45, 0.25)[0], height=(0.45, 0.25)[1],
    ori=0.0, pos=(-.5, -.2),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-13.0, interpolate=True)
buttonB = visual.Rect(
    win=win, name='buttonB',
    width=(0.45, 0.25)[0], height=(0.45, 0.25)[1],
    ori=0.0, pos=(.5, -.2),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-14.0, interpolate=True)
ins_txt_stroop = visual.TextStim(win=win, name='ins_txt_stroop',
    text='Match picture on top to word on bottom',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);

# Initialize components for Routine "stroop_extra_code"
stroop_extra_codeClock = core.Clock()

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank_text = visual.TextStim(win=win, name='blank_text',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
End_text = visual.TextStim(win=win, name='End_text',
    text='You have finished the experiment. You may now find the researcher to recieve SONA credit.\n\nPress spacebar to close the window',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
stroop_all_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='stroop_all_loop')
thisExp.addLoop(stroop_all_loop)  # add the loop to the experiment
thisStroop_all_loop = stroop_all_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStroop_all_loop.rgb)
if thisStroop_all_loop != None:
    for paramName in thisStroop_all_loop:
        exec('{} = thisStroop_all_loop[paramName]'.format(paramName))

for thisStroop_all_loop in stroop_all_loop:
    currentLoop = stroop_all_loop
    # abbreviate parameter names if possible (e.g. rgb = thisStroop_all_loop.rgb)
    if thisStroop_all_loop != None:
        for paramName in thisStroop_all_loop:
            exec('{} = thisStroop_all_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "stroop_square_welcome"-------
    continueRoutine = True
    # update component parameters for each repeat
    phase='prac'
    trial_count = 0
    if stroop_block ==0:
        condition_gen = "colorWorld_trialPool_0.csv"
        stm_height = 0.09
        Stim_2_txt = "RED"
        resp_A_2_txt = "RED"
        resp_B_2_txt = "BLUE"
        Stim_2_color = "darkblue"
        resp_A_2_color = "darkblue"
        resp_B_2_color = "darkred"
        Stim_2_image_setter = "transparent.png"
        resp_A_2_image_setter = "transparent.png"
        resp_B_2_image_setter = "transparent.png"
        stroop_image_size = (0,0)
        ins_cue_txt = "(text is in blue color)" 
        stroop_intro = "Next, we will perform a task where you must name the color of a word while ignoring the word's meaning.\nPress spacebar to view instructions"
    elif stroop_block ==1:
        condition_gen = "emotion_trialPool_0.csv"
        stm_height = .06
        Stim_2_txt = "ANGRY"
        resp_A_2_txt = "ANGRY"
        resp_B_2_txt = "HAPPY"
        Stim_2_color = "white"
        resp_A_2_color = "white"
        resp_B_2_color = "white"
        Stim_2_image_setter = "17.png"
        resp_A_2_image_setter = "17.png"
        resp_B_2_image_setter = "18.png"
        ins_cue_txt = "(face is happy)"
        stroop_image_size = (0.2, 0.25)
        stroop_intro = "Next, we will perform a task where you must identify the emotion shown by a face while ignoring a word written over the face.\nPress spacebar to view instructions"
    elif stroop_block ==2:
        condition_gen = "finance_trialPool_0.csv"
        stm_height = .06
        Stim_2_txt = "LOSS"
        resp_A_2_txt = "LOSS"
        resp_B_2_txt = "GAIN"
        Stim_2_color = "white"
        Stim_2_color = "white"
        resp_A_2_color = "white"
        resp_B_2_color = "white"
        Stim_2_image_setter = "1.png"
        resp_A_2_image_setter = "1.png"
        resp_B_2_image_setter = "2.png"
        stroop_image_size = (0.27, 0.1611405)
        ins_cue_txt = "(chart shows a gain)"
        stroop_intro = "Next, we will perform a task where you must identify the trend on a stock market chart while ignoring a word written over the chart.\nPress spacebar to view instructions"
    stroop_welcome_text.setText(stroop_intro)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    stroop_square_welcomeComponents = [stroop_welcome_text, key_resp]
    for thisComponent in stroop_square_welcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stroop_square_welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stroop_square_welcome"-------
    while continueRoutine:
        # get current time
        t = stroop_square_welcomeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stroop_square_welcomeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stroop_welcome_text* updates
        if stroop_welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stroop_welcome_text.frameNStart = frameN  # exact frame index
            stroop_welcome_text.tStart = t  # local t and not account for scr refresh
            stroop_welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stroop_welcome_text, 'tStartRefresh')  # time at next scr refresh
            stroop_welcome_text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stroop_square_welcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stroop_square_welcome"-------
    for thisComponent in stroop_square_welcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stroop_block = stroop_block +1
    # the Routine "stroop_square_welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    pracTOreal_loop = data.TrialHandler(nReps=2.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='pracTOreal_loop')
    thisExp.addLoop(pracTOreal_loop)  # add the loop to the experiment
    thisPracTOreal_loop = pracTOreal_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracTOreal_loop.rgb)
    if thisPracTOreal_loop != None:
        for paramName in thisPracTOreal_loop:
            exec('{} = thisPracTOreal_loop[paramName]'.format(paramName))
    
    for thisPracTOreal_loop in pracTOreal_loop:
        currentLoop = pracTOreal_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPracTOreal_loop.rgb)
        if thisPracTOreal_loop != None:
            for paramName in thisPracTOreal_loop:
                exec('{} = thisPracTOreal_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ColorWordIns"-------
        continueRoutine = True
        # update component parameters for each repeat
        if trial_count != 0:
            phase = "main"
        
        
        if stroop_block ==1:
            if phase == "prac":
                ins_txt = "See what color the top word is. Select that color from the two options below. DON'T pay attention to what the top word says or the color of the two options below. It's important to match the color of the top word with the meaning of the word below.\nWe will begin with a practice round. You will have 30 seconds to earn as many points as possible. Incorrect responses remove one point."
                button_msg = "        Begin Practice"
                WAIT_TXT = 'Start practice trials'
            else:
                ins_txt = "That's it for practice. Please review instructions one last time:\nSee what color the top word is. Select that color from the two opotions below. DON'T pay attention to what the top word says or the color of the two options below. It's important to match the color of the top word with the meaning of the word below.\nYou will have 90 seconds to earn as many points as possible."
                button_msg = "     Begin Experiment"
                WAIT_TXT = 'Start main trials'
                
        if stroop_block ==2:
            if phase == "prac":
                ins_txt = "See what emotion the top face is showing. Select that emotion's name from the two opotions below. DON'T pay attention to what the top word says or face of the two options below. It's important to match the displayed emotion of the top face with the meaning of the word below.\nWe will begin with a practice round. You will have 30 seconds to earn as many points as possible. Incorrect responses remove one point."
                button_msg = "        Begin Practice"
                WAIT_TXT = 'Start practice trials'
            else:
                ins_txt = "That's it for practice. Please review instructions one last time:\nSee what emotion the top face is showing. Select that emotion's name from the two opotions below. DON'T pay attention to what the top word says or face of the two options below. It's important to match the displayed emotion of the top face with the meaning of the word below.\nYou will have 90 seconds to earn as many points as possible."
                button_msg = "     Begin Experiment"
                WAIT_TXT = 'Start main trials'
                
        if stroop_block ==3:
            if phase == "prac":
                ins_txt = "See what price trend the stock chart is showing. Select the word for that trend from the two opotions below. DON'T pay attention to what the top word says or trend on the chart of the two options below. It's important to match the displayed trend of the top chart with the meaning of the word below.\nWe will begin with a practice round. You will have 30 seconds to earn as many points as possible. Incorrect responses remove one point."
                button_msg = "        Begin Practice"
                WAIT_TXT = 'Start practice trials'
            else:
                ins_txt = "That's it for practice. Please review instructions one last time:\nSee what price trend the stock chart is showing. Select the word for that trend from the two opotions below. DON'T pay attention to what the top word says or trend on the chart of the two options below. It's important to match the displayed trend of the top chart with the meaning of the word below.\nYou will have 90 seconds to earn as many points as possible."
                button_msg = "     Begin Experiment"
                WAIT_TXT = 'Start main trials'
        resp_B_2_image.setSize(stroop_image_size)
        resp_B_2_image.setImage(resp_B_2_image_setter)
        resp_A_2_image.setSize(stroop_image_size)
        resp_A_2_image.setImage(resp_A_2_image_setter)
        Stim_2_image.setSize(stroop_image_size)
        Stim_2_image.setImage(Stim_2_image_setter)
        colorWord_ins_txt_maker.setText(ins_txt
)
        Stim_2.setColor(Stim_2_color, colorSpace='rgb')
        Stim_2.setText(Stim_2_txt)
        resp_A_2.setColor(resp_A_2_color, colorSpace='rgb')
        resp_A_2.setText(resp_A_2_txt)
        resp_B_2.setColor(resp_B_2_color, colorSpace='rgb')
        resp_B_2.setText(resp_B_2_txt)
        button.setText(button_msg)
        ins_cue.setText(ins_cue_txt)
        # keep track of which components have finished
        ColorWordInsComponents = [resp_B_2_image, resp_A_2_image, Stim_2_image, colorWord_ins_txt_maker, Stim_2, resp_A_2, resp_B_2, buttonA_2, buttonB_2, button, ins_cue, checkmark, xmark, correct_txt, wrong_txt]
        for thisComponent in ColorWordInsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ColorWordInsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ColorWordIns"-------
        while continueRoutine:
            # get current time
            t = ColorWordInsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ColorWordInsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *resp_B_2_image* updates
            if resp_B_2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_B_2_image.frameNStart = frameN  # exact frame index
                resp_B_2_image.tStart = t  # local t and not account for scr refresh
                resp_B_2_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_B_2_image, 'tStartRefresh')  # time at next scr refresh
                resp_B_2_image.setAutoDraw(True)
            
            # *resp_A_2_image* updates
            if resp_A_2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_A_2_image.frameNStart = frameN  # exact frame index
                resp_A_2_image.tStart = t  # local t and not account for scr refresh
                resp_A_2_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_A_2_image, 'tStartRefresh')  # time at next scr refresh
                resp_A_2_image.setAutoDraw(True)
            
            # *Stim_2_image* updates
            if Stim_2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim_2_image.frameNStart = frameN  # exact frame index
                Stim_2_image.tStart = t  # local t and not account for scr refresh
                Stim_2_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_2_image, 'tStartRefresh')  # time at next scr refresh
                Stim_2_image.setAutoDraw(True)
            
            # *colorWord_ins_txt_maker* updates
            if colorWord_ins_txt_maker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                colorWord_ins_txt_maker.frameNStart = frameN  # exact frame index
                colorWord_ins_txt_maker.tStart = t  # local t and not account for scr refresh
                colorWord_ins_txt_maker.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(colorWord_ins_txt_maker, 'tStartRefresh')  # time at next scr refresh
                colorWord_ins_txt_maker.setAutoDraw(True)
            
            # *Stim_2* updates
            if Stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim_2.frameNStart = frameN  # exact frame index
                Stim_2.tStart = t  # local t and not account for scr refresh
                Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_2, 'tStartRefresh')  # time at next scr refresh
                Stim_2.setAutoDraw(True)
            
            # *resp_A_2* updates
            if resp_A_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_A_2.frameNStart = frameN  # exact frame index
                resp_A_2.tStart = t  # local t and not account for scr refresh
                resp_A_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_A_2, 'tStartRefresh')  # time at next scr refresh
                resp_A_2.setAutoDraw(True)
            
            # *resp_B_2* updates
            if resp_B_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_B_2.frameNStart = frameN  # exact frame index
                resp_B_2.tStart = t  # local t and not account for scr refresh
                resp_B_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_B_2, 'tStartRefresh')  # time at next scr refresh
                resp_B_2.setAutoDraw(True)
            
            # *buttonA_2* updates
            if buttonA_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buttonA_2.frameNStart = frameN  # exact frame index
                buttonA_2.tStart = t  # local t and not account for scr refresh
                buttonA_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buttonA_2, 'tStartRefresh')  # time at next scr refresh
                buttonA_2.setAutoDraw(True)
            
            # *buttonB_2* updates
            if buttonB_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                buttonB_2.frameNStart = frameN  # exact frame index
                buttonB_2.tStart = t  # local t and not account for scr refresh
                buttonB_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buttonB_2, 'tStartRefresh')  # time at next scr refresh
                buttonB_2.setAutoDraw(True)
            
            # *button* updates
            if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button.frameNStart = frameN  # exact frame index
                button.tStart = t  # local t and not account for scr refresh
                button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
                button.setAutoDraw(True)
            if button.status == STARTED:
                # check whether button has been pressed
                if button.isClicked:
                    if not button.wasClicked:
                        button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                        button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
                    else:
                        button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
                    if not button.wasClicked:
                        continueRoutine = False  # end routine when button is clicked
                        None
                    button.wasClicked = True  # if button is still clicked next frame, it is not a new click
                else:
                    button.wasClicked = False  # if button is clicked next frame, it is a new click
            else:
                button.wasClicked = False  # if button is clicked next frame, it is a new click
            
            # *ins_cue* updates
            if ins_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ins_cue.frameNStart = frameN  # exact frame index
                ins_cue.tStart = t  # local t and not account for scr refresh
                ins_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ins_cue, 'tStartRefresh')  # time at next scr refresh
                ins_cue.setAutoDraw(True)
            
            # *checkmark* updates
            if checkmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                checkmark.frameNStart = frameN  # exact frame index
                checkmark.tStart = t  # local t and not account for scr refresh
                checkmark.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(checkmark, 'tStartRefresh')  # time at next scr refresh
                checkmark.setAutoDraw(True)
            
            # *xmark* updates
            if xmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                xmark.frameNStart = frameN  # exact frame index
                xmark.tStart = t  # local t and not account for scr refresh
                xmark.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(xmark, 'tStartRefresh')  # time at next scr refresh
                xmark.setAutoDraw(True)
            
            # *correct_txt* updates
            if correct_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                correct_txt.frameNStart = frameN  # exact frame index
                correct_txt.tStart = t  # local t and not account for scr refresh
                correct_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(correct_txt, 'tStartRefresh')  # time at next scr refresh
                correct_txt.setAutoDraw(True)
            
            # *wrong_txt* updates
            if wrong_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wrong_txt.frameNStart = frameN  # exact frame index
                wrong_txt.tStart = t  # local t and not account for scr refresh
                wrong_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wrong_txt, 'tStartRefresh')  # time at next scr refresh
                wrong_txt.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ColorWordInsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ColorWordIns"-------
        for thisComponent in ColorWordInsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "ColorWordIns" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "blank"-------
        continueRoutine = True
        routineTimer.add(0.020000)
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [blank_text]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_text* updates
            if blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_text.frameNStart = frameN  # exact frame index
                blank_text.tStart = t  # local t and not account for scr refresh
                blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_text, 'tStartRefresh')  # time at next scr refresh
                blank_text.setAutoDraw(True)
            if blank_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank_text.tStartRefresh + .02-frameTolerance:
                    # keep track of stop time/frame for later
                    blank_text.tStop = t  # not accounting for scr refresh
                    blank_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank_text, 'tStopRefresh')  # time at next scr refresh
                    blank_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blank"-------
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "wait"-------
        continueRoutine = True
        # update component parameters for each repeat
        start_txt.setText(WAIT_TXT)
        # setup some python lists for storing info about the wait_mouse
        wait_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        waitComponents = [timer_image_2, time_left_2, score_lable_2, score_presenter_2, ins_again, again_button, start_txt, start_button, wait_mouse]
        for thisComponent in waitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wait"-------
        while continueRoutine:
            # get current time
            t = waitClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=waitClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *timer_image_2* updates
            if timer_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer_image_2.frameNStart = frameN  # exact frame index
                timer_image_2.tStart = t  # local t and not account for scr refresh
                timer_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer_image_2, 'tStartRefresh')  # time at next scr refresh
                timer_image_2.setAutoDraw(True)
            
            # *time_left_2* updates
            if time_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                time_left_2.frameNStart = frameN  # exact frame index
                time_left_2.tStart = t  # local t and not account for scr refresh
                time_left_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(time_left_2, 'tStartRefresh')  # time at next scr refresh
                time_left_2.setAutoDraw(True)
            
            # *score_lable_2* updates
            if score_lable_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_lable_2.frameNStart = frameN  # exact frame index
                score_lable_2.tStart = t  # local t and not account for scr refresh
                score_lable_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_lable_2, 'tStartRefresh')  # time at next scr refresh
                score_lable_2.setAutoDraw(True)
            
            # *score_presenter_2* updates
            if score_presenter_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_presenter_2.frameNStart = frameN  # exact frame index
                score_presenter_2.tStart = t  # local t and not account for scr refresh
                score_presenter_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_presenter_2, 'tStartRefresh')  # time at next scr refresh
                score_presenter_2.setAutoDraw(True)
            
            # *ins_again* updates
            if ins_again.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ins_again.frameNStart = frameN  # exact frame index
                ins_again.tStart = t  # local t and not account for scr refresh
                ins_again.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ins_again, 'tStartRefresh')  # time at next scr refresh
                ins_again.setAutoDraw(True)
            
            # *again_button* updates
            if again_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                again_button.frameNStart = frameN  # exact frame index
                again_button.tStart = t  # local t and not account for scr refresh
                again_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(again_button, 'tStartRefresh')  # time at next scr refresh
                again_button.setAutoDraw(True)
            
            # *start_txt* updates
            if start_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_txt.frameNStart = frameN  # exact frame index
                start_txt.tStart = t  # local t and not account for scr refresh
                start_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_txt, 'tStartRefresh')  # time at next scr refresh
                start_txt.setAutoDraw(True)
            
            # *start_button* updates
            if start_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_button.frameNStart = frameN  # exact frame index
                start_button.tStart = t  # local t and not account for scr refresh
                start_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_button, 'tStartRefresh')  # time at next scr refresh
                start_button.setAutoDraw(True)
            # *wait_mouse* updates
            if wait_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_mouse.frameNStart = frameN  # exact frame index
                wait_mouse.tStart = t  # local t and not account for scr refresh
                wait_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_mouse, 'tStartRefresh')  # time at next scr refresh
                wait_mouse.status = STARTED
                wait_mouse.mouseClock.reset()
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if wait_mouse.status == STARTED:  # only update if started and not finished!
                buttons = wait_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([again_button, start_button])
                            clickableList = [again_button, start_button]
                        except:
                            clickableList = [[again_button, start_button]]
                        for obj in clickableList:
                            if obj.contains(wait_mouse):
                                gotValidClick = True
                                wait_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wait"-------
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for pracTOreal_loop (TrialHandler)
        if wait_mouse.clicked_name[0] == 'again_button':
            ins_reps = 1
        else:
            ins_reps = 0
        if phase == 'prac':
            duration = 30
        else:
            duration = 90
            
        points = 0
        trial_count = 0
        # the Routine "wait" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        extra_ins = data.TrialHandler(nReps=ins_reps, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='extra_ins')
        thisExp.addLoop(extra_ins)  # add the loop to the experiment
        thisExtra_in = extra_ins.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExtra_in.rgb)
        if thisExtra_in != None:
            for paramName in thisExtra_in:
                exec('{} = thisExtra_in[paramName]'.format(paramName))
        
        for thisExtra_in in extra_ins:
            currentLoop = extra_ins
            # abbreviate parameter names if possible (e.g. rgb = thisExtra_in.rgb)
            if thisExtra_in != None:
                for paramName in thisExtra_in:
                    exec('{} = thisExtra_in[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "blank"-------
            continueRoutine = True
            routineTimer.add(0.020000)
            # update component parameters for each repeat
            # keep track of which components have finished
            blankComponents = [blank_text]
            for thisComponent in blankComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "blank"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = blankClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=blankClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank_text* updates
                if blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blank_text.frameNStart = frameN  # exact frame index
                    blank_text.tStart = t  # local t and not account for scr refresh
                    blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blank_text, 'tStartRefresh')  # time at next scr refresh
                    blank_text.setAutoDraw(True)
                if blank_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blank_text.tStartRefresh + .02-frameTolerance:
                        # keep track of stop time/frame for later
                        blank_text.tStop = t  # not accounting for scr refresh
                        blank_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(blank_text, 'tStopRefresh')  # time at next scr refresh
                        blank_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blankComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "blank"-------
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # ------Prepare to start Routine "ColorWordIns"-------
            continueRoutine = True
            # update component parameters for each repeat
            if trial_count != 0:
                phase = "main"
            
            
            if stroop_block ==1:
                if phase == "prac":
                    ins_txt = "See what color the top word is. Select that color from the two options below. DON'T pay attention to what the top word says or the color of the two options below. It's important to match the color of the top word with the meaning of the word below.\nWe will begin with a practice round. You will have 30 seconds to earn as many points as possible. Incorrect responses remove one point."
                    button_msg = "        Begin Practice"
                    WAIT_TXT = 'Start practice trials'
                else:
                    ins_txt = "That's it for practice. Please review instructions one last time:\nSee what color the top word is. Select that color from the two opotions below. DON'T pay attention to what the top word says or the color of the two options below. It's important to match the color of the top word with the meaning of the word below.\nYou will have 90 seconds to earn as many points as possible."
                    button_msg = "     Begin Experiment"
                    WAIT_TXT = 'Start main trials'
                    
            if stroop_block ==2:
                if phase == "prac":
                    ins_txt = "See what emotion the top face is showing. Select that emotion's name from the two opotions below. DON'T pay attention to what the top word says or face of the two options below. It's important to match the displayed emotion of the top face with the meaning of the word below.\nWe will begin with a practice round. You will have 30 seconds to earn as many points as possible. Incorrect responses remove one point."
                    button_msg = "        Begin Practice"
                    WAIT_TXT = 'Start practice trials'
                else:
                    ins_txt = "That's it for practice. Please review instructions one last time:\nSee what emotion the top face is showing. Select that emotion's name from the two opotions below. DON'T pay attention to what the top word says or face of the two options below. It's important to match the displayed emotion of the top face with the meaning of the word below.\nYou will have 90 seconds to earn as many points as possible."
                    button_msg = "     Begin Experiment"
                    WAIT_TXT = 'Start main trials'
                    
            if stroop_block ==3:
                if phase == "prac":
                    ins_txt = "See what price trend the stock chart is showing. Select the word for that trend from the two opotions below. DON'T pay attention to what the top word says or trend on the chart of the two options below. It's important to match the displayed trend of the top chart with the meaning of the word below.\nWe will begin with a practice round. You will have 30 seconds to earn as many points as possible. Incorrect responses remove one point."
                    button_msg = "        Begin Practice"
                    WAIT_TXT = 'Start practice trials'
                else:
                    ins_txt = "That's it for practice. Please review instructions one last time:\nSee what price trend the stock chart is showing. Select the word for that trend from the two opotions below. DON'T pay attention to what the top word says or trend on the chart of the two options below. It's important to match the displayed trend of the top chart with the meaning of the word below.\nYou will have 90 seconds to earn as many points as possible."
                    button_msg = "     Begin Experiment"
                    WAIT_TXT = 'Start main trials'
            resp_B_2_image.setSize(stroop_image_size)
            resp_B_2_image.setImage(resp_B_2_image_setter)
            resp_A_2_image.setSize(stroop_image_size)
            resp_A_2_image.setImage(resp_A_2_image_setter)
            Stim_2_image.setSize(stroop_image_size)
            Stim_2_image.setImage(Stim_2_image_setter)
            colorWord_ins_txt_maker.setText(ins_txt
)
            Stim_2.setColor(Stim_2_color, colorSpace='rgb')
            Stim_2.setText(Stim_2_txt)
            resp_A_2.setColor(resp_A_2_color, colorSpace='rgb')
            resp_A_2.setText(resp_A_2_txt)
            resp_B_2.setColor(resp_B_2_color, colorSpace='rgb')
            resp_B_2.setText(resp_B_2_txt)
            button.setText(button_msg)
            ins_cue.setText(ins_cue_txt)
            # keep track of which components have finished
            ColorWordInsComponents = [resp_B_2_image, resp_A_2_image, Stim_2_image, colorWord_ins_txt_maker, Stim_2, resp_A_2, resp_B_2, buttonA_2, buttonB_2, button, ins_cue, checkmark, xmark, correct_txt, wrong_txt]
            for thisComponent in ColorWordInsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ColorWordInsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ColorWordIns"-------
            while continueRoutine:
                # get current time
                t = ColorWordInsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ColorWordInsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *resp_B_2_image* updates
                if resp_B_2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    resp_B_2_image.frameNStart = frameN  # exact frame index
                    resp_B_2_image.tStart = t  # local t and not account for scr refresh
                    resp_B_2_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_B_2_image, 'tStartRefresh')  # time at next scr refresh
                    resp_B_2_image.setAutoDraw(True)
                
                # *resp_A_2_image* updates
                if resp_A_2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    resp_A_2_image.frameNStart = frameN  # exact frame index
                    resp_A_2_image.tStart = t  # local t and not account for scr refresh
                    resp_A_2_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_A_2_image, 'tStartRefresh')  # time at next scr refresh
                    resp_A_2_image.setAutoDraw(True)
                
                # *Stim_2_image* updates
                if Stim_2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Stim_2_image.frameNStart = frameN  # exact frame index
                    Stim_2_image.tStart = t  # local t and not account for scr refresh
                    Stim_2_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stim_2_image, 'tStartRefresh')  # time at next scr refresh
                    Stim_2_image.setAutoDraw(True)
                
                # *colorWord_ins_txt_maker* updates
                if colorWord_ins_txt_maker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    colorWord_ins_txt_maker.frameNStart = frameN  # exact frame index
                    colorWord_ins_txt_maker.tStart = t  # local t and not account for scr refresh
                    colorWord_ins_txt_maker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(colorWord_ins_txt_maker, 'tStartRefresh')  # time at next scr refresh
                    colorWord_ins_txt_maker.setAutoDraw(True)
                
                # *Stim_2* updates
                if Stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Stim_2.frameNStart = frameN  # exact frame index
                    Stim_2.tStart = t  # local t and not account for scr refresh
                    Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stim_2, 'tStartRefresh')  # time at next scr refresh
                    Stim_2.setAutoDraw(True)
                
                # *resp_A_2* updates
                if resp_A_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    resp_A_2.frameNStart = frameN  # exact frame index
                    resp_A_2.tStart = t  # local t and not account for scr refresh
                    resp_A_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_A_2, 'tStartRefresh')  # time at next scr refresh
                    resp_A_2.setAutoDraw(True)
                
                # *resp_B_2* updates
                if resp_B_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    resp_B_2.frameNStart = frameN  # exact frame index
                    resp_B_2.tStart = t  # local t and not account for scr refresh
                    resp_B_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_B_2, 'tStartRefresh')  # time at next scr refresh
                    resp_B_2.setAutoDraw(True)
                
                # *buttonA_2* updates
                if buttonA_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    buttonA_2.frameNStart = frameN  # exact frame index
                    buttonA_2.tStart = t  # local t and not account for scr refresh
                    buttonA_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(buttonA_2, 'tStartRefresh')  # time at next scr refresh
                    buttonA_2.setAutoDraw(True)
                
                # *buttonB_2* updates
                if buttonB_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    buttonB_2.frameNStart = frameN  # exact frame index
                    buttonB_2.tStart = t  # local t and not account for scr refresh
                    buttonB_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(buttonB_2, 'tStartRefresh')  # time at next scr refresh
                    buttonB_2.setAutoDraw(True)
                
                # *button* updates
                if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button.frameNStart = frameN  # exact frame index
                    button.tStart = t  # local t and not account for scr refresh
                    button.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
                    button.setAutoDraw(True)
                if button.status == STARTED:
                    # check whether button has been pressed
                    if button.isClicked:
                        if not button.wasClicked:
                            button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                            button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
                        else:
                            button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
                        if not button.wasClicked:
                            continueRoutine = False  # end routine when button is clicked
                            None
                        button.wasClicked = True  # if button is still clicked next frame, it is not a new click
                    else:
                        button.wasClicked = False  # if button is clicked next frame, it is a new click
                else:
                    button.wasClicked = False  # if button is clicked next frame, it is a new click
                
                # *ins_cue* updates
                if ins_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ins_cue.frameNStart = frameN  # exact frame index
                    ins_cue.tStart = t  # local t and not account for scr refresh
                    ins_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ins_cue, 'tStartRefresh')  # time at next scr refresh
                    ins_cue.setAutoDraw(True)
                
                # *checkmark* updates
                if checkmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    checkmark.frameNStart = frameN  # exact frame index
                    checkmark.tStart = t  # local t and not account for scr refresh
                    checkmark.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(checkmark, 'tStartRefresh')  # time at next scr refresh
                    checkmark.setAutoDraw(True)
                
                # *xmark* updates
                if xmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    xmark.frameNStart = frameN  # exact frame index
                    xmark.tStart = t  # local t and not account for scr refresh
                    xmark.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(xmark, 'tStartRefresh')  # time at next scr refresh
                    xmark.setAutoDraw(True)
                
                # *correct_txt* updates
                if correct_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    correct_txt.frameNStart = frameN  # exact frame index
                    correct_txt.tStart = t  # local t and not account for scr refresh
                    correct_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(correct_txt, 'tStartRefresh')  # time at next scr refresh
                    correct_txt.setAutoDraw(True)
                
                # *wrong_txt* updates
                if wrong_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    wrong_txt.frameNStart = frameN  # exact frame index
                    wrong_txt.tStart = t  # local t and not account for scr refresh
                    wrong_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(wrong_txt, 'tStartRefresh')  # time at next scr refresh
                    wrong_txt.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ColorWordInsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ColorWordIns"-------
            for thisComponent in ColorWordInsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ColorWordIns" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "blank"-------
            continueRoutine = True
            routineTimer.add(0.020000)
            # update component parameters for each repeat
            # keep track of which components have finished
            blankComponents = [blank_text]
            for thisComponent in blankComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "blank"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = blankClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=blankClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank_text* updates
                if blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blank_text.frameNStart = frameN  # exact frame index
                    blank_text.tStart = t  # local t and not account for scr refresh
                    blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blank_text, 'tStartRefresh')  # time at next scr refresh
                    blank_text.setAutoDraw(True)
                if blank_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blank_text.tStartRefresh + .02-frameTolerance:
                        # keep track of stop time/frame for later
                        blank_text.tStop = t  # not accounting for scr refresh
                        blank_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(blank_text, 'tStopRefresh')  # time at next scr refresh
                        blank_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blankComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "blank"-------
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # ------Prepare to start Routine "wait_2"-------
            continueRoutine = True
            # update component parameters for each repeat
            # setup some python lists for storing info about the wait_mouse_2
            wait_mouse_2.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            wait_2Components = [timer_image_3, time_left_3, score_lable_3, score_presenter_3, start_txt_2, start_button_2, wait_mouse_2]
            for thisComponent in wait_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            wait_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "wait_2"-------
            while continueRoutine:
                # get current time
                t = wait_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=wait_2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *timer_image_3* updates
                if timer_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    timer_image_3.frameNStart = frameN  # exact frame index
                    timer_image_3.tStart = t  # local t and not account for scr refresh
                    timer_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(timer_image_3, 'tStartRefresh')  # time at next scr refresh
                    timer_image_3.setAutoDraw(True)
                
                # *time_left_3* updates
                if time_left_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    time_left_3.frameNStart = frameN  # exact frame index
                    time_left_3.tStart = t  # local t and not account for scr refresh
                    time_left_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(time_left_3, 'tStartRefresh')  # time at next scr refresh
                    time_left_3.setAutoDraw(True)
                
                # *score_lable_3* updates
                if score_lable_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    score_lable_3.frameNStart = frameN  # exact frame index
                    score_lable_3.tStart = t  # local t and not account for scr refresh
                    score_lable_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(score_lable_3, 'tStartRefresh')  # time at next scr refresh
                    score_lable_3.setAutoDraw(True)
                
                # *score_presenter_3* updates
                if score_presenter_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    score_presenter_3.frameNStart = frameN  # exact frame index
                    score_presenter_3.tStart = t  # local t and not account for scr refresh
                    score_presenter_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(score_presenter_3, 'tStartRefresh')  # time at next scr refresh
                    score_presenter_3.setAutoDraw(True)
                
                # *start_txt_2* updates
                if start_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    start_txt_2.frameNStart = frameN  # exact frame index
                    start_txt_2.tStart = t  # local t and not account for scr refresh
                    start_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(start_txt_2, 'tStartRefresh')  # time at next scr refresh
                    start_txt_2.setAutoDraw(True)
                
                # *start_button_2* updates
                if start_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    start_button_2.frameNStart = frameN  # exact frame index
                    start_button_2.tStart = t  # local t and not account for scr refresh
                    start_button_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(start_button_2, 'tStartRefresh')  # time at next scr refresh
                    start_button_2.setAutoDraw(True)
                # *wait_mouse_2* updates
                if wait_mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    wait_mouse_2.frameNStart = frameN  # exact frame index
                    wait_mouse_2.tStart = t  # local t and not account for scr refresh
                    wait_mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(wait_mouse_2, 'tStartRefresh')  # time at next scr refresh
                    wait_mouse_2.status = STARTED
                    wait_mouse_2.mouseClock.reset()
                    prevButtonState = wait_mouse_2.getPressed()  # if button is down already this ISN'T a new click
                if wait_mouse_2.status == STARTED:  # only update if started and not finished!
                    buttons = wait_mouse_2.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(start_button)
                                clickableList = start_button
                            except:
                                clickableList = [start_button]
                            for obj in clickableList:
                                if obj.contains(wait_mouse_2):
                                    gotValidClick = True
                                    wait_mouse_2.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in wait_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "wait_2"-------
            for thisComponent in wait_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for extra_ins (TrialHandler)
            # the Routine "wait_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed ins_reps repeats of 'extra_ins'
        
        
        # set up handler to look after randomisation of conditions etc
        stroop_trials_loop = data.TrialHandler(nReps=400.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(condition_gen),
            seed=None, name='stroop_trials_loop')
        thisExp.addLoop(stroop_trials_loop)  # add the loop to the experiment
        thisStroop_trials_loop = stroop_trials_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisStroop_trials_loop.rgb)
        if thisStroop_trials_loop != None:
            for paramName in thisStroop_trials_loop:
                exec('{} = thisStroop_trials_loop[paramName]'.format(paramName))
        
        for thisStroop_trials_loop in stroop_trials_loop:
            currentLoop = stroop_trials_loop
            # abbreviate parameter names if possible (e.g. rgb = thisStroop_trials_loop.rgb)
            if thisStroop_trials_loop != None:
                for paramName in thisStroop_trials_loop:
                    exec('{} = thisStroop_trials_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "stroop_square_trials"-------
            continueRoutine = True
            # update component parameters for each repeat
            if trial_count == 0:
                trial_clock = core.Clock()
            stim_image.setSize(stroop_image_size)
            stim_image.setImage(stimImage)
            resp_A_image.setSize(stroop_image_size)
            resp_A_image.setImage(leftImage)
            resp_B_image.setSize(stroop_image_size)
            resp_B_image.setImage(rightImage)
            score_presenter.setText(points)
            Stim.setColor(stimColor, colorSpace='rgb')
            Stim.setText(stimWord)
            Stim.setHeight(stm_height)
            resp_A.setColor(leftColor, colorSpace='rgb')
            resp_A.setText(leftWord)
            resp_A.setHeight(stm_height)
            resp_B.setColor(rightColor, colorSpace='rgb')
            resp_B.setText(rightWord)
            resp_B.setHeight(stm_height)
            # setup some python lists for storing info about the Stroop_mouse
            Stroop_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            stroop_square_trialsComponents = [stim_image, resp_A_image, resp_B_image, timer_image, timer_mask, time_left, score_lable, score_presenter, Stim, resp_A, resp_B, Stroop_mouse, buttonA, buttonB, ins_txt_stroop]
            for thisComponent in stroop_square_trialsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            stroop_square_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "stroop_square_trials"-------
            while continueRoutine:
                # get current time
                t = stroop_square_trialsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=stroop_square_trialsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                Exp_dur = duration
                rate = 1.19/duration
                maskX = 1.19
                maskX = 1.19 - (rate*trial_clock.getTime())
                mask_position = [maskX, 0.4]
                
                if trial_clock.getTime() >= duration:
                    continueRoutine = False # end the current routine
                    stroop_trials_loop.finished = True # exit the current loop
                    Stroop_mouse.clicked_name = [999,999]
                    if phase == "prac":
                        phase = "main"
                
                # *stim_image* updates
                if stim_image.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
                    # keep track of start time/frame for later
                    stim_image.frameNStart = frameN  # exact frame index
                    stim_image.tStart = t  # local t and not account for scr refresh
                    stim_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_image, 'tStartRefresh')  # time at next scr refresh
                    stim_image.setAutoDraw(True)
                
                # *resp_A_image* updates
                if resp_A_image.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
                    # keep track of start time/frame for later
                    resp_A_image.frameNStart = frameN  # exact frame index
                    resp_A_image.tStart = t  # local t and not account for scr refresh
                    resp_A_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_A_image, 'tStartRefresh')  # time at next scr refresh
                    resp_A_image.setAutoDraw(True)
                
                # *resp_B_image* updates
                if resp_B_image.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
                    # keep track of start time/frame for later
                    resp_B_image.frameNStart = frameN  # exact frame index
                    resp_B_image.tStart = t  # local t and not account for scr refresh
                    resp_B_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_B_image, 'tStartRefresh')  # time at next scr refresh
                    resp_B_image.setAutoDraw(True)
                
                # *timer_image* updates
                if timer_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    timer_image.frameNStart = frameN  # exact frame index
                    timer_image.tStart = t  # local t and not account for scr refresh
                    timer_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(timer_image, 'tStartRefresh')  # time at next scr refresh
                    timer_image.setAutoDraw(True)
                
                # *timer_mask* updates
                if timer_mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    timer_mask.frameNStart = frameN  # exact frame index
                    timer_mask.tStart = t  # local t and not account for scr refresh
                    timer_mask.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(timer_mask, 'tStartRefresh')  # time at next scr refresh
                    timer_mask.setAutoDraw(True)
                if timer_mask.status == STARTED:  # only update if drawing
                    timer_mask.setPos(mask_position, log=False)
                
                # *time_left* updates
                if time_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    time_left.frameNStart = frameN  # exact frame index
                    time_left.tStart = t  # local t and not account for scr refresh
                    time_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(time_left, 'tStartRefresh')  # time at next scr refresh
                    time_left.setAutoDraw(True)
                
                # *score_lable* updates
                if score_lable.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    score_lable.frameNStart = frameN  # exact frame index
                    score_lable.tStart = t  # local t and not account for scr refresh
                    score_lable.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(score_lable, 'tStartRefresh')  # time at next scr refresh
                    score_lable.setAutoDraw(True)
                
                # *score_presenter* updates
                if score_presenter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    score_presenter.frameNStart = frameN  # exact frame index
                    score_presenter.tStart = t  # local t and not account for scr refresh
                    score_presenter.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(score_presenter, 'tStartRefresh')  # time at next scr refresh
                    score_presenter.setAutoDraw(True)
                
                # *Stim* updates
                if Stim.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
                    # keep track of start time/frame for later
                    Stim.frameNStart = frameN  # exact frame index
                    Stim.tStart = t  # local t and not account for scr refresh
                    Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                    Stim.setAutoDraw(True)
                
                # *resp_A* updates
                if resp_A.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
                    # keep track of start time/frame for later
                    resp_A.frameNStart = frameN  # exact frame index
                    resp_A.tStart = t  # local t and not account for scr refresh
                    resp_A.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_A, 'tStartRefresh')  # time at next scr refresh
                    resp_A.setAutoDraw(True)
                
                # *resp_B* updates
                if resp_B.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
                    # keep track of start time/frame for later
                    resp_B.frameNStart = frameN  # exact frame index
                    resp_B.tStart = t  # local t and not account for scr refresh
                    resp_B.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_B, 'tStartRefresh')  # time at next scr refresh
                    resp_B.setAutoDraw(True)
                # *Stroop_mouse* updates
                if Stroop_mouse.status == NOT_STARTED and t >= 0.02-frameTolerance:
                    # keep track of start time/frame for later
                    Stroop_mouse.frameNStart = frameN  # exact frame index
                    Stroop_mouse.tStart = t  # local t and not account for scr refresh
                    Stroop_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Stroop_mouse, 'tStartRefresh')  # time at next scr refresh
                    Stroop_mouse.status = STARTED
                    Stroop_mouse.mouseClock.reset()
                    prevButtonState = Stroop_mouse.getPressed()  # if button is down already this ISN'T a new click
                if Stroop_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = Stroop_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([buttonA, buttonB])
                                clickableList = [buttonA, buttonB]
                            except:
                                clickableList = [[buttonA, buttonB]]
                            for obj in clickableList:
                                if obj.contains(Stroop_mouse):
                                    gotValidClick = True
                                    Stroop_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *buttonA* updates
                if buttonA.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
                    # keep track of start time/frame for later
                    buttonA.frameNStart = frameN  # exact frame index
                    buttonA.tStart = t  # local t and not account for scr refresh
                    buttonA.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(buttonA, 'tStartRefresh')  # time at next scr refresh
                    buttonA.setAutoDraw(True)
                
                # *buttonB* updates
                if buttonB.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
                    # keep track of start time/frame for later
                    buttonB.frameNStart = frameN  # exact frame index
                    buttonB.tStart = t  # local t and not account for scr refresh
                    buttonB.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(buttonB, 'tStartRefresh')  # time at next scr refresh
                    buttonB.setAutoDraw(True)
                
                # *ins_txt_stroop* updates
                if ins_txt_stroop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ins_txt_stroop.frameNStart = frameN  # exact frame index
                    ins_txt_stroop.tStart = t  # local t and not account for scr refresh
                    ins_txt_stroop.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ins_txt_stroop, 'tStartRefresh')  # time at next scr refresh
                    ins_txt_stroop.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stroop_square_trialsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "stroop_square_trials"-------
            for thisComponent in stroop_square_trialsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_count = trial_count+1
            if Stroop_mouse.clicked_name[0] == response:
                points = points + 1
                thisExp.addData('resp_corr', 1)
            else: 
                points = points - 1
                thisExp.addData('resp_corr', 0)
            
            thisExp.addData('Stroop_crnt_score', points)
            trial_count = trial_count +1
            # store data for stroop_trials_loop (TrialHandler)
            x, y = Stroop_mouse.getPos()
            buttons = Stroop_mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([buttonA, buttonB])
                    clickableList = [buttonA, buttonB]
                except:
                    clickableList = [[buttonA, buttonB]]
                for obj in clickableList:
                    if obj.contains(Stroop_mouse):
                        gotValidClick = True
                        Stroop_mouse.clicked_name.append(obj.name)
            stroop_trials_loop.addData('Stroop_mouse.x', x)
            stroop_trials_loop.addData('Stroop_mouse.y', y)
            stroop_trials_loop.addData('Stroop_mouse.leftButton', buttons[0])
            stroop_trials_loop.addData('Stroop_mouse.midButton', buttons[1])
            stroop_trials_loop.addData('Stroop_mouse.rightButton', buttons[2])
            if len(Stroop_mouse.clicked_name):
                stroop_trials_loop.addData('Stroop_mouse.clicked_name', Stroop_mouse.clicked_name[0])
            # the Routine "stroop_square_trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 400.0 repeats of 'stroop_trials_loop'
        
    # completed 2.0 repeats of 'pracTOreal_loop'
    
    
    # ------Prepare to start Routine "stroop_extra_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    if stroop_block ==1:
        thisExp.addData('color_word_final_score', points)
    if stroop_block ==2:
        thisExp.addData('emotion_final_score', points)
    if stroop_block ==3:
        thisExp.addData('gain_loss_final_score', points)
    # keep track of which components have finished
    stroop_extra_codeComponents = []
    for thisComponent in stroop_extra_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stroop_extra_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stroop_extra_code"-------
    while continueRoutine:
        # get current time
        t = stroop_extra_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stroop_extra_codeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stroop_extra_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stroop_extra_code"-------
    for thisComponent in stroop_extra_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "stroop_extra_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'stroop_all_loop'


# ------Prepare to start Routine "blank"-------
continueRoutine = True
routineTimer.add(0.020000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [blank_text]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank_text* updates
    if blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank_text.frameNStart = frameN  # exact frame index
        blank_text.tStart = t  # local t and not account for scr refresh
        blank_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_text, 'tStartRefresh')  # time at next scr refresh
        blank_text.setAutoDraw(True)
    if blank_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_text.tStartRefresh + .02-frameTolerance:
            # keep track of stop time/frame for later
            blank_text.tStop = t  # not accounting for scr refresh
            blank_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank_text, 'tStopRefresh')  # time at next scr refresh
            blank_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(8.000000)
# update component parameters for each repeat
end_resp.keys = []
end_resp.rt = []
_end_resp_allKeys = []
# keep track of which components have finished
endComponents = [End_text, end_resp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End_text* updates
    if End_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End_text.frameNStart = frameN  # exact frame index
        End_text.tStart = t  # local t and not account for scr refresh
        End_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_text, 'tStartRefresh')  # time at next scr refresh
        End_text.setAutoDraw(True)
    if End_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > End_text.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            End_text.tStop = t  # not accounting for scr refresh
            End_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(End_text, 'tStopRefresh')  # time at next scr refresh
            End_text.setAutoDraw(False)
    
    # *end_resp* updates
    waitOnFlip = False
    if end_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.tStart = t  # local t and not account for scr refresh
        end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
        end_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_resp.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            end_resp.tStop = t  # not accounting for scr refresh
            end_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_resp, 'tStopRefresh')  # time at next scr refresh
            end_resp.status = FINISHED
    if end_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_resp.getKeys(keyList=['space'], waitRelease=False)
        _end_resp_allKeys.extend(theseKeys)
        if len(_end_resp_allKeys):
            end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
            end_resp.rt = _end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
