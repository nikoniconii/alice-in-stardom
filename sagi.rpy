#
# https://docs.google.com/spreadsheets/d/1DYo0ud8CJTObTpO89y-92ViCvc2vqX5KH3RR3O4uofY/edit#gid=0
# https://docs.google.com/document/d/1Rnl2qAMK_aeXaygW7lrQx3aFfnbQwbM9Xy8BLyxDlPI/edit#heading=h.dl77jqh3pa3q
#

label taylor2:
    $ config.side_image_tag = ""

    scene shop
    with fadee

    an "I know that Taylor has a thoroughly regimented exercise routine. I had to figure this out quickly, because she's annoying hard to track down to any one spot."
    an "If I want to talk to her, I'll have to catch her at the mall. I'm pretty sure she'll be refueling at Fruitastic Smoothies."
    an "...Maybe I put too much thought into this."

    $ config.side_image_tag = "alice"

    a "...Oh, there she is! Taylor!!"

    show taylor
    with dissolve

    t "...?"

    an "Right on cue, she made it to the smoothie cart."

    t talk "Alice. What's new with you?"
    t "{nw}"

    a "Not much! Figured I'd catch you while you were running."
    t down smile "...I hope you weren't stalking me."
    a frowntalk "No! ...Maybe a bit. I just see you heading out a lot in the mornings."
    a frown "{nw}"
    t up talk "Oh! You wanna buddy up. Yeah, I could use a partner. You ever go jogging in the city?"
    t smile "{nw}"
    a "Not in the city specifically, but there were all these winding bike trails around where I grew up, up in Wichita?"
    t "Heh, alright. The city isn't much different, you just wanna avoid the high traffic areas. Inhaling a strong whiff of car exhaust is a good way to get sick."
    t "Just need to refuel real quick and... wait. Hmmm..."
    a frown "What? What's wrong??"

    an "Taylor lowered her eyes to the ground. Her eyes squinted as she focused on something."
    an "She was looking at my... feet? No, my shoes."

    t frown "Tch. Thaaat won't do. I figured you'd bring better shoes for this."
    a frowntalk "Eh? Wh, what's wrong with my shoes? They're sneakers, it's not like I'm gonna wear them to a ball..."
    a frown "{nw}"

    t "For the best performance, you need the best equipment. You don't wanna get sore or pull a muscle for the big show, right?"
    a "...I guess not, but... it's probably not that big a deal."
    t "Nonsense. That'd be a pathetic way to go down."

    an "Her eyes drifted aside."

    t "Mmhm, mmhm... bet there's  sporting goods store somewhere in the mall. We'll scope it out and get a recommendation."
    a talk "You don't have to, really-"
    a smile "{nw}"
    t "I kinda have to, though? If we're gonna be exercise buddies.~"
    a "...Ooookaaaay..."

    an "Man, new shoes are gonna be really expensive. And they're gonna look ugly too..."

    t talk "Anyway, I gotta fill up. Let's get smoothies."
    t smile "{nw}"

    an "Without waiting for a response, Taylor strolled over to the cashier."

    t talk "Eyo, I'll get the Banana Slamma. Alice, what're you getting?"
    t smile "{nw}"
    a frown "aaaaaaaaaaaa"

    an "I look over the menu. There must be a hundred options up here! The raw power was overwhelming..."

    a down frowntalk "{i}AAAAAAAAAAAAAAAA{/i}"
    a down frown "{nw}"

    an "PICK SOMETHING QUICK PICK SOMETHING QUICK!!"

    a up smile "I'll get... the Honduran Passion Fruit Siesta!!"

    an "The girl working the counter gave me a concerned look. Her mouth flattened, she punched in the order."

    t smile "I got this covered."

    an "Taylor pulled out her wallet, pulling out a twenty."

    a "...?"

    an "Out of the corner of my eye, I spot something through a clear screen of her wallet. It appeared to be a photo."
    an "A photo of a boy and a Labrador, it looked like. There was a lot of resemblance to Taylor. Maybe she had a twin brother."
    an "I didn't get a very long look before Taylor pocketed it once more."

    a talk "Omigosh! Puppy!!"
    a smile "{nw}"
    t frowntalk "What? Alice!"
    t frown "{nw}"
    a "Puppy!! There was a photo of a puppy in your wallet! What's his name??"
    t "...Patriot. You looked into my wallet?"
    a "Yeah, at that photo in your wallet! I didn't know you had a brother too! Is that your brother?"

    #emote: confusion

    t down frown "..."
    t down frown "...I don't have a brother."
    extend "And you probably shouldn't go snooping into other people's belongings either..."
    a down frowntalk "Ahhh, I'm sorry, I only caught a glimpse just now."
    a down smile "...So is that your boyfriend? If he's not family then-"
    t up frown "It's me."
    a "...Um?"
    t frown "Yeaaah. That's an old photo. I transitioned five years ago."
    a down talk "Wow! Um..."
    a down smile "{nw}"

    an "Wasn't expecting that. What do I say...?"

    menu:
        "So you used to be a guy?":
            jump taylor2negative
        "Sorry about that...":
            jump taylor2neutral
        "You look great!":
            jump taylor2positive

label taylor2negative:
    a up talk "So you used to be a guy? That's interesting!"
    a up smile "{nw}"

    an "Her eyes narrow into a laser-sharp stare, and I immediately know I’ve made an error."

    t down frowntalk "No! I used to present as a guy."
    extend "I'm a woman. Always have been."
    t down frown "I just never had the chance to make other people see that until the last couple years..."
    a talk "OH! R-right, I get it. I think. Sorry about that, I..."
    a smile "{nw}"
    t frown "It's... something to get used to, I get it. People still mix it up all the time."

    an "Taylor furrowed her brow as she said this. That must've sounded super dumb."
    an "I wanna support her and not come off as a bigot... come on Alice."
    jump taylor2merge

label taylor2neutral:
    a frown "Sorry, I... don't know a lot of trans people. Hope I didn't overreact or anything."
    t down frown "Nah, you're fine. I get that kind of reaction a lot."
    a smile "Still, it has to be pretty stressful, right?"
    t up frown "You don't get this far in life without having thick skin. I just wanna correct misconceptions and stuff."
    t smile "We can talk about it, no worry. I could forward you some websites so you can learn more..."
    a talk "Ah! That's be really cool!"
    a smile "{nw}"

    an "I don't have a lot of trans friends. None I'm really close with. I'm glad Taylor is being really chill about all this."
    jump taylor2merge

# SAGI'S NOTE: label says one thing, comments say the other. I'm keeping this one for now
#don't use this label: use the next label
label taylor2positive:
    a up talk "You look great! I-I mean, this photo's also cute, but... now it's like, wow!"
    a smile "{nw}"
    #emote: blushu
    t smile "Hehe. Thanks Alice. I'm glad."
    t  "It's nice to know that HRT is doing something after all~"
    a talk "Oh! Is that something you get regularly?"
    a smile "{nw}"
    t talk "Oh yeah. Brutally expensive. Maybe if I get a contract to perform from this, paying the bills won't be a problem anymore."
    t smile "{nw}"
    a "You could hit up Mary! She's pretty rich."
    t down smile "I dunnoooo. She doesn't really care for hand-outs."
    a down smile "Ahh..."
    a up smile "{nw}"
    t up smile "{nw}"

    an"Taylor really appreciated the compliment. The smile on her face definitely indicates that much."
    jump taylor2merge

#use this label
label taylor2positivedeletethis:
    a "Wow, you’re—you’re like... magic."
    #emote: blushu
    t "Pfft. What the heck are you talking about?"
    a "It’s just… I see so little of that kid in you. You blossomed into a stunning woman."
    t "Ah! Uh, th—thanks, Alice."
    t "It’s... not like that just happened on it’s own, though. It’s been an uphill battle."
    a "Well… it’s one you’re definitely winning."
    t "If you say so."

    an "She’s pretending to be aloof, but it’s clear Taylor really appreciated the compliment. The smile on her face clearly indicates that much."

    t "It’s not the only thing I need to win, though. If I get a contract to perform from this, paying the bills won't be a problem anymore..."
    a "Ahhh…"
    jump taylor2merge

label taylor2merge:
    t down smile "It's not a big deal. I just keep an old photo to motivate me."
    t up talk "It's kind of an affirmation of how far I've come. And how long I need to go. And I just keep it in my wallet so it's never far away."
    t smile "Maybe I oughta just frame it and put on my bedside or something."
    a up talk "No, that's cool! Inspirational even!"
    a smile "{nw}"
    t smile "Heh. That's what I was going for."
    #sfx ding
    t talk "Oh! Smoothies are ready."
    t smile "{nw}"
    a talk "Alright! Let's find a table and-"
    a smile "{nw}"
    t smile "Nah. We got them to go. I don't really like sitting in one place too long."
    a smile "Ohhhh. ...I hope we're not gonna go jogging, I don't wanna spill mine."
    t down talk "Pfft. Don't worry about it. Just a leisurely stroll around the mall. We can go window shopping."
    t down smile "{nw}"
    a up talk "Ooh! Yeah! Do either of us have any money though...?"
    a up smile "{nw}"
    t up talk "Once we're all rich and famous, money opens all doors~"
    t up smile "{nw}"
    a smile "...Truuuue..."

    an "Sharing a laugh, the two of us head out to see the rest of the mall."

    hide taylor
    with dissolve
    $ config.side_image_tag = ""

    an "At the end, we part ways to get onto other things. I can only keep up with Taylor's energy for so long."



#####################################


#Mary 3 (After Elimination)
label mary3:
    $ config.side_image_tag = ""

    scene shop
    with fadee

    an "I think the producer had something special planned for Mary at the mall today. Maybe I'll check on that..."
    an "...There's actually a pretty big crowd forming near the water fountain. Mary's at a table... signing autographs?"

    show katja frown
    with dissolve
    k "Alice? Whatever are you doing here?"

    an "It seems the producer picked me out from the crowd. She seems disappointed to see me here."

    k frowntalk "Surely you have better things to do than to traipse about the mall... don't you have your own preparations to handle?"
    k frown "{nw}"

    $ config.side_image_tag = "alice"
    a down frowntalk "Eh? Well, yeah, but I wanted to see what Mary was up to over here."
    a down frown "{nw}"
    k frown "I'll have you know she's rather busy at the moment herself. Dealing with the demanding fanbase is practically a full-time job, you know."
    a down frown "...I can tell from the line-up."

    an "I catch a glance towards the front. She's flanked by two bodyguards, and furiously penning autograph after autograph."
    an "She looks busy. Maybe I should..."

    menu:
        "Leave her to her business":
            jump mary3neutral
        "Go and say hello":
            jump mary3negative
        "Ask for an autograph":
            jump mary3positive

label mary3neutral:
    a down frown "...Yeah, she looks busy. Probably doesn't need to see me. I'll check on her later..."
    k frowntalk "An excellent idea. Now go on. Shoo. I need you in peak form for our next show."
    k frown "And try not to let anyone spot you on the way out, it may distract from our signings over here."
    a up frown "R-right, of course."

    hide katja
    with dissolve

    $ config.side_image_tag = ""
    an "It's disappointing, but I figure I can catch Mary a little later..."

label mary3negative:
    an "...Eh, I'll get out of the producer's hair. But not before checking in with Mary first."

    k frowntalk "H-hey, come back here, you can't just-"

    hide katja
    with dissolve

    an "I manage to give the producer the slip, rushing towards Mary's table."

    a up talk "Hey, Mary! Over here!"

    an "I holler to try and get her attention, hurrying to the front of the line."
    an "Mary glanced up from her papers."

    show mary down frown
    with dissolve

    m "...Alice??"
    #character labels: Diehard Fan = DF, Obsessed Fan = OF, Super Fan = SF
    of "Is that Alice!?"
    sf "Holy crap it is!! Is she signing autographs too!?"
    df "I need to get another selfie with her!"
    a down frowntalk "{i}(\"ANOTHER!?\" I've never seen that guy in my life!!){/i}"
    a down frown "Oooookay, this was a mistake!"

    hide mary
    with dissolve

    $ config.side_image_tag = ""
    an "The crowds were suddenly converging on me, and the helpers on hands were struggling to hold them back."
    an "Across the room, Mary was glaring daggers at me. I get the sinking feeling I was ruining her event."
    an "...Yeah, definitely ruining her event. Time to make a hasty retreat...!"

label mary3positive:
    a up smile "...Is it okay if I get her autograph?"
    k frown "What?? What are you playing at, girl? If you want that so bad, you can ask back on set..."
    a "Yeah, but.. I wanna surprise her."
    k frowntalk "...Ugh. Children these days, with their one-upping mindgames and whatnot."
    k frown "{nw}"
    a frowntalk "I-it's nothing like that! Really!"
    a smile "{nw}"
    k "Well, the line starts there. Do put on a hat and some sunglasses if you're going for that."
    k "The last thing I need is for you to get recognized and drum up a riot..."
    a "Ah, good point..."

    hide katja
    with dissolve

    an "I think I got a big hat on me... oh, and sunglasses to hide my eyes! That'll only add to the surprise. I gotta thank Katja for the idea later!"
    an "Okay, time to get in line!"
    an "..."
    an "... ..."
    an "... ... ..."
    an "... ... ... ... ... ... ... ... ... ... ..."

    a down frown "This, uh... this is a pretty long line."
    #sfx bump
    df "HEY, BACK OFF! You're gonna break my selfie stick!"
    a down frowntalk "S-sorry! It's so cramped..."
    a down frown "{nw}"

    an "Somehow I make it to the front of the line."

    show mary
    with dissolve

    m talk "Hi there!~ And who do I make this out to?"
    m smile "{nw}"
    a down talk "Heeey, it's me! Just make it out to Alice."
    a down smile "{nw}"
    m down frown "...bwuh?"
    "Mary did a double take upon seeing me."
    m down frowntalk "W-what're you doing here!?"
    m down frown "{nw}"
    a up talk "I wanted your autograph!"
    a smile "{nw}"
    m up frown "...{i}why?{/i} You beat me."
    a "You're still an inspiration to me!~"
    #sprite: blushu
    m down smile "...Ugh, you sap."
    a down smile "Hehe!~"

    an "Mary was pretty easy to embarrass. She kept her head down, trying to hide her blushing cheeks, before sliding a signed photo over to me."

    m down talk "There. Now beat it."
    m up smile "...And... thanks."
    a talk "No, thank you! I'll catch you later..."
    a smile "{nw}"

    hide mary
    with dissolve

    $ config.side_image_tag = ""
    an "I probably shouldn't take up any more of Mary's valuable time. I'll track her down when this is all wrapped up."


################################################################


label cherrypostelim:
    $ config.side_image_tag = ""

    scene hallday
    with fadee

    an "Man... I can't believe it's just me and Taylor left."
    an "I haven't seen Cherry for a while. I should check up on her - she's so emotional and big-hearted, she can't be taking this news well."
    #sfx door knock
    play sound "doorknock.mp3"

    an "I knock at her door. I hope she's inside..."

    c "Come in!~"

    an "She called from inside. Huh, she didn't {i}sound particularly beat up about it."

    scene bedcherryday
    with fadee
    #sfx

    an "I let myself in, finding Cherry with a laptop. She's tucked into a comfy chair, rapidly typing away."

    show cherry
    with dissolve
    c talk "I made jelly! Do you want some?"
    c smile "{nw}"

    $ config.side_image_tag = "alice"
    a down "...You're... eating it from a teacup?"
    c down smile "I didn't have any bowls. They're like, Jell-O shots! Except, um, appropriate for kids."
    a up talk "Heheh! Alright. We can have our jelly with class and style."
    a smile "{nw}"

    an "I stroll past her, picking out a chilled teacup from her mini fridge."

    a down frown "So, uh... you seem well! Sorry that, well... you know."
    c down talk "Oh, it's okay! I was kinda.bummed earlier, but... look at this!"
    c down smile "{nw}"

    an "Cherry turns her laptop around towards me, beaming with pride."
    an "I lean forward, squinting to get a better look."
    an "...Is this a comment thread? From some kind of online forum..."

    a up frown "What's all this, Cherry?"
    c up talk "Look at all these people! They're all wishing me well!"
    c down smile "A lot of them were really sad too... others wanted to say I did a really fantastic job!"
    c down frowntalk "And then some people got really mad. This guy says he was gonna take matters into his own hands."
    c down frown "Maybe I should let the producer know??"
    a down frown "Mmmmmmaybe?? That sounds dicey."
    a up smile "...But maniacs aside, it sounds like everyone loved you."
    c smile "Mmhm! Reading everyone's words of support made me feel a looot better about this."
    c talk "And, and! I'll get a front-row seat when I see you and Taylor on stage!~"
    c smile "{nw}"
    a talk "Eh? O-oh, that's... that's true."
    a smile "{nw}"

    an "That's right. I don't think anyone's more of a fan than Cherry. She comes off as more of an idol superfan than an idol herself... even if she more than qualifies as the latter."

    a up smile "...Hey, Cherry, if you look on Mugshot, I'm sure you'll find more fans there."
    c talk "Ah, right!! I should make a post there. I was just finishing up making my account on this..."
    c smile "{nw}"
    a down smile "...Uhhh, maybe... {i}don't{/i} do that. That one guy's still taking matters into his own hands, and..."

    an "I spend the better part of the afternoon trying to keep Cherry out of trouble online."
    an "Even if she's no longer a contestant, it feels like nothing's changed."
    $ config.side_image_tag = ""
    hide cherry
    with dissolve



################################################################


label maryend:
    $ config.side_image_tag = ""

    scene bedaliceday
    with fadee

    an "A few hours later, the shock hasn't gone away. It feels unreal, that I was able to win it all."
    an "It makes it a little surreal that, now, at the end of the road, I have to pack my things and head out again."

    show mary down frown
    with dissolve

    m "Don't you have people for that, now?"

    $ config.side_image_tag = "alice"
    a up frowntalk "Ah! Mary! What're you doing here??"
    a frown "{nw}"
    #emote: smile
    m up smile "Your door was unlocked, idiot. Don't make that mistake again, you're a celebrity now."
    a down smile "Ah, right, I... gotta get used to that. I'm gonna have a team and everything, I guess."
    m down smile "Of course. I suppose there's a... {i}folksy{/i} charm to your personality."
    m up frowntalk "It could use some TLC, though. Something forward-facing for the ravenous public."
    m down frown "{nw}"
    a down frown "Maryyy, you're starting to sound like the producer..."
    m up frowntalk "I mean your outfits. They're rather plain, thank heavens for the costume department."
    m frown "{nw}"
    a up frowntalk "Eh?? I have great fashion sense!"
    a up frown "{nw}"
    m down frowntalk "Oh please. Look at this one. \"I Got Dirty at Big Richard's Buggies\"?"
    m down frown "{nw}"
    a up talk "They were mud buggies! And it was a souvenir. I like souvenirs."
    a smile "{nw}"
    m up smile "You're an idol now, and there's a certain... image you need to present."
    #emote: blushu
    m down smile "...I was hoping I could... maybe, perhaps... steer you in the right direction."
    a down smile "...Huh?"

    an "Mary flourished a business card, her eyes focused on the far wall. She didn't seem keen on making eye contact at the moment."
    an "I give it an examination. It was professionally made, ebony and glossy, with a slick font choice, contemporary and understated."

    a up smile "What's this about, Mary? You want to... keep hanging out?"
    m down frowntalk "\"Hanging out\", tch, no, no..."
    m down smile "...Okay, yes. I would like to continue seeing you."
    m up smile "You have this... precious naivety about you. It's almost infantile. I wondered if I could help you, well, ease into the pressures of idol culture."
    m up talk "Of course, I would make myself useful as a fashion consultant..."
    m up smile "{nw}"
    a down talk "Heh. You can be my personal chef too, if you like!"
    a down smile "{nw}"
    m down frown "I-I'm not sure that's a great idea..."
    a up smile "Aw, come on, Mary. You don't have to act so professional and stiff all the time."
    a down smile "...I like you too."
    m down smile "Really?"
    #emote: blushu
    extend "...I-I mean, the feeling's... mutual."
    a "...Thanks for being here with me, Mary."

    an "I hurry over to embrace her. Mary awkwardly pats my back in turn."

    m down smile "I-it's no problem, I... I look forward to working... "
    extend "...{i}spending{/i} more time with you."

    hide mary
    with dissolve
    $ config.side_image_tag = ""

    scene black
    with fadee
    an "It was strange. The two of us had spent so much time together as competitors. It was hard to tell if we could get along as just friends... or maybe more than that."
    an "But I'm glad she's here to stay."



################################################################


label cherryend:

    scene makeuproom
    with fadee

    $ config.side_image_tag = "alice"

    show katja smile
    with dissolve

    a down frowntalk "Holy crap... I can't believe I won!!"
    a down frown "{nw}"
    k "Language, dear. You're an idol now, you have an image to maintain."
    a up frowntalk "I can still hear the cheering!!"
    a up frown "{nw}"
    k frown "...They haven't gone anywhere, the show just ended."
    a "...Ohhh."
    k smile "Anyway, yes, congratulations all around, great work everyone. Our lease ends at midnight, so let's strip down and not waste any time-"
    #memo: give her big entrance idc how, bump or something

    show katja:
        easein 0.5 xalign 1.5
    show cherry with hpunch:
        xalign -0.5
        easein 0.3 xalign 0.52
        linear 0.1 xalign 0.5
    #sfx bump

    c "{b}ALIIIIIIICE!!!!{/b}"
    a "Wah!!"
    an "Out of the corner of my eye, Cherry was sprinting at me, full speed, and collided headlong into me."
    an "I might've been sent careening back onstage, if not for her enormous bear hug locking me in place."

    c talk "YOU DID IT! I'M SO PROUD OF YOUUUUU!~"
    c smile "{nw}"
    a up frowntalk "Ch-Cherry! Let... go! I'm... suffocating!!"
    a smile "{nw}"
    c down smile "Oh! Sorry..."

    an "Cherry relented on command, but her bombastic smile didn't waver a bit. She was bouncing up and down; her excitement could hardly be contained."

    c up talk "You did it! I knew you could do it!!"
    c smile "{nw}"
    a down smile "That's great to hear, but... what about Taylor?"
    c down talk "Oh! I believe in Taylor too! I knew she could do it too!!"
    c down smile "{nw}"
    di "They couldn't both do it! Ugh, who let this loser back on stage!?"

    show katja:
        easein 0.5 xalign 1.0
    k "Director! Heel, boy. Let the girls have their fun. I need you over here."
    show katja:
        easein 0.5 xalign 1.5

    an "..."
    hide katja
    an "The adults left us alone for the time being. Cherry was unphased by the director's harsh comments."

    a down frown "Ugh. Cherry, can you believe what that guy said...?"
    c up smile "Huh? Who said what? I didn't hear, the crowd's so loud..."
    a up smile "...Nevermind. You're unflappable, you know?"
    c down smile "Awww! Thanks! I mean, I guess that would be kind obvious, I'm not a bird or anything, but..."
    c up talk "But enough about me! You were amazing!!"
    c smile "{nw}"
    a down smile "Y-yeah, I'm... still not sure how I pulled it off."
    c down talk "Because you're the best!! And you're an inspiration to all of us!"
    c up smile "In fact, I'm gonna be the president of your fan club!"
    extend "...Can you help me figure out the paperwork for that? I-I dunno where to start."
    a down talk "Oh my gosh, Cherry..."
    a down smile "...Of course I'll help you. It's a really good idea."
    c talk "Yeah! And we can meet every month! ...Is that enough? Is that too much?"
    c up frown "I don't wanna... stop seeing you or anything. Even when you're big and famous, I..."
    a "...Cherry..."

    an "I step forward, embracing Cherry in a big hug."

    a "I could never forget you. The time we spent together, I could never forget that."
    a smile "...It's okay if we keep meeting up. There's a lot of this city I haven't seen."
    c down talk "Aaaa! We could go on dates!!"
    c down smile "{nw}"
    #emote: blushu
    a up talk "...Dates??"
    a up smile "{nw}"
    c up talk "Yeah! Girls can love girls, it's 2019!"
    c up smile "{nw}"
    #emote smile
    a down smile "...Yeah. You're right. One hundred percent."

    hide cherry
    with dissolve
    $ config.side_image_tag = ""

    scene black
    with fadee
    an "It was amazing how earnest Cherry could be, and not feel a smidgen of self-doubt. I had a lot to learn from her if I was really going to put myself out there."
    an "I'm glad she's in my corner. I don't know where this will go, but... I'm excited to reach for new possibilities."




################################################################


label taylorend:
    $ config.side_image_tag = ""

    scene musicroom
    with fadee

    an "It's been a day, and I've had time to process everything that's happened. Even then, I find myself wandering the music hall one more time."
    an "Part of me doesn't want to leave this all behind. Even as the workers are already making strides to tear everything down."
    an "It's a little bittersweet to watch. But I guess I shouldn't linger too much on what happened. I'm gonna be a celebrity; I gotta live in the moment, looking ahead..."

    show katja
    with dissolve

    k "Oh! Alice, finally, I found you!"

    $ config.side_image_tag = "alice"
    a up frowntalk "A-ah! Hi! S-sorry, I was a little spaced out there."
    a frown "{nw}"
    k "Nevermind that, can I borrow you for the next hour or so? We have a bit more filming to do."
    a down frown "Borrow me? For what? Isn't the contest over."
    k frown "Ahhh, no no, not quite. You see, we need featurettes for the home release. We stand to make a good deal of money on releasing the whole season on BluRay and HD."
    a up frown "...Ah. Right. Yeah, where do you need me?"
    k frown "We're setting up a room. Also, have you seen Taylor? Haven't seen the damn girl all day."
    a up frown "...Uh, no. Not recently."

    an "I recall briefly. I don't think I've seen her at all since the last show..."

    k "Well, if you stumble across her, do give her a heads up. We still have need of you girls."
    k "I suppose I shall wrangle the other two..."

    hide katja
    with dissolve
    $ config.side_image_tag = ""

    an "Shaking her head, the producer wandered off, leaving me to my thoughts."
    an "Maybe I'll see if Taylor's in her room..."

    scene hallday
    with fadee

    an "It didn't take too long to make my way over there."
    #sfx doorknock
    play sound "doorknock.mp3"
    an "I knock a few times at her door."

    $ config.side_image_tag = "alice"
    a up smile "Taylor? Are you in there?"

    an "...No response. This is weird."
    an "I figured out her general routine. Normally she'd be preparing to go on a run right about now."
    an "My hand lowers to the doorknob, finding it provided no resistance."
    #sfx door slowly open
    an "I open the door to sneak a peek inside."

    scene bedtaylorday
    with fadee

    show taylor down frown
    with dissolve

    a up talk "...Oh, Taylor, you're here!"
    extend down smile "...Taylor?"

    an "I found her. She was just sitting there, staring ahead at the far wall. She was completely still, cradling something in her lap."

    t ".........."
    a drown frown "...Oh dear."

    an "Commenting quietly to myself, I hurry in and sit next to her."

    a down smile "Taylor? Are you okay?"
    t "Why did you come back?"
    a up frown "...What?"
    t frowntalk "You won. And I lost. There's nothing more to it than that."
    t frown "I was so close... and now I have to start all over."

    an "Taylor was trying to hold it together, but her voice was heavy. She looked crushed..."

    a down frown "...I was worried about you, Taylor. Have you been in here all day?"
    t "...Yes."
    a down frown "Oh, honey..."
    t "I don't understand, I... I did everything right."
    t frowntalk "I exercise, I practice, I meditate. I... I maxed out all my credit cards for HRT, and for surgeries..."
    t frowntalk "I'm {i}broke{/i}, Alice, I-I don't know what to do...!"
    t frown "{nw}"
    a down frowntalk "Taylor!"
    a down frown "{nw}"

    an "Taylor's tough facade was breaking into pieces in the blink of an eye. It was heartbreaking to watch."
    an "I lean over, wrapping my arms around her to hold her close. She was shaking, choking back sobs."

    a down smile "Taylor, you're gonna be okay! You're smart, and talented, and strong..."
    t "...Why does everything have to be so hard?"
    t "It's like... like I've been going through life with a ball and chain, and I work, and I work..."
    t frowntalk "And it's never enough! What do I have to do? A-am I not girly enough!?"
    t frown "{nw}"
    a down talk "No! No, you're perfect, just the way you are, Taylor, I..."
    a down smile "...You inspire me, Taylor..."
    t up frown "...Really...?"

    an "Taylor hiccuped, her sobbing momentarily ceasing."

    a up smile "Yeah. You're the hardest worker of any of us. And you still made time so we could all be the best that we could be."
    a down smile "I... I learned so much from you. A-and I won't forget you. I don't {i}want{/i} to forget you."
    a down frown "...You're so important to me, Taylor. I hate to see you like this."
    t down frowntalk "...Y-you don't have to pity me. You won, you're gonna be a big star."
    t down frown "...You don't need me."
    a down frowntalk "No! That's wrong! I need you! Now... now more than ever, I..."
    a down frown "...I really really like you, Taylor. I want to keep working with you, a-and learning from you."
    t up frown "...You... like me?"
    a down smile "Yeah. You don't give up on people. I... I like that about you."
    a up smile "I think you have more to give than you realize."
    t down smile "...It doesn't feel like it, but... thank you."

    an "Taylor was starting to quiet down. Aside from a few sniffles, we held each other in silence."
    an "Taylor stirred slightly, before wriggling out from my grip. She raised a hand to wipe her eyes."

    t down frown "...I-I dunno if I can do an interview right now... look how red my eyes are."
    a up smile "We can reschedule. I'm sure the producer will understand."
    t up smile "Yeah. You tell her that. You have clout now, after all."
    t down smile "Hey, Alice, can I... keep working with you?"
    t up smile "You have something about you, that I can't really put a finger on. Maybe it's, I dunno, a humble worldview, Pure, untainted or something."
    t down smile "...I think I can learn something from you. If you would have me."

    an "Taylor wanted to learn from me now? It was such a strange concept, but... she was so earnest in everything she did."

    a down smile "...Of course, Taylor. That means the world to me."
    t down smile "...Maybe I should just suck it up. The show must go on, yada yada..."
    a down smile "Are you sure you're gonna be okay? You worked so hard, you can take a break for a bit."
    t up smile "...Maybe. I'll pull myself together. Always do."
    a up smile "Of course. I'll just... stay here with you for a bit."
    t up frown "What? But isn't the producer-"
    a up talk "She can wait. I'm a celebrity now, right?"
    a down smile "I'd rather make time for you."
    #emote: blush
    t up talk "...Pfft. Stop it."
    t up smile "{nw}"
    a up smile "Hehe..."

    hide taylor
    with dissolve
    $ config.side_image_tag = ""

    scene black
    with fadee
    an "Taylor and I stayed together in her room, simply enjoying each other's company."
    an "Things don't feel any different. I mean, we aren't competing with each other anymore, but we always tried to prop each other up."
    an "I think in the coming days, we'll find new ways to support each other... it's pretty exciting."
    an "I can't wait to see what the future brings."
