#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Thu Aug  1 13:23:36 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'Baseline_middle'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='/Users/martindockendorff/Desktop/Projects/Communication_game',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

#Initialize components for Routine "instructions"
instructionClock = core.Clock()
instructions1 = visual.TextStim(win=win, name='instructions',
    text="Welcome to the experiment. Press SPACE to continue",
    font='Arial',
    pos=(-0.37, 0), height=0.031, wrapWidth=0.7, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "trial"
trialClock = core.Clock()

mouse = event.Mouse(win=win, visible = False)
mouse.mouseClock = core.Clock()

area1 = visual.ImageStim(
    win=win,
    name='area',
    image='images/box_contour1.png', mask=None,
    ori=0, pos=(-0.7, 0), size=(0.16, 0.162),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

area2 = visual.ImageStim(
    win=win,
    name='area',
    image='images/box_contour1.png', mask=None,
    ori=0, pos=(0.35, 0), size=(0.16, 0.162),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

area3 = visual.ImageStim(
    win=win,
    name='area',
    image='images/box_contour1.png', mask=None,
    ori=0, pos=(0.7, 0), size=(0.16, 0.162),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

area4 = visual.ImageStim(
    win=win,
    name='area',
    image='images/box_contour1.png', mask=None,
    ori=0, pos=(0, 0), size=(0.16, 0.162),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

green_area = visual.ImageStim(
    win=win,
    name='area',
    image='images/box_contour.png', mask=None,
    ori=0, pos=(1, 1),size=(0.16, 0.162),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

green_area2 = visual.ImageStim(
    win=win,
    name='area',
    image='images/box_contour.png', mask=None,
    ori=0, pos=(1, 1),size=(0.16, 0.162),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

green_area3 = visual.ImageStim(
    win=win,
    name='area',
    image='images/box_contour.png', mask=None,
    ori=0, pos=(1, 1),size=(0.16, 0.162),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

line = visual.Line(
    win=win, name='line',
    start=(-0.625,0), end=(-0.077, 0),
    ori=0,
    lineWidth=100, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

line2 = visual.Line(
    win=win, name='line',
    start=(-0.625,-0.0035), end=(-0.077, -0.0035),
    ori=0,
    lineWidth=100, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

line3 = visual.Line(
    win=win, name='line',
    start=(0.077,0), end=(0.275, 0),
    ori=0,
    lineWidth=100, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

line4 = visual.Line(
    win=win, name='line',
    start=(0.077,-0.0035), end=(0.275, -0.0035),
    ori=0,
    lineWidth=100, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

line5 =visual.Line(
    win=win, name='line',
    ori=0, start=(0.425, 0), end=(0.625, 0),
    lineWidth=100, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

line6 =visual.Line(
    win=win, name='line',
    ori=0, start=(0.425, -0.0035), end=(0.625, -0.0035),
    lineWidth=100, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

box = visual.ImageStim(
    win=win,
    name='box',
    image='images/box22.png', mask=None,
    ori=0, pos=(-.7, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
box.boxClock=core.Clock()

correct_location = visual.ImageStim(
    win=win,
    name='correct_location',
    image='sin', mask=None,
    ori=0, pos=(-0.5, -0.46), size=(0.095, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
cross= visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0, pos=(-0.35, 0.1),
    lineWidth=1, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

msg=''
message = visual.TextStim(win=win, name='message',
    text='default text',
    font='Arial',
    pos=(-0.35,-0.1), height=0.04, wrapWidth=0.5, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);


red_score = 1
green_score = 1

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
mouseTimer = core.CountdownTimer(3)
# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_1 = keyboard.Keyboard()
# keep track of which components have finished
instructionComponents = [instructions1, key_resp_1]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructions1* updates
    if t >= 0.0 and instructions1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions1.tStart = t  # not accounting for scr refresh
        instructions1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instructions1, 'tStartRefresh')  # time at next scr refresh
        instructions1.setAutoDraw(True)

    # *key_resp* updates
    if t >= 0.0 and key_resp_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_1.tStart = t  # not accounting for scr refresh
        key_resp_1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
        key_resp_1.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
        key_resp_1.clearEvents(eventType='keyboard')
    if key_resp_1.status == STARTED:
        theseKeys = key_resp_1.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_1.keys = theseKeys.name  # just the last key pressed
            key_resp_1.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (already at the instructions screen)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions1.started', instructions1.tStartRefresh)
thisExp.addData('instructions1.stopped', instructions1.tStopRefresh)
#check responses
if key_resp_1.keys in ['', [], None]:  # No response was made
    key_resp_1.keys = None
thisExp.addData('key_resp_1.keys',key_resp_1.keys)
if key_resp_1.keys != None:  # we had a response
    thisExp.addData('key_resp_1.rt', key_resp_1.rt)
thisExp.addData('key_resp_1.started', key_resp_1.tStartRefresh)
thisExp.addData('key_resp_1.stopped', key_resp_1.tStopRefresh)
thisExp.nextEntry()
#the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=25, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # set up handler to look after randomisation of conditions etc THIS REPEATS OVERSHOOTING
    trials2 = data.TrialHandler(nReps=100, method='sequential',
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials2')
    thisExp.addLoop(trials2)  # add the loop to the experiment
    thisTrial2 = trials2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial2 != None:
        for paramName in thisTrial2:
            exec('{} = thisTrial2[paramName]'.format(paramName))

    for thisTrial2 in trials2:
        currentLoop = trials2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial2 != None:
            for paramName in thisTrial2:
                exec('{} = thisTrial2[paramName]'.format(paramName))


        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        mouse.x = []
        mouse.y = []
        mouse.time = []
        mouse.clicked_name = []
        mouseCenter = False
        mouseTimer.reset()
        gotValidClick = False  # until a click is received
        key_resp = keyboard.Keyboard()
        left_x_limit = -.7
        right_x_limit = 1
        mouse.setPos([-0.7,0])
        mouse.getPos()
        correct = False
        box.x =[] #creates list to store x values from box item
        box.time =[]
        key1 =[]
        key2 =[]
        key1pressed = False
        key2pressed = False
        thisResp=[]
        checkstart = False
        # keep track of which components have finished
        trialComponents = [mouse, key_resp, box, area1, area2, area3,area4, green_area, green_area2,green_area3, correct_location, line, line2, line3, line4, line5, line6]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

            # *key_resp* updates
            if t >= 0.0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
                key_resp.tStart = t  # not accounting for scr refresh
                key_resp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
            # keyboard checking is just starting
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                key_resp.clearEvents(eventType='keyboard')
            if key_resp.status == STARTED:
                theseKeys = key_resp.getKeys(keyList=['n', 'f'], waitRelease=False)
                for key in theseKeys:
                    if key == 'escape':
                        endExpNow = True

                    if key == 'n':
                        key1pressed = True
                        key1 = key

                    if key == 'f':
                        key2pressed = True
                        key2 = key

                    if key1pressed:
                        continueRoutine=False
                    if key2pressed:
                        continueRoutine=False

                    # was this 'correct'?
                    if key1 == corrAns1:
                        key_resp.corr = 1
                    if key2 == corrAns1:
                        key_resp.corr = 1


            #*mouse* updates
            if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
                mouse.tStart = t  # not accounting for scr refresh
                mouse.frameNStart = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                mouse.time.append(mouse.mouseClock.getTime())

            #Restricts mouse movements to one direction (left to right)
            if x < left_x_limit:
                x = left_x_limit
            elif x > right_x_limit:
                x = right_x_limit
            left_x_limit = x


            # *line* updates
            if t >= 0.0 and line.status == NOT_STARTED:
                # keep track of start time/frame for later
                line.tStart = t  # not accounting for scr refresh
                line.frameNStart = frameN  # exact frame index
                win.timeOnFlip(line, 'tStartRefresh')  # time at next scr refresh
                line.setAutoDraw(True)

            # *line2* updates
            if t >= 0.0 and line2.status == NOT_STARTED:
                # keep track of start time/frame for later
                line2.tStart = t  # not accounting for scr refresh
                line2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(line2, 'tStartRefresh')  # time at next scr refresh
                line2.setAutoDraw(True)

            # *line3* updates
            if t >= 0.0 and line3.status == NOT_STARTED:
                # keep track of start time/frame for later
                line3.tStart = t  # not accounting for scr refresh
                line3.frameNStart = frameN  # exact frame index
                win.timeOnFlip(line3, 'tStartRefresh')  # time at next scr refresh
                line3.setAutoDraw(True)

            # *line4* updates
            if t >= 0.0 and line4.status == NOT_STARTED:
                # keep track of start time/frame for later
                line4.tStart = t  # not accounting for scr refresh
                line4.frameNStart = frameN  # exact frame index
                win.timeOnFlip(line4, 'tStartRefresh')  # time at next scr refresh
                line4.setAutoDraw(True)

            # *line5* updates
            if t >= 0.0 and line5.status == NOT_STARTED:
                # keep track of start time/frame for later
                line5.tStart = t  # not accounting for scr refresh
                line5.frameNStart = frameN  # exact frame index
                win.timeOnFlip(line5, 'tStartRefresh')  # time at next scr refresh
                line5.setAutoDraw(True)

            # *line6* updates
            if t >= 0.0 and line6.status == NOT_STARTED:
                # keep track of start time/frame for later
                line6.tStart = t  # not accounting for scr refresh
                line6.frameNStart = frameN  # exact frame index
                win.timeOnFlip(line6, 'tStartRefresh')  # time at next scr refresh
                line6.setAutoDraw(True)

            # *area1* updates
            if t >= 0.0 and area1.status == NOT_STARTED:
                # keep track of start time/frame for later
                area1.tStart = t  # not accounting for scr refresh
                area1.frameNStart = frameN  # exact frame index
                win.timeOnFlip(area1, 'tStartRefresh')  # time at next scr refresh
                area1.setAutoDraw(True)

            # *area2* updates
            if t >= 0.0 and area2.status == NOT_STARTED:
                # keep track of start time/frame for later
                area2.tStart = t  # not accounting for scr refresh
                area2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(area2, 'tStartRefresh')  # time at next scr refresh
                area2.setAutoDraw(True)

            # *area3* updates
            if t >= 0.0 and area3.status == NOT_STARTED:
                # keep track of start time/frame for later
                area3.tStart = t  # not accounting for scr refresh
                area3.frameNStart = frameN  # exact frame index
                win.timeOnFlip(area3, 'tStartRefresh')  # time at next scr refresh
                area3.setAutoDraw(True)

            # *area4* updates
            if t >= 0.0 and area4.status == NOT_STARTED:
                # keep track of start time/frame for later
                area4.tStart = t  # not accounting for scr refresh
                area4.frameNStart = frameN  # exact frame index
                win.timeOnFlip(area4, 'tStartRefresh')  # time at next scr refresh
                area4.setAutoDraw(True)

            # *green_area* updates
            if t >= 0.0 and green_area.status == NOT_STARTED:
                # keep track of start time/frame for later
                green_area.tStart = t  # not accounting for scr refresh
                green_area.frameNStart = frameN  # exact frame index
                win.timeOnFlip(green_area, 'tStartRefresh')  # time at next scr refresh
                green_area.setAutoDraw(True)

            # *green_area2* updates
            if t >= 0.0 and green_area2.status == NOT_STARTED:
                # keep track of start time/frame for later
                green_area2.tStart = t  # not accounting for scr refresh
                green_area2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(green_area2, 'tStartRefresh')  # time at next scr refresh
                green_area2.setAutoDraw(True)

            # *green_area3* updates
            if t >= 0.0 and green_area3.status == NOT_STARTED:
                # keep track of start time/frame for later
                green_area3.tStart = t  # not accounting for scr refresh
                green_area3.frameNStart = frameN  # exact frame index
                win.timeOnFlip(green_area3, 'tStartRefresh')  # time at next scr refresh
                green_area3.setAutoDraw(True)

            # *box* updates
            if t >= 0.0 and box.status == NOT_STARTED:
                # keep track of start time/frame for later
                box.tStart = t  # not accounting for scr refresh
                box.frameNStart = frameN  # exact frame index
                win.timeOnFlip(box, 'tStartRefresh')  # time at next scr refresh
                box.status = STARTED
                box.boxClock.reset()
                box.setAutoDraw(True)
            if box.status == STARTED:
                box.x.append(x)
                box.time.append(box.boxClock.getTime())
                checkstart = True;
            box.pos = [x, 0] #This attaches the box to the mouse

            if(x > 0.34 and x < 0.36):
                green_area2.pos = (0.35, 0.0)
            else:
                green_area2.pos=(1,1)

            if(x > 0.69 and x < 0.71):
                green_area3.pos = (0.7, 0.0)
            else:
                green_area3.pos = (1, 1)

            #If key is pressed but the box is not within any of the delivery locations:    
            if(x < 0.01 and (key1pressed or key2pressed)) or (x > 0.01 and x < 0.34 and (key1pressed or key2pressed)) or (x > 0.36 and x < 0.69 and (key1pressed or key2pressed)):
                key_resp.corr = 4
                continueRoutine=False
            if (x > 0.71):
                key_resp.corr = 4
                continueRoutine=False

            #Clockdown starts 4 seconds after entering middle area
            if ((x > -0.005 and x < 0.005) and not mouseCenter): # the mouse was just moved inside the quad
                mouseTimer.reset()
                mouseCenter = True
            elif ((x > 0.005) and mouseCenter): # the mouse was just moved outside the quad
                mouseCenter = False

            if (mouseTimer.getTime() <= 0 and (x > -0.005 and x < 0.005)):
                green_area.pos = (0.0, 0.0)
            else:
                green_area.pos=(1,1)

            #Repeat trial if overshoots without resting in middle target for 4 seconds
            if (mouseTimer.getTime() > 0) and (x > 0.005):
                key_resp.corr = 3
                continueRoutine=False

            #Box disappears when entering the middle area
            if mouseCenter:
                box.pos=(1,1)
            #After 3 seconds the box reappears in the middle area
            if (mouseTimer.getTime() < 0) and mouseCenter:
                box.pos=(0,0)

            # *correct_location* updates
            if t >= 0.0 and correct_location.status == NOT_STARTED:
                # keep track of start time/frame for later
                correct_location.tStart = t  # not accounting for scr refresh
                correct_location.frameNStart = frameN  # exact frame index
                win.timeOnFlip(correct_location, 'tStartRefresh')  # time at next scr refresh
                correct_location.setAutoDraw(True)
            if correct_location.status == STARTED:  # only update if drawing
                print(f"Trial {trials.thisN}, Subtrial {trials2.thisN}: Attempting to set image: '{corrLoc}'") # Add this line
                correct_location.setImage(corrLoc, log=False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # store data for trials (TrialHandler)
        trials.addData('box.x', box.x)
        trials.addData('box.time', box.time)
        trials.addData('mouse.x', mouse.x)
        trials.addData('mouse.y', mouse.y)
        trials.addData('mouse.time', mouse.time)
        trials.addData('mouse.started', mouse.tStart)
        trials.addData('mouse.stopped', mouse.tStop)
        trials.addData('key_resp.keys',key_resp.keys)
        trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        trials.addData('key_resp.started', key_resp.tStartRefresh)
        trials.addData('key_resp.stopped', key_resp.tStopRefresh)

    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.200000)
        # update component parameters for each repeat
        if key_resp.corr== 1: #stored on last run routine
            cross.color='green'
            msg = 'The box is now being sent to one of the delivery locations!'
            cross.pos = (2,2)
            trials2.finished = True
        if key_resp.corr==0:
            msg = 'The box is now being sent to one of the delivery locations!'
            cross.color='green'
            cross.pos = (2,2)
            trials2.finished = True
        if key_resp.corr==3:
            cross.color='black'
            cross.pos=(-0.35, 0.1)
            msg = 'P1: You have to place the box inside the middle target!'
            trials2.finished = False
        if key_resp.corr==4:
            cross.color='black'
            msg = 'P2: You have to place the box in one one of the delivery locations!'
            cross.pos=(-0.35, 0.1)
            trials2.finished = False

        message.setText(msg)

        # keep track of which components have finished
        feedbackComponents = [cross, message]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *cross* updates
            if t >= 0.0 and cross.status == NOT_STARTED:
                # keep track of start time/frame for later
                cross.tStart = t  # not accounting for scr refresh
                cross.frameNStart = frameN  # exact frame index
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cross.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                cross.setAutoDraw(False)

            # *message* updates
            if t >= 0.0 and message.status == NOT_STARTED:
                # keep track of start time/frame for later
                message.tStart = t  # not accounting for scr refresh
                message.frameNStart = frameN  # exact frame index
                win.timeOnFlip(message, 'tStartRefresh')  # time at next scr refresh
                message.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if message.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                message.tStop = t  # not accounting for scr refresh
                message.frameNStop = frameN  # exact frame index
                win.timeOnFlip(message, 'tStopRefresh')  # time at next scr refresh
                message.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        mouse.setPos(newPos=(-.7,0))

        if key_resp.corr== 1: #stored on last run routine
            green_score += + 1
        else:
            if key_resp.corr==0:
                red_score += 1


# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
