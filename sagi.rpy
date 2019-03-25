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

    scene trailersnight
    with fade
    ann "{i}...It's actually a little spooky, coming out this late at night. A chilly breeze cuts through my clothes with ease.{/i}"
    ann "{i}I guess there's still security guards mulling about, but it's not much comfort when you're out here alone.{/i}"
    ann "{i}Well, the dining hall isn't far. I'll just grab a water battle and head back. Shouldn't be more than five minutes.{/i}"

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
