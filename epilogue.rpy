##################################################################################################################
##################################################################################################################
########################################        Post Game Scenes        ##########################################
##################################################################################################################
##################################################################################################################
image credits_text = ParameterizedText(outlines=[(2, "#3E0045", 0, 0)], size=40, xalign=0.5, yalign=0.5)

label credits:

    $ quick_menu = False 

    scene black
    with fadee

    show credits_text "Lead Designer & Sprite Artist: Violora"
    with dissolve

    pause 2

    show promo at leftt behind credits_text:
        zoom 0.50
        yalign -7.0
        subpixel True
        linear 15 yalign 13.0
        linear 1 alpha 0
    with Dissolve(1.0)

    pause 6

    hide text
    with dissolve

    show credits_text "Director, Lead Programmer & Marketer: MikomiKisomi"
    with dissolve
        
    pause 8

    show promomary at rightt behind credits_text:
        zoom 0.50
        yalign -7.0
        subpixel True
        linear 15 yalign 13.0
        linear 1 alpha 0
    with Dissolve(1.0)

    hide text
    with dissolve

    show credits_text "\nLead Writer: Kevin \"Tutty The Fruity\" Armstrong"
    with dissolve
        
    pause 8

    hide text
    with dissolve

    show credits_text "\nWriter: Kidd \"The Maniac\" Bowyer"
    with dissolve
        
    pause 8

    show promotaylor at leftt behind credits_text:
        zoom 0.50
        yalign -7.0
        subpixel True
        linear 15 yalign 13.0
        linear 1 alpha 0
    with Dissolve(1.0)

    hide text
    with dissolve

    show credits_text "\nWriter: Seigetsu"
    with dissolve
        
    pause 8

    hide text
    with dissolve

    show credits_text "\nStory Consultants: Penelope Pilbeam, Andi Wamboldt"
    with dissolve
        
    pause 8

    hide text
    with dissolve

    show promocherry at rightt behind credits_text:
        zoom 0.50
        yalign -7.0
        subpixel True
        linear 15 yalign 12.0
        linear 1 alpha 0
    with Dissolve(1.0)

    show credits_text "Special thanks to Ryanne Bowyer, \nNicoletta Christina Browne, and Ayu Sakata."
    with dissolve
        
    pause 8

    hide text
    with dissolve

    show credits_text "\"Fearless\" by Tavian St. James and \n\"Friends Forever\" and \"Forever Dreaming\" by Alcaknight"
    with dissolve
        
    pause 8

    hide text
    with dissolve

    show credits_text "\"Knocking Door\" by dersuperanton, \"Wooden Door Open\" by joedeshon, and \"On Stage Jingles\" by Setuniman"
    with dissolve
        
    pause 8

    hide text
    with dissolve

    show credits_text "This game was made with Ren'Py.\nThank you Pytom."
    with dissolve
        
    pause 8

    hide text
    with dissolve


    jump epilogue


#####################################
###################### After Credits
    
label epilogue:

    scene black
    with fadee

    $ config.side_image_tag = ""
    
    ann "{i}Oh shit, I'm gonna be late!{/i}"
    ann "{i}It’s all my own fault. I shouldn’t have been so damn excitable that I couldn’t fall asleep all night, then ended up dozing off on my chair just three hours before showtime!{/i}"
    ann "{i}Boss is so gonna kill me.{/i}"

    scene makeuproom
    with fade
    
    show mary up smile at center:
        zoom 1.35
        yalign 0.4
    with dissolve

    $ config.side_image_tag = "alice"

    an frown summer "{nw}"

    m talk "Relax, Alice. You fidgeting around like this makes it hard for me to draw your brows."

    show mary smile
    
    a frowntalk "Sorry... I'll try not to."
    a frown "{nw}"
    
    m frowntalk "Then again, if you weren’t so nervous, the makeup artist would be able to do this in my stead. Seriously, when have I become your personal assistant?"
    
    show mary frown

    a talk "Sorry to always rely on you, Mary. But... you’re the only one who can calm me down, you see, so..."
    a frown "{nw}"

    m talk "I know, I know. Now just sit back and stop curling up like a pillbug. I’ll finish this in no time."

    show mary smile

    show director smile at right:
        zoom 1.2
        yalign 0.8
    with moveinright
    
    di talk "You girls done?"
    
    show director smile

    m frowntalk "Just a moment."
    
    show mary frown

    di talk "Yeah, yeah, Superstar. Hurry it up, alright?"

    show director smile
    
    m down frowntalk "I'm trying!"
    
    show mary frown

    a frowntalk "I'm so sorry..."
    
    hide director with moveoutright

    show mary up

    ann frown "{i}Shortly after the director leaves us, Mary finishes lining my right brow.{/i}"
    
    a up talk "I think it’s good. Both brows are even."
    a smile "{nw}"
    
    m unsure frowntalk "Aren’t your expectations low..."
    
    show mary frown

    a talk "Can’t help it. I’ve gotta go!"
    
    show mary up smile

    ann smile "{i}I give Mary’s hands a squeeze and dash off for the stage, leaving her sighing in exasperation.{/i}"
    ann "{i}I know she just wants the best for me. I’m so lucky to have someone like her by my side.{/i}"
    
    scene black
    with fade
    
    a "Is it starting?"
    
    k "Made it just before I was about to send out my lackeys to hunt you down, dead or alive."

    scene stageclose
    with fade

    show jacques up smile at center:
        zoom 1.35
        yalign 0.3
    with dissolve
    
    j talk "Welcome to season two of your favorite idol show, Supernova! Are you ready for another month of heart-wrenching, blood-boiling struggles for the throne of your next superstar?"
    j "Yes! I know I’m ready! And she is too! Introducing our winner from season one - she will start us off with the first song of this new festival!"
    
    show jacques smile

    ann "{i}I make my way up the steps. The familiar light falls upon me.{/i}"
    ann "{i}Tay, Mary, Cherry... they’re all watching. I wave to them, feeling their cheers pour energy into my heart.{/i}"
    
    j talk "This is your idol, Alice Carroll......"

    show jacques smile

    return
    
    ###### end epilogue