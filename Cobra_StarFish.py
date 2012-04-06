"""Cobra_StarFish, Radio Automation System
Created by Jesse Jurman for WIRQ
Uses Pygame, Termios, Random, and Time modules
Uses python2.7 (should work with 3.2 if modules are loaded)"""

import pygame #pygame module for music
pygame.mixer.init() #initalize pygame module for music

import random
import time #time module for pauses and whatnot
import os

import ttyLinux #code borrowed for live input
ttyLinux.setSpecial()

from StarFish_Settings import * #variables for defined settings



def mainProgram():
    """Main script which contains various methods and the automation loop"""
    
    #code to populate what songs are available  #### DO NOT MODIFY ######
    rotFolders = os.listdir(rotDirectory) #the various folders in the rotation Directory
    rotAlbums = []
    #for loop to append file names of folder "i" into rotAlbums
    for i in range(0, len(rotFolders)):
        rotAlbums.append(os.listdir(rotDirectory+"/"+str(rotFolders[i])))

    
    song_count = -1 #so that first cue is actually for the song to be played first
    song_dir = ""
    cue_dir = ""
    song_length = 0
    uI = ""
    catch = [""] #needs starting variable for comparision
    logPath = logDirectory+"/"+time.strftime("%b_%d_%Y.txt")
    
    print("Cobra StarFish, Radio Automation Program")
    print("For Python 2.7, Made By Jesse Jurman")
    print("Controls: [j]-Start Player, [p]-Pause/Unpause, [q]-Close Program")
    print("\n")
    
    if(os.path.exists(logPath)):
        print("\'We now return to the log file already in progress\'")
        logFile = open(logPath, "a")
        logFile.write("Continued at "+time.strftime("%I:%M%p")+"\n")
    else:
        print("Creating LogFile")
        logFile = open(logPath, "w")
        logFile.write("Log File Created by Cobra StarFish on "+time.strftime("%A, %b %d, %Y at %I:%M%p")+"\n")
    
    print "Press [j] to start player: ",
    while("j" not in uI):
        time.sleep(.1)
        uI = ttyLinux.readLookAhead()

    def cueSong():
        """generates a new song based on the level on rotationDirectories"""
        level = (song_count+1) % (len(rotList))
        c_Album = rotAlbums[rotFolders.index(rotList[level])]
        dir_CURRENT = rotDirectory+"/"+rotList[level] #the rotation directory
        search = 0; s_CURRENT = catch[0]; full=True
        for songs in c_Album:
            if(songs not in catch): full=False
        if(full): #if the catch has all the albums songs, empty the catch
            for songs in c_Album:
                catch.remove(songs)
        while(s_CURRENT in catch):
            randgen = random.randint(0, len(c_Album)-1 )
            s_CURRENT = c_Album[randgen] #the current song
        catch.append(s_CURRENT)
        song_dir = dir_CURRENT+"/"+s_CURRENT
        return song_dir

    def printLog():
        """print data to terminal for song that is playing"""
        
        level = song_count % len(rotList)
        
        #rip current song out of directory
        c_song = song_dir.split("/")[len(song_dir.split("/"))-1]
        c_song = c_song.split(".")[0] #rip extension
        
        #current time
        c_TIME = time.strftime("%I:%M%p")
        
        #make song_length into readable string
        min = int(song_length/60); sec = int(song_length%60)
        if(min<10): min_str = "0"+str(min)
        else: min_str = str(min)
        if(sec<10): sec_str = "0"+str(sec)
        else: sec_str = str(sec)
        song_length_h = min_str+":"+sec_str
        
        #NUM. [FOLDER] SONG_TITLE [LENGTH]  TIME_PLAYED
        info = str(song_count)+". ["+rotList[level]+"] "+c_song+" len:["+song_length_h+"], at "+str(c_TIME)
        
        print("\r"+info)
        logFile.write(info+"\n")
        
        
    def printDisplay():
        """print display info for song in cue"""
        
        level = (song_count+1) % len(rotList)
        
        #rip current song out of directory
        c_song = cue_dir.split("/")[len(cue_dir.split("/"))-1]
        c_song = c_song.split(".")[0] #rip extension
        
        #gen minutes and seconds left
        time_left = song_length - timer
        min_left = int(time_left / 60)
        sec_left = int(time_left % 60)
        
        if(min_left<10): min_str = "0"+str(min_left)
        else: min_str = str(min_left)
        if(sec_left<10): sec_str = "0"+str(sec_left)
        else: sec_str = str(sec_left)
        
        #CUE: [FOLDER] SONG_TITLE in t-SONGLENGTH
        print "\r"+str("CUE: ["+rotList[level]+"] ")+c_song+" in "+min_str+":"+sec_str+" "+uI, 

    uI = ""
     
    wirq = pygame.mixer.Channel(0) #id=0?
    
    #play first song
    song_dir = cueSong(); song_count += 1
    wirq.play(pygame.mixer.Sound(song_dir))
    song_length = wirq.get_sound().get_length()
    printLog()
    
    #cue next song
    cue_dir = cueSong()
    wirq.queue(pygame.mixer.Sound(cue_dir))
    cue_length = wirq.get_queue().get_length()
   
    
    timer = 0; last_time=0
    mode = "Running"

    #MAIN LOOP FOR AUTOMATION
    while(uI!="q"):
        while(wirq.get_queue()!=None and mode!="Stopped"):
            
            time.sleep(.1)
            uI = ttyLinux.readLookAhead()
            
            if(uI=="q"): mode = "Stopped"
            elif(uI=="p" and mode!="Paused"): mode="Paused"; wirq.pause()
            elif(uI=="p" and mode=="Paused"): mode="Running"; wirq.unpause()
            
            if(int(time.strftime("%S")) != last_time and mode!="Paused"):
                last_time = int(time.strftime("%S"))
                timer+=1
            
            printDisplay()
            
        
        if(mode=="Running"):
            #pass cue info to current
            song_dir = cue_dir
            song_length = cue_length; timer = 0
            
            #generate new cue
            song_count += 1
            cue_dir = cueSong()
            wirq.queue(pygame.mixer.Sound(cue_dir))
            cue_length = wirq.get_queue().get_length()
            
            printLog()
        
    wirq.stop()
    logFile.write("Program Stopped at "+time.strftime("%I:%M%p")+"\n")
    logFile.close()

mainProgram()
print("\nClosing Program")
ttyLinux.setNormal()

