
#######################################################################################################################
##############################################                              ###########################################
##############################################           Mornings           ###########################################
##############################################                              ###########################################
#######################################################################################################################


######################### First morning

label morning1:

    scene dinnerday
    with fadee

    $ config.side_image_tag = ""

    an "Ugh... I somehow couldn't sleep at all and still slept like a log last night. It doesn't feel real- none of this."
    an "Do they feel the same way too?"
    an "There was a bit of an awkward tension in the air. Taylor and Mary didn't look all too happy to be here."
    an "Worse still, Cherry wasn't here yet. Usually she was pretty good at making things a little less uneasy."

    $ config.side_image_tag = "alice"

    a talk "Soooo... this is nice. A full breakfast, just us girls. Pretty neat."
    a smile "{nw}"

    show taylor up frown at center
    with dissolve

    t frowntalk "Mm. Seems a little calculated to me. You don't see the camera men off to the sides?"
    t "They're more interested in preparing some dumb direct-to-video featurette."

    show taylor frown

    a frowntalk "...You sure you want to mention that out loud?"
    a frown "{nw}"

    t talk "Ohhh, they'll edit it out. It's the magic of Hollywood."

    show taylor frown

    show taylor at leftt
    show mary up frown at rightt
    with moveinright

    m frowntalk "Ugh, they didn't cut the crust of my French toast. Useless gits, the lot of them."

    show mary frown

    a frowntalk "Okay, they're {i}definitely{/i} not cutting out that part..."
    a frown "{nw}"

    t talk "Mary, didn't anyone ever tell you that there's no cutting corners on the road to stardom?"

    show taylor smile

    m down frowntalk "Tch, seriously Taylor? It's too early in the morning for your insufferable tone."

    show mary frown

    an "I didn't have a comment prepared; I feel like Taylor's smug, holier-than-thou expression spoke volumes."

    t talk "We're all still competitors. I figured your skin would be thicker after surviving all the preliminary rounds, but I suppose not."
    t "Of course, I can't imagine a girl who didn't have to work for anything in her life would understand-"

    show taylor smile

    m frowntalk "Excuse me? Where do you come off, you mouthy, pompous-"

    show mary frown

    show cherry at center
    show mary at right
    show taylor at left

    c talk "Hi guys!!"

    show cherry smile

    a talk "Ohhhh thank god it's Cherry..."
    an frown "Before their catfight could escalate any further, Cherry bounced along, into her seat."

    c talk "Ooh, pancakes! Can we get any shaped like rabbits? Ohhhh, I bet they have those pancake artists! Like those videos online!"
    
    show cherry smile
    show taylor frown

    m unsure frowntalk "...Cherry, put your phone away. It's bad manners."

    show cherry frown

    c frowntalk "Eh?? But they're really cool! They make cartoon characters and stuff..."

    show cherry frown

    t frowntalk "I'm more curious about coffee art myself. I wonder if they make requests."

    show taylor frown

    a frowntalk "I doubt the producer is willing to pay out of pocket for baristas that can do that..."
    an smile "Things cooled off between the four of us quickly. Cherry had that calming effect on people, even as Taylor and Mary kept each other at an arm's length."
    
    t frowntalk "I suppose the execs want us all to start training together... and to get along more."

    show taylor frown

    m up frowntalk "Obviously. Only the best for our adoring fans..."

    show mary frown

    c talk "We're getting to practice together? YAAAY~!"

    show cherry smile

    a talk "...Heh."

    hide cherry
    hide taylor
    hide mary
    with dissolve

    $ config.side_image_tag = ""

    an smile "It looks like we're all going to be spending a lot more time together. Better fill up here - the next few days are going to be big."
    an "Now, where should I spend the day?"


    menu:
        "Go to the makeup room" (choiceimage="mary"):
            $ interaction1 = "mary1"
            jump mary1
        "Go to the music room" (choiceimage="director"):
            $ interaction1 = "musichall1"
            jump musichall1
        "Go to the mall" (choiceimage="cherry"):
            $ interaction1 = "cherry1"
            jump mall1




######################### Morning 2

label morningnormal1:
        
    scene bedaliceday
    with fadee
    
    ann "{i}Ahh, it's morning.{/i}"
    ann "{i}I can't recall my dreams, so I must've had some decent sleep. I feel rested enough.{/i}"
    ann "{i}Wow, I didn't even know my back could crack that much! These beds are really amazing. Alright, time to go to the washroom and make myself presentable before breakfast.{/i}"
    
    scene dinnerday
    with fade
    
    $ config.side_image_tag = "alice"

    show taylor up frown at rightt
    show jacques up smile at leftt
    with dissolve
    
    t frowntalk "Good morning."

    show taylor frown
    
    a talk "Morning."
    
    a smile "{nw}"

    j talk "How are you feeling today?"
    
    show jacques smile

    a talk "I guess I'm fine. What's for breakfast?"
    
    a smile "{nw}"

    j talk "Here's the selection for today."
    
    show jacques smile

    ann "{i}I'm still not really used to ordering from a menu. It's like eating at a restaurant, except you don't have to pay the bill!{/i}"
    ann "{i}Weird.{/i}"
    
    a talk "I'll have some pancakes!"
    
    ann smile "{i}As always, they're delicious. It doesn't take long before I gobble it all up.{/i}"
    ann "{i}Taylor keeps staring at their phone while I'm eating and Jacques is busy talking about a previous show to one of the waitresses.{/i}"
    ann "{i}I usually eat breakfast in my dorm room, all alone... and it's usually something terribly inapt, like a protein bar... or ramen...{/i}"
    ann "{i}So it's nice to have company in the room with you for a change.{/i}"

    j talk "Now that you're done, what are you going to do the rest of the morning?"
    
    show jacques smile

    $ interaction2 = "null"

    if interaction1 == "mary1":
        menu:
            "Go for a walk" (choiceimage="jacques"):
                $ interaction2 = "jacquesinterview"
                jump jacquesinterview
            "Go to the music room" (choiceimage="director"):
                $ interaction2 = "musichall1"
                jump musichall1
            "Go to the mall" (choiceimage="cherry"):
                $ interaction2 = "cherry1"
                jump mall1

    if interaction1 == "musichall1":
        menu:
            "Go to the makeup room" (choiceimage="mary"):
                $ interaction2 = "mary1"
                jump mary1
            "Go for a walk" (choiceimage="jacques"):
                $ interaction2 = "jacquesinterview"
                jump jacquesinterview
            "Go to the mall" (choiceimage="cherry"):
                $ interaction2 = "cherry1"
                jump mall1

    if interaction1 == cherry1:
        menu:
            "Go to the makeup room" (choiceimage="mary"):
                $ interaction2 = "mary1"
                jump mary1
            "Go to the music room" (choiceimage="director"):
                $ interaction2 = "musichall1"
                jump musichall1
            "Go for a walk" (choiceimage="jacques"):
                $ interaction2 = "jacquesinterview"
                jump jacquesinterview



#######################################################################################################################
########################################        Morning After Contest 1     ###########################################
#######################################################################################################################



label morning2: 

    scene musicroom
    with fadee

    $ config.side_image_tag = "alice"

    an smile "It's a bold new day, full of opportunity. The director was insistent that we take today to work on our dance routine."
    an frown "What he didn't mention was that Taylor would be in charge of the rehearsal. She led the pack, running us through the basic steps."
    
    show cherry up frown at left:
        zoom 1.4
        yalign 0.5
    show mary up frown at right:
        zoom 1.4
        yalign 0.5
    with dissolve

    c frowntalk "Hey, um, guys, why is Taylor up front? Did the director get a teacher?"

    show cherry frown

    a frowntalk "Taylor {i}is{/i} the teacher..."

    a frown "{nw}"

    m down frowntalk "Tch. What's the producer thinking? This is probably some stunt to save money..."

    show mary frown

    show taylor up frown at center behind mary, cherry:
        zoom 0.97
        yalign 1.0
    with moveinleft

    t frowntalk "I hear a lot of gossip back there, and not a lot of dancing!"

    show taylor frown

    an "Taylor called out behind her. Mary rolled her eyes, and continued to practice the motions." 

    show director at right behind mary:
        zoom 1.1
        xalign 1.2
    with moveinright

    di talk "Keep it up, girls! Being a star is more then having a good voice!"
    di "You gotta have the looks! The body movement! The swagger and finesse!"
    di "Work those hips! Wink to the crowd!"

    show director smile

    t up frowntalk "Mr. Director, um, please leave the instruction to me..."

    show taylor frown

    hide director with moveoutright

    an "To her credit, Taylor was a good instructor. She made her rounds to the rest of us."

    t frowntalk "Cherry, keep your legs like this. Try to keep them apart like that, and we'll work on the basic steps."

    show taylor frown

    c talk "Okay! ...Th-this is a little tricky..."

    show cherry frown

    t frowntalk "Mary, posture's important. Back straight, like this."

    show taylor frown

    m frowntalk "Oh come off it, I'm spent my entire childhood learning posture!" 

    show mary frown

    t talk "Well, give it a try. It's none of my business if the judges decide to cut you early..."

    show taylor frown

    m "...Hmph."

    t frowntalk "Alice... you're looking a little stiff over here."

    show taylor frown

    a frowntalk "I-I'm still finding my feet over here."
    a frown "{nw}"

    t frowntalk "It's because you're going straight to the tricky routines. Let's dissect the steps a bit."

    hide cherry with moveoutleft
    hide mary with moveoutright

    show taylor frown at center:
        zoom 1.4
        yalign 0.5
    with dissolve

    an "Taylor spent some time with me, making sure I understood the steps."
    an "Her movements were so fluid, rippling with dynamic energy. She had a bounce to her step. I envied that..."

    menu:
        "Can you teach me more?":
            jump morning2teach
        "Were you always this talented?": 
            jump morning2talent
        "This is tricky...":
            jump morning2tricky


    label morning2teach:
        a talk "Can you teach me more? I could use a tutor for this sort of thing."
        a smile "{nw}"
        t frowntalk "Oh, you never enrolled in a dance class? I suppose I could make some time when this whole competition is over..."
        show taylor frown
        a down frowntalk "When it's over!? But I won't need it then!"
        a frown "{nw}"
        t frowntalk "Ah, nonsense. You could be a showgirl in Vegas!"
        show taylor frown
        a up frowntalk "...That's implying I don't win this contest."
        a frown "{nw}"
        t frowntalk "Well, anything's possible."
        t frowntalk "Until then, I'll give you the best advice I can. We're here to put on a show, yes?"
        show taylor frown
        an "Taylor seemed up to the task. I wondered briefly why she would put so much effort in teaching her competitors, but..."
        an "I suppose that's just how she is. She likes the competition, the thrill of it all."
        jump morning2merge

    label morning2talent:
        a frowntalk "Were you always this talented, Taylor?"
        a frown "{nw}"
        t frowntalk "...Tch, perish the thought. I had to work damn hard to get this far."
        t "12 years as a competitive dancer, on theatre shows, choreography... it takes time and effort."
        show taylor frown
        a talk "Oh, wow! Then... then you've done this sort of thing before, huh?"
        a smile "{nw}"
        t frowntalk "Obviously. Now come on. You clearly don't have any natural aptitude, much as I loathe the term..."
        t "So you'll just have to play catch-up like everyone else."
        show taylor frown
        an "I get the feeling I slighted Taylor a bit with my earlier question... yeesh."
        jump morning2merge

    label morning2tricky:
        a frowntalk "This is tricky, is all. I keep mixing up my steps."
        a frown "{nw}"
        t frowntalk "You're overthinking it and using the same foot twice. That's why your legs keep getting tied up with each other."
        t "It's fine, you'll figure it out. Wouldn't be particularly worthwhile if it wasn't hard in the first place, right?"
        show taylor frown
        a frowntalk "Heheh, true. Just feeling a biiiiiit inadequate right now."
        a smile "{nw}"
        t frowntalk "It's normal. That's why we're all working at it together."
        t talk "Just between you and me, Mary's posture is muuuuch worse than your's."
        show taylor smile
        a smile "Pffft!"
        an "Taylor was patient, to be sure. I was feeling better about all this."
        jump morning2merge

    label morning2merge:
        an "The four of us kept at it until it was time to break for lunch. We then went our separate ways..."

        menu:
            "Go to Mary's room" (choiceimage="mary"):
                $ interaction3 = "mary"
                jump maryroom1
            "Go to the music room" (choiceimage="taylor"):
                $ interaction3 = "taylor"
                jump taylor1
            "Go to Cherry's room" (choiceimage="cherry"):
                $ interaction3 = "cherry"
                jump cherry1

        ## end scene

  

label hopeful:
    
    scene bedaliceday
    with fadee
    
    ann "{i}I awake to the first light of day streaming through my curtains.{/i}"
    ann "{i}My alarm has yet to sound. I turn it off, feeling rested enough that I don't need to sleep in any longer.{/i}"
    ann "{i}The air smells fresh. I take a deep breath in, letting the oxygen fill every cell in my body.{/i}"
    ann "{i}It’s a new day, and with it, a new adventure awaits. Just thinking about all that has happened is making me excited!{/i}"
    ann "{i}Yeah, I’m nervous, but I think I’m happy. Let’s try hard today too!{/i}"
    
    scene dinnerday
    with fade
    
    show cherry up smile at center
    with dissolve

    c talk "Good morning! Did you sleep well?"

    show cherry smile

    a talk "Good morning, Cherry- I did. How is breakfast?"

    a smile "{nw}"
    
    c talk "That’s good to hear. You’ll feel even better after you’ve filled your stomach. The piggy sausages are delicious!"
    
    show cherry smile

    ann "{i}I guess I’ll go for the pork sausages with hash browns this morning too. Those would go well with a fresh fruit salad and Greek yogurt to round it all up. Gosh, with an appetite like this, I’m gonna get real fat in no time!{/i}"
    ann "{i}Not that I mind a little extra weight. My mom keeps saying I'm not eating enough.{/i}"
    
    c talk "So what are you up to this morning?"

    show cherry smile
    
    #### call screen


label morning5:

    scene musicroom
    with fade

    an "Hoo! I should've put my phone away during the morning drills. It's been buzzing all morning."
    an "We're all wrapping up right about now. It took all of my willpower not to sneak a look."
    an "Of course, the director's watchful eye was keeping tabs on me all morning. I dunno if he had, I dunno, bat hearing or whatever. Like, he was bitten by a radioactive bat and developed sonar vision or something."
    an "...Better stop going down this rabbit hole. Taking a break, I look over my phone."
    $ config.side_image_tag = "alice"
    a frowntalk "Oh, crap! Look at all these messages!"
    a talk "Aww, Mom sent me cat photos. ...Oh no, they dressed up Vicky in a cheerleader outfit."
    a "Oh, she looks piiiiissed, hahaha! I gotta share this!"
    an smile "I open up my messages and start to draft a message for the accompanying photo..."
    an frown "...Ah, crap, my finger slipped. I was gonna send that to my bestie back home, Marge, but..."
    ## TODO sfx: phone ping
    an down "A phone's chiming broke my concentration."

    a frowntalk "! ....Oh no."
    a frown "{nw}"
    m "...Alice?"
    an "Craaaap, I sent it to the wrong person..."

    show mary up frown at center:
        zoom 1.3
        yalign 0.4
    with moveinright

    m frowntalk "What is this you sent me?"
    show mary frown
    a talk "T, that's my cat, Vicky! My, my mom dressed him up, see? Cuz he's... rooting for me, eheh..."
    a smile "{nw}"
    m frowntalk "...You should think of sending this to the director's phone instead of mine."
    show mary frown
    a frowntalk "Oh, no, God no, he'd flip his shit if I was texting during practice...!"
    a frown "{nw}"
    m talk "Hm. I wonder."
    show mary smile

    hide mary with moveoutleft

    an "Without any further comment, Mary walked off as if nothing happened."
    a up frowntalk "...Is she... gonna keep the photo on her phone?"
    a frown "{nw}"

    show cherry up smile at center:
        zoom 1.55
        yalign 0.5
    with moveinbottom

    c talk "OH! ARE YOU SHARING CAT PHOTOS!?"
    show cherry smile
    a frowntalk "AH! Cherry!?"
    a frown "{nw}"
    c talk "I got a ton of photos! Bunnies are my favourite! I got, like, twenty of the lil guys!!"
    show cherry smile

    show taylor up frown at right:
        zoom 0.98
        yalign 0.3
    with moveinright

    t frowntalk "Maybe you should start keeping them in separate cages..."
    show taylor frown
    a talk "Taylor! D, do you have any pets?"
    a smile "{nw}"
    t frowntalk "Eh, low maintenance ones, sure. I have a small aquarium at home. Has some loaches, some angelfish..."
    t talk "Don't have enough time to raise anything else. I came to win, after all."
    show taylor frown
    a talk "Yeah... right."
    a smile "{nw}"
    c talk "FOUND THEM!"
    show cherry smile
    a frowntalk "O-oh no..."
    a talk "...Oh, they're really fuzzy...!"
    a smile "{nw}"
    c talk "I KNOW, RIGHT!?"
    show cherry smile

    hide cherry
    hide taylor
    with dissolve

    an "Cherry proceeded to bombard me with bunny photos for the better part of half an hour. I thin Taylor managed to wriggled free in the ensuing chaos."
    an "Only when she was satisfied did Cherry finally release me from her grip..."

    ## end scene


        
label morning3:
    scene dinerday
    with fadee

    an "And then it was down to three. After the show last night, it still doesn't really feel real."
    an "It's just the three of us - Cherry, Taylor, and myself - at breakfast together."
    $ config.side_image_tag = "alice"

    show cherry up frown at rightt:
        zoom 1.2
        yalign 0.3
    with easeinright

    c frowntalk "Haah... it's so much quieter here without Mary around."
    show cherry frown
    a frowntalk "Aw, Cherry, don't take it so hard. Somebody needed to get eliminated."
    a frown "{nw}"
    c frowntalk "It's so... final, though. Like we're gonna be torn apart from each other!"
    
    show cherry frown
    show taylor up frown at leftt:
        zoom 1.2
        yalign 0.3
    with easeinleft

    t frowntalk "Yeeeeah. That's kind of the point of an elimination competition. Last one standing wins."
    show taylor frown
    a frowntalk "Taylor, you could be a bit more sympathetic..."
    a frown "{nw}"
    t frowntalk "Why? It's how the business goes. She didn't make the cut, so we all move on."
    t "I don't know why y'all are so torn up about it. It's not like she up and died."
    show taylor frown
    c frowntalk "Wah! I don't want her to die!!"
    show cherry frown
    an "Yeesh. The sight of Cherry... it reminds me of a puppy crying for its owner."
    a talk "L-look on the bright side! They'll probably invite us all for some kind of, uh, reunion dinner, or something!"
    a smile "{nw}"
    t frowntalk "Yeah. Probably at some cheap dive though. Producer's stingy as hell."
    show taylor frown
    c frowntalk "...That sounds nice..."
    show cherry frown
    t frowntalk "Also, there's probably gonna be cameos for future seasons in store for us."
    show taylor frown
    c talk "...Wow, I didn't even think of that! That makes me feel like... like I'm part of the show family! Or something..."
    show cherry smile
    a talk "...Y'all think we should take a picture together? We can use it for a Christmas card."
    a smile "{nw}"
    t frowntalk "...Y'know what. Sure. Why not? Let's just track down Mary and we'll get it done."
    t "There's probably a costume department around here somewhere too if we really wanted to accessorize..."
    show taylor frown
    c talk "Can we dress up as Santa's reindeer?? Ooh, I wanna be Cupid! I wanna be Cupid!!"
    show cherry smile
    a frowntalk "I-I dunno, if... if they have that sort of thing?"
    an frown "I wonder what Mary was up to. Last night must've been rougher for her than she's been letting on."
    $ config.side_image_tag = ""

    hide taylor
    hide cherry
    with dissolve

    an "I got another big day ahead. Maybe I'll find time to check up on her."
    an "Still, though, I gotta get time to practice on my own routine. Or they might cut me next..."
    
    ## end scene


label morning4:

    scene dinerday
    with fadee
    an "Man, having breakfast first thing in the morning used to be so light and breezy. Now with half of the girls cut from the competition, it was down to me and Taylor. Normally, I'd be ecstatic, but..."
    an "Right now, it just felt... weird. Just sitting here between the two of us. It was so weird."
    an "Taylor wasn't a talkative sort. She didn't lose sleep over the fates of the other girls. She was just... keeping to herself."
    an "I wanna say something. I'm {i}going{/i} to say something."
    
    $ config.side_image_tag = "alice"
    show taylor up frown at center:
        zoom 1.3
        yalign 0.4
    with dissolve

    a frowntalk "...So it's just us now."
    a frown "{nw}"
    t frowntalk "...Yup."
    show taylor frown
    a frowntalk "Big show last night. Hope Cherry's feeling better today."
    a frown "{nw}"
    t "Mmhm."
    a frowntalk "She just... kind of seems like the lonely sort. Maybe I'll see her later."
    a frown "{nw}"
    t frowntalk "You do you, girl."
    show taylor frown
    a down frowntalk "...What's your problem??"
    a frown "{nw}"
    t frowntalk "I have a problem?"
    show taylor frown
    a frowntalk "Yeah. I'm trying to have a conversation here!"
    a frown "{nw}"
    a frowntalk "Look, Alice, I like you. We practice together, we perform together, and hell, maybe we'll end up working together someday. Maybe on some collab album."
    t "But today? These next few days? We're competitors. And it's coming down to the wire now."
    t "I got better things to worry about than making hapless smalltalk. And I know you do too."
    show taylor frown
    a up frowntalk "...Ah."
    an frown "Well. That was decidedly decisive. Taylor didn't seem all that eager to hold a conversation."
    a frowntalk "...I was just hoping we'd all still be friends by the end."
    a frown "{nw}"
    t frowntalk "...I dunno."
    show taylor frown
    an "Taylor sighed to herself, poking at her scrambled eggs."
    t frowntalk "It's the messed up American model of competition, not us, it... it just kind of stirs up drama like this."
    t "Like... it's not enough that you win. Others have to lose."
    show taylor frown
    a frowntalk "...Do you really believe that?"
    a frown "{nw}"
    t frowntalk "I kinda have to. I'm not here to lose."
    t "And I'm sure as hell not going to waste the opportunities I'm given here. That I earned."
    t "...I'm aiming to crush this competition. No hard feelings, Alice."
    show taylor frown
    an "Taylor talked a big game. She was determined to win it all."
    a frowntalk "...Yeah. No hard feelings."
    a talk "Besides, I know you'd never admit it. I'm glad we're friends. And that we got to know each other."
    a smile "{nw}"
    t talk "...Heh. Ditto."
    show taylor smile
    an "Even through her thick armour, she still cared. She was smiling earnestly, she couldn't hide her real feelings."
    a talk "Let's do our best. I'm going into the finals prepared."
    a smile "{nw}"
    t talk "Good to hear. It'll make obliterating you all the more satisfying!"
    show taylor smile
    a frowntalk "Awww, c'mon Taylor..."
    a frown "{nw}"
    ## end scene



label anxious:
    
    scene bedaliceday
    with fade
    
    ann "{i}I have been tossing and turning the entire night. For some reason, I couldn't sleep.{/i}"
    ann "{i}The sun has finally risen. I turn off the alarm I set and drag myself out of bed.{/i}"
    ann "{i}No matter how many times I look at it, this room still feels so empty. Sure, there's pieces of high-class furniture to fill the space in an artsy arrangement, it’s still much too large a place for a single person to stay in.{/i}"
    ann "{i}I don't belong here, do I?{/i}"
    ann "{i}What the hell am I thinking? I must be having one of those days. Time to gather myself before heading down for breakfast.{/i}"
    
    scene dinnerday
    with fade
    
    show taylor up frown at left
    show director smile at right
    with dissolve
    
    t frowntalk "You look like a zombie."
    
    show taylor frown
    
    a frowntalk "I'm sure you're right."

    ann frown "{i}Not that I exactly want to hear it from you.{/i}"
        
    di talk "Eat up and get yourself together, Intie."
    
    show director smile

    ann "{i}The director slides the menu across the table. I don’t bother with it, just turning around to the maid to ask her for a glass of water and a piece of toast. I don’t have much of an appetite for anything else.{/i}"
    ann "{i}Ordering for food is just one of the many strange ways things are done here. It feels so alien.{/i}"
        
    t frowntalk "Better that you keep yourself preoccupied than to worry about unnecessary things."
    
    show taylor frown
    
    ann "{i}Yeah, I guess he's right. What should I do this morning?{/i}"
    
        
    


label tired:
    
    scene bedaliceday
    with fade
    
    ann "{i}What's that?{/i}"
    ann "{i}It takes a moment before my groggy mind can register the sound from my bedside. I reach an arm out to slam on the alarm clock before shrinking back under the sheets.{/i}"
    ann "{i}Cold... it's so cold out.{/i}"
    ann "{i}It's a lot warmer here. I still want to sleep.{/i}"
    ann "{i}Just five more minutes... I'll wake up after that...{/i}"
    
    scene bedaliceday
    with fade
    
    with hpunch
    
    ann "{i}Shit! I've slept an extra hour!{/i}"
    ann "{i}I'm so late for breakfast. I better get going!{/i}"
    
    scene dinnerday
    with fade
    
    show mary up frown at leftt
    show katja frown at rightt
    with dissolve
        
    m "Someone hasn't had a good night's sleep."
    
    show mary frown
    
    a frowntalk "Just a little tired, is all."

    a frown "{nw}"
    
    k frowntalk "Tiredness is the worst enemy for a woman's beauty."

    show katja frown
    
    ann "{i}For anybody's health for that matter. Not like I actually want to be so tired... sheesh.{/i}"
    
    m frowntalk "The air circulation system in this building needs work. We can adjust the temperature in our own rooms, but not the humidity. What blasphemy!"
    
    show mary frown
    
    ann "{i}Yes, Mary. We know you like to complain, but that’s really a non-complaint, okay? My whole apartment building back home has a single temperature control!{/i}"
    
    a frowntalk "Whatever. If there’s a second enemy for a woman’s beauty, it’s an empty stomach."
    a "I'll have some ice-cream waffles!"
    
    ann smile "{i}Maybe the sweets will help improve my mood for the morning.{/i}"
    ann "{i}Now what should I do for the rest of the day before lunch?{/i}"
    
    #### call screen


label morningtaylor:
    scene dinnerday
    with fade
    
    ann "{i}It's breakfast time again. Time to eat!{/i}"
    
    show t up frown at rightt
    show j up smile at leftt
    with dissolve

    $ config.side_image_tag = ""
    
    t frowntalk "The food here is ridiculous. Can’t I just get a sandwich?"
    
    show taylor frown

    j talk "You can. There’s the black truffle lobster sandwich topped with gold flakes."
    
    show jacques smile
    
    t "...Again, can't I just get a sandwich? Hello?"
    
    show taylor frown
    
    a talk "I suppose it does taste delicious."
    
    ann smile "{i}I order the \"sandwich\", but request that they take out the gold flakes. It feels like such a waste if they just pass right through my intestines.{/i}"
    ann "{i}I guess I shouldn't be thinking about that when I'm eating...{/i}"
        
    j talk "I'm done. What about you two?"
    
    show jacques smile

    t frowntalk "I’m in the process of dissecting my steak to make it more manageable for consumption."
    
    show taylor frown

    an frown "Who eats a steak for breakfast-?!"

    a talk "I’m almost done. There’s still much to do after all."
        
    ann smile "{i}So what am I going to do for the afternoon?{/i}"

    ## end scene





