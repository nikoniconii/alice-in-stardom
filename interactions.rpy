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
    
        
label maryroom1:

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
    
    m frowntalk "It's all over your face. At the show, while you're practicing here, heck, while you are walking these halls - you just give off the aura of \"I'm not good enough\"."
    
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

    if day == 3:
        jump excited1

    ## end scene

    
label mary1:

    scene makeuproom
    with fade

    $ config.side_image_tag = ""

    an "I think I'll find Mary over in the Makeup room."
    an "It's odd that the cosmetologist spends so much more time with Mary than the other girls. Stranger still, that she insists on getting her work down alone..."
    an "Even Jacques doesn't get to peep inside, and he basically owns the joint! It's so curious..."
    an "I think I'll surprise her. Then I can get to the bottom of this!"

    ## TODO sfx rattle door

    $ config.side_image_tag = "alice"

    a frowntalk "...Aaaaaand the door's locked. Damn."
    a frown "{nw}"

    m "Ugh, haven't you ever heard of knocking!?"

    ma "Calm down, we're almost done..."

    an "The door was thin. Even with the barrier between us, Mary's shrill commands were still piercingly loud."
    an "With a sigh, I waited a few minutes. Good time to collect my composure - speaking with Mary was a trial."

    ## TODO sfx door open

    scene makeuproom
    with fade

    show mary up frown at center:
        zoom 1.3
        yalign 0.4
    with dissolve

    m frowntalk "...You wished to see me?"

    show mary frown

    a talk "Oh hey! Mary! I wanted to talk to you!"

    a smile "{nw}"

    m frowntalk "...Talk? About what? Make it quick, I have a busy day."

    show mary frown

    an frown "Mary's tone was guarded. She didn't seem too happy to see me."
    an "She raised a hand to her forehead, trying to cover something up. She seemed to be hiding something..."
    a frowntalk "...What are you doing?"

    a frown "{nw}"

    m down frowntalk "What am I- I'm wiping my brow! Nearly got blush in my eyes..."

    show mary frown

    an "...That didn't seem to be what she was doing. And the way her voice raised was quite suspicious."
    an "I thought I saw something near her scalp. A thin line, barely noticeable."
    an "I think it's..."
    
    menu:
        "Her hairline.":
            jump mary1hairline
        "A scar.":
            jump mary1scar
        "The light getting in her eyes.":
            jump mary1sun

    label mary1hairline:
        a frowntalk "Oh no, is that your hairline?"
        a frown "{nw}"

        m frowntalk "What? What are you talking about?"

        show mary frown

        a frowntalk "Are you balding? It's okay, this competition is really stressful."
        a frown "{nw}"

        m "...?"
        a talk "I bet you could pull off a wig really well-"
        a frown "{nw}"

        m down frowntalk "I'M NOT GOING BALD! IDIOT!"

        show mary frown

        a frowntalk "...Oh."
        an frown "A swing and a miss."
        jump mary1merge

    label mary1scar:
        a frowntalk "Is it some kinda scar? Did you have surgery?"
        a frown "{nw}"

        m unsure frown "..."
        an "She cringed to herself. Looks like I hit the nail on the head."
        m frowntalk "Ugh, I was hoping to avoid this conversation entirely while I was here."
        jump mary1merge

    label mary1sun:
        a talk "Oh! The sun's getting in your eyes! I got some sunglasses in my purse."
        a smile "{nw}"
        m frowntalk "What the devil are you talking about? We're indoors!"
        show mary frown
        a talk "Well, the lighting in here gets pretty bright too. Like on set?"
        a smile "{nw}"
        m up frowntalk "...That's an impressive display of idiocy. I'm earnestly gobsmacked."
        show mary frown
        an frown "...Yeaaaah, not sure what I was thinking there."
        jump mary1merge

    label mary1merge:
        m frowntalk "It's a scar. You can stop looking, it's not a big deal."
        show mary up frown
        a talk "Aww, you don't have to be shy about it. It's barely noticeable."
        a smile "{nw}"
        m down frowntalk "{i}Well you sure noticed it!{/i}"

        show mary frown

        a frowntalk "H-hey, easy girl, calm down!"
        a frown "{nw}"

        m frowntalk "Tch. When I was younger, I begged my parents to let me into a ballet class."
        m "I slipped and hit my head against a metal bar at a bad angle. It was rather bloody."
        show mary frown
        a frowntalk "O-oh no, I... I didn't mean to dredge up bad memories..."
        a frown "{nw}"
        m up frowntalk "Don't pity me. Save your sympathy for someone else."
        show mary frown
        a up frowntalk "...Sorry?"
        a frown "{nw}"
        m frowntalk "My parents speed-dialed the family surgeon, and he sewed it up within half an hour. And that was that."
        m "Of course, Mother wouldn't let me back {i}into{/i} ballet. I must've been too fragile for it."
        show mary frown
        a talk "Well, hey, if you wanna be a dancer, why not ask Taylor? I hear she used to be on the circuit."
        a smile "{nw}"
        #sprite: look aside
        m "..."
        m frowntalk "...I will consider it. Goodbye."
        show mary frown

        hide mary with dissolve

        $ config.side_image_tag = ""
        
        an "With her parting words, Mary brushed past me. She was eager to keep her distance from me..."
        an "I hope I made a decent impression. It feels like I know nothing about her."
        an "Well, if she's not gonna talk to me, I guess I can chase her down some other day."

        if day == 1:
            jump insomnia1
        elif day == 2:
            jump sleepy1


        ## end scene


        
        
label taylorroom:
    
    label taylor1:
        scene hallday
        with fade

        $ config.side_image_tag = ""

        an "I opt to head over to Taylor's room for now."
        an "Her trailer's a bit of a walk to get to. It doesn't see a lot of foot traffic, and you kinda have to go out of the way to reach it."
        an "Stopping right in front of the door, I overhear some muffled music from the other side."
        an "It sounds {i}super familiar{/i}, but I can't quite put my finger on it."

        ## TODO sfx: knock knock

        ann "I knock at the door to her trailer, adding a bit more oomph. Hopefully the music wouldn't drown it out."

        $ config.side_image_tag = "alice"

        t "Door's open!"

        a frowntalk "Ah-"

        a frown "{nw}"

        ## TODO sfx door open

        scene black
        with dissolve

        an "Letting myself in, I catch a glimpse at the interior of Taylor's room."

        scene bedtaylorday
        with fade

        an "It's pretty organized, with each corner of her space dedicated to something. There was a yoga mat to the far corner, some exercise equipment..."
        an "She managed to fit a sofa in here! And that's where she was, sprawled along it as she picked at a pile of peeled oranges. She's watching some kind of movie on her TV."
        
        show taylor up frown at center
        with dissolve

        t frowntalk "Oh. Hey, Alice. Didn't expect you, what's up?"

        show taylor frown

        an "She turns her head to me with an affirmative nod."

        a frowntalk "Ah! I just wanted to see what you were up to! We barely talk, soooo..."

        a frown "{nw}"

        t frowntalk "...You know we're {i}competing{/i} against each other, right?"

        show taylor frown

        a talk "Right! Right, of course, but... we can still do stuff. I just kinda wanted to get to know you a bit better, that's all."
        
        a smile "{nw}"

        t "..."

        show taylor:
            zoom 1.4
            yalign 0.40
        with dissolve

        an frown "Taylor gave me a long look, like she was studying me and downloading my psyche. It was a little unnerving."
        an "Was she undressing me with her eyes?? Wait, no, you're only supposed to do that on stage..."

        t frowntalk "...Alright. I can vibe with that. C'mon, take a seat."

        show taylor frown:
            yalign 0.35

        an "She sat up, patting the spot next to her. Oh my gosh, she's accepting me as one of her own!"
        an "I take a seat next to her, getting a better look at the screen. There was some kind of a dance off in a dingy street alley..."

        t frowntalk "You remember \"Hiphop Streetz\"? They made a bunch of these movies."

        show taylor frown

        a talk "Vaaaaguely. I remember this song though! From Tiffany Lancer!! They played it everywhere when I was a kid!"
        a "Gosh, I wonder what she's up to nowadays, she was a huuuuge star..."

        a smile "{nw}"

        t frowntalk "Something about a mental breakdown. She drove her Impala into a fountain, hopped up on anti-depressants."

        show taylor frown

        a frowntalk "....Ohhhhhh. Ohhh noooo."

        an frown "Well, that was awkward. Silence hung in the air, the sick beats of the movie filling the void."
        an "I should probably say something..."

        menu:
            #negative
            "These movies are inspirational.":
                jump tbad1
            #positive
            "They're really good dancers!":
                jump tgood1
            #neutral
            "Do you watch a lot of movies?":
                jump tneutral1

        label tbad1:
            a talk "I love these kinds of underdog stories. They're so inspirational..."

            a smile "{nw}"

            t frowntalk "Eh. I dunno. I feel like movies like this kinda trick kids?"

            show taylor frown

            a frowntalk "Huh? What do you mean?"

            a frown "{nw}"

            t frowntalk "You don't get to be a superstar in a matter of two-and-something hours. You really gotta buckle down and {i}work{/i} at it, y'know?"
            t "And getting good at anything that matters takes years and years of dedication. Manufactured stuff like this kind of sends the wrong message."
            
            show taylor frown

            a frowntalk "...Then why are you watching it?"

            a frown "{nw}"

            t frowntalk "Pfft, it's not for the writing or anything. The choreography's sick, and I'm taking notes."

            show taylor frown

            a frowntalk "...Ohhhh."
            an frown "So she was studying after all."
            an "I don't think I made a very good impression..."
            jump tmerge1


        label tgood1:
            $ taylor_stat += 1

            a talk "These dancers are incredible, wow!"

            a smile "{nw}"

            t talk "Yeah, right? The actual writing's all over the place, but who cares. These guys are definitely professionals."
            t frowntalk "Sucks that you're only getting to see the end of it, though. Maybe I can loan you the disc?"

            show taylor frown

            a frowntalk "Really? You'd do that?"

            a frown "{nw}"

            t talk "Yeah. I think it's good research material. Being a pop idol isn't about having great chords, you gotta have energy and stage presence."
            t "And you can say a lot with the right motions of the body... you're feeling me, right?"

            show taylor frown

            a talk "Yeah, yeah! Of course! Ah, now I wish I took classes a lot sooner."

            a smile "{nw}"

            t talk "Heheh! You got plenty of time, don't sweat it."

            show taylor smile

            an "We really hit it off! That went great!"
            jump tmerge1

        label tneutral1:
            a talk "Do you watch a lot of movies, Taylor?"

            a smile "{nw}"

            t frowntalk "Mm. I let them play in the background. They're good background noise for when I'm doing something actually important."
            t "Liiiike... you watch documentaries? They're good for new perspectives. I probably prefer those."

            show taylor frown

            a frowntalk "...These movies aren't based on true stories though, aren't they?"

            a frown "{nw}"

            t frowntalk "Nah. I mean, maybe. Who knows? I'm just in it for the choreography."

            show taylor frown

            an smile "I learned something new about Taylor, at least."
            an "I made an okay impression, I guess."
            jump tmerge1

        label tmerge1:
            scene bedtaylorday
            with fade

            an "Before long, Taylor and I finished watching the movie."

            show taylor up frown at center:
                zoom 1.4
                yalign 0.40
            with dissolve

            a talk "I should get going. Thanks for having me, Taylor!"

            a smile "{nw}"

            t frowntalk "No problem. Don't be a stranger."

            show taylor frown

            an "It was strange. I kinda kept my distance, thinking she was so serious and aloof, but... she's nicer than I gave her credit for!"

            if day == 3:
                jump excited1

            ### end scene


label cherry1:

    scene bedaliceday
    with fade

    $ cherry_stat += 1

    an "I wonder what Cherry's up to? I'll call her."
    ## TODO sfx ringtone
    "{cps=40}... ... ...{/cps}"
    c "Hello?"
    a "Heyyy, Cherry, it's Alice. You up to anything?"
    c "Oh, Alice! I'm getting my hair done in the makeup room! You should come over, we can get matching styles!"
    c "...What? Oh, the hairstylist says we're not allowed it. Producer says something something, blah blah blah."
    a "Well, sure! Be right over."

    scene black
    
    an "I make a beeline to the makeup room. I don't know if Cherry was almost done..."

    scene makeuproom
    with fade

    $ config.side_image_tag = "alice"

    an "...When I arrived, though, it looks like they had barely started. The hairstylist looked flustered."
    hs "Alice, honey, can you talk some sense into this girl? She's driving me up the wall..."
    an "Heaving a sigh, the hair stylist stepped out the back. Presumably to get a smoke - she reeked of tobacco."
    a frowntalk "Uhhhh... okay."
    a frown "{nw}"

    show cherry up smile at center:
        zoom 1.4
        yalign 0.4
    with dissolve

    c talk "Aliceee! What's up?"
    show cherry smile
    a talk "Not much, I just... figured I'd catch you at the tail end of your appointment."
    a smile "{nw}"
    c frowntalk "Ohhh, I'm still deciding what I wanna do. I wanted a beehive, but the hairstylist said no..."
    show cherry frown
    a frowntalk "A beehive? From, like, the fifties? ...Why?"
    a frown "{nw}"
    c talk "Well, it'd make me look taller, and more mature... and the bees would have a home too!"
    show cherry smile
    a down frowntalk "Wh... i-it's not a {i}literal beehive{/i}, Cherry!"
    a frown "{nw}"
    c down frowntalk "Wha? Oh no... then they won't have a home. You know they're all dying, right?"
    show cherry frown
    a up frowntalk "I can't imagine they'd fair any better inside your hair. Hair spray's probably another chemical that's bad for them."
    a frown "{nw}"
    c frowntalk "Ah, really? ...Maybe I could use honey..."
    show cherry frown
    a talk "Okay! How about we pick out a style for you that {i}doesn't{/i} drive the hairstylist to drink?"
    a smile "{nw}"
    c talk "Mm... okay! I don't really see the point though..."
    c "Iiiiiii'm thinkingggg... Long hair. Or no hair."
    show cherry smile
    a frowntalk "...Okay, I'll bite. Why would you want to go bald?"
    a frown "{nw}"
    c talk "I could wear a wig like my mum, before she went into chemo! Then my hair could be {i}whatever I want!{/i} It could be pink, or white, or shamrock green..."
    show cherry smile
    a frown "!"
    an "...Should I ask her about that?"

    menu:
        "Ask about it":
            a frowntalk "Your mom had cancer...?"
            a frown "{nw}"
            c talk "Ah, yeah. But she's better now! She's in town, actually."
            show cherry smile
            a talk "Oh, really? Thank god..."
            a smile "{nw}"
            c talk "Mmhm! When the producer heard about it, she paid out of her own pocket to fly her out. She's gonna be in the front row!"
            c "So I gotta look really good for Mom. I love her a lot..."
            show cherry smile
            a talk "...Well, let's see if we can't get this figured out."
            an smile "Cherry revealed something close to her heart to me. For someone as flighty as her, she's uncompromisingly caring about the people around her."
            jump cherry1merge

        "Don't ask about it":
            an frown "Might be a painful talk. I opt to change topics."
            a talk "I think the producer would prefer long hair, at least."
            a smile "{nw}"
            c talk "Mmmm, okidoke. Lesse..."
            show cherry smile
            jump cherry1merge

    label cherry1merge:
        hide cherry with dissolve

        an "Cherry and I spend some time looking over hairstyles."
        an "Before long, Cherry has something picked out... and the hairstylist boots me out so she can work. Rude..."

        if day == 3:
            jump excited1
        ## end scene



label cherry2:

    scene hallway
    with fade

    an "Cherry said she was working on something over in the dining room. Maybe I'll head over there to check on her."

    scene dinnerday
    with fade

    $ config.side_image_tag = "alice"

    an "I catch her at a table by herself. She's surrounded by emptied bottles of store-bought cappuccinos."
    c "Alice! Over here!"

    show cherry up smile at center:
        zoom 1.4
        yalign 0.4
    with dissolve

    a talk "Hey!! ...What are you doing over here?"
    a smile "{nw}"
    c talk "Aaaah, I have to work on my speech. The director wants me to answer a bunch of questions for the next episode but..."
    c "....I'm a little blocked over here. Everything I'm thinking of, is... kinda boring."
    show cherry smile
    a frowntalk "Mm? What kind of questions?"
    a smile "{nw}"
    c talk "Ohhh, just... personal questions. Like... what my dream job was gonna be. My inspirations..."
    c "My favourite animal? I thought that was kinda obvious. Oh, you think they'd let me have like twenty rabbits on stage to perform? Can you train rabbits to dance??"
    show cherry smile
    a frowntalk "What?? I... I really doubt that."
    a frown "{nw}"
    c frowntalk "...Awwww..."
    show cherry frown
    an "Cherry deflated, flopping over the table."
    a talk "...Well, if you're stuck, maybe I can help? Do you have anything written down?"
    a smile "{nw}"
    c frowntalk "Mmmmm. I went with my gut on some of these."
    show cherry smile
    an "Cherry slid some papers over to me."
    a talk "Alright, lesse... when you were growing up, you wanted to be a..."
    a frowntalk "...Veterinarian?"
    a frown "{nw}"
    c talk "Yeah! I wanna work with animals, and help at a zoo, and stuff!"
    c "I guess it's not as interesting as, well... Mary wants to be a fashion tycoon, and Taylor, um... I don't know, she wouldn't tell me."
    show cherry smile
    an smile "It sounds like Cherry already talked with the other two about this."
    a talk "Well, hey, that's a good idea, Cherry! Everyone loves animals! But... don't you have to go to school for that?"
    a smile "{nw}"
    c talk "Yeah, you do. I was thinking of getting into university for that, but... I ended up auditioning for this show instead."
    show cherry smile
    a frowntalk "Oh, is that how that happened? I guess they put us all through those nationwide auditions."
    a "I just wanted to see how far I'd go, honestly. I'm not even really sure where I'll end up by the end of it."
    a smile "{nw}"
    c talk "Mmhm... my friends kinda dared me to do it, and I wasn't really sure I was good enough."
    show cherry smile
    a talk "Heh! Well you sure showed them, right? You're in the finals!"
    a smile "{nw}"
    c talk "...Hehe. I guess so. It's a little reassuring I'm not the only one just kinda riding along."
    show cherry smile


    ## end scene


label cherry3:
    an "The next contest is coming up soon. I should probably get some practice in ahead of time."
    an "Cherry's probably in her room. Out of all the girls, she's definitely the most approachable."
    an "I'll go see what she's up to."

    scene hallwayday
    with fade
    ## TODO sfx doorknock

    an "I knock on her door."
    $ config.side_image_tag = "alice"
    a talk "Hey, Cherry, it's Alice! Are you free right now?"
    a smile "{nw}"
    c "..."
    a talk "I figured we can practice together! How does that sound?"
    a smile "{nw}"
    c "...Okaay."
    a frown "...?"
    an "Cherry didn't seem all that enthused about it. Which was weird, because it's... Cherry."
    a frowntalk "May I come in?"
    a frown "{nw}"
    c "...Okaaay."
    a "...Mm."
    an "At least the door was unlocked. I let myself in."

    scene bedcherryday
    with fade

    show cherry up frown at center:
        zoom 1.4
        yalign 0.4
    with dissolve

    an "I didn't usually get to see the inside of Cherry's room. The mood was more anxious than I expected."
    an "Cherry was sitting at a table by herself. She had a bowl of corn flakes - it looked like she hadn't touched them in a while."
    an "And the expression on her face was pretty miserable. I should say something."
    a frowntalk "Hey, Cherry, you okay?"
    a frown "{nw}"
    c frowntalk "...I dunno."
    show cherry frown
    an "Yeah, something was up. Normally it was difficult to get Cherry to quiet down for a second. Now it was a struggle for her to string together more than two words."
    a frowntalk "Did something happen? ...Oh no, did your mom-"
    a frown "{nw}"
    c frowntalk "No, no, nothing like that, I... sorry, I'm not really feeling it today."
    c "...Feeling really self-conscious today, that's all."
    show cherry frown
    a frowntalk "Oh. Sorry, I... d-do you wanna talk about it?"
    a frown "{nw}"
    c frowntalk "...I guess it can't hurt."
    show cherry smile
    an "I talke a seat across from her. I give her a gentle nod, encouraging her to speak her mind."
    c frowntalk "...I feel like I'm in over my head here. Like I'm... not good enough?"
    c "Like... Everyone else is way smarter, and they were working towards this way longer, and I kinda feel like... like I don't belong."
    show cherry frown
    an "She seemed pretty bummed about this. I should say something..."

    menu:
        "That's not true!":
            jump cherry3negative
        "I can relate":
            jump cherry3neutral
        "You're not wrong, but...":
            jump cherry3positive

    label cherry3negative:
        a frowntalk "That's not true, Cherry! You won a lot of other contests to get this far!"
        a "And everyone thinks - no, they {i}know{/i} you're super talented."
        a frown "{nw}"
        c frowntalk "Yeah, but... sometimes it feels like it's a trick, like..."
        c "Like I'm really a fraud, and nobody else knows that, and it just makes this loop in my head and..."
        show cherry frown
        a frowntalk "...Ah."
        a frown "{nw}"
        c frowntalk "Sorry, this is my fault, when I get depressed, it's hard to... turn it off."
        show cherry frown
        an "I have a feeling I ended up making Cherry feel worse."
        jump cherry3merge

    label cherry3neutral:
        a frowntalk "If it helps, you aren't the only one. Mary and Taylor are in a whole other world, but..."
        a "We're still here, and we can tough it out. I think it just helps to do the best that we can."
        a frown "{nw}"
        c frowntalk "Yeah. I-I agree. I guess that's how you made it this far."
        c "I wish I could be as determined as you are. At least I'm not alone in feeling a little... weird."
        show cherry frown
        a talk "...Yeah. You aren't alone."
        an smile "I think I helped Cherry feel a little bit better."
        jump cherry3merge

    label cherry3positive:
        a frowntalk "You feel like you're not good enough, and I get that, it... self-comparisons are really hard."
        a frown "{nw}"
        c frowntalk "...Yeah..."
        show cherry frown
        a frowntalk "I don't wanna disregard your feelings. I just want you to know that..."
        a talk "...I think you're incredible, and I know you can work past this."
        a smile "{nw}"
        c "...!"
        c frowntalk "Y-you really think so?"
        show cherry frown
        a talk "You came this far, right? I believe in you."
        a smile "{nw}"
        c talk "...Hehe. I'll try not to let you down."
        show cherry smile
        an "It seems like Cherry was really happy to hear that someone believes in her."
        jump cherry3merge

    label cherry3merge:
        c talk "...Maybe I just need a distraction. We can go practice if you like."
        show cherry smile
        a talk "Yeah. That might help. We could probably just do it here if you like."
        a smile "{nw}"
        c talk "Like, some voice exercises? Taylor does some weird ones from someplace far away, and it's like, {i}wawawawaaaa...!{/i}"
        show cherry smile
        a frowntalk "...What {i}is{/i} that? Is it like yodelling?"
        a frown "{nw}"
        c frowntalk "No, with the throat, like, {i}wawaWAAAA!{/i}"
        show cherry smile
        a frowntalk "...Wha...?"
        a frown "{nw}"
        c frowntalk "No, lower!"
        show cherry frown
        a frowntalk "...wawawa..."
        a frown "{nw}"
        c talk "Hehe! Closer!"
        show cherry smile
        an "I'm not sure what Mongolian throat vocalization had to do with idol practice, and we both looked like idiots trying to emulate it..."
        
        $ config.side_image_tag = ""
        hide cherry with dissolve
        an "But it cheered Cherry up. I think that's a net positive."
        ## end scene



        
label musicroom:
    
    
    label musichall2:
        scene musicroom
        with fade

        $ config.side_image_tag = ""

        an "I feel like swinging by the music hall. I can get some practice in."
        an "Performing on the big stage is still kind of a new thing, so I need to get in as much practice as I can."
        an "...I figured some of the other girls would have the same idea, but I don't see anyone. What gives?"
        an "...Oh, wait, scratch that, the Boss is here. She's just in front of the stage, holding... a clipboard?"

        ## TODO sfx banging wood

        $ config.side_image_tag = "alice"
        
        a down frowntalk "Ah-!"
        an frown "She was banging the back of her hand against the stage! What on earth was she doing?"
        an "...Y'know what, I'll just ask her."
        a frowntalk "Um, miss producer?"
        a frown "{nw}"

        show katja frown at center:
            zoom 1.2
            yalign 0.4
        with dissolve

        k frowntalk "Ugh, what is it, Alice? Can't you see I'm busy?"

        show katja frown

        an "...?"
        an "I squint my eyes, trying to make out what exactly she was doing."
        a frowntalk "...Sorry, I don't think I see it."
        a frown "{nw}"

        k frowntalk "Seriously? Ugh, stupid kids..."

        show katja frown

        an "Shaking her head, she scribbled something in her clipboard."

        k frowntalk "I'm doing a preliminary check of the entire set. I kindly suggest you stay the hell out of my way for the time being."
        
        show katja frown

        a frowntalk "...Is that your job? I thought you just, um, paid for everything."
        a frown "{nw}"

        k frowntalk "It pays to have an eye for potential disasters. They're rather costly, and it's not the kind of publicity I like to pay for."
        k "Remember this, Alice: literally anything can go wrong at any given moment, and only constant vigilance and due diligence will keep the barbarians at the gates..."
        
        show katja frown

        an "...I think she mixed up her metaphors. But I keep that comment to myself for the time being."
        a frowntalk "S-still, inspections sound like a job for, uh, a safety contractor, or something..."
        a frown "{nw}"

        k frowntalk "Ugh, child, I don't fathom why you're so obstinate about this. I can eyeball test whatever I damn well please on the set."
        k "Better to catch these things earlier instead of later. Who knows what could happen when the lot of you go up on stage together."
        k "Collapsing spotlights, rotten floorboards, malfunctioning trapdoors, toxic smog, roadies hellbent on revenge. There's a long checklist to go over!"
        
        show katja frown

        an "She flashed the thing, gesturing to it with a pointed finger that could pierce armor." 
        a frowntalk "...Oooookay. I... guess I can practice somewhere else for the time being."
        a talk "Thanks for making sure everything's safe for the rest of us, Ms. Producer! It's a sweet gesture-"
        a frown "{nw}"

        k frowntalk "You misunderstand me. After the show's over and your contracts are up, I couldn't care less if the lot of you got hit by a train."
        
        show katja frown

        a frowntalk "...Ah."
        an frown "Well, she isn't the sentimental sort. I guess I'll just give her a wide berth and leave her to her business..."

        hide katja with dissolve

        $ config.side_image_tag = ""

        an "...God I hope I survive this goddamn show."

        ## end scene

        
    label marymusic:
        
        scene musicroom
        with fade
        
        $ mary_stat += 1

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

        hide mary with dissolve

        $ config.side_image_tag = ""

        an "Mary and I end up practicing for a couple of hours before eventually changing it to karaoke."
        
        ## end scene


    label musichall1:

        scene musicroom
        with fade

        an "I decide to head over to the music hall. It's a little late to get personal time with the trainers, but I could probably get some solo practice in."
        an "There aren't many people here. Just custodial staff and the odd security guard."
        an "A few of them would look at me with this weird, sidelong glance, and then continue to go about their business."
        an "I guess I'm not really a celebrity yet. Or they're just professionals..."

        $ config.side_image_tag = "alice"

        a talk "Well, let's see, I should exercise my... huh?"
        an frown "As I raised my hand to my throat to try and massage my vocal chords, some murmuring breaks the silence."
        an "It was coming from backstage, just a little to the right. In the total silence of the big, empty music hall, I could make out someone's voice."
        
        na "Whosa little wuzzabutt... whosa cutey patootie..."
        a "...???"
        an "It was a man's voice. It was speaking total nonsense. Who the hell was he speaking to? It couldn't have been me, right...?"
        an "...There was barely anyone else here. My curiosity got the better of me, and I decided to go investigate."

        show director smile at center
        with dissolve

        di talk "Ohhhh, I miss you guys soooo much... Daria, get them all together, okay?"

        show director smile

        a frowntalk "...Holy crap."
        an frown "It was the director, hunched over his tablet. I could see on the screen, he was watching a livestream of a puddle of kittens!"
        
        di talk "There's Jean, and there's Marco, and Tuna, and Leia, and ohhhhh, littlest Tungston! I love you guys, but Daddy needs to do his job, okay??"
        
        show director smile

        a talk "...Omigosh, they're adorable!"

        a smile "{nw}"

        di talk "HUH!? WHO'S THERE!?"

        show director smile

        a up frowntalk "Oh, shit-" 

        an frown "I try to make a quick getaway. But my leg doesn't cooperate. It gets caught in some cables!"
        ## TODO sfx thud

        an "I fall to the ground with a thud. I try to spin around to get back on my feet quickly, but I'm met with the director's fuming expression."

        show director at center:
            zoom 1.3
            yalign 0.65
        with hpunch

        di talk "WHAT ARE YOU DOING HERE!? YOU'RE NOT SUPPOSED TO BE HERE!"

        show director smile

        a frowntalk "I-I'm sorry! I didn't realize... I-I was just getting some practice-"

        a frown "{nw}"

        di talk "PRACTICE IN YOUR ROOM YOU LOUSE! YOU BUFFOON! YOU ABSOLUTE DINGUS!"

        show director smile

        a frowntalk "AH!!"

        hide director with moveoutleft

        $ config.side_image_tag = ""

        an frown "That was my cue to get the hell out of there, as quickly as my legs could take me!"
        an "I glance behind me to check if the enraged director is chasing me."
        an "To my surprise, and my relief, he had his back turned to me."

        di "Ohhhh nooo, Daddy didn't mean to frighten you little schnookie wookies...!"

        if day == 1:
            jump insomnia1
        elif day == 2:
            jump sleepy1



        ## end scene



        

label lounge:
    
    label jacquesinterview:

        an "You know what? I think I need to stretch my legs for a while..."
        an "I’ll take a walk around the grounds and see if I can clear my head."

        scene fountainday
        with fade

        an "As I step outside, the gravel crunches softly under my feet."
        an "It’s crunching much {i}less{/i} softly as a tall, harried figure paces back and forth on the other side of the fountain."
        an "I peek my head around."

        $ config.side_image_tag = "alice"

        a frowntalk "...{i}Jacques[/i}?"
        an frown "He stops and looks up at me."

        show jacques up frown at center:
            zoom 1.2
            yalign 0.3
        with dissolve

        j frowntalk "Yes? Can I help you, mademoiselle?" 

        show jacques frown

        a frowntalk "Umm..."

        menu: 
            "Ask him what’s wrong.":
                jump jacqueschat1

            "Forget it and leave.":
                jump jacquesscene1end

        label jacqueschat1:

            a "You look like you’re... thinking about something."
            an frown "{nw}"

            j talk "My dear Alice, I’m {i}always{/i} thinking about something."
            j frowntalk "...But you’re right. This morning I am... how do you say... {i}elsewhere{/i}."

            show jacques frown

            a frowntalk "Excuse me?"
            an frown "{nw}"

            j frowntalk "It’s an {i}interview{/i}, mademoiselle."

            show jacques frown

            an "That... didn’t really answer my question."
            a frowntalk "So are you interviewing {i}us{/i}? Like, for the show."
            an frown "Jacques waves his hand dismissively."

            j frowntalk "No, it’s nothing like {i}that{/i}."
            j "It’s the {i}press{/i}. {i}They{/i} want to interview {i}me{/i}... Ah, {i}moi{/i}."

            show jacques frown

            a frowntalk "Oh? How come?"
            an frown "Jacques raises an eyebrow."
            a down talk "I mean, {i}aside{/i} from the fact that you’re very famous and talented."
            a smile "{nw}"

            j talk "{i}And{/i} handsome."
            j "But you’ve got a point."
            j frowntalk "You see...this show, {i}Supernova{/i}, it’s my first \"big project\" in a very long time."

            show jacques frown

            an frown "That’s right."
            an "I’d remembered seeing Jacques on all kinds of kids’ variety shows growing up."
            an "Gameshows, talk shows, stuff where he’d interview tween pop stars..."
            an "But that stuff kind of...fell out of fashion around the time I graduated junior high."
            an "I hadn’t thought about it until now, but {i}Supernova{/i} was the first time I’d seen Jacques Bellvance in {i}years{/i}."
            a frowntalk "So... this is kind of like your big comeback?"
            a frown "{nw}"

            j frowntalk "Oh, I never really {i}went away{/i}, it’s just the lovely public got {i}distracted{/i} by all the new fads out there."
            
            show jacques down frown

            an "He sounds... maybe just a little bitter about that."

            j up talk "But the past is in the past! C’est la vie, non?"
            j "Now we’re back on track, and I’m becoming a household name once again."

            show jacques smile

            a frowntalk "So, is that what they’re going to ask you about?"
            a frown "{nw}"

            j frowntalk "Hmm, most likely {i}not{/i}, but {i}that’s{/i} the art of the interview."

            show jacques smile

            an "He winks at me, smiling."
            j talk "The presss always want to ask the same old boring questions."
            j "But if you know the right words to say, well... a well-aimed {i}bon mot{/i} can help you steer the conversation."

            show jacques smile

            a talk "So you can talk about what {i}you{/i} want to talk about."
            a smile "{nw}"

            j talk "{i}Exactement{/i}, dear Alice."
            j "And {i}that{/i} is your little Bellvance Industry Pro Tip of the day."

            show jacques smile

            an "My {i}what{/i} now?"
            a down talk "Well, uh, thanks, Jacques."
            a "It was nice talking to you."
            a smile "{nw}"

            j talk "Of course it was."

            show jacques smile

            an "He winks again."

            j talk "After all, that’s my {i}job{/i} Alice."
            j "~Conversation With Style!~"

            show jacques smile

            an smile "Cheesy as it is, I can’t help by smile as I walk away."
            an "He may be kind of an eccentric, but deep down, Jacques is a really nice person."
            an "At least... I think he is."

            jump jacquessceneending

        label jacquessceneoneend:

            an frown "As much as I’d like to keep talking to Jacques, I’ve got other things I need to do..."

        label jacquessceneending:

            $ config.side_image_tag = ""

            an "I part ways with him and walk back inside."

            if day == 2:
                jump sleepy1





        

        
label rooftop:  ## garden
    
    label maryrooftop1:
        
        scene fountainday
        with fade
        
        $ mary_stat += 1
        
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
        
        

        
label shopping:
    
    label mall1:

        scene shop
        with fade

        an "I decide to check out the mall today. It's not far from the production studio, and I'm pretty excited to shop around."
        an "Being smack dab in the middle of the big city has its perks. There's stuff in these stores that you can't find anywhere else!"
        an "And it's so biiiiig. I could spend all day here. But I shouldn't— I don't want to miss rehearsals."
        c "{b}AAAAAAAAAALIIIIIIIIICE!!{/b}"

        $ config.side_image_tag = "alice"

        show cherry down frown at center:
            zoom 1.8
            yalign 0.5
        with hpunch

        an down frown "Before I knew it, Cherry darted from the crowds and collided with me head on."

        a frowntalk "Ah! Cherry!? What're you doing here? L-let go of my collar!"

        c frowntalk "Alice! Alice! It's an emergency! A total catastropheeeee!!"

        show cherry frown

        an frown "Cherry was absolutely hysterical. Tears were forming in the corner of her eyes."

        a frowntalk "O-oh crap, what happened Cherry? Is there a fire? A stampede? ...An avalanche?" 

        a frown "{nw}"

        c frowntalk "...Avalanche??"

        show cherry frown:
            zoom 1.3
            yalign 0.54
        with dissolve

        a frowntalk "I-I mean, they have indoor ski resorts in malls like these! It's not completely out of the question."

        a frown "{nw}"

        c frowntalk "Well, it's worse than all of those things!!"

        show cherry frown

        a frowntalk "Okay Cherry, take it easy. Deep breaths, okay? In and out..."
        an up frown "I help Cherry come to her senses, the both of us practicing our deep breathing exercises."
        an "When the two of us were sufficiently calmed down, I grabbed her shoulders."
        a frowntalk "Okay. Cherry. Tell me {i}everything.{/i}"

        a frown "{nw}"

        c frowntalk "I-I looked up and down this whooole mall, and they don't have the Kettleman's ketchup chips I like!!"

        show cherry frown

        a frowntalk "Wh... ketchup... chips?"

        a frown "{nw}"

        c frowntalk "YEAH! I CAN'T FIND IT ANYWHERE!"

        show cherry frown

        an "Cherry was quickly winding herself right back up again. I'd have to say something."

        menu:
            #negative
            "That sounds nasty.":
                jump shopnegative1

            "Can't you just order it online?":
                jump shoppositive1

            "Maybe we can get something else?":
                jump shopneutral1

        label shopnegative1:
            a frowntalk "That sounds kinda gross, uhhhh... is it like, ketchup-y glop inside of a bag?"
            a frown "{nw}"

            c frowntalk "NO! It's ketchup powder! And it's really savory and good!"
            c "Are you some kind of ketchup hater!? Do you eat your fries {i}naked{/i} too? That's boring!"

            show cherry frown

            a frowntalk "That's not what I mean, I just... didn't understand..."

            a frown "{nw}"

            c frowntalk "Aaaah, I can't find it anywhere... if I had a bag, I could prove to you how wrong you are..."

            show cherry frown

            a frowntalk "I-I'm not a ketchup hater!"
            an frown "It was no use. Cherry had already cast her judgment upon me."
            an "I don't think I made a very good impression..."
            jump shopmerge1

        label shoppositive1:
            a frowntalk "That sounds like an import item. You sure you can't just order it online?"
            a smile "{nw}"

            c frowntalk "Noooo. You need a credit card to order stuff online."

            show cherry frown

            a frowntalk "...Youuuuu... don't have a credit card? Really?"
            a frown "{nw}"

            c frowntalk "They're scary! Do you know how interest rates work! I don't need loan debt in my life!"
            c "And the premiums! Blech, no thanks!"

            show cherry frown

            a talk "...Well, if you're just getting chips, I could just order some for you."
            a smile "{nw}"

            c frowntalk "Haaaa!? You mean it? You really mean it!?"

            show cherry smile

            a talk "I-it's not a big deal, really."
            a smile "{nw}"

            c talk "Oh I could just kiss you~!"

            show cherry smile

            a frowntalk "Ah- not in public, Cherry!!"
            an frown "With some finagling on my phone, I worked out an order from my phone to deliver to the production studio. The chips were a northerner thing, it looks like."
            an "Cherry absolutely glowed with appreciation. I guess the fastest way to a girl's heart really is her stomach."
            jump shopmerge1

        label shopneutral1:
            a talk "Well, this is a pretty big mall. Maybe we could find something else?"
            a smile "{nw}"

            c frowntalk "Weeeh... I was really excited, though."

            show cherry frown

            a talk "There's a nice chocolatier towards the end of the mall. And there's crepes! Do you like crepes?"
            a smile "{nw}"

            c frowntalk "...Crepes are pretty good..."

            show cherry smile

            an "Cherry was warming up to the idea. Her mind was drifting away from the notion of ketchup chips."
            a talk "And we can swing by the pet shop too! To take a look at the kitties, and the birds..."
            a smile "{nw}"

            c talk "And the rabbits!! They're huuuuge, like this big! They got nothing on the ones running around my grandpapi's farm..."
            
            show cherry smile

            an "Cherry's good cheer was back to its usual splendor. Pity about the ketchup chips. Probably better to avoid bringing it up for now."
            an "I think that went okay."
            jump shopmerge1

        label shopmerge1:
            scene shop
            with fade

            an smile "Cherry and I did a lap around the mall, checking out the storefronts along the way. We spotted plenty of deals, but neither of us were rich and famous to splurge at that point."
            
            show cherry up smile at center:
                zoom 1.3
                yalign 0.4
            with dissolve

            c talk "This was fun! Thanks for hanging out with me, Alice!!"

            show cherry smile

            a talk "Yeah! It was great bumping into you. You heading back to the studio?"

            a smile "{nw}"

            c talk "In a bit! I'm gonna swing back and see if I can get some stuff to make my {i}own{/i} ketchup chips~!"
            c "And then, when I control the supply, I'll live foreeeeeeever~!"

            show cherry smile

            show cherry at 2.0 with moveoutright

            show cherry at -1.1 with moveinleft

            a talk "...Well, alright. Godspeed."
            an smile "She's dedicated, I'll give her that..."


            if day == 1:
                jump insomnia1
            elif day == 2:
                jump sleepy1

            ## end scene
















