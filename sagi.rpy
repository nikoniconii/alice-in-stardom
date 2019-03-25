#
# https://docs.google.com/spreadsheets/d/1DYo0ud8CJTObTpO89y-92ViCvc2vqX5KH3RR3O4uofY/edit#gid=0
# https://docs.google.com/document/d/1Rnl2qAMK_aeXaygW7lrQx3aFfnbQwbM9Xy8BLyxDlPI/edit#heading=h.dl77jqh3pa3q
#

label night1:
    scene bedalicenight
    with fade

    $ config.side_image_tag = "alice"

    a "...Nn."

    $ config.side_image_tag = ""

    ann "{i}Stirring awake in the middle of the night, I come to a realization.{/i}"
    ann "{i}I'm, like, super thirsty. My throat's all dry too.{/i}"
    ann "{i}Maybe I'll go get a glass of water. Ehh, but the dining hall is kinda far just for water.{/i}"
    ann "{i}...Eh. I'm already awake, and if I try to go back to sleep now, I'll just think about my intense thirst.{/i}"
    ann "{i}Slipping into a robe, I get ready for the trek across the studio lot.{/i}"

    scene fountainnight
    with fade
    ann "{i}...It's actually a little spooky, coming out this late at night. A chilly breeze cuts through my clothes with ease.{/i}"
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

    #sfx footsteps

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

    scene fountainnight
    with fade
    scene bedalicenight
    with fade
    scene black
    with fade
    ann "{i}I book it back to my trailer, lock all the doors and windows, and throw the covers over my head.{/i}"
    ann "{i}I had a pretty restless night... now I was thirsty AND terrified. Maybe I should've told someone about the robber??{/i}"
    ann "{i}...Security will be on top of it, surely...{/i}"

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
        yalign 0.35
    with dissolve

    $ config.side_image_tag = ""
    ann "{i}She had a plate out on the counter, with a sandwich stacked almost a foot tall! It looked like she packed an entire deli in the thing.{/i}"
    ann "{i}...It looked really good, too. I inched forward slightly to get a better look.{/i}"
    ann "{i}It was in that moment that our eyes met. Her hands stopped as she was buttering up one of the slices of rye.{/i}"

    show mary frowntalk
    m "Alice!?"
    ann "{i}Ohhh crap.{/i}"
    ann "{i}Gotta think fast gotta think fast... I came here for a purpose...{/i}"

    $ config.side_image_tag = "alice"
    a "...Damn, that looks really good. Can you make me one?"

    show mary down frowntalk
    m "WHAT!? NO! What am I, your personal maid!?"
    a frown "No, that's not what I meant! I just, since you're here and all-"

    show mary down frown
    m "Get out! GET. OUT!"
    a down frown "O-okay! Just let me get my water..."

    $ config.side_image_tag = ""
    ann "{i}I hurry over to the fridge, reaching for a few bottles.{/i}"

    $ config.side_image_tag = "alice"
    a "Damn, this is the premium stuff they bottle in Switzerland..."

    show mary down frowntalk
    m frowntalk "WOULD YOU STOP GAWKING AND JUST GET OUT!"

    a frown "Fine, fine! Not like we're supposed to be in here anyway..."

    hide mary
    with dissolve
    $ config.side_image_tag = ""
    ann "{i}Under considerable duress, I make a point of getting out of there as quickly as possible.{/i}"

    scene black
    with fade


########################################################



label maryafterelim:

    scene bedaliceday
    with dissolve

    $ config.side_image_tag = ""

    ann "{i}I think I'll see what Mary's up to. I haven't seen a lot of her since she got eliminated.{/i}"
    ann "{i}Hoo, that was a stressful show.  Things are really coming down to the wire now.{/i}"
    ann "{i}In the back of my mind, I wonder what Mary's gonna do now? They didn't kick her out of her, so what gives?{/i}"

    scene fountainday
    with fade

    ann "{i}She doesn't come to group practices anymore. Sometimes I see her rehearsing by herself, but... are we all just supposed to move forward?{/i}"
    ann "{i}These questions all ring in the back of my head as I stand in front of Mary's trailer.{/i}"

    #sfx knock knock

    ann "{i}I knock at her door, hoping for a response.{/i}"
    ann "{i}...{/i}"
    ann "{i}... ...{/i}"

    $ config.side_image_tag = "alice"
    a frown "...?"

    $ config.side_image_tag = ""
    ann "{i}Quietly, I listen closely. Inside, I could hear her voice. She was murmuring to someone.{/i}"

    #sfx: louder knock
    ann "{i}So she is in there! I knock again with a little more oomph.{/i}"

    m "Can you sit still for {i}one second!?{/i} I'm on the phone!"

    $ config.side_image_tag = "alice"
    a frown "Ah!"

    $ config.side_image_tag = ""
    ann "{i}I made out an exasperated sigh from the other side of the door.{/i}"
    ann "{i}Well, Mary seemed to be... well, pretty much the same as usual. That was oddly relieving.{/i}"
    ann "{i}And I already announced my presence, so... all I could do was awkwardly stand there until Mary summoned for me.{/i}"

    #sfx door open
    ann "{i}Thankfully, it wasn't long until the door swung open.{/i}"

    m "Come in."

    "With that low-spoken invitation, I let myself in."

    scene bedmaryday
    with fade

    show mary unsure frown at center:
        zoom 1.4
        yalign 0.35
    with dissolve

    m "Tch... sorry for making you wait. I was on the phone with my agent."

    $ config.side_image_tag = "alice"
    a down frown "Hi, Mary, um... how are you feeling?"

    show mary down frown
    m "...? What does that mean? Don't tell me you came over for pity."

    a frown "Well, since you got eliminated, we don't really see you a lot, so I wondered..."

    show mary down
    m "You wondered what?? That I'd be sitting in here all day crying my eyes out? {i}Please.{/i}"
    m "You gotta give me a little bit of credit here..."

    a down "Th-that's not what I meant, I..."
    extend "I wanted to see you again, that's all!"

    show mary frown
    m "...Heh. So bloody sentimental."

    $ config.side_image_tag = ""
    ann "{i}She scoffed, folding her arms. I feel like she was judging me.{/i}"

    m "Don't worry your pretty little head. The producer's keeping me around to talk to fans."
    m "And my agent's already lined me up with a deal to produce a solo album. I'd say I'm in good shape."

    $ config.side_image_tag = "alice"
    a "Oh! That's so great!! Let me know when it drops so I can buy, like, ten copies!"

    show mary
    m "Only ten? You wound me, Alice."

    $ config.side_image_tag = ""
    ann "{i}We share a laugh. Mary seemed to be in high spirits.{/i}"

    $ config.side_image_tag = "alice"
    a "Aaaaah, you're gonna be an idol after all..."

    show mary down
    m "Well, I wasn't about to go back and live on Daddy's credit cards all over again."
    m "And it's not like life's just over when you lose. You just go and do something else, yeah?"

    show mary
    m "...I mean, I'm famous now, and I got fans, so I figure I made it out okay."

    a "...Yeah. You're right."
    a down "Honestly, I was really worried about what would happen if I lost. I don't really have a plan, you know, so...."

    m "You need an agent. I could get you in with my guy, she's fantastic, absolutely cutthroat!~"

    a frown "Eh? ...Cutthroat how?"

    show mary down
    m "She's a master at power plays, like... like making sure you only get the blue M&Ms, or so help them-"

    a frowntalk "What, seriously? Is that one of your requests?"
    a frown "{nw}"

    show mary
    m "Me? Pfft, no, I'm not crazy. They're all the same."

    a "...Right."

    $ config.side_image_tag = ""
    ann "{i}Mary and I hung out for a few hours...{/i}"

    scene black
    with fade
