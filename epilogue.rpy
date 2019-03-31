##################################################################################################################
##################################################################################################################
########################################        Post Game Scenes        ##########################################
##################################################################################################################
##################################################################################################################
image credits_text = ParameterizedText(outlines=[(2, "#3E0045", 0, 0)], size=40, xalign=0.5, yalign=0.5)

image small_text1 = ParameterizedText(outlines=[(2, "#3E0045", 0, 0)], size=35, xalign=0.5, yalign=0.35)
image small_text2 = ParameterizedText(outlines=[(2, "#3E0045", 0, 0)], size=35, xalign=0.5, yalign=0.65)


label credits:

    $ quick_menu = False 

    scene black
    with creditsfade

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

    hide credits_text
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

    hide credits_text
    with dissolve

    show credits_text "\nLead Writer: Kevin \"Tutty The Fruity\" Armstrong"
    with dissolve
        
    pause 8

    hide credits_text
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

    hide credits_text
    with dissolve

    show credits_text "\nWriter: Seigetsu"
    with dissolve
        
    pause 8

    hide credits_text
    with dissolve

    show credits_text "\nGuest Artist: Ani"
    with dissolve
        
    pause 8

    hide credits_text
    with dissolve

    show promocherry at rightt behind credits_text:
        zoom 0.50
        yalign -7.0
        subpixel True
        linear 15 yalign 12.0
        linear 1 alpha 0
    with Dissolve(1.0)

    show credits_text "\nStory Consultants: Penelope Pilbeam, Andi Wamboldt"
    with dissolve
        
    pause 8

    hide credits_text
    with dissolve

    show credits_text "Special thanks to Ryanne Bowyer, \nNicoletta Christina Browne, and Ayu Sakata."
    with dissolve
        
    pause 8

    hide credits_text
    with dissolve

    show small_text1 "\"Fearless\" by Tavian St. James and \n\"Friends Forever\" and \"Forever Dreaming\" by Alcaknight"
    show small_text2 "\"Knocking Door\" by dersuperanton, \"Wooden Door Open\" by joedeshon, and \"On Stage Jingles\" by Setuniman"
    with dissolve
        
    pause 8

    hide credits_text
    with dissolve

    show credits_text "This game was made with Ren'Py.\nThank you Pytom."
    with dissolve
        
    pause 8

    hide credits_text
    with dissolve


    if win:
        jump epilogue
    else:
        return


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

    show director smile at right behind mary:
        zoom 1.1
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

    $ config.side_image_tag = ""
    
    a "Is it starting?"
    
    k "Made it just before I was about to send out my lackeys to hunt you down, dead or alive."

    scene stageclose
    with fade

    show jacques up smile at center:
        zoom 1.35
        yalign 0.3
    with dissolve

    $ config.side_image_tag = ""
    
    j talk "Welcome to season two of your favorite idol show, Supernova! Are you ready for another month of heart-wrenching, blood-boiling struggles for the throne of your next superstar?"
    j "Yes! I know I’m ready! And she is too! Introducing our winner from season one - she will start us off with the first song of this new festival!"
    
    show jacques smile

    ann "{i}I make my way up the steps. The familiar light falls upon me.{/i}"
    ann "{i}Tay, Mary, Cherry... they’re all watching. I wave to them, feeling their cheers pour energy into my heart.{/i}"
    
    j talk "This is your idol, Alice Carroll......"

    show jacques smile

    return
    
    ###### end epilogue



#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################


label endingSwitch:
    if mary_stat > taylor_stat and cherry_stat:
        jump maryend
    if taylor_stat > mary_stat and cherry_stat:
        jump taylorend
    if cherry_stat > mary_stat and taylor_stat:
        jump cherryend
    if mary_stat == taylor_stat or mary_stat == cherry_stat:
        jump credits
    if taylor_stat == mary_stat or taylor_stat == cherry_stat:
        jump credits


label maryend:
    scene bedaliceday
    with fadee

    $ config.side_image_tag = ""

    an "A few hours later, the shock hasn't gone away. It feels unreal, that I was able to win it all."
    an "It makes it a little surreal that, now, at the end of the road, I have to pack my things and head out again."

    show mary up frown:
        zoom 1.4
        yalign 0.5
    with dissolve

    m frowntalk "Don't you have people for that, now?"

    $ config.side_image_tag = "alice"

    a up frowntalk "Ah! Mary! What're you doing here??"
    a frown "{nw}"
    m up talk "Your door was unlocked, idiot. Don't make that mistake again, you're a celebrity now."
    show mary smile
    a down talk "Ah, right, I... gotta get used to that. I'm gonna have a team and everything, I guess."
    a smile "{nw}"
    m talk "Of course. I suppose there's a... {i}folksy{/i} charm to your personality."
    m up frowntalk "It could use some TLC, though. Something forward-facing for the ravenous public."
    m down frown "{nw}"
    a down frowntalk "Maryyy, you're starting to sound like the producer..."
    a smile "{nw}"
    m up frowntalk "I mean your outfits. They're rather plain, thank heavens for the costume department."
    show mary frown
    a up frowntalk "Eh?? I have great fashion sense!"
    a up frown "{nw}"
    m down frowntalk "Oh please. Look at this one. \"I Got Dirty at Big Richard's Buggies\"?"
    show mary frown
    a up talk "They were mud buggies! And it was a souvenir. I like souvenirs."
    a smile "{nw}"
    m up talk "You're an idol now, and there's a certain... image you need to present."
    m frowntalk "...I was hoping I could... maybe, perhaps... steer you in the right direction."
    show mary frown
    a down talk "...Huh?"
    an smile "Mary flourished a business card, her eyes focused on the far wall. She didn't seem keen on making eye contact at the moment."
    an "I give it an examination. It was professionally made, ebony and glossy, with a slick font choice, contemporary and understated."
    a up talk "What's this about, Mary? You want to... keep hanging out?"
    a smile "{nw}"
    m down frowntalk "\"Hanging out\", tch, no, no..."
    m down talk "...Okay, yes. I would like to continue seeing you."
    m up "You have this... precious naivety about you. It's almost infantile. I wondered if I could help you, well, ease into the pressures of idol culture."
    m up frowntalk "Of course, I would make myself useful as a fashion consultant..."
    show mary smile
    a down talk "Heh. You can be my personal chef too, if you like!"
    a down smile "{nw}"
    m unsure frowntalk "I-I'm not sure that's a great idea..."
    show mary frown
    a up talk "Aw, come on, Mary. You don't have to act so professional and stiff all the time."
    a "...I like you too."
    a smile "{nw}"
    m frowntalk "Really?"
    extend "...I-I mean, the feeling's... mutual."
    show mary smile
    a talk "...Thanks for being here with me, Mary."
    an smile "I hurry over to embrace her. Mary awkwardly pats my back in turn."

    m talk "I-it's no problem, I... I look forward to working..."
    extend "...{i}spending{/i} more time with you."

    show mary smile

    hide mary
    with dissolve

    scene black
    with fadee

    $ config.side_image_tag = ""

    an "It was strange. The two of us had spent so much time together as competitors. It was hard to tell if we could get along as just friends... or maybe more than that."
    an "But I'm glad she's here to stay."

    jump credits



################################################################


label cherryend:

    scene makeuproom
    with fadee

    show katja smile
    with dissolve

    $ config.side_image_tag = "alice"

    a down frowntalk princess "Holy crap... I can't believe I won!!"
    a down frown "{nw}"
    k frowntalk "Language, dear. You're an idol now, you have an image to maintain."
    show katja frown
    a up frowntalk "I can still hear the cheering!!"
    a up frown "{nw}"
    k frowntalk "...They haven't gone anywhere, the show just ended."
    show katja frown
    a frowntalk "...Ohhh."
    a frown "{nw}"
    k talk "Anyway, yes, congratulations all around, great work everyone. Our lease ends at midnight, so let's strip down and not waste any time-"
    #memo: give her big entrance idc how, bump or something

    show katja:
        easein 0.5 xalign 0.8
    show cherry with hpunch:
        xalign -0.5
        easein 0.3 xalign 0.52
        linear 0.1 xalign 0.5
    #sfx bump

    c talk "{b}ALIIIIIIICE!!!!{/b}"
    show cherry smile
    a frowntalk "Wah!!"
    an frown "Out of the corner of my eye, Cherry was sprinting at me, full speed, and collided headlong into me."
    an "I might've been sent careening back onstage, if not for her enormous bear hug locking me in place."

    c talk "YOU DID IT! I'M SO PROUD OF YOUUUUU!~"
    show cherry smile
    a up frowntalk "Ch-Cherry! Let... go! I'm... suffocating!!"
    a smile "{nw}"
    c down frowntalk "Oh! Sorry..."
    show cherry smile
    an "Cherry relented on command, but her bombastic smile didn't waver a bit. She was bouncing up and down; her excitement could hardly be contained."

    c up talk "You did it! I knew you could do it!!"
    show cherry smile
    a down talk "That's great to hear, but... what about Taylor?"
    a smile "{nw}"
    c down talk "Oh! I believe in Taylor too! I knew she could do it too!!"
    show cherry smile

    show director smile:
        xalign 0.0
    with moveinleft

    di talk "They couldn't both do it! Ugh, who let this loser back on stage!?"

    show director smile

    k frowntalk "Director! Heel, boy. Let the girls have their fun. I need you over here."

    show katja frown

    hide director
    hide katja
    with dissolve

    an "The adults left us alone for the time being. Cherry was unphased by the director's harsh comments."

    a down frowntalk "Ugh. Cherry, can you believe what that guy said...?"
    a frown "{nw}"
    c up talk "Huh? Who said what? I didn't hear, the crowd's so loud..."
    show cherry smile
    a up talk "...Nevermind. You're unflappable, you know?"
    a smile "{nw}"
    c down talk "Awww! Thanks! I mean, I guess that would be kind obvious, I'm not a bird or anything, but..."
    c up talk "But enough about me! You were amazing!!"
    show cherry smile
    a down talk "Y-yeah, I'm... still not sure how I pulled it off."
    a smile "{nw}"
    c down talk "Because you're the best!! And you're an inspiration to all of us!"
    c up talk "In fact, I'm gonna be the president of your fan club!"
    extend "...Can you help me figure out the paperwork for that? I-I dunno where to start."
    show cherry smile
    a down frowntalk "Oh my gosh, Cherry..."
    a down talk "...Of course I'll help you. It's a really good idea."
    a smile "{nw}"
    c talk "Yeah! And we can meet every month! ...Is that enough? Is that too much?"
    c up frowntalk "I don't wanna... stop seeing you or anything. Even when you're big and famous, I..."
    show cherry smile
    a frowntalk "...Cherry..."

    an smile "I step forward, embracing Cherry in a big hug."

    a talk "I could never forget you. The time we spent together, I could never forget that."
    a "...It's okay if we keep meeting up. There's a lot of this city I haven't seen."
    a smile "{nw}"
    c up talk "Aaaa! We could go on dates!!"
    show cherry smile
    a up frowntalk "...Dates??"
    a up smile "{nw}"
    c up talk "Yeah! Girls can love girls, it's 2019!"
    
    show cherry smile

    #emote smile
    a talk "...Yeah. You're right. One hundred percent."
    a smile "{nw}"

    hide cherry
    with dissolve
    scene black
    with fadee
    
    $ config.side_image_tag = ""

    an "It was amazing how earnest Cherry could be, and not feel a smidgen of self-doubt. I had a lot to learn from her if I was really going to put myself out there."
    an "I'm glad she's in my corner. I don't know where this will go, but... I'm excited to reach for new possibilities."

    jump credits



################################################################


label taylorend:
    scene musicroom
    with fadee

    $ config.side_image_tag = ""

    an "It's been a day, and I've had time to process everything that's happened. Even then, I find myself wandering the music hall one more time."
    an "Part of me doesn't want to leave this all behind. Even as the workers are already making strides to tear everything down."
    an "It's a little bittersweet to watch. But I guess I shouldn't linger too much on what happened. I'm gonna be a celebrity; I gotta live in the moment, looking ahead..."

    show katja
    with dissolve

    k talk "Oh! Alice, finally, I found you."
    show katja frown

    $ config.side_image_tag = "alice"

    a up frowntalk "A-ah! Hi! S-sorry, I was a little spaced out there."
    a frown "{nw}"
    k frowntalk "Nevermind that, can I borrow you for the next hour or so? We have a bit more filming to do."
    show katja frown
    a down frowntalk "Borrow me? For what? Isn't the contest over."
    a frown "{nw}"
    k frowntalk "Ahhh, no no, not quite. You see, we need featurettes for the home release. We stand to make a good deal of money on releasing the whole season on BluRay and HD."
    show katja frown
    a up frowntalk "...Ah. Right. Yeah, where do you need me?"
    a smile "{nw}"
    k frowntalk "We're setting up a room. Also, have you seen Taylor? Haven't seen the damn girl all day."
    show katja frown
    a up frowntalk "...Uh, no. Not recently."

    an frown "I recall briefly. I don't think I've seen her at all since the last show..."

    k frowntalk "Well, if you stumble across her, do give her a heads up. We still have need of you girls."
    k "I suppose I shall wrangle the other two..."
    show katja frown

    hide katja
    with dissolve

    $ config.side_image_tag = ""

    an "Shaking her head, the producer wandered off, leaving me to my thoughts."
    an "Maybe I'll see if Taylor's in her room..."

    scene hallday
    with fadee

    an "It didn't take too long to make my way over there."

    play sound "doorknock.mp3"

    an "I knock a few times at her door."

    $ config.side_image_tag = "alice"

    a up talk "Taylor? Are you in there?"
    an frown "...No response. This is weird."
    an "I figured out her general routine. Normally she'd be preparing to go on a run right about now."
    an "My hand lowers to the doorknob, finding it provided no resistance."
    #sfx door slowly open
    an "I open the door to sneak a peek inside."

    scene bedtaylorday
    with fadee

    a up talk "...Oh, Taylor, you're here!"
    extend down frowntalk "...Taylor?"

    show taylor down frown
    with dissolve

    an frown "I found her. She was just sitting there, staring ahead at the far wall. She was completely still, cradling something in her lap."

    t ".........."
    a frowntalk "...Oh dear."

    an frown "Commenting quietly to myself, I hurry in and sit next to her."

    show taylor:
        zoom 1.5
        yalign 0.5
    with dissolve

    a down frowntalk "Taylor? Are you okay?"
    a frown "{nw}"
    t frowntalk "Why did you come back?"
    show taylor frown
    a up frowntalk "...What?"
    a frown "{nw}"
    t frowntalk "You won. And I lost. There's nothing more to it than that."
    t "I was so close... and now I have to start all over."
    show taylor frown
    an "Taylor was trying to hold it together, but her voice was heavy. She looked crushed..."

    a down frowntalk "...I was worried about you, Taylor. Have you been in here all day?"
    a frown "{nw}"
    t frowntalk "...Yes."
    show taylor frown
    a down frowntalk "Oh, honey..."
    a frown "{nw}"
    t frowntalk "I don't understand, I... I did everything right."
    t "I exercise, I practice, I meditate. I... I maxed out all my credit cards for HRT, and for surgeries..."
    t "I'm {i}broke{/i}, Alice, I-I don't know what to do...!"
    show taylor frown
    a down frowntalk "Taylor!"
    an frown "Taylor's tough facade was breaking into pieces in the blink of an eye. It was heartbreaking to watch."
    an "I lean over, wrapping my arms around her to hold her close. She was shaking, choking back sobs."

    a down frowntalk "Taylor, you're gonna be okay! You're smart, and talented, and strong..."
    a frown "{nw}"
    t frowntalk "...Why does everything have to be so hard?"
    t "It's like... like I've been going through life with a ball and chain, and I work, and I work..."
    t "And it's never enough! What do I have to do? A-am I not girly enough!?"
    show taylor frown
    a down frowntalk "No! No, you're perfect, just the way you are, Taylor, I..."
    a down talk "...You inspire me, Taylor..."
    a smile "{nw}"
    t up frowntalk "...Really...?"
    show taylor frown

    an "Taylor hiccuped, her sobbing momentarily ceasing."

    a up talk "Yeah. You're the hardest worker of any of us. And you still made time so we could all be the best that we could be."
    a "I... I learned so much from you. A-and I won't forget you. I don't {i}want{/i} to forget you."
    a down "...You're so important to me, Taylor. I hate to see you like this."
    a frown "{nw}"
    t down frowntalk "...Y-you don't have to pity me. You won, you're gonna be a big star."
    t down "...You don't need me."
    show taylor frown
    a down frowntalk "No! That's wrong! I need you! Now... now more than ever, I..."
    a down talk "...I really really like you, Taylor. I want to keep working with you, a-and learning from you."
    a smile "{nw}"
    t up frowntalk "...You... like me?"
    show taylor frown
    a down talk "Yeah. You don't give up on people. I... I like that about you."
    a up "I think you have more to give than you realize."
    a smile "{nw}"
    t down talk "...It doesn't feel like it, but... thank you."
    show taylor smile

    an "Taylor was starting to quiet down. Aside from a few sniffles, we held each other in silence."
    an "Taylor stirred slightly, before wriggling out from my grip. She raised a hand to wipe her eyes."

    t down frowntalk "...I-I dunno if I can do an interview right now... look how red my eyes are."
    show taylor frown
    a up talk "We can reschedule. I'm sure the producer will understand."
    a smile "{nw}"
    t up talk "Yeah. You tell her that. You have clout now, after all."
    t down "Hey, Alice, can I... keep working with you?"
    t up "You have something about you, that I can't really put a finger on. Maybe it's, I dunno, a humble worldview, Pure, untainted or something."
    t down "...I think I can learn something from you. If you would have me."
    show taylor smile
    an frown "Taylor wanted to learn from me now? It was such a strange concept, but... she was so earnest in everything she did."

    a down talk "...Of course, Taylor. That means the world to me."
    a smile "{nw}"
    t down talk "...Maybe I should just suck it up. The show must go on, yada yada..."
    show taylor smile
    a down talk "Are you sure you're gonna be okay? You worked so hard, you can take a break for a bit."
    a smile "{nw}"
    t up talk "...Maybe. I'll pull myself together. Always do."
    show taylor smile
    a up talk "Of course. I'll just... stay here with you for a bit."
    a smile "{nw}"
    t up frowntalk "What? But isn't the producer-"
    show taylor smile
    a up talk "She can wait. I'm a celebrity now, right?"
    a down "I'd rather make time for you."
    a smile "{nw}"
    #emote: blush
    t up talk "...Pfft. Stop it."
    show taylor smile
    a up talk "Hehe..."
    a smile "{nw}"

    hide taylor
    with dissolve

    scene black
    with fadee

    $ config.side_image_tag = ""

    an "Taylor and I stayed together in her room, simply enjoying each other's company."
    an "Things don't feel any different. I mean, we aren't competing with each other anymore, but we always tried to prop each other up."
    an "I think in the coming days, we'll find new ways to support each other... it's pretty exciting."
    an "I can't wait to see what the future brings."

    jump credits






