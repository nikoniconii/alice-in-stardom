#######################################################################################################################
##############################################                              ###########################################
##############################################          Contest             ###########################################
##############################################                              ###########################################
#######################################################################################################################


label testMinigame:
    $ ui.timer(8.0, ui.jumps("too_slow"))
    
    python:
        line = renpy.input("Hello my love")
        line = line.strip()
        
    if line == 'Hello my love':
        jump line1C
        
    if line == 'hello my love':
        jump line1C
        
    else:
        jump testMinigame


label line1C:
    $ ui.timer(8.0, ui.jumps("too_slow"))
    
    python:
        line = renpy.input("Goodbye my friend")
        line = line.strip()
        
    if line == 'Goodbye my friend':
        jump line2C
        
    if line == 'goodbye my friend':
        jump line2C
        
    else:
        jump line1C


label line2C:
    $ ui.timer(8.0, ui.jumps("too_slow"))
    
    python:
        line = renpy.input("Hello new world")
        line = line.strip()
        
    if line == 'Hello new world':
        jump line3C
        
    if line == 'hello new world':
        jump line3C
        
    else:
        jump line2C


label line3C:
    #timer 10 action Jump("too_slow")
    $ ui.timer(8.0, ui.jumps("too_slow"))
    
    python:
        line = renpy.input("Will I see you again?")
        line = line.strip()
        
    if line == 'Will I see you again?':
        jump done
        
    if line == 'will I see you again?':
        jump done
        
    if line == 'Will I see you again':
        jump done
        
    if line == 'will I see you again':
        jump done

    else:
        jump line3C

default slow = 0

label too_slow:
    $ slow += 1

    if slow < 3:
        a "Ack, I stumbled!"

        jump testMinigame

    else:
        a "Oh no.... I completely failed...."

        $ renpy.quit()


label done:
    a "I... I can't believe it..... I finished the song perfectly!"


