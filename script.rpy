# Declare characters used by this game.
define di = Character('Director', color="#fff", image='director')
define a = Character('Alice', color="#ee9dc6", image='alice')     #protag
define an = Character(' ', color="#ee9dc6", image='alice', what_prefix='{i}', what_suffix='{/i}')     #protag nar
define ann = Character(' ', color="#ee9dc6", image='alice')     #protag nar
define na = Character('???', color="#fff")
define k = Character('Katja', color="#e74969", image='katja')     #producer
define j = Character('Jacques', color="#e19f69", image='jacques')    #host
define m = Character('Mary', color="#c899c9", image='mary')      #mary-sue - darkskinned
define t = Character('Taylor', color="#aac9e5", image='taylor')    #slop
define c = Character('Cherry', color="#e5bdf6", image='cherry')    #pale


define ma = Character('Makeup Artist', color="#fff")
define hs = Character('Hair Stylist', color="#fff")
define p = Character('Paul', color="#fff")


#character labels for label mary3: Diehard Fan = DF, Obsessed Fan = OF, Super Fan = SF
define of = Character('Obsessed Fan', color="#fff")
define df = Character('Diehard Fan', color="#fff")
define sf = Character('Super Fan', color="#fff")


define fadee = Fade(1.0, 1.0, 1.0, color="#000")
define whitefade = Fade(1.0, 1.0, 1.0, color="#fff")

transform leftt:

    xalign 0.25
    yalign 1.0

transform centerr:

    xalign 0.65
    yalign 1.0

transform rightt:

    xalign 0.80
    yalign 1.0

init python:
    config.side_image_tag = "alice"

# The game starts here.
label start:

    #$ config.side_image_tag = "alice"

    $ mary_stat = 1
    $ cherry_stat = 1
    $ taylor_stat = 1
    $ katja_stat = 1
    $ jacque_stat = 1
    $ director_stat = 1

    scene stagefar
    with fade

    "Hey, you, get those lights shining. And move those stands over. We can't have the stage band in the way of the screen!"
    "And Intern..."
    "Hey, Intie, look this way!"

    "{i}The director can't be referring to me, right?{/i}"

    show director talk
    with Dissolve(0.5)

    di "Yeah, I'm talking to you. Now get your ass over here!"

    show director smile

    "{i}{cps=45}Uhm... my name is Alice.{/cps} Not Intie. Don't tell me he somehow got that from my rather unglorified position as the production crew's intern.{/i}"

    a frowntalk "Coming..."

    ann frown "{i}Here I am, on the set of the {i}Supernova{/i} singing contest, the first project I've been involved in since graduating from a specialized arts school and starting my internship at this production company.{/i}"
    ann "{i}When I say my position is unglorified, it really is as it sounds. Move this, carry that, hold the camera cable, escort a big-shot over wherever...{/i}"
    ann "{i}...one would think showbiz is all about shiny things and outrageous gossip, but my job is no where close to either... that and it hardly pays for the roof atop my head.{/i}"

    di "How long do you plan on taking, Intie? Get those heels clicking... 1, 2, 1, 2..."

    show director smile

    ann "{i}I'm not even wearing heels, sheesh. It's just that I can't exactly jump over all the seats in the audience area to get to the stage. Can't he give me 30 seconds?{/i}"

    scene stageclose
    show director smile at center:
        zoom 1.2
        yalign 0.6
    with Dissolve(0.5)

    a talk "Here... I... am. What do... what do you want... exactly?"

    ann smile "{i}I can't help but sound a little bitter as I pant out those words. The director doesn't seem to care about the jog I had to make to the stage.{/i}"
    ann "{i}He has his head turned in another direction as he orders somebody else to set up the speakers before looking back at me.{/i}"

    di talk "The boss wanted a bottle of water. She's probably in the back with the contestants."

    show director smile

    ann down frown "{i}Seriously?! That's why I had to run from the back row seats all the way over here? To fetch the producer a bottle of water that's in the room next to hers? What, does she not have hands and feet?{/i}"
    ann "{i}Well, not as though complaining would help. I'm just the little lowly intern, afterall. He'd say I have nothing better to do. Ya right...{/i}"

    a talk "Yes sir. I'll go do that now."

    an "{nw}"

    scene black
    with fade

    $ config.side_image_tag = ""

    ann "{i}Water... water... there we go! You'd think on a singing show the singers would want water instead of caffeinated drinks...{/i}"
    ann "{i}And here's where the producers should be...!{/i}"

    scene makeuproom
    with fade

    $ config.side_image_tag = "alice"

    show mary smile at center
    with Dissolve(0.5)

    ann "{i}Seated closest to the door is a dark-skinned girl with this... {/i}cascade{i} of perfect, black hair. She's... she's gorgeous!{/i}"
    ann "{i}Those eyes are so striking I couldn't stop myself from staring. At least she's too preoccupied with talking to her makeup artist and hair stylist to notice.{/i}"

    show mary up frowntalk

    na "Not so much blush, please. Oh, and maybe just a little bit of curl on my hair? Only the bottom though. So... you know... it's wavy but not too much?"
    na "Oh, not that curling wand! That one will make my hair {i}too{/i} curly! Can't you find one smaller?! My delicate hair can only handle the low heat setting by the way, but most designer wands come with that."

    show mary down
    with hpunch

    na "Are you kidding me?! That's a {i}straightener{/i} you idiot! I want my hair curled, not flat-ironed! Ugh, send in the other team of stylists! They at least might be able to salvage the mess you've made."

    show mary frown

    ann "{i}Wow, but that attitude... If my first impression of her were glass, it would've shattered into a billion pieces and now lie littered beneath my feet.{/i}"
    ann "{i}The lilt and tone in her voice is priceless. Maybe there is a perk of being sent way over here just for the producer.{/i}"

    hide mary
    with dissolve

    na "No, no, no! You've gotta color Cherry's cheeks more! Here, gimme that. I'll rescue her from that vampire skin."

    show cherry down frowntalk at center
    with Dissolve(0.5)

    ann "{i}The pale girl one of the makeup artists just called \"Cherry\" doesn't look too happy about being rescued, if you can even call it that. In fact, if she could run, she would've probably ran off to the moon.{/i}"
    ann "{i}Yet, she seems too shy for that, so she resorts to shrinking into a ball on the opposite side of her chair.{/i}"

    ann "{i}Please don't tell me these two are contestants...{/i}"

    hide cherry
    with dissolve

    na "...Why...?"

    ann "{i}Over on the couch is the only other contestant in the room, a mess that is too into texting to get a stylist to work a miracle on their look.{/i}"

    show taylor frown at center
    with Dissolve(0.5)

    ann "{i}The baggy shirt, the huge-rimmed glasses, the blonde hair that looks worse than mine after sleeping for a whole day... are they actually a contestant?{/i}"

    show katja frown at leftt
    show taylor at rightt
    with hpunch

    k frowntalk "Will somebody do something about this?!"

    show katja frown

    ann "{i}Oh, great, she must be the boss of this whole thing. I hear her heels actually clicking in her wake as she makes her way over to snatch their phone away, probably until they brush their hair.{/i}"

    k frowntalk "I see that bastard won't answer your texts either..."

    show katja frown

    ann "{i}Wait, so this isn't about Blondie's hair?{/i}"

    show taylor frowntalk

    na "Adam is not usually like this. I'm worried something might have happened to him."

    show taylor frown

    ann "{i}Boss tosses the phone back to Blondie and literally rolls her eyes.{/i}"

    k frowntalk "And I am mighty worried my wallet is gonna deflate if he doesn't show up soon. What am I gonna fill his showtime with?"

    show katja frown

    ann "{i}At least that's the same- it's always about money with her. Maybe if Blondie colored their hair neon orange and shaved half of it off along a zigzag line she'd be even more pleased.{/i}"
    ann "{i}If it's outrageous, viewership goes up. She's the one that makes the big bucks around here, so no one seems to question her logic.{/i}"

    na "Did somebody call me~?"

    ann smile "{i}That voice... those sparkles... it can only be...!{/i}"

    show katja at left with moveinleft

    show taylor at right with moveinright

    show jacques smile at center
    show sparkles1 at center
    show sparkles2 at center
    with dissolve

    ann "{i}The host, of course! He floated out of the changing room gracefully in his usual fashion, the attire just as sparkly as always.{/i}"
    ann "{i}What's even more sparkly than his jacket is by far his name- Jacque Bellavance. He's not even French, but thought it sounded cool. Of course, the Boss thought it was unique enough to go along with.{/i}"

    j talk "Oh, my dear Katja, I shall defend your wallet with my life! If it's just filling in for a couple minutes, I can be talking about gelato and I know the audience won't change the channel!"

    show jacques smile

    k frowntalk "I'm sure you can blind the audience with just your flashy costume for this episode, but we can't have you filling in for the missing guy forever after. We have an elimination contest here, after all."
    k "It's plastered all over the ads that our grand finale showdown is at the end of the month. With a contestant short, what are we gonna do? Have everybody sing the national anthem and then put on a football game?"

    show katja frown

    j talk "That might not actually be such a bad idea..."

    show jacques smile

    k frowntalk "Jacques, please. I'm not in the mood when I can practically feel my bills slip away into nothingness. And I can almost hear that asshole from Teabag TV laughing the rest of his ass off at my misery!"

    show katja frown

    ann "{i}If she's not in the mood for Jacques, the household name for \"entertainment\", I don't know if she'd be in the mood for me and her water.{/i}"
    ann "{i}Is the director pulling a prank on me or something? Even if he hates me, he can't be thinking of digging me a hole so I'd get fired, right?{/i}"

    hide taylor
    hide sparkles1
    hide sparkles2
    with dissolve

    k talk "Are you the water-bearer?"

    show katja frown

    ann "{i}The boss suddenly turns to me and points at the water bottle in my hands. Water-bearer... so I'm now relegated to the humble post of water-bearer...{/i}"

    a talk "Yes... Ah, yes Ma'am!"

    ann smile "{i}She takes the bottle from me and seems about to turn away until she stops and looks me top to bottom over again.{/i}"


    show jacques at right:
        zoom 1.3
        yalign 0.4
    show katja at left:
        zoom 1.3
        yalign 0.4
    with dissolve


    k talk "You have a pretty face, don't you?"

    show katja smile

    a down frowntalk "Uhm... thank you?"

    ann frown "{nw}"

    k talk "Jacque, who is this girl?"

    show katja smile

    ann "{i}It shouldn't be a surprise that the producer doesn't know me. But damn, she could've asked me the question directly, right?{/i}"

    j frowntalk "I don't know either. A stray cat, perhaps?"

    show jacques smile

    ann "{i}Now that's just cold. And I used to watch the silly children's quiz shows you hosted, too!{/i}"

    a up talk "I'm Alice. I'm the new intern, Ma'am."

    ann frown "{nw}"

    k frowntalk "So she {i}is{/i} a stray cat. Or kitten."

    show katja frown

    ann down "{i}Please, dig me a hole and let me rest in peace. Reality is too harsh to bear.{/i}"

    k frowntalk "You think she can sing?"

    show katja frown

    a frowntalk "No, I can't."

    an frown "{nw}"

    j frowntalk "Don't we take interns from the Presley School of Arts? They have a really good music program, don't they?"

    show jacques smile

    a frowntalk "But I wasn't enrolled in that program..."

    a frown "{nw}"

    k talk "So that means she {i}can{/i} sing. Tracy, make her presentable. Rob, tell her what to do on stage. We're going live in thirty, understand?"

    show katja smile

    an "{i}Who's grabbing my arm-? Why is Tracy making me sit in this chair--?!{/i}"

    hide katja
    hide jacques
    with Dissolve(0.5)

    an "{i}Boss is already out the door, and Jacques has his back turned, focusing on the script. Did that just--{/i}"

    a frowntalk "Wait! I really can't sing! I seriously can't do it to save my life!"

    scene black
    with fadee

    $ config.side_image_tag = ""

    j "Ladies and Gentlemen..."

    scene stageonclose
    with fade

    show jacques up smile at center:
        zoom 1.4
        yalign 0.35
    with dissolve

    j talk "Welcome to {i}Supernova{/i}, the brand new, not-so-average singing contest show hosted by your not-so-average host, Jaaaacques Belleeeeeevance~!"

    play sound "applause.mp3" fadeout 0.5

    $ renpy.pause(1.0)

    j "Thank you, thank you, you are all so kind. I shall ensure you, our esteemed audience, the most blood-boiling, heart-wrenching viewing experience of the month as you journey with our contestants."
    j "Now, without further ado, let's introduce our first contestant, Maryyyy Vissssswanathaaaan!"

    show jacques smile

    hide jacques
    with dissolve

    show mary up smile at center:
        zoom 1.35
        yalign 0.45
    with dissolve

    ann "{i}The dark-skinned girl from before... I guess she's up first. Good thing too, because I can't stop shaking! How did I get roped into this?!{/i}"

    hide mary
    with dissolve

    ann "{i}She, of course, got every note perfect... I'd be locked in a trance by the music if I wasn't about to be pushed on stage next. There's no way I can do that! I'd look like a little kid singing Mary Had a Little Lamb!{/i}"

    show jacques talk at center:
        zoom 1.4
        yalign 0.35
    with dissolve

    j "If you think that’s all we have to deliver, you’re wrong! Let’s now listen to our second contestant’s self-selection: Mary Had a Little Lamb. Welcome, Raisa Chereeenkooov!"

    show jacques smile

    hide jacques
    with dissolve

    show cherry up smile at center:
        zoom 1.4
        yalign 0.5
    with dissolve

    ann "{i}Are you kidding me? I don't even get the comfort of singing a damn nursery rhyme?{/i}"

    ann "{i}Cherry goes on to deliver the most amazing performance of Mary Had a Little Lamb I’ve ever heard.  Like seriously... how can she make it sound like a masterpiece on the simple love between child and lamb?{/i}"
    ann "{i}Oh gosh, and the Boss is eating it up! ...Is that a handkerchief in her hand?{/i}"

    hide cherry
    with dissolve

    scene stageonfar
    with dissolve

    $ config.side_image_tag = "alice"

    show katja smile at center
    with dissolve

    k talk "She's... worthy of my pre\u017Eganka..."

    show katja smile

    a up frowntalk "I... I'm sorry, Boss, but what is pre\u017Eganka?"

    a frown "{nw}"

    k talk "You have much to learn, Child, if you don't know about pre\u017Eganka. It's the most delicious soup in the world."

    show katja smile

    ann "{i}So Cherry is worthy of soup? Wait, is her name Cherry? That’s what her friend called her, right? But Jacques said it’s Raisin.{/i}"
    ann "{i}No... that can’t be right. Cherries and raisins? That sounds like fruit toppings on a bowl of cereal!{/i}"

    hide katja smile
    with dissolve

    scene stageonclose
    with dissolve

    $ config.side_image_tag = ""

    show jacques talk at center:
        zoom 1.4
        yalign 0.35
    with Dissolve(0.5)

    j "And now we have our third contestant, a net musician with perfect nerdy charm. Taylor Warren, the stage is now yours."

    show jacques smile

    hide jacques smile
    with dissolve

    show taylor up frown at center:
        zoom 1.35
        yalign 0.5
    with dissolve

    ann "{i}The light dims, the keyboard’s notes sound between gentle strums of guitar. The audience is captured, their glow sticks waving with the rhythm of the melody.{/i}"

    ann "{i}Taylor’s thin voice begins the main theme. There’s a subtle shaking, corresponding with the lyrics of how humanity is so small and fragile. But that’s not to say his singing is weak. It’s really the contrary.{/i}"
    ann "{i}I may not be an expert, but I know it takes a lot of skill to sound each note with such accuracy, control the volume so precisely that each word comes clear and penetrates the audience, but doesn’t overwhelm.{/i}"

    hide taylor
    with dissolve

    scene stageonfar
    with dissolve

    $ config.side_image_tag = "alice"

    show katja smile at center:
        zoom 1.4
        yalign 0.5
    with dissolve

    a down frowntalk "I... really can't do it, Boss."

    a frown "{nw}"

    k talk "You're in the showbiz. There's only one thing you can't do: say you can't do anything."

    show katja smile

    a frowntalk "But I'm not trying to be a star."

    a frown "{nw}"

    k frowntalk "Silly. You enter the entertainment industry without the dream of shining on-stage? Ridiculous!"

    show katja frown

    ann "{i}I don’t think I can argue with Boss about this. She won’t understand.{/i}"

    k frowntalk "You gonna delude yourself into thinking you’re satisfied running errands backstage? Suit yourself. I’m not your counselor."
    k "But let me tell ya this - you miss this chance? You won’t get another one. The world doesn’t stop spinning so you can be absorbed in your self-pity."
    k "You think you aren’t good enough for this? Who gives. Sitting here thinking ain’t gonna make you better. Go out there and just do whatever you can."
    k "If you suck, a producer somewhere might still spot your comedic talents. Not everybody can pull off an epic failure, ya know?"

    show katja smile

    ann "{i}I... I can't actually be smiling at this, right?{/i}"
    ann "{i}But I am. Damn.{/i}"

    a talk "I'll try my best."

    a smile "{nw}"

    k talk "That’s it, my kid. Now go earn me a wad of cash. I don’t honor just anybody with that opportunity any day!"

    show katja smile

    hide katja
    with dissolve

    show jacques talk at center:
        zoom 1.4
        yalign 0.35
    with Dissolve(0.5)

    j "And now, let me introduce our last contestant, a recent graduate from the Presley School of Arts, humble intern working diligently on tasks big and small."
    j "She has a dream. To sing here for you."
    j "Today, she’ll fulfill it."
    j "Welcome, Alice Carroll."

    scene stageonclose
    with Dissolve(0.5)

    $ config.side_image_tag = ""

    ann "{i}I step onto the stage. The lights are so blinding, but when I stare out into the audience below, all is dark.{/i}"
    ann "{i}It’s a bit intimidating until the squint of my eyes brings me a clearer view of the front row, then those behind them, and those behind them yet.{/i}"
    ann "{i}They’re all watching me. The teenage lovebirds, smiling seniors, parents with toddlers on their laps...{/i}"
    ann "{i}For a second, I thought I’d stop breathing. But once the intro of my favorite song cues my first note, I sing.{/i}"

label firstConcert:
    $ quick_menu = False

    call screen firstTry

label firstDone:
    $ quick_menu = True
    $ config.side_image_tag = ""

    show concert1
    with dissolve

    ann "{i}Complete my dream, Jacques said.{/i}"
    ann "{i}Yeah, he may be right. Boss may be right. I only didn’t dare admit it.{/i}"
    ann "{i}Who enters this industry without at least the slightest sliver of hope that we’d one day capture the crowd’s attention?{/i}"
    ann "{i}The audience members below aren’t the only ones watching. There are thousands, if not millions more watching behind television screens.{/i}"
    ann "{i}Just the thought that my voice is being projected from so many speakers nationwide is making me warm inside.{/i}"
    ann "{i}I can't disappoint them.{/i}"
    ann "{i}I may not have long, but with what little screen time I have been given, I will make it count!{/i}"

########################## END OPENING SCENE #################################

    scene black
    with fadee

    $ config.side_image_tag = ""

    ann "{i}After the show, we were herded onto a bus and shipped to a gigantic building on the city’s suburbs.{/i}"
    ann "{i}At first, I thought it was a shopping center. But that’s just the ground floor. The upper floors are all part of a huge private residence.{/i}"
    ann "{i}Is this real silk for curtains? No, the actual question should be is this real silk beneath my feet!? I can probably wear this rug as an exotic wedding dress and all my guests would be singing praises to its beauty!{/i}"
    ann "{i}And the faint scent coming from that cabinet in the corner... that’s agarwood, right?{/i}"
    ann "{i}It’s now a threatened species, so there’s no way you can acquire such a big piece for furniture. The cabinet must then be a legit antique!{/i}"
    ann "{i}Holy shit... this is too much. My head hurts just thinking over how many digits went into the cost for the furnishings.{/i}"

    scene fountainafternoon
    with fade

    $ config.side_image_tag = "alice"

    show katja smile
    with Dissolve(0.5)

    k talk "Alright guys, here’s the place you’ll be staying in for the next month."
    k "Learn all you can from our teachers and prepare yourself to rock the stage. You’ll be fighting for a chance to stay on next week’s episode."

    show katja frown

    ann "{i}Boss' voice shakes me back to reality.{/i}"

    a frowntalk "Wait, are we going to be living here?"

    a frown "{nw}"

    k frowntalk "Of course. Haven’t you read the contest description? Point is, you’ll use the chance to learn from each other, learn from our teachers, and bring the competition up a notch."
    k "It’s all about putting on the best show for your audience."

    show katja frown

    ann "{i}And make her the most money...{/i}"
    ann "{i}No, that’s not what I should be thinking right now. There’s a more immediate problem here!{/i}"

    a frowntalk "I have read the contest description and I know about this, but... {size=20}I’m not a real contestant, right? I should’ve been eliminated today, right?{/size}"

    a frown "{nw}"

    k frowntalk "You say you’ve read the contest description? Today isn’t even the elimination round. Besides, when the other contestants get eliminated, most of them will stay here for a time."
    k talk "It’s an opportunity to further yourself and help others. Consider it a generous offer from our production team."

    show katja smile

    ann "{i}No, I’m sure it’s because you want to stir shit between the contestants, then take it to the media as a cheap way for promoting the show!{/i}"

    a frowntalk "Do I really need to be a part of this?"

    a frown "{nw}"

    k frowntalk "The question should be: do you want to be a part of this? And the answer is yes. There’s no other way."

    show katja frown

    ann "{i}Like I can say no. It’s either stay or quit my job. Who wouldn’t pick this luxurious mansion over a homeless shelter?{/i}"

    scene hallday
    with fade

    show jacques smile
    with Dissolve(0.5)

    ann "{i}Jacque shows us around the house for a tour along with the other contestants. This place is so huge, so lavish that I feel like I’ve been dumped into some sort of wonderland.{/i}"

    j talk "This is the lounge. Designer chairs and an ultra-high-definition TV. Love the surround sound system too. Great place to relax in good company."

    show jacques smile

    ann "{i}I may be the one most at shock about this turn of events, but I see that some of the others are a little surprised too. Sure, they expected the mansion, but the scale of things probably exceeds their wildest imagination.{/i}"
    ann "{i}Taylor has slowed to take in everything, his mouth gaping a little. Only Mary seems nonchalant, walking with crossed arms and closed eyes for dramatic effect.{/i}"

    show jacques at left
    show mary up frown at center
    show cherry up frowntalk at right
    with moveinright

    m frowntalk "I suppose this house meets my standards... barely."

    show mary frown

    ann "{i}Cherry seems as awe-struck as I am. If not for Taylor towing her along, she’d still be stuck gawking outside the door.{/i}"

    c "You can farm pigs here..."

    a frowntalk "...Pigs? Really?"
    a "I mean, this place is so big it'd fit a herd of buffaloes."

    a frown "{nw}"

    c talk "{i}Sus scrofa domesticus{/i}, cute to look at and delicious to eat. There’s nothing more I’d like in life than to open a pig farm."

    show cherry smile

    ann "{i}I don’t see the logic, but I’m pretty sure she got that line from an anime or something...{/i}"

    m frowntalk "So Jacques, do you own the house?"

    show mary frown

    j frowntalk "If I did, I’d already have retired, hahaha... I have been living here for a while though. Perks of working for this company."
    j "The director is on the ground floor next to the shopping district, and the producer is at the penthouse overlooking the rooftop garden."

    show jacques smile

    scene dinnerafternoon
    with fade

    show jacques up smile at left
    show mary up frown at right
    show cherry up frowntalk at center
    with Dissolve(0.5)

    j talk "So, this is the dining hall..."

    show jacques smile

    c "A real chandelier above the dining table. Wow!"

    show cherry smile

    m down frowntalk "Of course it's a real chandelier. Are there fake chandeliers?"

    show mary frown

    hide mary
    with moveoutright

    show taylor up frown at right
    with moveinright

    t frowntalk "I doubt I can find the appetite for food when I can practically taste the wasted cash that went into this room."

    show taylor frown

    ann "{i}Sure, Taylor sorta spoils the mood, but I’m inclined to support them. Imagine eating instant ramen on this table long as my bedroom back home. I’d feel ashamed! {/i}"

    j talk "You’ll get used to the furnishings, Taylor. Just sink into one of those chairs and you wouldn’t want to get up."
    j "The lighting makes the food look sparkly. Oh, and wine. Yes. Clear and deep but shining like rubies. Ooh la la... c’est la vie."

    show jacques smile

    ann frown "{i}Please, Jacques. Don’t make a fool out of yourself with your half-assed français.{/i}"

    scene musicroom
    with fade

    show jacques up smile at center
    with dissolve

    j talk "And of course, here is your training ground. Fully sound-proof. You can sing to your heart’s content and you wouldn’t startle a fly in the hallway, not that there would be flies here, Dear Lord."
    j "Practice with your own instruments if you like, or if you’re feeling ambitious, try out the ones we have here."
    j "Repair parts and services are also available in the shop down the hall. Everything’s set for you to up your skills in no time."

    show jacques smile

    scene workoutday
    with fade

    show jacques up smile at left
    show mary up frown at right
    show cherry up smile at center
    with Dissolve(0.5)

    j talk "As you should all know, your faces and bodies are no less important than your voices. You’ve gotta keep up your appearances when you’re working in this business."
    j "Here’s the place to keep fit, with certified instructors to aid your training everyday, 9 to 5."

    show jacques smile

    c frowntalk "What is this thing?"

    show cherry smile

    m frowntalk "It's a skiing simulator. Is it really such a big deal?"

    show mary frown

    hide jacques
    with moveoutleft

    show taylor up frown at left
    with moveinleft

    t frowntalk "A big deal of idiocy, that’s what. I don’t see it simulating the crisp scent of winter pine and soft powder beneath my boots."

    show taylor frown

    ann "{i}Cherry isn’t listening though. While we are having this conversation, she has already coerced one of the staff members to teach her how to use the machine.{/i}"

    c talk "This is amazing! The very peak of engineering science!"

    show cherry smile

    m unsure frowntalk "You said that about the lawn mower."

    show mary frown

    ann "{i}I rest my face in my palms. I don’t know if I’m overwhelmed by the sheer extravagance of everything, or is it just my companions’ absurdity.{/i}"

    hide cherry with dissolve

    show jacques up smile at center
    with dissolve

    j talk "For those who enjoy water sports, there are pools adjacent to this room, one of which is equipped with a wave generator."

    show jacques smile

    a frowntalk "Pools? Plural?"

    a frown "{nw}"

    j talk "Why, yes. Do you perhaps need a baby pool?"

    show jacques smile

    a frowntalk "I know how to swim, thank you very much."

    a frown "{nw}"

    j talk "So, those are some of the features we have in this mansion. It’d take too much time to walk you through all of them, so feel free to explore on your own."
    j "Now I’m sure you’re all tired after everything you’ve done today. Let me show you to your rooms."

    show jacques smile

    scene bedalicenight
    with fade

    $ config.side_image_tag = ""

    ann "{i}Jacques is right- I am tired. Probably the most tired of everybody. After all, I’m not even supposed to be here!{/i}"
    ann "{i}I guess I’ll leave a text for Ma to make sure she knows I’ll be living here for the month. Don’t want her to visit my apartment only to find that I’m not even there.{/i}"
    ann "{i}Should probably ask her to do me the favor of clearing out the fridge too. I don’t want to go home next month to the odor of rotting cabbages.{/i}"
    ann "{i}I lie down on the over-sized bed with overly-fluffy pillows probably filled with the finest of feathers.{/i}"
    ann "{i}I was about to complain how my salary can’t even afford the damn sheets, but the comfort lulls me to sleep before I can formulate the sentence in my head...{/i}"

    scene black
    with fadee

    $ day = 1



    jump morning1



    return
