README for Cobra-StarFish

WHAT'S INSIDE:
    This file should be included with the Cobra_StarFish folder, as well as "Cobra_StarFish.py", "StarFish_Settings.py", and "ttyLinux.py". This folder might also contain "StarFish_Settings.pyc" and "ttyLinux.pyc" which are created when the program is started.

COPYRIGHT JIBBER-JABBER:
    You are allowed to re-distribute this software, however by downloading this program you agree to include all original documentation unmodified and clearly labeled as free. You must notify the original Author if you intend to redistribute this program with modifications. If you disagree with any of these points, you can delete this program. You can contact the author via email at j.r.jurman@gmail.com or facebook at www.facebook.com/JRJurman.

PROGRAMMING JIBBER-JABBER:
    The program is written for python2.7, since pygame is not supported (as of now) in python3.
    The special input required for this program requires that the program be run on a Linux Distribution.
    Required modules:
        random: included with python
        time: included with python
        os: included with python
        termios: included with python
        sys: included with python
        pygame: can be downloaded through pygame.org, may be included in your repositories

HOW TO RUN:
    Before you run the program, open StarFish_Settings.py with a simple text-editor or IDE. This file contains the settings that Cobra-StarFish will look for by name in the same directory. If you wish to have backups or multiple setting files, you may store these in a different folder. In this file will be the settings for the rotation Directory (rotDirectory), log Directory (logDirectory), and the rotation List (rotList). Simply write the directories you wish the program to look for the certain folders. 
    For Example, the file may look like this if you wanted the program to rotate through RED, BLUE, RED, BLUE, GREEN in the folder /home/USERNAME/Desktop/RotationFolder, and you wanted the logs to be saved on the /home/USERNAME/Desktop/Logs:

        rotDirectory = "/home/USERNAME/Desktop/RotationFolder"
        logDirectory = "/home/USERNAME/Desktop/Logs"
        
        rotList = [
            "RED",
            "BLUE",
            "RED",
            "BLUE",
            "GREEN"
        ]

    After you have setup this file for your system, open Terminal and "cd" to this folder. This may look like:
        USERNAME ~ $ cd Downloads/Cobra_StarFish/
        USERNAME ~/Downloads/Cobra_StarFish $ 

    To run the program call "python Cobra_StarFish.py". If you have all the required modules the program will greet you with the opening text.

IF SOMETHING GOES WRONG:
    The ttyLinux that offers dynamic input will cause your terminal window to hide the text you type as well as force some other settings to your terminal window. Should the program crash, take note of the error and then type "reset" (no quotes) and press enter/return, the text will not appear, but it is going in the terminal and will clear the window as well as the visual settings.

WHAT'S GOING ON:
    The program will find the folders labeled in rotList, and grab a file from those folders. It will grab any file so BE SURE THAT THE ROTLIST CONTAINS ONLY AUDIO FILES (to check if there are any out of ordinary files, open the rotation folder and press ctrl+h. If this folder is dedicated to audio files, it should be ok to remove these files). It cues a file from the next folder and displays it like so:
        
        SONG_NUMBER. [rotList] SONG_NAME len:[SONG_LENGTH], at TIME_PLAYED
        CUE: [rotList+1] SONG_NAME in t-SONG_LENGTH

    So if you were currently listening to (lets say a minute in) The Hoosiers' "Goodbye Mr.A" (which is 4:28) and Streetlight Manifesto's "Watch It Crash" was up next, it would look like this:

        4. [REDS] The_Hoosiers:Goodbye_Mr_A len:[04:28], at 02:45PM
        CUE: [BLUES] Streetlight_Manifesto:Watch_It_Crash in 03:28

    The "03:28" would constantly update until it reached 00:00, and would put Streetlight Manifesto in a similar format as The Hoosiers, and have a new song in cue, counting down from a new time.

THE LOG:
    Everytime the console (aka Terminal) displays the standard format (song number, the length, and the time it played) it writes the same data to a log. This log also includes a header stating when it was made and at what time. If the program was opened multiple times in one day, the log will take note of that, stating: "Continued at " and the current time. This will also be noted in the console before you start the program.

WHAT'S NEW/FEATURES:
    For those of you who used NightCrawler, there are some significant updates to the functionallity and simplicity. While Cobra-StarFish may not contain as many settings prompts, it is far more verstaile, while remaining simple to operate and run.
        OLD STUFF:
            -Cobra-StarFish will load songs, one from each folder, and then loop. This is optimal compared to a simple shuffle function as this will call a certain set of songs more often than another. This also allows for mic breaks to be assuringly added every few songs.
            -You may choose the directory that you load folders from (it is recommended that you write the entire directory)
            -You may choose the directory logs are saved in (again, recommend that you write the entire directory)
            -You may choose the order of the sets contained in the rotation directory.
        
        WHAT'S NOT THERE (in the sake of simplicity, and the fact you really never needed it):
            -The ability to dictate the name of log files
            -The positive/negative delay
            -Saving and loading settings
            -Generate New Cue
            -The delayed stop function
            -Stop indicator
            -The GUI
        
        THE NEW STUFF:
            -Pause/Unpause: Immediate pausing when you press [p]. You may unpause the current song by pressing [p] again.
            -Quit: Immediatly stops the current song and closes the program. Quiting through other ways will cause the terminal to behave oddly and require you to type "reset" and press enter.
            -Smart Shuffling: Plays every possible song in a folder without repeating. NOTE: If the program can find no new songs to play in a folder, it empties the "catch" for that folder and picks a song from that folder, while remebering all the other songs it had played before.
            -Log Interface: The console acts as an interactive log, allowing you to see all the songs previously played, and when they were played.
            -CountDown: The console shows how much time is left in min:sec until the next song, allowing DJs to get ready for a next set and pause the system promptly before the next song.
            -Open/Close System: Cobra-StarFish accurately opens and closes audio files supported by pygame. These occur one at a time, and should not require modifying the system settings.
            -Appending Log System: If you open the program more than once per day, Cobra-StarFish will recognize the previously existing log file and append to it, noting the new session in both the console and the log.
            -File Nomenclature: You can now use spaces in file names, however it is still not recommended to use "/" or "."
            -It Works!: Where NightCrawler crashed often, this should run as smooth as a whistle!

Enjoy The New System, if you need to contact the Author, look in the COPYRIGHT JIBBER-JABBER listed above.
