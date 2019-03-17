
#######################################################################################################################
##############################################                              ###########################################
##############################################            Nights            ###########################################
##############################################                              ###########################################
#######################################################################################################################


        
        
############ Normal Night
label normalnight:

    label normalnight1:
            
        $ day += 1
        
        scene bedalicenight
        with fade
        
        $ config.side_image_tag = ""

        ann "{i}After dinner and relaxing at the lounge for a bit, I return to my room to sleep.{/i}"
        ann "{i}It has been a long day. It feels good to be back here, resting on the soft bed.{/i}"
        ann "{i}I pull the covers up to my shoulders and move into a comfortable position. The sheets smell of fresh lemony detergent, matching the residue of minty mouthwash between my teeth.{/i}"
        ann "{i}I close my eyes, ready to be further refreshed by slumber.{/i}"
        
        ###### call screen

        
    label normalnight2:
        
        $ day += 1
                
        scene bedalicenight
        with fade
        
        $ config.side_image_tag = ""
        
        ann "{i}Dinner was enjoyable as usual, even after I had to slip past the director and Boss arguing in the hallway afterwards.{/i}"
        ann "{i}This place is so huge... I feel like I haven't even began to see all of it!{/i}"
        ann "{i}Tomorrow is a new day, and with it, new opportunities.{/i}"
        ann "{i}I lay my head down and slowly but surely fall asleep.{/i}"
        
        #### call screen
        
        
    
label excited:
    
    $ excited = renpy.random.randint(1,5)
    
    label excited1:
        
        $ day += 1
        
        scene bedalicenight
        with fade
        
        $ config.side_image_tag = ""
        
        ann "{i}So much has happened today.{/i}"
        ann "{i}After dinner, I had fun with the others at the lounge. I guess I’m starting to get along after all.{/i}"
        ann "{i}It’s amazing, considering that I’ve never even imagined this situation would happen to me. I often still struggle with the idea of being here, but sometimes, I find the courage to face the things coming my way.{/i}"
        ann "{i}It’s an opportunity, huh?{/i}"
        ann "{i}As much as I usually find Boss to be a vain, money-greedy woman, she does speak some words of wisdom occasionally, doesn’t she?{/i}"
        ann "{i}I'll try hard again tomorrow!{/i}"
        ann "{i}I tug myself into bed and empty out my thoughts. The unknown future is always scary, but if we were to know everything that would befall us, what fun is life?{/i}"
        ann "{i}It’s okay to step into the dark. We’ll find our way eventually.{/i}"
        
        
        ###### call screen
        
    label excited2:
        
        $ day += 1
                
        scene bedalicenight
        with fade
        
        $ config.side_image_tag = ""
        
        ann "{i}Phew! Today was a blast!{/i}"
        ann "{i}Maybe this whole idol standby thing wasn't such a bad idea after all...{/i}"
        ann "{i}I'm going to work extra hard tomorrow, that's for sure!{/i}"
        ann "{i}A little rest, and then I'll be back at it tomorrow...{/i}"
        
        ### call screen
        
        
        
label sleepy:
    
    ## $ sleepy = renpy.random.randint(1,5)


    ############### Night 2
    label sleepy1:
        
        $ day += 1
                
        scene bedalicenight
        with fade
        
        $ config.side_image_tag = ""
        
        ann "{i}It has been such a hectic day.{/i}"
        ann "{i}I almost didn’t want to eat dinner, but knowing I’d be hungry at night otherwise, I stuffed something down my stomach, took a shower, brushed my teeth, then headed off to bed.{/i}"
        ann "{i}If not for the soundproof doors and walls, I’m sure I’d still be able to hear sounds of activity outside. The others are probably in the lounge watching a movie or something.{/i}"
        ann "{i}I would’ve joined them, but I’m just too tired. My muscles are screaming to be relaxed. I can only comply.{/i}"
        ann "{i}I lie down on the bed, relieved that the soft mattress does help my body lose some of its tension.{/i}"
        ann "{i}I close my eyes and immediately stop thinking. The darkness envelops me, and before I know it, I fall asleep.{/i}"
        
        jump week1contest



        
        
    label sleepy2:
        
        $ day += 1
        
        scene bedalicenight
        with fade
        
        $ config.side_image_tag = ""
        
        ann "{i}I never thought anyone could sing so much in one day!{/i}"
        ann "{i}After listening to Mary and Taylor practice at the same time for hours on end, I feel like I could just collapse!{/i}"
        ann "{i}Between their lovely tones and the soft background music, I'm surprised I wasn't lulled to sleep back there...{/i}"
        ann "{i}But, my bed looks so comfy... Just a little rest before tomorrow will be good.{/i}"
        
        
        ###### call screen
        
        
        
        
label insomnia:
    
    ##$ insomnia = renpy.random.randint(1,5)
    
    ################# Night 1
    label insomnia1:
        
        $ day += 1
                
        scene bedalicenight
        with fade
        
        $ config.side_image_tag = ""
        
        ann "{i}It has been a long day.{/i}"
        ann "{i}After dinner, I took a shower, brushed my teeth, and headed off to bed, but somehow, I couldn’t sleep.{/i}"
        ann "{i}I drag myself up to a sitting position and just stay like that, hunched over my bed for a moment. Should I turn on the lights and read for a bit?{/i}"
        ann "{i}I haven’t finished the paperback I’ve been reading on my commutes before coming here, but if I start now, I doubt I could stop. Maybe I should do something less engaging.{/i}"
        ann "{i}I decide to take a walk. The night outside looks lovely.{/i}"
        
        scene fountainnight
        with fade
                
        ann "{i}I take the elevator to the roof where a garden stands. At this hour, it’s quite dark, but parts of the garden remain lighted with panels of LED lights. The fountain looks stunning with colors playing on the rippling water surface.{/i}"
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
        
        
        scene morningnormal1
        with fadee
        
        
        
        
        