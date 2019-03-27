
#######################################################################################################################
##############################################                              ###########################################
##############################################            Nights            ###########################################
##############################################                              ###########################################
#######################################################################################################################


label nightSwitch:
    if day == 1:
        jump insomnia1          ### jump morningnormal1
    elif day == 2:
        jump sleepy1            ### jump week1contest
    elif day == 3:
        jump excited1           ### jump morning5
    elif day == 4:
        jump night1             ### jump week3contest
    elif day == 5:
        jump normalnight1       ### jump hopeful
    elif day == 6:
        jump sleepy2            ### jump week4contest
    elif day == 7:
        jump normalnight2       ### jump anxious
    else:
        jump excited2           ### jump finalcontest



label daySwitch:
    if day == 2:
        jump morningnormal1
    elif day == 3:
        jump week1contest
    elif day == 4:
        jump morning5
    elif day == 5:
        jump week3contest
    elif day == 6:
        jump hopeful
    elif day == 7:
        jump week4contest
    elif day == 8:
        jump anxious
    else:
        jump finalcontest


        
        
############ Normal Night
label normalnight:

    label normalnight1:
            
        $ day += 1
        
        scene bedalicenight
        with fadee
        
        $ config.side_image_tag = ""

        ann "{i}After dinner and relaxing at the lounge for a bit, I return to my room to sleep.{/i}"
        ann "{i}It has been a long day. It feels good to be back here, resting on the soft bed.{/i}"
        ann "{i}I pull the covers up to my shoulders and move into a comfortable position. The sheets smell of fresh lemony detergent, matching the residue of minty mouthwash between my teeth.{/i}"
        ann "{i}I close my eyes, ready to be further refreshed by slumber.{/i}"
        
        jump daySwitch

        ###### call screen

        
    label normalnight2:
        
        $ day += 1
                
        scene bedalicenight
        with fadee
        
        $ config.side_image_tag = ""
        
        ann "{i}Dinner was enjoyable as usual, even after I had to slip past the director and Boss arguing in the hallway afterwards.{/i}"
        ann "{i}This place is so huge... I feel like I haven't even began to see all of it!{/i}"
        ann "{i}Tomorrow is a new day, and with it, new opportunities.{/i}"
        ann "{i}I lay my head down and slowly but surely fall asleep.{/i}"
        
        jump daySwitch

        #### call screen
        
        
    
label excited:
    
    ############################# Night 3
    label excited1:
        
        $ day += 1
        
        scene bedalicenight
        with fadee
        
        $ config.side_image_tag = ""
        
        ann "{i}So much has happened today.{/i}"
        ann "{i}After dinner, I had fun with the others at the lounge. I guess I’m starting to get along after all.{/i}"
        ann "{i}It’s amazing, considering that I’ve never even imagined this situation would happen to me. I often still struggle with the idea of being here, but sometimes, I find the courage to face the things coming my way.{/i}"
        ann "{i}It’s an opportunity, huh?{/i}"
        ann "{i}As much as I usually find Boss to be a vain, money-greedy woman, she does speak some words of wisdom occasionally, doesn’t she?{/i}"
        ann "{i}I'll try hard again tomorrow!{/i}"
        ann "{i}I tug myself into bed and empty out my thoughts. The unknown future is always scary, but if we were to know everything that would befall us, what fun is life?{/i}"
        ann "{i}It’s okay to step into the dark. We’ll find our way eventually.{/i}"
        
        jump daySwitch
        
        
    label excited2:
        
        $ day += 1
                
        scene bedalicenight
        with fadee
        
        $ config.side_image_tag = ""
        
        ann "{i}Phew! Today was a blast!{/i}"
        ann "{i}Maybe this whole idol standby thing wasn't such a bad idea after all...{/i}"
        ann "{i}I'm going to work extra hard tomorrow, that's for sure!{/i}"
        ann "{i}A little rest, and then I'll be back at it tomorrow...{/i}"
        
        jump daySwitch

        ### call screen
        
        
        
label sleepy:
    
    ## $ sleepy = renpy.random.randint(1,5)


    ############### Night 2
    label sleepy1:
        
        $ day += 1
                
        scene bedalicenight
        with fadee
        
        $ config.side_image_tag = ""
        
        ann "{i}It has been such a hectic day.{/i}"
        ann "{i}I almost didn’t want to eat dinner, but knowing I’d be hungry at night otherwise, I stuffed something down my stomach, took a shower, brushed my teeth, then headed off to bed.{/i}"
        ann "{i}If not for the soundproof doors and walls, I’m sure I’d still be able to hear sounds of activity outside. The others are probably in the lounge watching a movie or something.{/i}"
        ann "{i}I would’ve joined them, but I’m just too tired. My muscles are screaming to be relaxed. I can only comply.{/i}"
        ann "{i}I lie down on the bed, relieved that the soft mattress does help my body lose some of its tension.{/i}"
        ann "{i}I close my eyes and immediately stop thinking. The darkness envelops me, and before I know it, I fall asleep.{/i}"
        
        jump daySwitch



        
        
    label sleepy2:
        
        $ day += 1
        
        scene bedalicenight
        with fadee
        
        $ config.side_image_tag = ""
        
        ann "{i}I never thought anyone could sing so much in one day!{/i}"
        ann "{i}After listening to Cherry and Taylor practice at the same time for hours on end, I feel like I could just collapse!{/i}"
        ann "{i}Between their lovely tones and the soft background music, I'm surprised I wasn't lulled to sleep back there...{/i}"
        ann "{i}But, my bed looks so comfy... Just a little rest before tomorrow will be good.{/i}"
        
        jump daySwitch
        
        ###### call screen
        
        
        
        
label insomnia:
    
    ##$ insomnia = renpy.random.randint(1,5)
    
    ################# Night 1
    label insomnia1:
        
        $ day += 1
                
        scene bedalicenight
        with fadee
        
        $ config.side_image_tag = ""
        
        ann "{i}It has been a long day.{/i}"
        ann "{i}After dinner, I took a shower, brushed my teeth, and headed off to bed, but somehow, I couldn’t sleep.{/i}"
        ann "{i}I drag myself up to a sitting position and just stay like that, hunched over my bed for a moment. Should I turn on the lights and read for a bit?{/i}"
        ann "{i}I haven’t finished the paperback I’ve been reading on my commutes before coming here, but if I start now, I doubt I could stop. Maybe I should do something less engaging.{/i}"
        ann "{i}I decide to take a walk. The night outside looks lovely.{/i}"
        
        scene fountainnight
        with fade
                
        ann "{i}I take the elevator to the roof where a garden stands.{/i}"
        ann "{i}At this hour, it’s quite dark, but parts of the garden remain lighted with panels of LED lights. The fountain looks stunning with colors playing on the rippling water surface.{/i}"
        ann "{i}I sit down on the stone by the fountain, hearing the water rise and fall. Looking upwards, I can faintly make out the stars above me.{/i}"
        ann "{i}It’s too bright here in the city to see star curtains, but the few twinkling in the dark, heavenly seas still look beautiful as rare gems.{/i}"
        ann "{i}It’s weird that I prefer this view over the view overlooking the rest of the city. We’re easily on the tallest building in town, but there is something more enticing about nature, especially at a time like this.{/i}"
        ann "{i}While looking down at all the houses and streets below may give a feeling of power and entitlement, looking at the endless expanse above is far more liberating.{/i}"
        ann "{i}I breathe in a breath of fresh air. It’s a little cold here by night, but the crisp, clean feeling is nonetheless amazing. It makes my worries slip away one by one.{/i}"
        ann "{i}Alright, I can do this.{/i}"
        ann "{i}I need not care about how others view me. I need not care about the outcome of this challenge. I just need to try as hard as I can.{/i}"
        ann "{i}I’d be able to live up to myself then.{/i}"
        
        scene bedalicenight
        with fade
        
        ann "{i}Empowered with renewed confidence, I snuggle back into bed. I may like the rooftop garden, but there’s nothing better than a warm bed on a cold night.{/i}"
        ann "{i}With the weight of all my pressures finally lifting away, I drift off into sleep.{/i}"
        
        
        jump daySwitch
        
        

######################
label night1:
    scene bedalicenight
    with fadee

    $ day += 1

    $ config.side_image_tag = ""

    a "...Nn."

    ann "{i}Stirring awake in the middle of the night, I come to a realization.{/i}"
    ann "{i}I'm, like, super thirsty. My throat's all dry too.{/i}"
    ann "{i}Maybe I'll go get a glass of water. Ehh, but the dining hall is kinda far just for water.{/i}"
    ann "{i}...Eh. I'm already awake, and if I try to go back to sleep now, I'll just think about my intense thirst.{/i}"
    ann "{i}Slipping into a robe, I get ready for the trek up the stairs.{/i}"

    scene hallnight
    with fade

    ann "{i}...It's actually a little spooky, coming out this late at night.{/i}"
    ann "{i}I guess there's still security guards mulling about, but it's not much comfort when you're out here alone.{/i}"
    ann "{i}Well, the dining hall isn't far. I'll just grab a water battle and head back. Shouldn't be more than five minutes.{/i}"

    scene dinnernight
    with fade

    $ config.side_image_tag = "alice"
    a "Alright, made it to the dining hall in one piece. Now to find the vending machines-"

    #sfx: door close

    a frowntalk "!?"

    $ config.side_image_tag = ""
    ann "{i}I heard a door closing over in the direction of the kitchen. The doors were still swinging!{/i}"

    ##TODO sfx footsteps

    ann "{i}And the loud click of footsteps followed soon after. They were getting softer, but... was someone there!?{/i}"

    $ config.side_image_tag = "alice"
    a frown down "O-oh crap, are we being robbed?? Maybe this wasn't a good idea..."

    $ config.side_image_tag = ""
    menu:
        "Run to safety":
            jump night1chickenout
        "Investigate the noise":
            jump night1progress

    label night1chickenout:
        ann "{i}Nope. Not about this life. I'm too young to die in a slasher flick.{/i}"

        scene black
        with fade
        ann "{i}I book it back to my room, lock all the doors and windows, and throw the covers over my head.{/i}"
        ann "{i}I had a pretty restless night... now I was thirsty AND terrified. Maybe I should've told someone about the robber??{/i}"
        ann "{i}...Security will be on top of it, surely...{/i}"

        jump night1end

    label night1progress:
        ann "{i}This was a really, REALLY bad idea, but my curiosity was piqued. And I doubt I'd sleep any better if I ran off.{/i}"
        ann "{i}From underneath the door frame, I could make out light moving back and forth erratically.{/i}"
        ann "{i}They must've brought a flashlight! Then they came prepared!{/i}"
        ann "{i}...To... rob a kitchen. Weird flex, but okay, sure.{/i}"
        ann "{i}I open the door just a smidge to peek inside, hoping to get a better look at the robber and profile them for later.{/i}"
        ann "{i}To my great surprise, it was someone I knew!{/i}"

        $ config.side_image_tag = "alice"
        a frowntalk down "{i}(...Mary?){/i}"

        show mary unsure frown at center:
            zoom 1.4
            yalign 0.5
        with dissolve

        ann "{i}She had a plate out on the counter, with a sandwich stacked almost a foot tall! It looked like she packed an entire deli in the thing.{/i}"
        ann "{i}...It looked really good, too. I inched forward slightly to get a better look.{/i}"
        ann "{i}It was in that moment that our eyes met. Her hands stopped as she was buttering up one of the slices of rye.{/i}"

        m frowntalk "Alice!?"
        show mary frown
        ann "{i}Ohhh crap.{/i}"
        ann "{i}Gotta think fast gotta think fast... I came here for a purpose...{/i}"

        a "...Damn, that looks really good. Can you make me one?"

        m down frowntalk "WHAT!? NO! What am I, your personal maid!?"
        show mary frown
        a frown "No, that's not what I meant! I just, since you're here and all-"

        m frowntalk "Get out! GET. OUT!"
        show mary frown
        a down frowntalk "O-okay! Just let me get my water..."

        ann frown "{i}I hurry over to the fridge, reaching for a few bottles.{/i}"

        a frowntalk "Damn, this is the premium stuff they bottle in Switzerland..."
        a frown "{nw}"

        m frowntalk "WOULD YOU STOP GAWKING AND JUST GET OUT!"
        show mary frown

        a frowntalk  "Fine, fine! Not like we're supposed to be in here anyway..."
        a frown "{nw}"

        hide mary
        with dissolve

        $ config.side_image_tag = ""
        ann "{i}Under considerable duress, I make a point of getting out of there as quickly as possible.{/i}"

    label night1end:
        
        jump daySwitch
        