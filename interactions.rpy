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
    
    play music "New Day.mp3" fadeout 1
    queue music "New Day.mp3"

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
        yalign 0.4
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
    
    m talk "The paint is good quality, I suppose."
    
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
    
    m down frowntalk "Not as rich as me? Being rich doesn’t make you a better singer."
    
    show mary frown
    
    a frowntalk "But you were born in this kind of environment. You know how to act in this kind of environment."
    
    a frown "{nw}"
    
    m frowntalk "Which is what? To act like what common people like you would call snobs? I am well-aware of what people call me behind my back."
    
    show mary frown

    a frowntalk "That's... I don't mean to put it that way..."
    
    a frown "{nw}"
    
    m frowntalk "And I do not take offense. People react differently to the environment around them. There is no right or wrong. Why can’t you gawk at the beautiful furnishings and call it a waste of societal resources like Taylor does?"
    
    show mary frown
    
    a frowntalk "I suppose I can... but that’s not the issue here, right?"
    a "The rich thing... yes. I guess I have felt a little inferior because of it and come to think of it, it is stupid."
    a "But rich or not, you and the others are better singers. I can’t change that!"
    
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

    jump nightSwitch

    ## end scene

    
label mary1:

    scene makeuproom
    with fade

    play music "New Day.mp3" fadeout 1
    queue music "New Day.mp3"

    $ mary_stat += 1

    $ config.side_image_tag = ""

    an "I think I'll find Mary over in the Makeup room."
    an "It's odd that the cosmetologist spends so much more time with Mary than the other girls. Stranger still, that she insists on getting her work down alone..."
    an "Even Jacques doesn't get to peep inside, and he basically owns the joint! It's so curious..."
    an "I think I'll surprise her. Then I can get to the bottom of this!"

    play sound "doorknock.mp3"

    $ config.side_image_tag = "alice"

    a frowntalk "...Aaaaaand the door's locked. Damn."
    a frown "{nw}"

    m "Ugh, haven't you ever heard of knocking!?"

    ma "Calm down, we're almost done..."

    an "The door was thin. Even with the barrier between us, Mary's shrill commands were still piercingly loud."
    an "With a sigh, I waited a few minutes. Good time to collect my composure - speaking with Mary was a trial."

    play sound "dooropen.mp3"

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

        jump nightSwitch


        ## end scene


label maryafterelim:

    scene hallday
    with fade

    play music "New Day.mp3" fadeout 1
    queue music "New Day.mp3"

    $ config.side_image_tag = ""

    ann "{i}I think I'll see what Mary's up to. I haven't seen a lot of her since she got eliminated.{/i}"
    ann "{i}Hoo, that was a stressful show.  Things are really coming down to the wire now.{/i}"
    ann "{i}I wonder what Mary's gonna do now?{/i}"
    ann "{i}She doesn't come to group practices anymore. Sometimes I see her rehearsing by herself, but... are we all just supposed to move forward?{/i}"
    ann "{i}These questions all ring in the back of my head as I stand in front of Mary's room.{/i}"

    play sound "doorknock.mp3"

    ann "{i}I knock at her door, hoping for a response.{/i}"
    ann "{i}...{/i}"
    ann "{i}... ...{/i}"

    $ config.side_image_tag = "alice"
    a frown "...?"
    ann "{i}Quietly, I listen closely. Inside, I could hear her voice. She was murmuring to someone.{/i}"

    play sound "doorknock.mp3"

    ann "{i}So she is in there! I knock again with a little more oomph.{/i}"

    m "Can you sit still for {i}one second!?{/i} I'm on the phone!"

    a frowntalk "Ah!"

    ann frown "{i}I made out an exasperated sigh from the other side of the door.{/i}"
    ann "{i}Well, Mary seemed to be... well, pretty much the same as usual. That was oddly relieving.{/i}"
    ann "{i}And I already announced my presence, so... all I could do was awkwardly stand there until Mary summoned for me.{/i}"

    play sound "dooropen.mp3"

    ann "{i}Thankfully, it wasn't long until the door swung open.{/i}"

    m "Come in."

    an "With that low-spoken invitation, I let myself in."

    scene bedmaryday
    with fade

    show mary unsure frown at center:
        zoom 1.4
        yalign 0.5
    with dissolve

    $ config.side_image_tag = "alice"

    m frowntalk "Tch... sorry for making you wait. I was on the phone with my agent."

    show mary frown

    a down talk "Hi, Mary, um... how are you feeling?"
    a smile "{nw}"

    m down frowntalk "...? What does that mean? Don't tell me you came over for pity."

    show mary frown

    a frowntalk "Well, since you got eliminated, we don't really see you a lot, so I wondered..."
    a frown "{nw}"

    m frowntalk "You wondered {i}what{/i}? That I'd be sitting in here all day crying my eyes out? {i}Please.{/i}"
    m up "You gotta give me a little bit of credit here..."

    show mary frown

    a frowntalk "Th-that's not what I meant, I..."
    extend "I wanted to see you again, that's all!"

    a frown "{nw}"

    m talk "...Heh. So bloody sentimental."

    show mary smile

    ann "{i}She scoffed, folding her arms. I feel like she was judging me.{/i}"

    m talk "Don't worry your pretty little head. The producer's keeping me around to talk to fans."
    m "And my agent's already lined me up with a deal to produce a solo album. I'd say I'm in good shape."

    show mary smile

    a up talk "Oh! That's so great!! Let me know when it drops so I can buy, like, ten copies!"
    a smile "{nw}"

    m talk "Only ten? You wound me, Alice."

    show mary smile

    ann "{i}We share a laugh. Mary seemed to be in high spirits.{/i}"

    a talk "Aaaaah, you're gonna be an idol after all..."
    a smile "{nw}"

    m talk "Well, I wasn't about to go back and live on Daddy's credit cards all over again."
    m "And it's not like life's just over when you lose. You just go and do something else, yeah?"
    m "...I mean, I'm famous now, and I got fans, so I figure I made it out okay."

    show mary smile

    a talk "...Yeah. You're right."
    a frowntalk "Honestly, I was really worried about what would happen if I lost. I don't really have a plan, you know, so...."
    a frown "{nw}"

    m talk "You need an agent. I could get you in with my guy, she's fantastic, absolutely cutthroat!"

    show mary smile

    a frowntalk "Eh? ...Cutthroat how?"
    a frown "{nw}"

    m frowntalk "She's a master at power plays, like... like making sure you only get the blue M&Ms, or so help them-"

    show mary frown

    a frowntalk "What, seriously? Is that one of your requests?"
    a frown "{nw}"

    m talk "Me? Pfft, no, I'm not crazy. They're all the same."

    show mary frown

    a frowntalk "...Right."

    $ config.side_image_tag = ""
    ann "{i}Mary and I hung out for a few hours...{/i}"

    jump nightSwitch


        
        
    
label taylor1:
    scene hallday
    with fade

    $ config.side_image_tag = ""

    an "I opt to head over to Taylor's room for now."
    an "Her trailer's a bit of a walk to get to. It doesn't see a lot of foot traffic, and you kinda have to go out of the way to reach it."
    an "Stopping right in front of the door, I overhear some muffled music from the other side."
    an "It sounds {i}super familiar{/i}, but I can't quite put my finger on it."

    play sound "doorknock.mp3"

    ann "I knock at the door to her trailer, adding a bit more oomph. Hopefully the music wouldn't drown it out."

    $ config.side_image_tag = "alice"

    t "Door's open!"

    a frowntalk "Ah-"

    a frown "{nw}"

    play sound "dooropen.mp3"

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

        jump nightSwitch

        ### end scene

label taylorstagecheckscene:
    
    scene black
    with fade

    an "I lay around the lounge for a few hours and catch up on some shows until it gets dark."
    an "You know, for some reason I feel like swinging by the stage area."
    an "Things have been so {i}intense{/i} with the contest these past few days that I kinda wanna see what it’s like after dark."

    scene stagefar
    with fade

    $ taylortrying = False

    $ config.side_image_tag = "alice"

    an down "Wow, it’s... {i}massive{/i}."
    an "I mean, I know that the room is {i}big{/i}, but something about seeing it so empty is just..."
    an up "Hang on, is that Taylor?"
    an "She’s kneeling by the stage, holding up a long, black cord."

    menu:
        "Call out to her":
            jump heytaylorwhatchadoing

        "I probably shouldn’t bother her":
            jump taylorstagecheckend

        "Whatever she’s doing, I’m sure she doesn’t want me butting in":
            jump taylorstagecheckend

    label heytaylorwhatchadoing:

        a talk "Taylor?"
        a smile "{nw}"

        $ taylor_stat += 1

        an "She turns around, rising to her feet."

        show taylor up smile at center:
            zoom 1.3
            yalign 0.4
        with dissolve

        t talk "Hey, Alice. Can’t sleep?"

        show taylor smile

        a talk "Eh, I just kind of felt like wondering around."
        a smile "{nw}"

        t frowntalk "Just don’t stay up {i}too{/i} late. Wouldn’t want you oversleeping and missing the contest."

        show taylor frown

        menu:
            "I want to hang out with you.":
                jump insertawfulsempaijokehere

            "Why do {i}you{/i} care?":
                jump shutuptaylor

            "I could say the same to you.":
                jump dontsassmetaylor

        label dontsassmetaylor:

            a frowntalk "Hey, I could say the same to you, y’know."
            a "You’re {i}also{/i} up late in a big, empty auditorium."
            a frown "{nw}"

            an "A soft smirk tugs at Taylor’s lips."

            show taylor smile

            t talk "Well, maybe you {i}should{/i} say it."

            show taylor smile

            a frowntalk "Okay."
            a "Get the hell to bed, Taylor."
            a smile "{nw}"

            an "She laughs."

            t down talk "That’s not what I said {i}at all{/i}, you know."

            show taylor frown

            a talk "Yeah, but...I’m paraphrasing."
            a smile "{nw}"

            show taylor up smile

            an "Taylor rolls her eyes, then smiles."

            t talk "I didn’t come down here to get {i}sassed{/i}, Alice."

            show taylor up smile

            a "Then what {i}did{/i} you come down here for?"
            a "Whatever you’re doing, it looks like it’s pretty interesting."
            a smile "{nw}"

            t talk "...Alright, if you insist."

            jump taylortalkstech

        label shutuptaylor:

            a down talk "So? Aren’t we supposed to be competing against each other?"
            a up "If anything, you should be {i}glad{/i} I’m losing sleep."
            a smile "{nw}"

            show taylor frown

            an "Taylor rolls her eyes."

            t frowntalk "Nice job channeling Mary, there, but I’m not that kind of person."
            t "I plan on winning fair and square."

            show taylor frown

            a down talk "Don’t you mean you’re {i}trying{/i} to win fair and square?"
            a smile "{nw}"

            t talk "\"Win or don’t win, there is no \"try\"\"."

            show taylor smile

            $ taylortrying = True

            an "I can’t help but giggle."

            t talk "Once you start saying you’re \"trying\" to win, that implies you’re not sure you can do it."
            t "That kind of self-talk might trip you up in the long run."

            show taylor smile

            a down talk "You’re giving me {i}more{/i} advice?"
            a smile "{nw}"

            t talk "It’s a habit."

            show taylor smile

            an "Damn it. There’s just no way I can be antagonistic towards her."
            an "No matter what I say, she’ll just keep being {i}awesome{/i}."

            a up talk "Okay, so...what’re you doing down here?"
            a smile "{nw}"

            t down talk "Oh, just checking some stuff."

            show taylor smile

            a down talk "What kind of stuff?"
            a smile "{nw}"

            t talk "You really wanna know?"

            show taylor smile

            a up talk "Yeah."
            a smile "{nw}"

            t up talk "Okay, so..."

            jump taylortalkstech

        label insertawfulsempaijokehere:

            a up talk "Eh, I don’t mind losing sleep if it means we get to hang out."
            a smile "{nw}"

            show taylor smile

            an "Taylor smiles, looking almost...surprised."

            t talk "{i}That{/i} was sweet."

            show taylor smile

            a talk "No, I mean it."
            a "Really, I wish we {i}all{/i} had more time to just hang out and...{i}be friends{/i}."
            a down frowntalk "When I think about how I’ll probably never see you after this is done, well..."
            a frown "{nw}"

            t down talk "We can still stay in touch, you know."
            t "It just hadn’t occurred to me that you’d {i}want{/i} to."

            show taylor smile

            a talk "Of course I do!"
            a up smile "{nw}"

            an "I reach into my pocket for my phone."

            a talk "Come on, I’ll add you on NetPals!"
            a smile "{nw}"

            t down frown "..."
            t frowntalk "I...don’t have one of those."

            show taylor frown

            a down talk "Really?"
            a smile "{nw}"

            t up frowntalk "Well, I did for a while, but...It just got kind of outdated, and I ended up deleting it."

            show taylor frown

            a up talk "You could always make a new profile, I’d be happy to be your first friend!"
            a "On the app, I mean. I know you have other friends in real life."
            a smile "{nw}"

            an "Taylor smiles, running a hand through her hair."

            t up talk "Yeah, but none of ‘em are quite as...{i}unique{/i} as you are."

            show taylor smile

            a down frowntalk "Is that a bad thing?"
            a frown "{nw}"

            t talk "No. I love it."

            show taylor smile

            an up smile "For some reason, hearing her say that makes me feel {i}incredibly{/i} happy."
            an "Crap, I must be smiling like an idiot."

            a up talk "{i}Anyway{/i}, what’re you working on down here? It looked like you were doing something with the wires."
            a smile "{nw}"

            t down talk "You’re really interested in that?"
            t up "Alright, well..."

            jump taylortalkstech

        label taylortalkstech:

            t up talk "I’m taking a look at the sound setup, seeing how it’s all hooked up."

            show taylor smile

            a down talk "How come?"
            a smile "{nw}"

            an "Taylor shrugs, pausing to think for a moment."

            t talk "I just...want to know, I guess."
            t "I started reading up on this stuff a few years back, when I first started doing small events."

            show taylor smile

            a down talk "Wait, you do {i}concerts{/i}?"
            a smile "{nw}"

            t talk "Nothing {i}that{/i} fancy. Just thirty minutes at a local coffee shop, or a quick song at a talent show."

            show taylor smile

            a up talk "That’s still pretty cool."
            a smile "{nw}"

            t frowntalk "Yeah, well, when you {i}go{/i} to those tiny little shows, a lot of times there can be...{i}issues{/i} with the equipment."
            t "So I taught myself some basic stuff."
            t "Setting up a mic, working a soundboard, checking speaker hookups..."
            t talk "Just a few little things so that if something broke, I could at least {i}try{/i} to fix it."

            show taylor smile

            if taylortrying:
                a up talk "I thought you said that \"trying\" is an excuse."
                a smile "{nw}"

                t down talk "...I did, didn’t I?"
                t "Alright then, I {i}will{/i} fix anything that breaks!"

                show taylor smile

            a frowntalk "But...this is a {i}TV show{/i}, they’ve {i}got{/i} to have everything right, right?"
            a frown "{nw}"

            t talk "Yeah, it’s well done. And {i}that’s{/i} why I’m taking a look."
            t "There’s still so much I have to learn, and getting to see such a high-end setup is...awesome."

            show taylor smile

            a talk "So, have you learned anything so far?"
            a smile "{nw}"

            t talk "I’ve learned that...there are {i}far{/i} too many weird, propriety hookups down here."
            t "Seriously, I don’t even {i}know{/i} what half of these are."

            menu:
                "I know the feeling.":
                    jump relatetotaylor

                "I don’t know what {i}any{/i} of them are.":
                    jump whatisthistechnowizardy

                "I do!":
                    jump ipromiseiknowwhatimdoing

            label whatisthistechnowizardy:

                a down talk "I have absolutely no idea what I’m looking at, here."
                a "All this stuff just looks like...noise spaghetti."
                a smile "{nw}"

                show taylor down

                an "Taylor cocks her head on one side."

                t talk "Electric squid ink noodles..."

                show taylor up smile

                a up talk "Exactly."
                a smile "{nw}"

                show taylor down

                an "She pauses for a moment, looking thoughtful."

                t up talk "I’m sure you’re not as clueless as you think, though."
                t "Like, do you know what kind of cord you’d usually use to hook a smartphone to a speaker?"

                menu:
                    "An AUX cable?":
                        jump auxellent

                    "Is it HDMI?":
                        jump hdmwhy

                    "Can’t you just bluetooth?":
                        jump bluetoothblues

                label bluetoothblues:

                    a up talk "I always just hit the little bluetooth-y button."
                    a smile "{nw}"

                    t down talk "...Well. I mean. You {i}could{/i}, but..."

                    show taylor up smile

                    a down talk "But?"
                    a smile "{nw}"

                    an "Taylor waves her hands through the air."

                    t talk "But we’re being...{i}educational{/i}, here."
                    t "If it helps, the cable has the same kind of connector as a pair of headphones."

                    show taylor smile

                    a up talk "{i}Ohhhhhhhh{/i}. That’s an AUX cable, right?"
                    a smile "{nw}"

                    t talk "Yeah!"

                    show taylor smile

                    an "She smiles, looking oddly...{i}proud{/i}?"

                    jump taylortalkstechparttwo

                label hdmwhy:

                    a up talk "HDMI, right?"
                    a smile "{nw}"

                    t down frowntalk "Uh..."
                    t "I mean, those {i}can{/i} carry audio, but they’re mainly used for video data."
                    t up "Also, the connector’s kind of thick compared to the width of most smartphones."

                    show taylor smile

                    a down frowntalk "Crap, you’re right."
                    a frown "{nw}"

                    t talk "Have you heard of AUX cables?"

                    show taylor smile

                    a up talk "Oh, yeah! Like those old jokes about hooking your phone to a friend’s car speaker!"
                    a smile "{nw}"

                    t talk "Yup, that’s the one."
                    t "It’s probably the most common sound cord you there. It’s only when you get to the really professional stuff that things get...complicated."

                    jump taylortalkstechparttwo

                label auxellent:

                    a up talk "You’re talking about an AUX cable, right? Three and a half millimeters?"
                    a smile "{nw}"

                    t talk "Yeah, I am."

                    show taylor smile

                    an "I feel kind of...proud of myself right now."

                    a talk "I have trouble studying without music, so...I had to learn things."
                    a smile "{nw}"

                    t down talk "...So you could know what might be wrong?"

                    show taylor smile

                    a talk "Yes. {i}Exactly{/i} like you."
                    a smile "{nw}"

                    show taylor up

                    an "Taylor chuckles, her eyes shining."

                    t talk "I guess we just have a lot in common."

                    jump taylortalkstechparttwo

            label relatetotaylor:

                a up talk "Now you know how I feel about the contest."
                a smile "{nw}"

                an "Taylor chuckles a little."

                t talk "That’s right, you never studied music, did you?"
                t "So all this stuff about performing on stage, and having your makeup done..."
                t "All this must be totally foreign to you."

                show taylor smile

                a talk "Well, not {i}totally{/i} foreign. I did pick up a lot of things as an Intern, but..."
                a "Sometimes I just look at all this and think \"What is going {i}on{/i}?\""
                a smile "{nw}"

                t talk "Yeah, it’s pretty easy to get overwhelmed sometimes."
                t frowntalk "Hell, even {i}I{/i} used to get really confused by all this..."

                show taylor down frown

                an "She stares off into space for a moment, looking wistful."

                t up talk "But anyway, you’re doing really well."

                show taylor smile

                a down talk "What do you mean?"
                a smile "{nw}"

                t talk "Well, you keep saying that you’re not the right person to {i}be{/i} on this show, but..."
                t "You landed {i}square{/i} on your feet."

                show taylor smile

                an up "Her words send a jolt of happiness up my spine."
                an "And... embarrassment?"

                t talk "Seriously, you should be proud of yourself."

                show taylor smile

                a talk "Thanks."
                a smile "{nw}"

                jump taylortalkstechparttwo

            label ipromiseiknowwhatimdoing:

                show taylor down

                an "Taylor raises an eyebrow."

                t talk "You {i}do{/i}? Could you give me a rundown?"

                show taylor up smile

                an down frown "Wait, she {i}believed{/i} me?"
                an "Oh god. {i}Why{/i} did I say that? {i}Whyyyyyyyyyyy{/i}."
                an "Okay, {i}think{/i}. Just take a deep breath and...use context clues?"

                t down frowntalk "Like this one right here, it {i}looks{/i} like a coaxial cable, but I have no idea why it’d be near the stage..."

                show taylor frown

                an "...I don’t even know what the thing she just mentioned is."

                a frowntalk "Um..."

                menu:
                    "It’s definitely that thing you just said.":
                        jump coaxialishardtospell

                    "It’s an ICP connector!":
                        jump whatisacableoh

                    "I think it’s a WLW extension...":
                        jump badumtish

                label whatisacableoh:

                    a up talk "It looks like an ICP connector!"
                    a smile "{nw}"

                    show taylor down frown

                    an "Taylor raises an eyebrow."

                    t frowntalk "And, ah..."
                    t "{i}What{/i} does that stand for?"

                    show taylor up frown

                    a down frown "..."

                    an "{i}Think{/i}, Alice. {i}Quickly.{/i}"

                    menu:
                        "Instant Cloud Processing.":
                            jump speakenglishdammit

                        "It Contains P’Audio.":
                            jump whatthehellispaudio

                        "Intranet Containment Protocols":
                            jump speakenglishdammit

                    label speakenglishdammit:

                        t down frowntalk "...{i}What.{/i}"

                        show taylor frown

                        a down frowntalk "I..."
                        a "I don’t {i}know{/i}. I just...tried to sound science fiction-y, I guess."
                        a "Really, I have {i}no{/i} idea what that cord is called. Sorry."
                        a frown "{nw}"

                        show taylor down

                        an "Taylor shakes her head."

                        t frowntalk "It’s fine, but you didn’t {i}need{/i} to lie, you know. There’s no shame in not knowing something."
                        t "Not knowing something is the first step to learning it."

                        show taylor up frown

                        a frowntalk "Yeah, I know. I just....panicked, I guess."

                        jump taylortalkstechparttwo

                    label whatthehellispaudio:

                        t down frowntalk "P...{i}P’Audio?!{/i}"

                        show taylor frown

                        a down frowntalk "I..."
                        a "That was a terrible lie. I’m sorry."
                        a "It’s not even called an ICP cable..."
                        a frown "{nw}"

                        t frowntalk "I mean, I’d figured as much when you said the word \"p’audio\", but..."

                        show taylor frown

                        an "She lets out a small sigh."

                        t up frowntalk "You didn’t need to pretend you knew what the cord was."
                        t "It’s not like I’d respect you any less for not knowing about random audio equipment."

                        show taylor frown

                        a frowntalk "Yeah, I just..."
                        a "I wanted to impress you a little."
                        a frown "{nw}"

                        t talk "...You already {i}do{/i}."

                        show taylor smile

                        an smile "...{i}Did she really just say that?{/i}"
                        an "Oh god, I think my ears are burning."

                        jump taylortalkstechparttwo

                label badumtish:

                    a up talk "I’m pretty sure it’s a WLW extension, like...to make it longer, for bigger rooms?"
                    a smile "{nw}"

                    t down frown "..."
                    t frowntalk "To make...the WLW...longer?"

                    show taylor frown

                    an frown "I bite my lip."

                    a down frowntalk "I’m bad at lying, aren’t I?"
                    a frown "{nw}"

                    t up frowntalk "Usually not {i}this{/i} bad, as far as I’m aware."
                    t down talk "You...{i}do{/i} know what WLW actually means, right?"

                    show taylor smile

                    an "...Oh crap."
                    an "\"Women Who Love Women\"..."

                    a "..."

                    show taylor up smile

                    an "My face goes bright red, and Taylor breaks into a playful smirk."

                    t talk "{i}Everybody{/i} knows that to have a good sound setup, you {i}need{/i} a WLW."

                    show taylor smile

                    a frowntalk "Okay, okay, I get it."
                    a frown "{nw}"

                    t talk "Hey, I needed to tease you a {i}little{/i} bit."

                    show taylor smile

                    jump taylortalkstechparttwo

                label coaxialishardtospell:

                    a up talk "Actually, I think it might be that thing you just said, a conch shell hookup?"
                    a smile "{nw}"

                    t down frowntalk "Coaxial?"

                    show taylor frown

                    a talk "Yeah. I’ve {i}heard{/i} that word before, and I’m pretty sure I’ve seen those around my apartment."
                    a smile "{nw}"

                    show taylor up

                    an "Taylor nods, frowning."

                    t frowntalk "Yeah, but {i}those{/i} are the things you use to hook up the internet..."
                    t "Wait, {i}hang on{/i}."

                    show taylor frown:
                        xalign -0.5
                    with moveoutright

                    show taylor frown:
                        zoom 1.3
                        yalign 0.4
                    with moveinright

                    an "Taylor jumps to her feet, runs over to the side of the stage, and then runs back."

                    t down talk "Holy shit you were right."

                    show taylor smile

                    a down talk "I {i}was{/i}?"
                    a smile "{nw}"

                    t up talk "Yeah."
                    t "They’ve got some kind of weird...cobbled together setup for some of the camera feeds."

                    show taylor smile

                    a talk "...{i}With an internet cable?{/i}"
                    a smile "{nw}"

                    t talk "Yeah. I meant it when I said it was weird."
                    t "A lot of the stuff is made by companies I’ve never even {i}heard{/i} of."
                    t "It’s some kind of proprietary nightmare setup."

                    show taylor smile

                    a up frowntalk "...Sounds annoying."
                    a frown "{nw}"

                    t talk "Oh, it {i}would{/i} be."
                    t "I think it’s safe to say that if {i}that{/i} stuff broke, we’d be utterly up a creek."

                    show taylor smile

                    a up talk "Huh..."

                    jump taylortalkstechparttwo

            label taylortalkstechparttwo:

                t up talk "So, I think we’ve thoroughly established that this whole setup is {i}way{/i} over our heads."
                t "Maybe I’ll get a chance to talk to some of the AV people in a few days, but until then..."

                show taylor smile

                an "Taylor yawns softly."

                t talk "I think it’s time we both got some sleep."

                a up talk "Yeah, sounds good."
                a smile "{nw}"

                an "We walk out of the room, making sure to close the door behind us."

                scene hallnight
                with fade

                an "As we head towards the stairs, a sudden thought flashes through my head."

                a down frowntalk "Ah-!"
                a smile "{nw}"

                an "I almost spill forward, but manage to catch myself."

                t down talk "You okay?"

                show taylor smile

                a up talk "Y... yeah."
                a smile "{nw}"

                an "Taylor and I walk up the stairs in silence."

                scene bedalicenight
                with fade

                show taylor up smile at center:
                    zoom 1.3
                    yalign 0.4
                with dissolve

                t talk "Well, goodnight."

                show taylor smile

                a up talk "...You too."
                a smile "{nw}"

                hide taylor with dissolve

                an "As I watch Taylor walk back towards her room, my hand drifts up to my face."

                a down talk "What was {i}that{/i} all about?"
                a frown "{nw}"

                $ config.side_image_tag = ""

                $ taylor_stat += 1

                an "That odd little thought that almost made me trip."
                an "For some reason, I’d thought about holding her hand..."

                jump taylorstagecheckend

    label taylorstagecheckend:
        jump nightSwitch
        
        ## end scene



label cherry1:

    scene bedaliceday
    with fade

    $ cherry_stat += 1

    an "I wonder what Cherry's up to? I'll call her."

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

    play music "Friends Forever.wav" fadeout 1
    queue music "Friends Forever.wav"

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

        jump nightSwitch

        ## end scene



default cherry2_seen = False
label cherry2:

    scene hallday
    with fade

    $ cherry_stat += 1

    $ cherry2_seen = True

    an "Cherry said she was working on something over in the dining room. Maybe I'll head over there to check on her."

    scene dinnerday
    with fade

    play music "Friends Forever.wav" fadeout 1
    queue music "Friends Forever.wav"

    $ config.side_image_tag = "alice"

    an "I catch her at a table by herself. She's surrounded by emptied bottles of store-bought cappuccinos."
    c "Alice! Over here!"

    show cherry up smile at center:
        zoom 1.4
        yalign 0.5
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

    jump nightSwitch

    ## end scene


label cherry3:
    an "The next contest is coming up soon. I should probably get some practice in ahead of time."
    an "Cherry's probably in her room. Out of all the girls, she's definitely the most approachable."
    an "I'll go see what she's up to."

    $ cherry_stat += 1

    scene hallday
    with fade

    play sound "doorknock.mp3"

    an "I knock on her door."
    $ config.side_image_tag = "alice"
    a talk "Hey, Cherry, it's Alice! Are you free right now?"
    a smile "{nw}"
    c "..."
    if day < 6:
        a talk "I figured we can practice together! How does that sound?"
    else:
        a talk "I just wanted to come by and see how you were doing."
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

    play music "Friends Forever.wav" fadeout 1
    queue music "Friends Forever.wav"

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
        $ cherry_stat += 1
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

        jump nightSwitch

        ## end scene



        
label musicroom:
    
    
    label musichall2:
        scene stagefar
        with fade

        $ config.side_image_tag = ""

        an "I feel like swinging by the stage. I can get some practice in."
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

        jump nightSwitch

        ## end scene

        
    label marymusic:
        
        play music "New Day.mp3" fadeout 1
        queue music "New Day.mp3"

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
        
        ann "{i}If Mary is willing to practice with me, I think I’d benefit a lot from working with her. It’d be more fun to have company too. Mary is actually quite nice now that I’m getting to know her better.{/i}"
        
        a talk "Alright. Let's start!"
        
        a smile "{nw}"

        hide mary with dissolve

        $ config.side_image_tag = ""

        an "Mary and I end up practicing for a couple of hours before eventually changing it to karaoke."

        jump nightSwitch
        
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

        jump nightSwitch



        ## end scene

        

        
label rooftop:  ## garden
    
    label maryrooftop1:
        
        play music "New Day.mp3" fadeout 1
        queue music "New Day.mp3"

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
        
        jump nightSwitch
        
#############################################################################################################
#############################################################################################################


label taylor2:
    scene shop
    with fade

    $ config.side_image_tag = ""

    an "I know that Taylor has a thoroughly regimented exercise routine. I had to figure this out quickly, because she's annoying hard to track down to any one spot."
    an "If I want to talk to her, I'll have to catch her at the mall. I'm pretty sure she'll be refueling at Fruitastic Smoothies."
    an "...Maybe I put too much thought into this."

    $ config.side_image_tag = "alice"

    a talk "...Oh, there she is! Taylor!!"
    an smile "{nw}"

    $ taylor_stat += 1

    show taylor up frown at center:
        zoom 1.3
        yalign 0.3
    with dissolve

    t "...?"

    an "Right on cue, she made it to the smoothie cart."

    t talk "Alice. What's new with you?"
    
    show taylor smile

    a talk "Not much! Figured I'd catch you while you were running."
    an smile "{nw}"

    t down frowntalk "...I hope you weren't stalking me."

    show taylor frown

    a frowntalk "No! ...Maybe a bit. I just see you heading out a lot in the mornings."
    a frown "{nw}"

    t up talk "Oh! You wanna buddy up. Yeah, I could use a partner. You ever go jogging in the city?"
    show taylor smile
    a talk "Not in the city specifically, but there were all these winding bike trails around where I grew up, up in Wichita?"
    a smile "{nw}"
    t up talk "Heh, alright. The city isn't much different, you just wanna avoid the high traffic areas. Inhaling a strong whiff of car exhaust is a good way to get sick."
    t frowntalk "Just need to refuel real quick and... wait. Hmmm..."
    show taylor frown
    a frowntalk "What? What's wrong??"
    an frown "Taylor lowered her eyes to the ground. Her eyes squinted as she focused on something."
    an "She was looking at my... feet? No, my shoes."

    t frowntalk "Tch. Thaaat won't do. I figured you'd bring better shoes for this."
    show taylor frown
    a frowntalk "Eh? Wh, what's wrong with my shoes? They're sneakers, it's not like I'm gonna wear them to a ball..."
    a frown "{nw}"

    t frowntalk "For the best performance, you need the best equipment. You don't wanna get sore or pull a muscle for the big show, right?"
    
    show taylor frown

    a frowntalk "...I guess not, but... it's probably not that big a deal."
    a frown "{nw}"

    t frowntalk "Nonsense. That'd be a pathetic way to go down."
    show taylor frown

    an "Her eyes drifted aside."

    t frowntalk "Mmhm, mmhm... bet there's  sporting goods store somewhere in the mall. We'll scope it out and get a recommendation."
    show taylor frown
    a talk "You don't have to, really-"
    a smile "{nw}"
    t talk "I kinda have to, though? If we're gonna be exercise buddies."
    show taylor smile
    a talk "...Ooookaaaay..."

    an frown "Man, new shoes are gonna be really expensive. And they're gonna look ugly too..."

    t talk "Anyway, I gotta fill up. Let's get smoothies."
    show taylor smile

    an "Without waiting for a response, Taylor strolled over to the cashier."

    t talk "Eyo, I'll get the Banana Slamma. Alice, what're you getting?"
    show taylor smile
    a frowntalk "aaaaaaaaaaaa"

    an frown "I look over the menu. There must be a hundred options up here! The raw power was overwhelming..."

    a down frowntalk "{i}AAAAAAAAAAAAAAAA{/i}"

    an frown "PICK SOMETHING QUICK PICK SOMETHING QUICK!!"

    a up talk "I'll get... the Honduran Passion Fruit Siesta!!"

    an smile "The girl working the counter gave me a concerned look. Her mouth flattened, she punched in the order."

    t talk "I got this covered."

    show taylor smile

    an "Taylor pulled out her wallet, pulling out a twenty."

    a "...?"

    an "Out of the corner of my eye, I spot something through a clear screen of her wallet. It appeared to be a photo."
    an "A photo of a boy and a Labrador, it looked like. There was a lot of resemblance to Taylor. Maybe she had a twin brother."
    an "I didn't get a very long look before Taylor pocketed it once more."

    a talk "Omigosh! Puppy!!"
    a smile "{nw}"
    t frowntalk "What? Alice!"
    show taylor frown
    a talk "Puppy!! There was a photo of a puppy in your wallet! What's his name??"
    a smile "{nw}"
    t frowntalk "...Patriot. You looked into my wallet?"
    show taylor frown
    a talk "Yeah, at that photo in your wallet! I didn't know you had a brother too! Is that your brother?"
    a smile "{nw}"
    t down frown "..."
    t down frowntalk "...I don't have a brother."
    extend "And you probably shouldn't go snooping into other people's belongings either..."
    show taylor frown
    a down frowntalk "Ahhh, I'm sorry, I only caught a glimpse just now."
    a down talk "...So is that your boyfriend? If he's not family then-"
    a smile "{nw}"
    t up frowntalk "It's me."
    show taylor frown
    a frowntalk "...Um?"
    a frown "{nw}"
    t frown "Yeaaah. That's an old photo I only keep around since I don't have other photos of Patriot. I transitioned a few years ago."
    a down talk "Wow! Um..."
    an frown "Wasn't expecting that. What do I say...?"

    menu:
        "So you used to be a guy?":
            jump taylor2negative
        "Sorry about that...":
            jump taylor2neutral
        "You look great!":
            jump taylor2positive

    label taylor2negative:
        a up talk "So you used to be a guy? That's interesting!"
        an frown "Her eyes narrow into a laser-sharp stare, and I immediately know I’ve made an error."

        t up frowntalk "No! I used to present as a guy."
        extend "I'm a woman. Always have been."
        t "I just never had the chance to make other people see that until the last couple years..."
        show taylor frown
        a talk "OH! R-right, I get it. I think. Sorry about that, I..."
        a frown "{nw}"
        t frowntalk "It's... something to get used to, I get it. People still mix it up all the time."
        show taylor frown
        an "Taylor furrowed her brow as she said this. That must've sounded super dumb."
        an "I wanna support her and not come off as a bigot... come on Alice."
        jump taylor2merge

    label taylor2neutral:
        a frowntalk "Sorry, I... don't know a lot of trans people. Hope I didn't overreact or anything."
        a frown "{nw}"
        t up frowntalk "Nah, you're fine. I get that kind of reaction a lot."
        show taylor frown
        a talk "Still, it has to be pretty stressful, right?"
        a smile "{nw}"
        t up frown "You don't get this far in life without having thick skin. I just wanna correct misconceptions and stuff."
        t smile "We can talk about it, no worry. I could forward you some websites so you can learn more..."
        a talk "Ah! That's be really cool!"
        an smile "I don't have a lot of trans friends. None I'm really close with. I'm glad Taylor is being really chill about all this."
        jump taylor2merge

    label taylor2positive:
        $ taylor_stat += 1
        a up talk "Wow, you’re— you’re like... magic."
        a smile "{nw}"
        t down talk "Pfft. What the heck are you talking about?"
        show taylor smile
        a talk "It’s just... I see so little of that kid in you. You blossomed into a stunning woman."
        a smile "{nw}"
        t talk "Ah! Uh, th—thanks, Alice."
        t up frowntalk "It’s... not like that just happened on it’s own, though. It’s been an uphill battle."
        show taylor smile
        a talk "Well... it’s one you’re definitely winning."
        a smile "{nw}"
        t up talk "If you say so."
        show taylor smile
        an "She’s pretending to be aloof, but it’s clear Taylor really appreciated the compliment. The smile on her face clearly indicates that much."

        t up frowntalk "It’s not the only thing I need to win, though. If I get a contract to perform from this, paying the bills won't be a problem anymore..."
        show taylor frown
        a down talk "Ahhh..."
        a frown "{nw}"
        jump taylor2merge

    label taylor2merge:
        t down frowntalk "It's not a big deal. I just keep an old photo to motivate me. And for Patriot."
        t up talk "It's kind of an affirmation of how far I've come. And how long I need to go. And I just keep it in my wallet so it's never far away."
        show taylor smile
        a up talk "No, that's cool! Inspirational even!"
        a smile "{nw}"
        t talk "Heh. That's what I was going for."
        show taylor smile
        #sfx ding
        t talk "Oh! Smoothies are ready."
        show taylor smile
        a talk "Alright! Let's find a table and-"
        a smile "{nw}"
        t talk "Nah. We got them to go. I don't really like sitting in one place too long."
        show taylor smile
        a talk "Ohhhh. ...I hope we're not gonna go jogging, I don't wanna spill mine."
        a smile "{nw}"
        t down talk "Pfft. Don't worry about it. Just a leisurely stroll around the mall. We can go window shopping."
        show taylor up smile
        a up talk "Ooh! Yeah! Do either of us have any money though...?"
        a up smile "{nw}"
        t up talk "Once we're all rich and famous, money opens all doors~"
        show taylor up smile
        a down talk "...Truuuue..."
        an up smile "Sharing a laugh, the two of us head out to see the rest of the mall."

        hide taylor
        with dissolve

        $ config.side_image_tag = ""

        an "At the end, we part ways to get onto other things. I can only keep up with Taylor's energy for so long."

        jump nightSwitch


#####################################


#Mary 3 (After Elimination)
label mary3:
    scene shop
    with fade

    $ config.side_image_tag = ""

    an "I think the producer had something special planned for Mary at the mall today. Maybe I'll check on that..."
    an "...There's actually a pretty big crowd forming near the water fountain. Mary's at a table... signing autographs?"

    play music "New Day.mp3" fadeout 1
    queue music "New Day.mp3"

    show katja frown:
        zoom 1.3
        yalign 0.3
    with dissolve

    $ config.side_image_tag = "alice"

    k frowntalk "Alice? Whatever are you doing here?"

    show katja frown

    an "It seems the producer picked me out from the crowd. She seems disappointed to see me here."

    k frowntalk "Surely you have better things to do than to traipse about the mall... don't you have your own preparations to handle?"
    show katja frown

    a down frowntalk "Eh? Well, yeah, but I wanted to see what Mary was up to over here."
    a down frown "{nw}"
    k frowntalk "I'll have you know she's rather busy at the moment herself. Dealing with the demanding fanbase is practically a full-time job, you know."
    show katja frown
    a down frowntalk "...I can tell from the line-up."

    an "I catch a glance towards the front. She's flanked by two bodyguards, and furiously penning autograph after autograph."
    an "She looks busy. Maybe I should..."

    menu:
        "Leave her to her business":
            jump mary3neutral
        "Run up and yell hello":
            jump mary3negative
        "Ask for an autograph":
            jump mary3positive

    label mary3neutral:
        a down frowntalk "...Yeah, she looks busy. Probably doesn't need to see me. I'll check on her later..."
        a frown "{nw}"
        k frowntalk "An excellent idea. Now go on. Shoo. I need you in peak form for our next show."
        k "And try not to let anyone spot you on the way out, it may distract from our signings over here."
        show katja frown
        a up frowntalk "R-right, of course."

        hide katja
        with dissolve

        $ config.side_image_tag = ""

        an "It's disappointing, but I figure I can catch Mary a little later..."

        jump endaftermaryelim

    label mary3negative:
        an "...Eh, I'll get out of the producer's hair. But not before checking in with Mary first."

        k frowntalk "H-hey, come back here, you can't just-"

        hide katja
        with dissolve

        an "I manage to give the producer the slip, rushing towards Mary's table."

        a up talk "Hey, Mary! Over here!"

        an "I holler to try and get her attention, hurrying to the front of the line."
        an "Mary glanced up from her papers."

        show mary down frown:
            zoom 1.35
            yalign 0.4
        with dissolve

        m unsure frowntalk "...Alice?"
        show mary frown
        #character labels: Diehard Fan = DF, Obsessed Fan = OF, Super Fan = SF
        of "Is that Alice!?"
        sf "Holy crap it is!! Is she signing autographs too!?"
        df "I need to get another selfie with her!"
        a down frowntalk "{i}(\"ANOTHER!?\"){/i}"
        a down "Oooookay, this was a mistake!"

        hide mary
        with dissolve

        $ config.side_image_tag = ""
        an "The crowds were suddenly converging on me, and the helpers on hands were struggling to hold them back."
        an "Across the room, Mary was glaring daggers at me. I get the sinking feeling I was ruining her event."
        an "...Yeah, definitely ruining her event. Time to make a hasty retreat...!"

        jump endaftermaryelim

    label mary3positive:
        $ mary_stat += 1
        a up talk "...Is it okay if I get her autograph?"
        k frowntalk "What? What are you playing at, girl? If you want that so bad, you can ask back on set..."
        show katja frown
        a talk "Yeah, but.. I wanna surprise her."
        a smile "{nw}"
        k frowntalk "...Ugh. Children these days, with their one-upping mindgames and whatnot."
        show katja frown
        a frowntalk "I-it's nothing like that! Really!"
        a smile "{nw}"
        k frowntalk "Well, the line starts there. Do put on a hat and some sunglasses if you're going for that."
        k "The last thing I need is for you to get recognized and drum up a riot..."
        show katja frown
        a frowntalk "Ah, good point..."
        a frown "{nw}"

        hide katja
        with dissolve

        an "I think I got a big hat on me... oh, and sunglasses to hide my eyes! That'll only add to the surprise. I gotta thank Katja for the idea later!"
        an "Okay, time to get in line!"
        an "..."
        an "... ..."
        an "... ... ..."
        an "... ... ... ... ... ... ... ... ... ... ..."

        a down frowntalk "This, uh... this is a pretty long line."
        a frown "{nw}"
        ##TODO sfx bump
        df "HEY, BACK OFF! You're gonna break my selfie stick!"
        a down frowntalk "S-sorry! It's so cramped..."
        an frown "Somehow I make it to the front of the line."

        show mary up smile:
            zoom 1.3
            yalign 0.35
        with dissolve

        m talk "Hi there~! And who do I make this out to?"
        show mary smile
        a down talk "Heeey, it's me! Just make it out to Alice."
        a down smile "{nw}"
        m unsure frown "...bwuh?"
        an "Mary did a double take upon seeing me."
        m down frowntalk "W-what're you doing here!?"
        show mary frown
        a up talk "I wanted your autograph!"
        a smile "{nw}"
        m frowntalk "...{i}why?{/i} You beat me."
        show mary frown
        a talk "You're still an inspiration to me~!"
        a smile "{nw}"
        m down frowntalk "...Ugh, you sap."
        show mary frown
        a down talk "Hehe!~"
        an smile "Mary was pretty easy to embarrass. She kept her head down, trying to hide her blushing cheeks, before sliding a signed photo over to me."

        m down frowntalk "There. Now beat it."
        m up "...And... thanks."

        show mary smile

        a talk "No, thank you! I'll catch you later..."
        a smile "{nw}"

        hide mary
        with dissolve

        $ config.side_image_tag = ""
        an "I probably shouldn't take up any more of Mary's valuable time. I'll track her down when this is all wrapped up."

        label endaftermaryelim:
            jump nightSwitch

################################################################


label cherrypostelim:
    scene hallday
    with fadee

    $ cherrypostelimseen == True

    $ config.side_image_tag = ""

    an "Man... I can't believe it's just me and Taylor left."
    an "I haven't seen Cherry for a while. I should check up on her - she's so emotional and big-hearted, she can't be taking this news well."

    play sound "doorknock.mp3"

    an "I knock at her door. I hope she's inside..."

    c "Come in!"

    an "Huh, she didn't sound particularly beat up about it."

    scene bedcherryday
    with fadee

    $ config.side_image_tag = "alice"

    play music "Friends Forever.wav" fadeout 1
    queue music "Friends Forever.wav"

    an "I let myself in, finding Cherry with a laptop. She's tucked into a comfy chair, rapidly typing away."

    show cherry up smile:
        zoom 1.4
        yalign 0.45
    with dissolve

    c talk "I made jelly! Do you want some?"
    
    show cherry smile

    a down frowntalk "...You're... eating it from a teacup?"
    a frown "{nw}"

    c down smile "I didn't have any bowls. They're like, Jell-O shots! Except, um, appropriate for kids."

    show cherry smile

    a up talk "Heheh! Alright. We can have our jelly with class and style."
    an smile "I stroll past her, picking out a chilled teacup from her mini fridge."

    a down frowntalk "So, uh... you seem well! Sorry that, well... you know."
    an frown "{nw}"

    c down talk "Oh, it's okay! I was kinda bummed earlier, but... look at this!"
    
    show cherry smile

    an "Cherry turns her laptop around towards me, beaming with pride."
    an "I lean forward, squinting to get a better look."
    an "...Is this a comment thread? From some kind of online forum..."

    a up frowntalk  "What's all this, Cherry?"
    an frown "{nw}"

    c up talk "Look at all these people! They're all wishing me well!"
    c down "A lot of them were really sad too... others wanted to say I did a really fantastic job!"
    c down frowntalk "And then some people got really mad. This guy says he was gonna take matters into his own hands."
    c down "Maybe I should let the producer know??"

    show cherry frown

    a down frowntalk "Mmmmmmaybe?? That sounds dicey."
    a up talk "...But maniacs aside, it sounds like everyone loved you."
    an smile "{nw}"

    c talk "Mmhm! Reading everyone's words of support made me feel a looot better about this."
    c "And, and! I'll get a front-row seat when I see you and Taylor on stage~!"
    
    show cherry smile

    a talk "Eh? O-oh, that's... that's true."
    an smile "That's right. I don't think anyone's more of a fan than Cherry. She comes off as more of an idol superfan than an idol herself... even if she more than qualifies as the latter."
    a talk "...Hey, Cherry, if you look on Mugshot, I'm sure you'll find more fans there."
    an smile "{nw}"

    c talk "Ah, right!! I should make a post there. I was just finishing up making my account on this..."
    
    show cherry smile

    a down frowntalk "...Uhhh, maybe... {i}don't{/i} do that. That one guy's still taking matters into his own hands, and..."
    an frown "I spend the better part of the afternoon trying to keep Cherry out of trouble online."

    $ config.side_image_tag = ""

    an "Even if she's no longer a contestant, it feels like nothing's changed."

    hide cherry
    with dissolve

    jump nightSwitch


        
label shopping:
    
    label mall1:

        scene shop
        with fade

        an "I decide to check out the mall today. It's not far from the production studio, and I'm pretty excited to shop around."
        an "Being smack dab in the middle of the big city has its perks. There's stuff in these stores that you can't find anywhere else!"
        an "And it's so biiiiig. I could spend all day here. But I shouldn't— I don't want to miss rehearsals."
        c "{b}AAAAAAAAAALIIIIIIIIICE!!{/b}"

        play music "Friends Forever.wav" fadeout 1
        queue music "Friends Forever.wav"

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

            show cherry:
                xalign 2.0 
            with moveoutright

            $ renpy.pause(0.5)

            show cherry:
                xalign -1.1
            with MoveTransition(1.0)

            a talk "...Well, alright. Godspeed."
            an smile "She's dedicated, I'll give her that..."

            jump nightSwitch

            ## end scene




##“Cherry and the Bunny” scene

label cherrybunnyscene:

    scene fountainday
    with fade

    play music "Friends Forever.wav" fadeout 1
    queue music "Friends Forever.wav"

    $ config.side_image_tag = "alice"

    an "As I step out onto the grounds, the morning sunlight almost blinds me."
    an "When my vision comes back into focus, I see Cherry jogging clumsily past the fountain."
    an "Her face is flushed, with an unusually focused expression."

    menu:
        "Call out to her.":
            jump cherrybunnycall

        "See where this is going.":
            jump cherrybunnywatch

    label cherrybunnyend:

        an "I give Cherry a small wave before heading back inside."
        an "I hope she doesn’t spend {i}too{/i} long out there..."

        jump bunnyend2

    label cherrybunnycall:

        a down talk "Cherry?"
        a smile "{nw}"

        show cherry up smile at center:
            zoom 1.3
            yalign 0.4
        with dissolve

        c down talk "Ah-!"

        an "She lets out an embarrassed squeak before stumbling, almost crashing into the fountain."
        an "...{i}Oops.{/i} Sorry, Cherry."
        an "I walk over to her, offering my hand."

        show cherry frown

        a down frowntalk "You okay?"
        a frown "{nw}"

        an "She nods, slightly out of breath."

        c up talk "Yeah, I’m fine."
        c "I was just..."
        c "Ummmm... exercising?"

        show cherry smile

        a up frown "..."

        an "Wow."
        an "She is {i}the worst{/i} liar."
        an "After a few moments of awkward silence, Cherry mutters something under her breath."

        c down frowntalk "{size=16}...Bunnies.{/size}"

        show cherry frown

        a down frowntalk "Huh?"
        a frown "{nw}"

        an "Cherry straightens up."

        c up talk "There’s {i}bunnies{/i} here. {i}Tons{/i} of ‘em."

        show cherry smile

        a down talk "There are?"
        a smile "{nw}"

        an "Now that I think about it, I did notice a few different types of animals roaming the grounds..."
        an "First the pigs, and now this, huh?"
        "Cherry nods, beaming."

        c talk "It’s like some kind of..."
        show sparkles1 at center
        show sparkles2 at center
        extend "~Mansion Petting Zoo~." #Can we do something silly here with colors/popup effects?

        show cherry smile

        an down "Did... she just speak in sparkles?"
        an up "It’s probably best not to think about it."

        hide sparkles1
        hide sparkles2

        a talk "So, you were running... because you saw a rabbit?"
        a smile "{nw}"

        an "Cherry bites her lip, looking even more flustered than she had when she was running."

        c down frowntalk "Mmm-hmm."
        c "Sorry, I know it must seem {i}really{/i} childish and dumb, but..."
        c "I just want to enjoy this while I still can."

        show cherry frown

        menu:
            "I know what you mean.":
                jump cherrywowigetit

            "What’s \"This\"?":
                jump cherrywowexplain

        label cherrywowigetit:

            a up talk "Yeah, I know what you mean."
            a "I’m actually trying to do the same, I guess."
            a "I needed some fresh air, and these gardens are just..."
            a smile "{nw}"

            c up talk "{i}Amazing{/i}?"

            show cherry smile

            a talk "Yup."
            a smile "{nw}"

            jump backtothebunn

        label cherrywowexplain:

            a down talk "Uhhh, {i}\"This\"{/i}?"
            a smile "{nw}"

            an "Cherry looks down at her feet for a moment."

            c down frowntalk "I...I don’t normally {i}live{/i} like this."
            c "This mansion, with all these big {i}rooms{/i}, and expensive {i}food{/i}, and the {i}animals...{/i}"
            c "This isn’t anything like back home."
            c "And...while I definitely can’t see myself living my whole {i}life{/i} like this, I still want to have fun while I can."

            show cherry frown

            a up talk "Hmm, I guess that makes sense."
            a down frowntalk "I mean, god knows that once {i}I’m{/i} all done with this, well..."
            a "It’s back to being an intern for me."
            a frown "{nw}"

            c up talk "Mmmm yeah, but who knows?"
            c "Maybe you {i}won’t{/i} be an intern."
            c "Maybe someone out there will discover you, and you can do something else!"

            show cherry smile

            an smile "I...actually hadn’t thought of that."
            an up "Who knows? Maybe a year from now, I’ll be doing what Katja does... or even Jacques."
            an "Nope. {i}That{/i} mental image just does {i}not{/i} work."
            an "I mean, me in a glitter-drenched suit, randomly breaking into French?"

            a up talk "Pfft!"
            a smile "{nw}"

            c down frowntalk "...I was being serious, you know."

            show cherry frown

            a talk "Yeah, I know. I just kind of had one of those...I dunno, brain farts?"
            a smile "{nw}"

            c up talk "Oh, okay."

            show cherry smile

            jump backtothebunn

        label cherrybunnywatch:

            an up smile "I have to admit, I’m kind of curious about what she’s doing."
            an "Cherry takes a few more clumsy strides, then sighs and straightens up."

            show cherry up smile at center:
                zoom 1.3
                yalign 0.4
            with dissolve

            c down frowntalk "{size=16}This isn’t working, is it?{/size}"

            show cherry frown

            a down frowntalk "What’s not working?"
            a frown "{nw}"

            c down frowntalk "Ah-!"

            show cherry frown

            an "Cherry looks up with a start, her eyes wide with embarrassment."

            c frowntalk "Oh, uh... Hi, Alice."

            show cherry frown

            an up "I smile as reassuringly as I can."

            a up talk "You doing okay, Cherry?"
            a smile "{nw}"

            c up talk "Yeah. I’m fine."
            c down frowntalk "It’s just..."

            show cherry frown

            a talk "Just what?"
            a smile "{nw}"

            an "But Cherry doesn’t reply. She just stares sheepishly off to the side."
            #Can we play a sound effect here? Like grass rustling?
            an "Wait, what was {i}that{/i}?"
            an "I turn my head towards where I {i}think{/i} that sound was coming from..."

            a down talk "“...Oh!"
            a smile "{nw}"

            an "Hunched between a few small tufts of grass is a small white {i}something{/i}."
            an "...With long furry ears."

            a up talk "Cherry, were you trying to... chase that rabbit?"
            a smile "{nw}"

            an "Her eyes dart over to the ball of fluff, then back to me."

            c up talk "...Yep."

            show cherry smile

            an "She sighs."

            c down frowntalk "Buuuuut I think he kind of hates me."

            show cherry frown

            menu:
                "He doesn’t hate you.":
                    jump bunnylikesyou

                "Same.":
                    jump bunnyhateseveryone

                "Wait, how do you know it’s a boy?":
                    jump bunnygenderdiscourse

            label bunnylikesyou:

                a up talk "I don’t think he {i}hates{/i} you, Cherry."
                a smile "{nw}"

                an "I mean, can rabbits even {i}feel{/i} love?"
                an "...I should look that up sometime."

                a talk "Rabbits are just... kind of shy, you know?"
                a "They’re not like dogs and cats; they’re nervous around people."
                a smile "{nw}"

                an "Cherry nods."

                c up talk "I know, but..."
                c "All this stuff with the {i}contest{/i}, and the {i}mansion{/i}... It makes me feel like some kind of fairytale princess."

                show cherry smile

                a down talk "And princesses can talk to animals?"
                a smile "{nw}"

                c down talk "Yeah. ...But now that you’re {i}saying it out loud{/i}..."

                show cherry frown

                a up talk "Don’t worry about it. I know {i}I’m{/i} pretty starstruck by all this stuff."
                a smile "{nw}"

                an "Cherry smiles."

                show cherry up smile

                c up talk "And that’s why {i}you’re{/i} so quiet, right? Like the rabbit."

                $ cherryshy = True
                #We have to initialize the flag at the start of the game

                show cherry smile

                a "..."

                an "Wait, what? Where did {i}that{/i} come from?"
                an "I mean, I’ve never really thought of myself as {i}shy{/i}, but..."

                a talk "I guess compared to people like Katja and everyone else, I would seem kind of low-key..."
                a smile "{nw}"

                c talk "Yeah, but in a good way!"
                c "You’re so straightforward and unpretentious. It’s like you’re not trying to impress anyone, you know?"

                show cherry smile

                an "I’m... not sure if that was supposed to be a compliment, or..."

                a talk "Well, I {i}am{/i} trying to impress {i}some{/i} people. I want to win, after all."
                a smile "{nw}"

                c down "..."
                c frowntalk "Oh gosh, I’m sorry. I wasn’t trying to be {i}mean{/i} or anything. I {i}like{/i} that you seem normal."

                show cherry frown

                an "She starts gesticulating wildly."

                c up talk "You and Taylor are still acting like {i}yourselves{/i}, even with all of this {i}stuff{/i} happening!"
                c "You’re not treating the staff like {i}servants{/i}, and you’re not treating {i}me{/i} like..."
                c "Like I’m some kind of {i}enemy.{/i}"
                c "You {i}both{/i} just want to do your best!"

                show cherry down frown

                an "Cherry frowns."

                c frowntalk "I really hope...I hope {i}I{/i} can keep my head straight like you do."
                c "{i}Especially{/i} when I get kicked off..."

                show cherry frown

                menu:
                    "Cheer her up.":
                        jump backtothebunn

                    "Leave her alone for a while.":
                        jump cherrybunnyend

            label bunnyhateseveryone:

                a up talk "Well in {i}that{/i} case, he probably hates me, too."
                a smile "{nw}"

                c down frowntalk "Huh?"

                show cherry frown

                a talk "He’s probably got awful taste."
                a "In fact, that bunny {i}sucks{/i}."
                a smile "{nw}"

                show cherry up smile

                c talk "Well, even if he {i}does{/i}, I still wish we could pet him."

                show cherry smile

                a down talk "\"We\"?"
                a smile "{nw}"

                c talk "Don’t tell me you don’t wanna touch his fuzzy-wuzzy tail."

                show cherry smile

                menu:
                    "Yah.":
                        jump wannapetabunn

                    "Nah.":
                        jump bunnsaredumb

                label wannapetabunn:

                    a up talk "Oh, I {i}absolutely{/i} do."
                    a smile "{nw}"

                    an "Now {i}I’m{/i} giggling."
                    an "The two of us must look like such {i}dorks{/i} right now."
                    an "Standing in the morning sun, debating about a bunny’s butt..."
                    an "But you know...maybe there {i}is{/i} a way to charm that skittish ball of fuzz."

                    menu:
                        "Attempt to befriend the smol bunn":
                            jump backtothebunn

                        "Forget it.":
                            jump bunnsaredumb

                label bunnsaredumb:

                    a down talk "Honestly, I’m not {i}that{/i} interested."
                    a "I mean really, it’s just an animal."
                    a up smile "{nw}"

                    c down frowntalk "Oh."

                    show cherry frown

                    an "Cherry looks absolutely crestfallen."
                    an "Maybe I shouldn’t have been so harsh."

                    a down frowntalk "Umm, listen-"
                    a frown "{nw}"

                    an "But Cherry shakes her head."

                    c frowntalk "It’s fine, I know I’m being dumb."
                    c "Anyway, I’m sure you’ve got important stuff to do, so..."
                    c "I’ll see you around."

                    show cherry down smile

                    an "She offers a weak smile, but it’s pretty obvious that she’s hurt."
                    an "Still, what can I do?"
                    an "I think I need to leave her alone for a while..."

                    jump cherrybunnyend

                label bunnygenderdiscourse:

                    show cherry up frown

                    an "Cherry frowns for a moment."

                    c talk "Well, I’m not a hundred percent sure, but I {i}have{/i} read a lot about rabbits."
                    c "In some breeds, the male rabbits have these weird, smooshed-up little cheeks."
                    c "And the girl rabbits’ cheeks tend to be more...spoofle-y?"
                    c "Like {i}this{/i}."

                    show cherry smile

                    an "She draws a kind of football shape in the air."
                    an "I glance back over at the small, white poof that’s still vibrating in the grass."
                    an "I can’t even {i}see{/i} its face from here."

                    a talk "Well, I guess I’ll take your word for it."
                    a smile "{nw}"

                    c talk "Thanks."

                    show cherry smile

                    an "A few moments pass before Cherry pipes back up."

                    c talk "Anyway, I’m sure you’ve got all kinds of important things to do."
                    c "Really, I know I {i}should{/i} be practicing right now, but..."

                    show cherry smile

                    a talk "But bunnies are cute?"
                    a smile "{nw}"

                    c talk "Yup."

                    show cherry smile

                    an "Cherry smiled at me, looking more at ease than I’ve ever seen her."

                    menu:
                        "Offer to help her touch the floof.":
                            jump backtothebunn

                        "I’ve got better things to do.":
                            jump cherrybunnyend

                    label backtothebunn:

                        an "I take a deep breath."

                        a up talk "So."
                        a "You were chasing after that white rabbit, right?"
                        a smile "{nw}"

                        c up smile "Mmmhmm."

                        a talk "What if...I try to help you out?"
                        a smile "{nw}"

                        c down talk "Really?"

                        show cherry smile

                        a talk "Yeah."
                        a "I mean, I’m not exactly a Bunny Whisperer or anything..."
                        a "But maybe we can work together to figure something out."
                        a smile "{nw}"

                        show cherry up smile

                        an "Cherry is practically beaming at me."
                        an "Who knows? Maybe charming rabbits is some kind of secret talent of mine..."

                        scene fountainday
                        with fade

                        show cherry down frown at center:
                            zoom 1.3
                            yalign 0.4
                        with dissolve

                        $ config.side_image_tag = "alice"

                        an down frown "...Well, I was wrong about {i}that.{/i}"
                        #Can we maybe put a CG here? If not, don’t worry.
                        an "The two of us are sitting in the grass, trying to catch our breaths."
                        an "Turns out that {i}two{/i} bunny hunters are only slightly better than one."
                        an "Wait, \"Bunny Hunters\"? That sounds too grim."
                        an "..."
                        an "Oh gosh, I just spaced out again, didn’t I?"
                        an "I look over to Cherry, who’s twirling a piece of grass between her fingers."

                        a up talk "So, were you always big into animals?"
                        a smile "{nw}"

                        an "That...was’t exactly a great conversation starter."

                        show cherry smile

                        an "Cherry smiles anyway."

                        c up talk "Yeah, I was."
                        c "I was {i}super{/i} into horses back in elementary school. Like, {i}obsessed{/i}."

                        show cherry smile

                        a talk "Unicorns, too?"
                        a smile "{nw}"

                        c frown "..."
                        c frowntalk "Unicorns are cool, you know."

                        show cherry frown

                        a talk "Yeah, I know. I was just teasing."
                        a smile "{nw}"

                        c talk "Oh? Well what was {i}your{/i} animal growing up?"
                        c "I mean, everybody has one, right?"

                        show cherry smile

                        an "She’s right. But how am I supposed to answer her?"
                        an "It feels like any kind of answer I could give would be embarrassing..."

                        menu:
                            "Cats. It was cats.":
                                jump alicelikescats

                            "I was a horse girl, too.":
                                jump alicelikeshorses

                            "Would you believe it was dolphins?":
                                jump alicelikesdolphins

                            "Bunnies, actually.":
                                jump alicelikesbunnies

                            "Do ghosts count as an animal?":
                                jump alicelikesghosts

                        label alicelikesghosts:

                            a talk "Actually, I was into {i}ghosts{/i}."
                            a smile "{nw}"

                            c down frowntalk "Ghosts?"

                            show cherry smile

                            a talk "Well, Halloween and all that stuff."
                            a "You know, witches and spiders and werewolves..."
                            a smile "{nw}"

                            c up talk "That...doesn’t really seem much like you right now."
                            c "Buuuuut I think I can see it."
                            c "Maybe that’s why you’re so brave."

                            show cherry smile

                            if cherryshy:
                                a talk "I thought you said I was shy."
                                a smile "{nw}"

                                c talk "Well, maybe you’re both!"

                                show cherry smile

                            a talk "Thanks."
                            a smile "{nw}"

                            c talk "I’m not really a fan of that stuff, but it’s cool that you like it."

                            show cherry smile

                            jump cutebunnymoment

                        label alicelikescats:

                            a talk "I was a cat girl."
                            a "House cats, kittens, big cats at the zoo..."
                            a "Heck, I even went through a {i}Friendly Meow-Meow{/i} phase."
                            a smile "{nw}"

                            c talk "Oh? Did you ever read those {i}Traveler Cat{/i} books? I used to {i}love{/i} those."

                            show cherry smile

                            a talk "Oh gosh, yeah. Bramblepelt was like, my {i}role model{/i} or something."
                            a smile "{nw}"

                            c talk "Mmmm, I was always more of a Sunfern gal."
                            c "Man, I need to re-read those some day..."

                            show cherry smile

                            jump cutebunnymoment

                        label alicelikeshorses:

                            a talk "A horse, of course."
                            a smile "{nw}"

                            c smile "Hm?"

                            a talk "I ah...also liked horses."
                            a "When I was about five or six, there was this movie about a girl who adopted a lost foal."
                            a smile "{nw}"

                            c talk "...And the foal turned out to be a unicorn, right?"

                            show cherry smile

                            a down talk "You’ve {i}seen{/i} that movie? Everyone else I’ve asked says I’d made it up."
                            a up smile "{nw}"

                            c talk "No, I remember it. I had it on VHS."
                            c "I don’t remember the name, though..."
                            c "Still, it’s nice that we have something in common like that."

                            jump cutebunnymoment

                        label alicelikesdolphins:

                            a talk "I was {i}biiiiiig{/i} into dolphins, me."
                            a "...{i}Maybe{/i} it’s because I wanted to be a mermaid when I grew up."
                            a smile "{nw}"

                            an "Cherry giggles a little."

                            c talk "Well, if it makes you feel any better, {i}I{/i} wanted to be a fairy."
                            c "Or a magic dentist."

                            show cherry smile

                            a down talk "A...magic...dentist?"
                            a smile "{nw}"

                            c talk "Yeah. There was this cartoon I used to watch about a doctor who could like...teleport into people’s bodies and stuff."
                            c "So {i}I{/i} wanted to do the same thing, but...as a dentist."

                            show cherry smile

                            a talk "...Why?"
                            a smile "{nw}"

                            c talk "Didn’t want to compete."

                            show cherry smile

                            a up talk "With the tiny cartoon doctor?"
                            a smile "{nw}"

                            c talk "I never said I was a {i}smart{/i} kid, you know."
                            c "I think all kids have those kind of... bizarre fantasies."
                            c "Just silly stuff you daydream about when you’re bored at school..."

                            jump cutebunnymoment

                        label alicelikesbunnies:

                            a talk "Bunnies have always been my favorite animal."
                            a smile "{nw}"

                            c down talk "Really?"

                            a talk "Yeah. Why?"
                            a smile "{nw}"

                            show cherry up smile

                            an "Cherry giggles a little."

                            c talk "Well I mean, your name is {i}Alice{/i}."
                            c "And your favorite animal is {i}rabbits{/i}."

                            show cherry smile

                            an down "...Oh."

                            a up talk "Yes, Cherry, my name is Alice and I like rabbits, and I know {i}exactly{/i} what joke you’re about to make."
                            a smile "{nw}"

                            c talk "Hmmm, alright. I’ll keep it to myself."

                            show cherry smile

                            an "She winks."
                            an "Okay, that {i}was{/i} pretty cute."

                            c talk "Although now I’m kind of curious..."
                            c "Did you ever like the {i}book{/i}?"

                            show cherry smile

                            an "{i}Alice in Wonderland,{/i} huh..."
                            an "Well..."

                            menu:
                                "I loved that book.":
                                    jump alicelovesalice

                                "I was never really a fan...":
                                    jump alicehatesalice

                                "I’ve actually never read it.":
                                    jump readingisfornerds

                            label alicelovesalice:

                                a up talk "Actually, I {i}loved{/i} it."
                                a "I’ve always liked fantasy stuff, and the idea of escaping your boring life to go somewhere {i}amazing{/i} just..."
                                a smile "{nw}"

                                c talk "It makes you happy?"

                                show cherry smile

                                a talk "Yeah."
                                a smile "{nw}"

                                c talk "I guess that’s why you like it so much {i}here{/i}, right?"

                                show cherry smile

                                a talk "Huh. I guess you’re right."
                                a smile "{nw}"

                                c talk "I like it here, too."
                                c "It’s kind of stressful but...nice."

                                jump cutebunnymoment

                            label alicehatesalice:

                                a up talk "Eh, I never really liked it that much."
                                a smile "{nw}"

                                c down talk "Oh?"

                                show cherry frown

                                a frowntalk "Yeah."
                                a "Something about reading a book where the main character has your name is just {i}weird{/i}."
                                a "On top of that, I’d occasionally get teased about it, so..."
                                a frown "{nw}"

                                c up talk "So not really a lot of good memories about the book."

                                show cherry up smile

                                a talk "Yeah."
                                a smile "{nw}"

                                c talk "Well, {i}I{/i} kinda liked it, but I can see why it’d feel strange when a character has the same name as you."
                                c "Maybe I wouldn’t like it if it was \"{i}Cherry in Wonderland{/i}\"..."

                                jump cutebunnymoment

                            label readingisfornerds:

                                a up talk "I’ve uh...never read the book."
                                a smile "{nw}"

                                c down talk "But it’s {i}Alice in Wonderland{/i}. It’s one of those books that {i}everyone’s{/i} read."
                                c "It’s like saying you’ve never read Grimm’s Fairy Tales."

                                show cherry frown

                                a down talk "Wait...those are from {i}books{/i}?"
                                a smile "{nw}"

                                c "..."
                                c up talk "Were you, um...not a big fan of books growing up?"

                                show cherry smile

                                a up talk "Well, it’s not so much that I didn’t like {i}books{/i}, I just didn’t like {i}old{/i} books."
                                a "I always preferred reading about kids who I could relate to. You know, kids with CDs and skateboards and stuff like that."
                                a "Besides, it’s not like I don’t know what happens. I saw the movie a few times."
                                a smile "{nw}"

                                c talk "Which one?"

                                show cherry smile

                                a down talk "...There’s more than one?"
                                a smile "{nw}"

                                an "Cherry’s face makes an...indescribable expression."

                                c talk "Alright, so...after the contest, I am giving you a {i}crash course{/i} on classic children’s books."

                                show cherry smile

                                a talk "But...I mean...why?"
                                a frown "{nw}"

                                show cherry frown

                                an "She looks at me, her face oddly serious."

                                c frowntalk "To give you a {i}childhood{/i}, that’s why."

                                show cherry frown

                                an up smile "I can’t stop myself from giggling a little."
                                an "Cherry frowns, then starts giggling, too."

                                show cherry smile

                                an "She’s got an interesting way of telling a joke..."

                                jump cutebunnymoment

                        label cutebunnymoment:

                            an "Cherry and I sit like that for a while, just chatting about whatever pops into our heads."
                            an "Over the course of the conversation, we end up shifting our positions so that we’re sitting next to each other."
                            an "..."
                            an "...Seems like the wind is picking up a bit."
                            an "I can feel the soft summer breeze brushing against my face."
                            an "..."
                            an "And {i}something}{/i} is brushing against my {i}hand{/i}."
                            an "Something {i}hairy{/i}."

                            a down frowntalk "Huh?"
                            a frown "{nw}"

                            an "I look down and see...the rabbit."
                            an "A small, white bundle of fur with long, pointy ears and piercing red eyes."

                            a up talk "Uhh, hi?"
                            a smile "{nw}"

                            an "Cherry looks over to my hand."

                            c down talk "!"

                            show cherry down talk

                            an "She almost squeaks with joy, but manages to clap her left hand over her mouth."
                            an "And her {i}right{/i} hand is now gripping my arm."
                            an "Ow."
                            an "The bunny raises its head, gingerly sniffing the air."
                            an "I try to whisper."

                            a down talk "Did he...{i}come over to us{/i}?"
                            a smile "{nw}"

                            an "Cherry nods."

                            c talk "I...I think he’s saying \"Hi\"!"

                            show cherry down smile

                            an "Her grip on my arm tightens, but I can’t really blame her."
                            an "This thing is {i}insanely{/i} cute."
                            an "I let out a shaky sigh."

                            a up talk "Do you want to try to pet him?"
                            a smile "{nw}"

                            c up talk "Hmmm... yeah."

                            show cherry smile

                            an "She lets go of my arm."

                            c talk "He might run away, but..."
                            c "I want to try."

                            show cherry smile

                            a talk "Okay."
                            a smile "{nw}"

                            an "I smile at her encouragingly, and watch as she reaches out, her arm shaking."
                            an "The tips of her fingers brush against the rabbit’s back, and for a moment it tenses."
                            an "Then...the bunny goes back to sniffing the air, unbothered by Cherry’s touch."

                            c down talk "{i}Oh. My. Gosh!{/i}"

                            show cherry smile

                            an "Even though she’s whispering, her voice cracks slightly."

                            c talk "He is {i}so{/i} soft!"

                            show cherry smile

                            a talk "Really?"
                            a smile "{nw}"

                            an "I reach out to pet him, but the rabbit jumps backwards and scoots away into the grass."

                            a down frowntalk "Sorry, Cherry."
                            a frown "{nw}"

                            c up talk "No, it’s fine. I got to pet the bunny, and that’s what I wanted to do."

                            show cherry smile

                            a up talk "That’s great."
                            a "Anyway, d’you think we should head back inside?"
                            a "I feel like we’ve been here for a while."
                            a smile "{nw}"

                            c talk "Sure, let’s go."

                            show cherry smile

                            an "I push myself to my feet, then turn to Cherry and offer my hand."
                            an "She grabs it, and pulls herself up, smiling."

                            c talk "Well, I dunno about you. But I could {i}really{/i} go for a snack about now."

                            show cherry smile

                            a talk "That sounds like a plan."
                            a smile "{nw}"

                            hide cherry with dissolve

                            an "We head inside, still chatting along the way."
                            an "It’s really nice, getting to spend time with her..."

            label bunnyend2:
                jump nightSwitch

                ## end scene












