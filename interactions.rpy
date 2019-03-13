#######################################################################################################################
##############################################                              ###########################################
##############################################        Interactions          ###########################################
##############################################                              ###########################################
#######################################################################################################################


######## PLACE LIST ########

# Mary's Room
# Taylor's Room
# Cherry's Room
# Music Hall
# Lounge
# Shopping Area
    
        
label maryroom:
    
    $ int3 = renpy.random.randint(1,5)
    
    if mary >= 8:

        $ mary_stat += 1
        
        scene hallday
        with fade
        
        $ config.side_image_tag = ""
        
        ann "{i}The stress is really eating me away. I feel sick.{/i}"
        ann "{i}It’s weird, because I keep trying to convince myself that I have nothing to lose. I should stop caring so much. After all, Boss got the backup contestant she wanted.{/i}"
        ann "{i}Even if I were to get eliminated, I would’ve fulfilled the purpose. It’s not as though I would be punished or anything.{/i}"
        ann "{i}Life will go on as it always has. I get to keep my job. I get to keep the old roof atop my head. All is good, right? This month will just be a little vacation - and it’s for free too! Like what else could I have hoped for?{/i}"
        ann "{i}But saying all this isn’t making my heart feel any easier. I don’t want to give myself any false hopes, but it just keeps coming to me either way.{/i}"
        ann "{i}Truth is, I do want to win, huh? Even if it were impossible.{/i}"
        ann "{i}The contradiction leaves me in my current state. I’m just too preoccupied with these thoughts to focus on training.{/i}"
        ann "{i}And yet, who can I talk to about all this? My mom? She’d just say I’m silly. It’s not that she really wants to chide me, but she’d think that putting it lightly would make me feel better.{/i}"
        ann "{i}Guess where I inherited these genes of idiocy from? They obviously have to come from somewhere...{/i}"
        ann "{i}Sorry, Mom.{/i}"
        ann "{i}So I end up just wandering around the mansion, trying to keep my mind off things. I mean, just look at everything here, so ridiculously lavish.{/i}"
        ann "{i}I’m sure some exotic vase from some distant Chinese dynasty or whatnot would be enough to keep me preoccupied... maybe...{/i}"
        ann "{i}Before I know it, I’m here, in front of Mary’s room. The door is left open.{/i}"
        ann "{i}Why am I even here? I mean, I’ve been hanging out with Mary a little, but that doesn’t mean I intend to confide my problems with her!{/i}"
        ann "{i}I was about to walk away when something within her room captures my gaze. It’s a painting. Mary is busily working on it - probably the reason why she has yet to notice my presence.{/i}"
        ann "{i}The painting is not clean and neat. I can’t exactly pinpoint what she is painting at all. But the turbulent colors resonate with my heart.{/i}"
        ann "{i}Blazing hues evoke pride and confidence, lighter yellows speak of a more subdued hope. Then all of this mingles and clashes, forming darker streaks at their interface, just like the doubts I am feeling.{/i}"
        
        m "Alice...?"
        
        $ config.side_image_tag = "alice"

        show mary unsure frown at center:
            zoom 1.4
            yalign 0.35
        with dissolve
        
        a frowntalk "Ah! I'm sorry! I didn't mean to peak!"
        
        ann frown "{i}Well, I already did. Like my denial amounts to anything.{/i}"
                
        m up talk "I don't mind an audience."

        show mary smile

        a frowntalk "I see..."

        a frown "{nw}"
        
        m frowntalk "It means that you can come in and take a seat if you want."
        
        show mary frown

        a talk "Thanks."
        
        ann smile "{i}It’d be rude if I refused. Plus, I do actually want to take a closer look at the painting.{/i}"
        
        scene bedmaryday
        with fade
        
        show mary up smile at center:
            zoom 1.4
            yalign 0.35
        with dissolve
        
        a frowntalk "You're so good at everything you do, Mary."
        
        ann frown "{i}I can’t help but utter this sentence. It may sound like a praise to Mary, but maybe I’m just saying it to myself to reaffirm my own incompetence.{/i}"
        
        m frowntalk "This is just a random splatter of paint. I’m sure anybody can do it."

        show mary smile
        
        a frowntalk "You've got to be kidding."

        a frown "{nw}"
        
        m unsure frowntalk "Why would I be? Do you see anything distinct here?"
        
        show mary frown
        
        a frowntalk "Well... no..."

        a frown "{nw}"
        
        m talk "That’s because I’m not an artist. I merely enjoy the feel of putting paint on canvas."
        
        show mary smile
        
        a frowntalk "But... it looks good."
        
        a frown "{nw}"
        
        m "The paint is good quality, I suppose."
        
        show mary smile
        
        ann frown "{i}I don’t know what to say. Mary does sound serious here. So she hasn’t ever had any formal artistic training?{/i}"
        
        a frowntalk "You must be really talented then."
        
        a frown "{nw}"
        
        m frowntalk "Or I just have the guts to waste high quality paint on high quality canvas? What makes you think you can’t do the same?"
        
        show mary frown
        
        a down frowntalk "I didn’t get very high grades whenever painting is concerned."
        
        a frown "{nw}"
        
        m frowntalk "I didn’t get any grades on painting because I never took a class. Now kill me."
        
        show mary smile
        
        ann up smile "{i}I enjoy a little laugh with Mary. She then hands her brush over to me.{/i}"
        
        m "Here, give it a try."
        
        show mary smile
        
        a frowntalk "You mean... on your painting?"
        
        a frown "{nw}"
        
        m frowntalk "Why not? It’s not as though I’m trying to sell it. And who knows, maybe after your expert fine-tuning, it’d really be worthy of sale."
        
        show mary smile
        
        ann "{i}I reluctantly take up the brush and wonder how should I start. What color should I use? Where should I paint?{/i}"
        ann "{i}Mary’s painting is already perfect without my tampering, perfect just like her.{/i}"
                
        m frowntalk "Why are you hesitating?"
        
        show mary frown
        
        a frowntalk "I... I don't want to make it worse."
        
        a frown "{nw}"
        
        m frowntalk "What do you mean worse?"
        
        show mary frown
        
        a frowntalk "I... don't really know. If I knew, I wouldn't mess it up, right?"
        
        ann frown "{i}Mary sighs, coming around behind me. She clasps onto my hand that is holding the brush.{/i}"
        
        m talk "Now paint. If I don’t like what you do, I’d be able to stop you. I bear the final responsibility here."
        
        show mary smile
        
        a frowntalk "Mary?"
        
        a frown "{nw}"
        
        m frowntalk "Look, Alice. You need to be more confident."
        
        show mary frown
        
        a frowntalk "I know. I'm trying."
        
        a frown "{nw}"
        
        m frowntalk "But you think the problem of your wavering is that you’re not good enough to be confident?"
        
        show mary frown
        
        a frowntalk "How did you..."
        
        a frown "{nw}"
        
        m frowntalk "It's all over your face. At the show, while you're practising here, heck, while you are walking these halls - you just give off the aura of \"I'm not good enough\"."
        
        show mary frown
        
        a frowntalk "But I'm {i}not{/i} good enough. I'm not like you."
        
        a frown "{nw}"
        
        m frowntalk "Not as rich as me? Being rich doesn’t make you a better singer."
        
        show mary frown
        
        a frowntalk "But you were born in this kind of environment. You know how to act in this kind of environment."
        
        a frown "{nw}"
        
        m frowntalk "Which is what? To act like what common people like you would call snobs? I am well-aware of what people call me behind my back."
        
        show mary frown

        a frowntalk "That's... I don't mean to put it that way..."
        
        a frown "{nw}"
        
        m frowntalk "And I do not take offense. People react differently to the environment around them. There is no right or wrong. Why can’t you gawk at the beautiful furnishings and call it a waste of societal resources like Taylor does?"
        
        show mary frown
        
        a frowntalk "I suppose I can... but that’s not the issue here, right? The rich thing... yes. I guess I have felt a little inferior because of it and come to think of it, it is stupid. But rich or not, you and the others are better singers. I can’t change that!"
        
        a frown "{nw}"

        m frowntalk "Yes you can. If you work harder. If you pour your heart into it."
        
        show mary frown

        a frowntalk "I don't believe I...{w=1.0}{nw}"
        
        a frown "{nw}"
        
        m talk "Then believe."
        
        show mary smile
        
        ann "{i}Mary plunges the brush into pure red paint and presses it against the canvas.{/i}"
        
        a down frowntalk "No!"
        
        a frown "{nw}"
        
        m talk "It's not too late to change what I'm doing. Fight me for control over the brush."
        
        show mary smile
        
        ann "{i}I finally strengthen my grip and drag the brush in a curve down the left side of the painting, then with the remainder of the paint, I draw a similar curve down the right side.{/i}"
        ann "{i}It’s a heart, my heart, bleeding red.{/i}"
        
        a frowntalk "These are my feelings. I want to have hope, but whenever I feel it, it’s accompanied by darkness. I’m worried that I won’t succeed. It’s stupid, because I have no right to be asking for success to begin with!"
        
        a frown "{nw}"
        
        m talk "You have every right."
        m "Didn’t I draw this because it’s exactly what I felt, too?"
        m "You may think that I’m confident and proud, but like you said, whenever you have hope, you’d have the worry of not fulfilling the hope. It’s like wherever there is light, a shadow would be cast."
        
        show mary smile
        
        ann "{i}I can’t quite believe Mary would have such mundane worries too. She should have no doubts that she’d at least be a finalist!{/i}"
        
        m talk "I think the heart you painted really completes the picture. It shows that anybody with a heart can be bothered by these conflicting emotions."
        m "It may be so painful that it’s like our hearts are bleeding! But look, isn’t the red so vivid? This must be what it means to be alive."
        
        show mary smile
        
        a frowntalk "You make everything sound so sentimental, Mary..."
        
        a frown "{nw}"
        
        m talk "You’re the one who painted it."
        
        show mary smile
        
        a up talk "Didn’t you say you were gonna bear the final responsibility?"
        
        ann smile "{i}We laugh together again. Mary pats my shoulder, smiling.{/i}"
        
        m talk "Look, Alice. We’re all on the same boat. Don’t doubt yourself. All of us should have the right to want to win. That’s why we are here."
        
        show mary smile
                
        ann "{i}I don’t know what to say. Maybe Mary is right. Even if I don’t stand a chance of winning, I can still dream, right?{/i}"
        
        a talk "Thanks. I think I feel better now."
        
        a smile "{nw}"
        
        m talk "Knowing that you aren’t the only one who thinks badly of yourself?"
        
        show mary smile
        
        a talk "Well... it came as a surprise that you’d also have these thoughts... and I hate to admit it, but yeah, I guess I do feel better knowing I’m not alone."
        
        a smile "{nw}"
        
        m frowntalk "Asshole."        
        m talk "But I feel better too. I don’t like being alone either."
        
        show mary smile

        ## end scene

        
        
        
label taylorroom:
    
    $ int4 = renpy.random.randint(1,5)
    
    if int4 == 1:
        
        scene bedtaylorday
        
        ann "{i}I wanted to ask Taylor for some words of confidence, but it seems like he isn't in his room. Maybe another time.{/i}"
        


label cherryroom:
    
    $ int6 = renpy.random.randint(1,5)
    
    if int6 == 1:
        
        scene bedcherryday
        
        ann "{i}I wanted to ask Cherry for some advice, but it seems like she is not in her room. Maybe next time.{/i}"
        
 
 
        
label musicroom:
    
    $ int11 = renpy.random.randint(1,5)
    
    if int11 == 1:
        
        scene musicroom
        with fade
        
        ann "{i}Seems like I'm the only one in the music room. Let's use the opportunity to practice lots!{/i}"
        
    if int11 == 2:
        
        scene musicroom
        with fade
        
        ann "{i}I should really get some practicing done. I'm still not very confident about my skills.{/i}"
        ann "{i}I head down to the music room. Seems like Mary is already there.{/i}"
        
        show mary up frown at center:
            zoom 1.4
            yalign 0.35
        with dissolve
        
        m frowntalk "You here to practice too?"
        
        show mary smile
        
        a talk "Yeah, I was thinking about it, but if you want to be left alone..."
        
        a smile "{nw}"

        m talk "Let's practice together."
        
        show mary smile
                
        a frowntalk "You sure? I'm not really good, and..."
        
        a frown "{nw}"

        m frowntalk "Do you have a secret skill you're hiding or something?"
        
        show mary smile

        a frowntalk "Of course not!"
        
        a frown "{nw}"

        m talk "Then why hesitate? Let's work together to become better singers."
        
        show mary smile
        
        ann "{i}If Mary is willing to practise with me, I think I’d benefit a lot from working with her. It’d be more fun to have company too. Mary is actually quite nice now that I’m getting to know her better.{/i}"
        
        a talk "Alright. Let's start!"
        
        a smile "{nw}"

        $ mary_stat += 1
        
        ## end scene
        

label lounge:
    
    $ int13 = renpy.random.randint(1,5)
    
    if int13 == 1:
        
        scene loungeday
        
        ann "{i}I haven't watched TV in a while. Gotta catch up on some sappy romance drama and watch the news!{/i}"
        

        
label rooftop:  ## garden
    
    $ int15 = renpy.random.randint(1,5)
    
    if int15 == 1:
        
        scene fountainday
        with fade
        
        ann "{i}I really need a breath of fresh air. I enjoy the peace and serenity of the rooftop garden.{/i}"
        
    if int15 == 2:
        
        scene fountainday
        with fade
        
        ann "{i}I really need a breath of fresh air. I head upstairs to the rooftop garden.{/i}"        
        ann "{i}Seems like I’m not the only one. Mary is also at the garden, practicing.{/i}"
        
        show mary up frown at center:
            zoom 1.4
            yalign 0.35
        with dissolve
        
        a talk "Hey, Mary."

        a smile "{nw}"
        
        m frowntalk "Good morning. Are you here to practice too?"
        
        show mary frown 

        a talk "Nah. I'm just here to relax."
        
        a smile "{nw}"

        m frowntalk "I'm not disturbing you, right? I can practice elsewhere if you want."
        
        show mary smile
        
        a talk "That's okay. You aren't bothering me."
        
        a smile "{nw}"

        m talk "Thanks."
        
        show mary smile
        
        ann "{i}Mary continues practicing, projecting her voice into the crisp, morning air. I have fun watching her, even learning a bit along the way.{/i}"
        
        $ mary_stat += 1
        
        
        
label shopping:
    
    $ int16 = renpy.random.randint(1,5)
    
    if int16 == 1:
        
        scene shop
        
        ann "{i}I need a break from everything. I have fun doing some shopping on my own.{/i}"
















