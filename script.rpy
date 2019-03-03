# Declare characters used by this game.
define di = Character('Director', color="#fff")
define a = Character('Alice', color="#ee9dc6", image='alice')     #protag
define na = Character('???', color="#fff")
define k = Character('Katja', color="#698fe1")     #producer
define j = Character('Jacque', color="#e19f69")    #host
define m = Character('Mary', color="#b03f3f")      #mary-sue - darkskinned
define t = Character('Taylor', color="#e7cc5a")    #slop
define c = Character('Cherry', color="#e3a7d7")    #pale

define fadee = Fade(1.0, 1.0, 1.0, color="#000")

transform leftt:
    
    xalign 0.30
    yalign 1.0
    
transform centerr:
    
    xalign 0.65
    yalign 1.0
    
transform rightt:
    
    xalign 1.10
    yalign 1.0
    
init python:
    config.side_image_tag = "alice"

# The game starts here.
label start:

    #$ config.side_image_tag = "alice"
    
    $ mary = 1
    $ cherry = 1
    $ taylor = 1
    $ katja = 1
    $ jacque = 1
    $ director = 1
    
    scene stagefar
    with fade

    "Hey, you, get those lights shining. And move those stands over. We can't have the stage band in the way of the screen!"
    "And Intern..."
    "Hey, Intie, look this way!"

    "{i}The director can't be referring to me, right?{/i}"
    
    show d talk
    with Dissolve(0.5)
    
    di "Yeah, I'm talking to you. Now get your ass over here!"
    
    "{i}{cps=45}Uhm... my name is Alice.{/cps} Not Intie. Don't tell me he somehow got that from my rather unglorified pisition as the production crew's intern.{/i}"
    
    a frowntalk "Coming..."
    
    a frown "{i}Here I am, on the set of the {i}Supernova{/i} singing contest, the first project I've been involved in since graduating from a specialized arts school and starting my internship at this production company.{/i}"
    a "{i}When I say my position is unglorified, it really is as it sounds. Move this, carry that, hold the camera cable, escort a big-shot over wherever...{/i}"
    a "{i}...one would think showbiz is all about shiny things and outrageous gossip, but my job is no where close to either... that and it hardly pays for the roof atop my head.{/i}"
    
    show d talk at left
    
    di "How long do you plan on taking, Intie? Get those heels clicking... 1, 2, 1, 2..."
    
    show d smile at left
    
    a "{i}I'm not even wearing heels, sheesh. It's just that I can't exactly jump over all the seats in the audience area to get to the stage. Can't he give me 30 seconds?{/i}"
    
    scene stageclose
    show d smile at left
    with Dissolve(0.5)
    
    a "Here... I... am. What do... what do you want... exactly?"
    
    a "{i}I can't help but sound a little bitter as I pant out those words. The director doesn't seem to care about the jog I had to make to the stage.{/i}"
    a "{i}He has his head turned in another direction as he orders somebody else to set up the speakers before looking back at me.{/i}"
    
    show d talk at left
    
    di "The boss wanted a bottle of water. She's probably in the back with the contestants."
    
    show d smile at left
    
    a "{i}Seriously?! That's why I had to run from the back row seats all the way over here? To fetch the producer a bottle of water that's in the room next to hers? What, does she not have hands and feet?{/i}"
    a "{i}Well, not as though complaining would help. I'm just the little lowly intern, afterall. He'd say I have nothing better to do. Ya right...{/i}"
    
    a "Yes sir. I'll go do that now."
    
    scene black
    with fade
    
    a "{i}Water... water... there we go! You'd think on a singing show the singers would want water instead of caffinated drinks...{/i}"
    a "{i}And here's where the producers should be...!{/i}"
    
    scene makeuproom
    with fade
    
    show m smile at left
    show a shock at right
    with Dissolve(0.5)
    
    a "{i}Seated closest to the door is a dark-skinned girl with this... {/i}cascade{i} of perfect, black hair. She's... she's gorgeous!{/i}"
    a "{i}Those honey eyes are so striking I couldn't stop myself from staring. At least she's too preoccupied with talking to her makeup artist and hair stylist to notice.{/i}"
    
    show m blush at left
    
    na "Not so much blush, please. Oh, and maybe just a little bit of curl on my hair? Only the bottom though. So... you know... it's wavy but not too much?"
    na "Oh, not that curling wand! That one will make my hair {i}too{/i} curly! Can't you find one smaller?! My delicate hair can only handle the low heat setting by the way, but most designer wands come with that."
    
    show m frown at left
    with hpunch
    
    na "Are you kidding me?! That's a {i}straightener{/i} you idiot! I want my hair curled, not flat-ironed! Ugh, send in the other team of stylists! They at least might be able to salvage the mess you've made."
    
    a "{i}Wow, but that attitude... If my first impression of her were glass, it would've shattered into a billion pieces and now lie littered beneath my feet.{/i}"
    a "{i}The lilt and tone in her voice is priceless. Maybe there is a perk of being sent way over here just for the producer.{/i}"
    
    na "No, no, no! You've gotta color Cherry's cheeks more! Here, gimme that. I'll rescue her from that vampire skin."
    
    show c shock at center
    with Dissolve(0.5)
    
    a "{i}The pale girl one of the makeup artists just called \"Cherry\" doesn't look too happy about being rescued, if you can even call it that. In fact, if she could run, she would've probably ran off to the moon.{/i}"
    a "{i}Yet, she seems too shy for that, so she resorts to shrinking into a ball on the opposite side of her chair.{/i}"

    a "{i}Please don't tell me these two are contestants...{/i}"
    
    show g smile at centerr
    show c shock at leftt
    show a shock at rightt
    with Dissolve(0.5)
    
    na "...Why...?"
    
    hide g smile
    hide c shock
    hide l frown
    with Dissolve(0.5)
    
    a "{i}Over on the couch is the only other contestant in the room, a mess that is too into texting to get a stylist to work a miracle on their look.{/i}"
    
    show t frown at center
    show a frown at right
    with Dissolve(0.5)
    
    a "{i}The baggy shirt, the huge-rimmed glasses, the blonde hair that looks worse than mine after sleeping for a whole day... are they actually a contestant?{/i}"
    
    show k frown at left
    with hpunch
    
    k "Will somebody do something about this?!"
    
    a "{i}Oh, great, she must be the boss of this whole thing. I hear her heels actually clicking in her wake as she makes her way over to snatch their phone away, probably until they brush their hair.{/i}"
    
    k "I see that bastard won't answer your texts either..."
    
    a "{i}Wait, so this isn't about Blondie's hair?{/i}"
    
    show t frowntalk at center
    
    na "Adam is not usually like this. I'm worried something might have happened to him."
    
    show t frown at center
    
    a "{i}Boss tosses the phone back to Blondie and literally rolls her eyes.{/i}"
    
    k "And I am mighty worried my wallet is gonna deflate if he doesn't show up soon. What am I gonna fill his showtime with?"
    
    a "{i}At least that's the same- it's always about money with her. Maybe if Blondie colored their hair neon orange and shaved half of it off along a zigzag line she'd be even more pleased.{/i}"
    a "{i}If it's outrageous, viewership goes up. She's the one that makes the big bucks around here, so no one seems to question her logic.{/i}"
    
    na "Did somebody call me~?"
    
    a "{i}That voice... those sparkles... it can only be...!{/i}"
    
    hide t frown
    with Dissolve(0.5)
    
    show j smile at center
    
    a "{i}The host, of course! He floated out of the changing room gracefully in his usual fashion, the attire just as sparkly as always.{/i}"
    a "{i}What's even more sparkly than his jacket is by far his name- Jacque Bellavance. He's not even French, but thought it sounded cool. Of course, the Boss thought it was unique enough to go along with.{/i}"
    
    show j talk at center
    
    j "Oh, my dear Katja, I shall defend your wallet with my life! If it's just filling in for a couple minutes, I can be talking about gelato and I know the audience won't change the channel!"
    
    show j smile at center
    
    k "I'm sure you can blind the audience with just your flashy costume for this episode, but we can't have you filling in for the missing guy forever after. We have an elimination contest here, after all."
    k "It's plastered all over the ads that our grand finale showdown is at the end of the month. With a contestant short, what are we gonna do? Have everybody sing the national anthem and then put on a football game?"
    
    show j talk at center
    
    j "That might not actually be such a bad idea..."
    
    show j smile at center
    
    k "Jacque, please. I'm not in the mood when I can practically feel my bills slip away into nothingness. And I can almost hear that asshole from Teabag TV laughing the rest of his ass off at my misery!"
    
    a "{i}If she's not in the mood for Jacque, the houshold name for \"entertainment\", I don't know if she'd be in the mood for me and her water. Is the director pulling a prank on me or something?{/i}"
    a "{i}I know he hates me, but he can't be thinking of digging me a hole so I'd get fired, right?{/i}"
    
    k "Are you the water-bearer?"
    
    a "{i}The boss suddenly turns to me and points at the water bottle in my hands. Water-bearer... so I'm now relegated to the humble post of water-bearer...{/i}"
    
    show a sing at right
    
    a "Yes... Ah, yes Ma'am!"
    
    show a frown at right
    
    a "{i}She takes the bottle from me and seems about to turn away until she stops and looks me top to bottom over again.{/i}"
    
    k "You have a pretty face, don't you?"
    
    show a sing at right
    
    a "Uhm... thank you?"
    
    show a cute at right
    
    k "Jacque, who is this girl?"
    
    a "{i}It shouldn't be a surprise that the producer doesn't know me. But damn, she could've asked me the question directly, right?{/i}"
    
    show j talk at center
    
    j "I don't know either. A stray cat, perhaps?"
    
    show j smile at center
    
    a "{i}Now that's just cold. And I used to watch the silly children's quiz shows you hosted, too!{/i}"
    
    show a sing at right
    
    a "I am Alice. I am the new intern, Ma'am."
    
    show a frown at right
    
    k "So she {i}is{/i} a stray cat. Or kitten."
    
    a "{i}Please, dig me a hole and let me rest in peace. Reality is too harsh to bear.{/i}"
    
    k "You think she can sing?"
    
    show a sing at right
    
    a "No, I can't."
    
    show a frown at right
    show j talk at center
    
    j "Don't we take interns from the Presley School of Arts? They have a really good music program, don't they?"
    
    show a sing at right
    show j smile at center
    
    a "But I wasn't enrolled in that program..."
    
    show a frown at right
    
    k "So that means she {i}can{/i} sing. Tracy, make her presentable. Rob, tell her what to do on stage. We're going live in thirty, understand?"
    
    show a shock at right    
    
    a "{i}Who's grabbing my arm-? Why is Tracy making me sit in this chair--?!{/i}"
    
    hide k frown at left
    hide j smile at center
    show a shock at center
    with Dissolve(0.5)
    
    a "{i}Boss is already out the door, and Jacque has his back turned, focusing on the script. Did that just--{/i}"
    
    a "Wait! I really can't sing! I seriously can't do it to save my life!"
    
    scene black
    with fadee
    
    j "Ladies and Gentlemen..."
    
    scene stagefar
    with fade
    
    show j talk
    with Dissolve(0.5)
    
    j "Welcome to {i}Supernova{/i}, the brand new, not-so-average singing contest show hosted by your not-so-average host, Jaaaacque Belleeeeeevance~!"
    
    j "Thank you, thank you, you are all so kind. I shall ensure you, our esteemed audience, the most blood-boiling, heart-wrenching viewing experience of the month as you journey with our contestants."
    j "Now, without further ado, let's introduce our first contestant, Maryyyy Vissssswanathaaaan!"
    
    show j smile
    
    hide j smile
    show m smile
    with Dissolve(0.5)
    
    a "{i}The dark-skinned girl from before... I guess she's up first. Good thing too, because I can't stop shaking! How did I get roped into this?!{/i}"
    
    show m sing
    
    a "{i}She, of course, got every note perfect... I'd be locked in a trance by the music if I wasn't about to be pushed on stage next. There's no way I can do that! I'd look like a little kid singing Mary Had a Little Lamb!{/i}"
    
    show m smile
    
    hide m smile
    show j talk
    with Dissolve(0.5)
    
    j "If you think that’s all we have to deliver, you’re wrong! Let’s now listen to our second contestant’s self-selection: Mary Had a Little Lamb. Welcome, Raisa Chereeenkooov!"
    
    show j smile
    
    hide j smile
    show c cute
    with Dissolve(0.5)
    
    a "{i}Are you kidding me? I don't even get the comfort of singing a damn nursery rhyme?{/i}"
    
    show c sing
    
    a "{i}Cherry goes on to deliver the most amazing performance of Mary Had a Little Lamb I’ve ever heard.  Like seriously... how can she make it sound like a masterpiece on the simple love between child and lamb?{/i}"
    a "{i}Oh gosh, and the Boss is eating it up! ...Is that a handkerchief in her hand?{/i}"
    
    hide c sing
    show k smile at left
    show a frown at right
    with Dissolve(0.5)    
    
    k "She's... worthy of my pre\U+017Eganka..."
    
    a "I... I'm sorry, Boss, but what is pre\U+017Eganka?"
    
    k "You have much to learn, Child, if you don't know about pre\U+017Eganka. It's the most delicious soup in the world."
    
    a "{i}So Cherry is worthy of soup? Wait, is her name Cherry? That’s what her friend called her, right? But Jacque said it’s Raisin.{/i}"
    a "{i}No...that can’t be right. Cherries and raisins? That sounds like fruit toppings on a bowl of cereal!{/i}"
    
    hide k smile
    hide a frown
    show j talk
    with Dissolve(0.5)
    
    j "And now we have our third contestant, a net musician with perfect nerdy charm. Taylor Warren, the stage is now yours."
    
    show j smile
    
    hide j smile
    show t frown
    with Dissolve(0.5)
    
    a "{i}The light dims, the keyboard’s notes sound between gentle strums of guitar. The audience is captured, their glow sticks waving with the rhythm of the melody.{/i}"
    
    show t sing
    
    a "{i}Taylor’s thin voice begins the main theme. There’s a subtle shaking, corresponding with the lyrics of how humanity is so small and fragile. But that’s not to say his singing is weak. It’s really the contrary.{/i}"
    a "{i}I may not be an expert, but I know it takes a lot of skill to sound each note with such accuracy, control the volume so precisely that each word comes clear and penetrates the audience, but doesn’t overwhelm.{/i}"
    
    hide t sing
    show a frown at right
    show k smile at left
    with Dissolve(0.5)

    show a frowntalk at right

    a "I... really can't do it, Boss."
    
    k "You're in the showbiz. There's only one thing you can't do: say you can't do anything."
    
    a "But I'm not trying to be a star."
    
    k "Silly. You enter the entertainment industry without the dream of shining on-stage? Ridiculous!"
    
    a "{i}I don’t want to argue with Boss about this. She won’t understand.{/i}"
    
    k "You gonna delude yourself into thinking you’re satisfied running errands backstage? Suit yourself. I’m not your councillor."
    k "But let me tell ya this - you miss this chance? You won’t get another one. The world doesn’t stop spinning so you can be absorbed in your self-pity."
    k "You think you aren’t good enough for this? Who gives. Sitting here thinking ain’t gonna make you better. Go out there and just do whatever you can."
    k "If you suck, a producer somewhere might still spot your comedic talents. Not everybody can pull off an epic failure, ya know?"
    
    a "{i}I... I can't actually be smiling at this, right?{/i}"
    a "{i}But I am. Damn.{/i}"
    
    a "I'll try my best."
    
    k "That’s my kid. Now go earn me a wad of cash. I don’t honor just anybody with that opportunity any day!"
    
    hide a frown
    hide k smile
    show j talk
    with Dissolve(0.5)
    
    j "And now, let me introduce our last contestant, a recent graduate from the Presley School of Arts, humble intern working diligently on tasks big and small. She has a dream. To sing here for you. Today, she’ll fulfill it. Welcome, Alice Carroll."
    
    scene stageclose
    with Dissolve(0.5)
    
    show a cute
    with Dissolve(0.5)
    
    a "{i}I step onto the stage. The lights are so blinding, but when I stare out into the audience below, all is dark. It’s a bit intimidating until the squint of my eyes brings me a clearer view of the front row, then those behind them, and those behind them yet.{/i}"
    a "{i}They’re all watching me. The teenage lovebirds, smiling seniors, parents with toddlers on their laps...{/i}"
    a "{i}For a second, I thought I’d stop breathing. But once the intro of my favorite song cues my first note, I sing.{/i}"
    a "{i}Completed my dream, Jacque said.{/i}"
    a "{i}Yeah, he may be right. Boss may be right. I only didn’t dare admit it.{/i}"
    a "{i}Who enters this industry without at least the slightest sliver of hope that we’d one day capture the crowd’s attention?{/i}"
    a "{i}The audience members below aren’t the only ones watching. There are thousands, if not millions more watching behind television screens.{/i}"
    a "{i}Just the thought that my voice is being projected from so many speakers nationwide is making me warm inside.{/i}"
    a "{i}I can't disappoint them.{/i}"
    a "{i}I may not have long, but with what little screen time I have been given, I will make it count!{/i}"
    
########################## END OPENING SCENE #################################

    scene black

    a "{i}After the show, we were herded onto a bus and shipped to a gigantic building on the city’s suburbs. At first, I thought it was a shopping centre. But that’s just the ground floor. The upper floors are all part of a huge private residence.{/i}"
    a "{i}Is this real silk for curtains? No, the actual question should be is this real silk beneath my feet!? I can probably wear this rug as an exotic wedding dress and all my guests would be singing praises to its beauty!{/i}"
    a "{i}And the faint scent coming from that cabinet in the corner...that’s agarwood, right? It’s now a threatened species, so there’s no way you can acquire such a big piece for furniture. The cabinet must then be a legit antique!{/i}"
    a "{i}Holy shit...this is too much. My head hurts just thinking over how many digits went into the cost for the furnishings.{/i}"
    
    scene fountainafternoon
    with fade
    
    show k smile
    with Dissolve(0.5)
    
    k "Alright guys, here’s the place you’ll be staying in for the next month. Learn all you can from our teachers and prepare yourself to rock the stage. You’ll be fighting for a chance to stay on next week’s episode."
    
    a "{i}Boss' voice shakes me back to reality.{/i}"
    
    show k smile at left
    show a shock at right
    with Dissolve(0.5)
    
    a "Wait, are we going to be living here?"
    
    k "Of course. Haven’t you read the contest description? Point is, you’ll use the chance to learn from each other, learn from our teachers, and bring the competition up a notch. It’s all about putting on the best show for your audience."
    
    a "{i}And make her the most money...{/i}"
    a "{i}No, that’s not what I should be thinking right now. There’s a more immediate problem here!{/i}"
    
    show a frown at right
    
    a "I have read the contest description and I know about this, but...(whispers) I’m not a real contestant, right? I should’ve been eliminated today, right?"
    
    k "You say you’ve read the contest description? Today isn’t even the elimination round. And even after getting eliminated, you would still stay here till the finale is aired."
    k "It’s an opportunity to further yourself and help others. Consider it a generous offer from our production team."
    
    a "{i}No, I’m sure it’s because you want to stir shit between the contestants, then take it to the media as a cheap way for promoting the show!{/i}"
    
    a "Do I really need to be a part of this?"
    
    k "The question should be: do you want to be a part of this? And the answer is yes. There’s no other way."
    
    a "{i}Like I can say no. It’s either stay or quit my job. Who wouldn’t pick this luxurious mansion over a homeless shelter?{/i}"
    
    scene hallday
    with fade
    
    show j smile
    with Dissolve(0.5)
    
    a "{i}Jacque shows us around the house for a tour along with the other contestants. This place is so huge, so lavish that I feel like I’ve been dumped into some sort of wonderland. I really didn’t drop down a rabbit hole, did I?{/i}"
    
    show j talk
    with Dissolve(0.5)
    
    j "So this is the lounge. Designer chairs and an ultra-high-definition TV. Love the surround sound system too. Great place to relax in good company."
    
    show j smile
    
    a "{i}I may be the one most at shock about this turn of events, but I see that some of the others are a little surprised too. Sure, they expected the mansion, but the scale of things probably exceeds their wildest imagination.{/i}"
    a "{i}Taylor has slowed to take in everything, his mouth gaping a little. Only Mary seems nonchalant, walking with crossed arms and closed eyes for dramatic effect.{/i}"
    
    hide j smile
    show m frown at right
    show c cute at center
    with Dissolve(0.5)
    
    m "I suppose this house meets my standards... barely."
    
    a "{i}Cherry seems as awe-struck as I am. If not for Lis towing her along, she’d still be stuck gawking outside the door.{/i}"
    
    hide m frown at right
    show a smile at right
    show c shock at center
    with Dissolve(0.5)
    
    c "You can farm pigs here..."
    
    show a shock at right
    
    a "...Pigs? Really?"
    a "I mean, this place is so big it'd fit a herd of buffalos."
    
    c "{i}Sus scrofa domesticus{/i}, cute to look at and delicious to eat. There’s nothing more I’d like in life than to open a pig farm."
    
    show a frown at right
    
    a "{i}I don’t see the logic, but I’m pretty sure she got that line from an anime or something...{/i}"
    
    l "So Jacque, do you own the house?"
    
    hide c shock at center
    show j talk at center
    with Dissolve(0.5)
    
    j "If I did, I’d already have retired, hahaha... I have been living here for a while though. Perks of working for this company. The director is on the ground floor next to the shopping district, and the producer is at the penthouse overlooking the rooftop garden."
    
    scene dinnerafternoon
    with fade
    
    show j smile at left
    show m frown at right
    with Dissolve(0.5)
    
    show j talk at left
    
    j "So this is the dining hall..."
    
    show j smile at left
    
    c "A real chandelier above the dining table. Wow!"
    
    m "Of course it's a real chandelier. Are there fake chandeliers?"
    
    hide m frown at right
    show a smile at right
    show t frowntalk at center
    with Dissolve(0.5)
    
    t "I doubt I can find the appetite for food when I can practically taste the wasted cash that went into this room."
    
    show t frown at center
    
    a "{i}Sure, Taylor sorta spoils the mood, but I’m inclined to support him. Imagine eating instant ramen on this table long as my bedroom back home. I’d feel ashamed! {/i}"
    
    show j talk at left
    
    j "You’ll get used to the furnishings, Taylor. Just sink into one of those chairs and you wouldn’t want to get up. The lighting makes the food look sparkly. Oh, and wine. Yes. Clear and deep but shining like rubies. Ooh la la...c’est la vie."
    
    show j smile at left
    
    a "{i}Please, Jacque. Don’t make a fool out of yourself with your half-assed français.{/i}"
    
    show j talk at left
    
    j "And of course, here is your training ground. Fully sound-proof. You can sing to your heart’s content and you wouldn’t startle a fly in the hallway, not that there would be flies here, Dear Lord."
    j "Practise with your own instruments if you like, or if you’re feeling ambitious, try out the ones we have here."
    j "Repair parts and services are also available in the shop down the hall. Everything’s set for you to up your skills in no time."
    
    scene workoutday
    with fade
    
    show j talk at left
    show m frown at right
    with Dissolve(0.5)
    
    j "As you should all know, your faces and bodies are no less important than your voices. You’ve gotta keep up your appearances when you’re working in this business. Here’s the place to keep fit, with certified instructors to aid your training everyday, 9 to 5."
    
    show j smile at left
    
    c "What is this thing?"
    
    m "It's a skiing simulator. Is it really such a big deal?"
    
    hide m frown at right
    show t frowntalk at right
    with Dissolve(0.5)
    
    t "A big deal of idiocy, that’s what. I don’t see it simulating the crisp scent of winter pine and soft powder beneath my boots."
    
    show t frown at right
    
    a "{i}Cherry isn’t listening though. While we are having this conversation, she has already coerced Grant to teach her how to use the machine.{/i}"
    
    hide t frown
    show c shock at right
    with Dissolve(0.5)
    
    c "This is amazing! The very peak of engineering science!"
    
    m "You said that about the lawn mower."
    
    a "{i}I rest my face in my palms. I don’t know if I’m overwhelmed by the sheer extravagance of everything, or is it just my companions’ absurdity.{/i}"
    
    hide c shock at right
    show j talk at left
    show a smile at right
    with Dissolve(0.5)
    
    j "For those who enjoy water sports, there are pools adjacent to this room, one of which is equipped with a wave generator."
    
    show j smile at left
    show a shock at right
    
    a "Pools? Plural?"
    
    show j talk at left
    
    j "Why, yes. Do you perhaps need a baby pool?"
    
    show j smile at left
    
    a "I know how to swim, thank you very much."
    
    show j talk at left
    show a frown at right
    
    j "So those are some of the features we have in this mansion. It’d take too much time to walk you through all of them, so feel free to explore on your own."
    j "Now I’m sure you’re all tired after everything you’ve done today. Let me show you to your rooms."
    
    scene bedalicenight
    with fade
    
    show a cute
    with Dissolve(0.5)
    
    a "{i}Jacque is right- I am tired. Probably the most tired of everybody. Afterall, I’m not even supposed to be here!{/i}"
    a "{i}I guess I’ll leave a text for Ma to make sure she knows I’ll be living here for the month. Don’t want her to visit my apartment only to find that I’m not even there.{/i}"
    a "{i}Should probably ask her to do me the favour of clearing out the fridge too. I don’t want to go home next month to the odor of rotting cabbages.{/i}"
    a "{i}I lie down on the oversized bed with overly-fluffy pillows probably filled with the finest of feathers. I was about to complain how my salary can’t even afford the damn sheets, but the comfort lulls me to sleep before I can formulate the sentence in my head...{/i}"
    
    with fade
    
    $ day = 1
    
    jump whatday
    
    
    
    
    
    
    
    
        

    return
