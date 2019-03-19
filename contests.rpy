#######################################################################################################################
##############################################                              ###########################################
##############################################          Contest             ###########################################
##############################################                              ###########################################
#######################################################################################################################



########### Contests!!

label week1contest:
    
    scene stage2far
    with fadee

    $ config.side_image_tag = "alice"

    ann summer frown "{i}Another contest already...{/i}"
    
    show jacques up smile at center
    with dissolve
    
    j talk "You look nervous, Kid."
    
    show jacques smile
    
    ann frown "{i}Now that I’m back at the studio, I can’t even fathom how I got past these last few days.{/i}"
 
    a frowntalk "How do you do it, Jacque?"

    a frown "{nw}"
    
    j frowntalk "Do what?"

    show jacques frown
    
    a frowntalk "Be all composed like that. You’re up in front of hundreds of people, and probably millions behind the TV screen!"
    
    a frown "{nw}"
    
    j frowntalk "Didn't you do it last week too?"
    
    show jacques smile
    
    ann "{i}I groan. I need not be reminded.{/i}"
    
    show jacques at leftt with moveinright
    show taylor up frown summer at rightt with moveinright

    t frowntalk "She probably was in shock last week. Didn’t even realize what she was doing."
    
    show taylor frown
    
    a frowntalk "Very funny, Taylor..."

    hide jacques
    hide taylor
    with dissolve
    
    ann frown "{i}But they're probably right. Even when I think back to what I did on-stage, it’s all a blur. I think I sang my favourite song. This week, though, I have to pick from a selection, but I’ve barely heard this song prior to practicing it!{/i}"
    ann "{i}The others are taking this rather calmly though. Cherry is in a corner, giggling at her phone. Mary is arguing over jewellery.{/i}"
    ann "{i}I sigh- might as well get this over with.{/i}"
    ann "{i}To match the summer theme for this week’s contest, I’m wearing a purple crop-top and black shorts. My attire isn’t anything too glaring, but those red heels... they’re so hard to walk in!{/i}"
    
    show mary down frown summer at center:
        zoom 1.4
        yalign 0.5
    with hpunch
    
    m frowntalk frowntalk "You better thank me for catching you, Clumsy!"

    show mary frown
    
    ann down "{i}When I try to walk over to the jewellery and prop counter, I nearly fall face-first onto the linoleum floor. Luckily, Mary manages to steady me with her outstretched arms.{/i}"
    
    a frowntalk "Sorry..."

    a frown "{nw}"
    
    m frowntalk up frowntalk "I didn’t ask for an apology. I asked for a word of gratitude."

    show mary frown

    menu:
        "Thank you, Princess.":
            a talk "Yes, I’m really grateful for your aid, Princess."

            a smile "{nw}"

        "Sure, thanks.":
            a frowntalk "Sure, thanks for catching me."

            a frown "{nw}"
    
    m talk "Better."

    show mary smile
    
    ann "{i}Mary holds my hand and guides me over to the seat beside hers. She’s wearing some platform shoes herself, but looks graceful as a swan while she glides along the floor.{/i}"
        
    a talk "You can pass off as a feetless ghost sliding down the hall, Mary."
    a "I, on the other hand, am like an elephant trying to dance."
    
    a smile "{nw}"
    
    m talk "Crude humor as always, but I like it."
    m frowntalk "Oh, and they do a better dance than you. Trust me."
    
    show mary smile
    
    ann "{i}Has she worked at a circus training elephants? I wouldn’t put it past her to do something super-exotic like that. Then again, Mary is so seemingly rich and pretty and perfect that she probably owns the circus instead.{/i}"
    
    a talk "I trust you, but do you really have to say that?"

    a smile "{nw}"
    
    m frowntalk "If you don’t like it, consider improving."
    
    show mary smile
    
    a frowntalk "Whatever. Heels are a symbol of patriarchy’s oppression of women."
    
    a frown "{nw}"
    
    m frowntalk "Wrong. High-heels have been depicted in Egyptian murals from 3500 BC, worn by the nobility, women and men alike. They were also worn by butchers to walk over animal carcasses."
    m "Persian horse riders from the 9th century also wore heels to help hold their feet in stirrups. If anything, it is your view that you are obliged to wear heels for the viewing pleasure of men that is oppressive."
    m talk "You should embrace heels as a possible fashion choice to make yourself look good, for your own confidence and joy."

    show mary smile
    
    ann "{i}Rich, pretty, perfect, and smart too? Maybe Mary should change her last name to Sue.{/i}"
    
    a frowntalk "Philosophical debates about feminism aside, I just can’t do this. The heels make me sort of lean forward, and I keep feeling as though I’d trip."
    
    a frown "{nw}"

    m talk "That’s because you aren’t confident enough. Say you’re sexy."
    
    show mary smile
    
    ## TODO alice blush 

    a down "What...?"

    a frown "{nw}"
    
    m talk "Just say it."
    
    show mary smile

    show cherry down frown summer at left behind mary:
        zoom 0.98
        xalign -0.05
    show taylor up frown summer at right behind mary:
        zoom 0.98
        xalign 0.25
    with moveinleft
    
    ann "{i}I can feel heat rush into my cheeks, especially when the nearby staff all seem to turn around to look at me right this moment. Even Cherry and Taylor pause what they're doing...{/i}"
    
    a frowntalk "I... I'm... se... sexy?"

    a frown "{nw}"
    
    show director smile at right:
        zoom 1.1
    with moveinright
        
    di talk "Yeah, dream on, Intie. Now get that makeup on and meet me by the stage in ten. All of you too! Hurry up and get your asses moving!"
    
    show director smile

    hide director with moveoutright
    
    hide cherry
    hide taylor
    with moveoutleft
    
    ann "{i}What bad timing. I feel like my head's about to blast apart from embarrassment.{/i}"

    m talk "Now look at yourself in the mirror. What’s that shameful face for?"

    show mary smile
    
    a frowntalk "What do you think? The Director heard me..."
    
    a frown "{i}I want to hide myself under some sand. Shouldn’t have trusted Mary.{/i}"
    
    m down frowntalk "Who cares what he thinks? You are sexy and you know it. Now lift your chin up, arch your back, show your curves, swing that pretty bottom of yours. Move like you own the floor, and I assure you that you won’t fall."
    
    show mary up smile

    a frowntalk "You're asking the impossible. I'm not a model."

    a frown "{nw}"
    
    m talk "Well, I have worked as a model, so I know it isn’t impossible."

    show mary smile
    
    ann up frown "{i}Right. It makes total sense for Mary to be a supermodel. She’s probably also the daughter of a billionaire and can communicate with eight animal species through telepathy.{/i}"
    ann "{i}While I’m musing about such useless things, Mary stands up and walks towards the exit, leaving only a pat on my shoulder.{/i}"
    
    m talk "The show is gonna start soon and I’m up first. You better advance too."

    show mary smile
    
    ann "{i}The arrogant way that Mary is speaking should be irritating, but it’s somewhat comforting to know that someone supports me.{/i}"
    ann "{i}Have I possibly made a friend...?{/i}"
    
    a talk "I promise to try my best."

    a smile "{nw}"
    
    scene stage2close
    with fade

    $ config.side_image_tag = ""

    show jacques up smile at center:
        zoom 1.35
        yalign 0.35
    with dissolve
    
    j talk "Welcome again to your most spectacular idol show of the year, Supernova! I am your host, Jacque Bellavance!"
    j "Last time, we introduced our four contestants. You’ve had the chance to see their unique glory, taken your pick about who will make it to the throne of stardom’s next idol. Now, our contestants will be pitted against each other."
    j "Only the best will remain. One will be eliminated tonight!"
    j "Without further ado, lend your applause to our first contestant, Mary Viswanathan!"

    show jacques smile

    hide jacques with dissolve

    show mary up smile summer at center:
        zoom 1.35
        yalign 0.5
    with dissolve
    
    ann "{i}The bright lights shine down on Mary’s shining black hair. Her dark skin gleams while she waves at the audience, drawing roaring applause.{/i}"
    ann "{i}Charming, cheerful music blares out the speakers and Mary starts dancing along with it, her peach-colored dress whirling with the rhythm.{/i}"
    ann "{i}Though her performance last week was elegant and formal, she completely changed her style today. Her voice is one of joy and life, skipping easily with the beat of drums and cymbals.{/i}"
    ann "{i}She’s smiling wide like the summer sun, absolutely stunning in her radiance. The crowd becomes more excited as the chorus takes her notes higher, their glow sticks pounding the air.{/i}"
    ann "{i}I stare at the scene, only realizing then that I’ve been mouthing the words of her lyrics.{/i}"
    
    t "Captivating."

    hide mary with dissolve

    show jacques up smile at center:
        zoom 1.35
        yalign 0.35
    with dissolve
    
    j talk "Thank you very much for that wonderful performance, Mary."
    j "Let’s see how our next contestant holds up. Raisa Cherenkov, you’re up next!"

    show jacques smile

    hide jacques with dissolve

    show cherry up smile summer at center:
        zoom 1.35
        yalign 0.5
    with dissolve
    
    ann "{i}The simple piano accompaniment rolls through the air with Cherry’s soothing voice. There is also something youthful about her singing.{/i}"
    ann "{i}The song itself is of mid-tempo, soft and delicate, like the raindrops the lyrics describe. Cherry takes these raindrops from the skies, letting them drip onto shallow puddles, rippling lakes, great oceans.{/i}"
    ann "{i}There is both something small and relatable, and something larger and more meaningful in what she expresses.{/i}"
    
    hide cherry with dissolve

    $ config.side_image_tag = "alice"

    a summer smile "{nw}"

    scene stage2far
    with dissolve

    show katja smile at rightt
    show taylor up frown summer at leftt
    with dissolve

    k talk "This girl is really someone special."

    show katja smile
    
    t frowntalk "Her technique can use further polishing, but her talent is undeniable. She can be missing half the notes and most people won’t even notice."
    
    show taylor frown

    a frowntalk "She missed some notes?"

    a frown "{nw}"
    
    t down frowntalk "She sang one of the lines almost completely different from the original."

    show taylor frown
    
    k talk "But if she sounds better, I doubt anybody would care about the original."

    show katja smile
    
    ann "{i}I have never heard this song, so I can’t really comment on it. But seriously? Sounding better than the original?{/i}"
    ann "{i}Is that even possible?{/i}"
    
    k talk "A friend of mine wants to sign the girl into his record company after hearing her Mary had a Little Lamb last week, can you believe it?"
    
    show katja smile

    t frowntalk "If I had the money, I would."

    show taylor frown
    
    ann "{i}To be so good that even Taylor would willingly admit her talents... that’s amazing!{/i}"
    
    k talk "I take it that you aren’t gonna go down without a fight though, Taylor."

    show katja smile
    
    t up frowntalk "I am not fighting. I just think I’m not necessarily less skilled than her."

    show taylor frown
    
    k frowntalk "Oh?"

    show katja frown
    
    t frowntalk "She beats me in potential. I will admit that much. But I am far more experienced."

    show taylor frown
    
    j "Thank you, Raisa. That was beautiful. Next up, we have Taylor Warren."
    
    k talk "Show us what your experience will do for you then."

    show katja smile

    hide katja
    hide taylor
    with dissolve

    scene stage2close
    with dissolve

    $ config.side_image_tag = ""
    
    ann "{i}Taylor sure is no match for Cherry appearance-wise. While both of them went for the floral theme, Cherry matched her rosy wreath with a delicate pink dress, while Taylor just put on the same faded blue t-shirt as last week.{/i}"
    ann "{i}Which one of the stylists let her walk out on stage with a shirt that clashes that horribly with the mult-colored flower ring around her neck?{/i}"
    ann "{i}I suppose her stubborn attitude does give her a unique kind of charisma, though. Once again, she opts for minimal background music while she sings, opening the song with smooth falsetto.{/i}"
    ann "{i}Would it be accurate to call her singing wailing? That would give it a negative connotation, would it? But I mean it in a good way, actually. There is just so much emotion in the way she sings.{/i}"
    ann "{i}But if I were to try to convey such sadness and regret, I would’ve tried for a stronger sound. I would’ve tried to sing my lungs out. Taylor does no such thing.{/i}"
    ann "{i}She has so much control at even pitches difficult for me to reach, switching easily to lower tones for drastic, powerful effects.{/i}"
    ann "{i}The song, originally a summer tune about some generic campus, transforms to a bittersweet, nostalgic kind of sound. The simple, metallic notes are underlain by hints of darkness and remorse.{/i}"
    ann "{i}Why is it that Taylor is always depressed? Why does she want to express this on-stage?{/i}"
    ann "{i}So much I don’t understand, but her voice propels me to try. The more I listen, the more I want to know... I’m being carried away by her message.{/i}"
    ann "{i}The crowd is silent after her performance. She bows and leaves us stunned to our spots.{/i}"

    scene stage2far
    with dissolve

    show katja smile at center:
        zoom 1.3
        yalign 0.4
    with dissolve
    
    $ config.side_image_tag = "alice"

    a summer smile "{nw}"

    k frowntalk "Kitty, you better snap out of it before you get up there."

    show katja frown
    
    a frowntalk "Wh... what!?"

    a frown "{nw}"
    
    k frowntalk "You haven't forgotten that you're up next, right?"

    show katja frown
    
    a "..."
    ann "{i}Shit!{/i}"
    ann "{i}That’s right. This is a contest. I’m not part of the audience. I’m supposed to be a participant!{/i}"
    
    k talk "Don’t look so shocked. Like I said, if you can’t outshine the others, then make the biggest fool out of yourself. A catastrophic failure would have entertainment value too."
    
    show katja smile

    ann "{i}Like I want to be a failure on that level!{/i}"
    
    j "That was certainly a memorable performance, Taylor. Next, we have our last contestant, Alice Carroll."

    hide katja with dissolve

    scene stage2close
    with fade

    $ config.side_image_tag = ""
    
    ann "{i}I don’t even get the chance to practice the first line of my song in my head before I get unceremoniously shoved onto the stage by my smirking boss.{/i}"
    ann "{i}Shit, shit, shit, shit... I’m so not prepared for this!{/i}"
    ann "{i}Oh God, please, somebody, save me!{/i}"

    $ waitTime = 5
    
    call screen week1minigame
    
label week1win:

    $ config.side_image_tag = ""
    
    ann "{i}The musical accompaniment is so plain.{/i}"
    ann "{i}It’s not plain in an absolute sense, but compared to the uniqueness of Cherry and Taylor’s performances, it’s just so common. It’s totally something a regular schoolgirl would sing at a karaoke place with her friends.{/i}"
    ann "{i}But is that necessarily a bad thing?{/i}"
    ann "{i}I have been a regular schoolgirl till just a few months ago. After graduation, I became a regular working-class young adult. I’m just a plain and ordinary girl. Nothing special.{/i}"
    ann "{i}But that’s not something to be ashamed of, right?{/i}"
    ann "{i}I remember watching a show like this on TV. Of course, you’d want to see the superstar in all his glory, singing so brilliantly that it nearly stops your heart. But what you feel is that you must worship her.{/i}"
    ann "{i}He is so far away from you, so difficult to reach. His song is beautiful, yes, but it shames you to sing along.{/i}"
    ann "{i}I’m not a superstar, but that doesn’t mean I can’t sing for them, the audience, the people just like me.{/i}"
    ann "{i}What did Mary say? Chin up, back straight, show ’em those hips. 1, 2, 3, 4, click those heels forward!{/i}"

    show concert2
    with dissolve
    
    a "Sing with me!"
    
    ann "{i}The colorful lights play on my face. They are dazzling. They are pretty. I pour everything I have into my voice, amplifying it above the crowd’s cheers.{/i}"
    ann "{i}I can see them wave along with me. I walk towards them, waving back, pumping my free hand high into the air with the beat.{/i}"
    ann "{i}I’m no longer on the stage. I’m in a karaoke room. The music video is playing on the screen behind me, and I’m going along with it, imitating the pop idol group dancing with the tune.{/i}"
    ann "{i}I’m gonna outdo Katie’s score on the karaoke machine. Nothing is going to stop me. What is there to stop me?{/i}"
    ann "{i}I don’t care that this is a generic sound. This is my sound. If what Cherry and Taylor sang were considered unique, then so is this. This is me. I should be proud of my identity, no matter what it is.{/i}"
    ann "{i}This summer, I’m gonna be an idol.{/i}"
    ann "{i}I know it.{/i}"
    
    scene stage2close
    with whitefade

    show jacques up smile at center:
        zoom 1.3
        yalign 0.35
    with dissolve
    
    j talk "Alright, so you’ve heard all the performances from our contestants: Mary, Raisa, Taylor, and Alice. Now is your chance to vote for your favourite idol!"
    j "Those in the audience, please click on the number corresponding to your contestant of choice. Those watching this show from home, please log into our webpage to cast your vote."
        
    show jacques smile

    hide jacques with dissolve

    scene stage2far
    with dissolve

    $ config.side_image_tag = "alice"
    
    ann "{i}As the commercials play, we eagerly await the results of the poll. Though I’ve resigned myself to whatever fate will befall me, I can’t help but admit that I still hold onto some hopes of advancing.{/i}"
    
    show director smile at center
    with dissolve

    di talk "Ready to pack your bags, Intie?"

    show director smile
    
    a frowntalk "Am I not supposed to stay even if I were to be eliminated?"

    a frown "{nw}"

    hide director with dissolve

    show mary summer up smile at center
    with dissolve
    
    m frowntalk talk "Wrong response. True, you'll probably stay either way, but you shouldn’t even consider the possibility of elimination."

    show mary smile
    
    a frowntalk "That’s... a little... optimistic, don’t you think?"

    a frown "{nw}"
    
    m frowntalk frowntalk "Well, do you really think you did worse than the rest of us?"

    show mary frown
    
    ann "{i}Maybe.{/i}"
    a frowntalk "I didn’t really say that, did I? But because I’m not crazy good and much, much better than everybody else, I can’t help but at least consider the possibility of elimination, right?"
    
    a frown "{nw}"

    m frowntalk frowntalk "It’s not about whether that possibility is there. It’s about whether to consider it."

    show mary frown
    
    ann "{i}Whether to consider it?{/i}"

    show taylor summer up frown at right with moveinright
    
    t frowntalk "If you think you did well, just admit it. You have every right."

    show taylor frown
    
    a frowntalk "Taylor..."

    a frown "{nw}"

    show cherry summer up frown at left with moveinleft
    
    c talk "Even if I were to be eliminated, I would still be happy to stay and help everybody else as best as I can!"

    show cherry smile
    
    ann "{i}Cherry, really? Eliminated? You and Taylor are the ones with least to worry about, alright?{/i}"
    ann smile "{i}Still, it’s sorta nice to feel welcomed here.{/i}"
    
    hide cherry
    hide mary
    hide taylor
    with dissolve

    show katja frown with dissolve

    k talk "If you four are all done giggling, I believe Jacques has an announcement."

    show katja frown

    scene stage2close
    with dissolve

    show jacques up smile at center:
        zoom 1.4
        yalign 0.35
    with dissolve

    $ config.side_image_tag = ""

    j talk "And here are the results in my very hands. Who will be the winners? Who will be the loser?"
    j "Taylor Warren, you are the highest-scoring contestant of this round. You have advanced."

    show jacques smile
    
    c "Why isn't he announcing the one who lost first?"
    
    k "You, Little Girl, know nothing about running a successful TV show."
    
    t "Your sadistic audience enjoys torturing us. Great."
    
    a "You mean torturing us. You’ve already advanced!"
    
    j "And the next highest scoring contestant is... Mary Viswanathan. Congratulations, you have also advanced!"
    j "After her, the next highest scoring was... Raisa Cherenkov!"
    j "Lastly... Alice Carroll! Now that you've seen all of our contestants, join us Saturday to see them compete again!"

    a "..."

    scene stage2far
    with dissolve

    $ config.side_image_tag = "alice"

    show mary summer up frown at left
    show katja smile at center
    show cherry summer up frown at right
    with dissolve

    a frowntalk "Wait... so, does that mean..."

    a frown "{nw}"

    k talk "It means you'll all be performing in a few more days. Get ready."

    show katja smile

    c talk "We all made it!"

    show cherry smile

    m frowntalk frowntalk "This wasn't an elimination round, was it?"

    show mary frown

    k talk "No, it wasn't. If you have any more questions, ask me after dinner. Bye!"

    show katja frown

    hide katja with moveoutright

    a "..."

    m frowntalk frowntalk "Quit looking so glum. You've made it past the first round."

    show mary frown

    a frowntalk "It was a freebie round..."

    a frown "{nw}"

    m frowntalk frowntalk "Don't be too sure about that. If you had gone up there screeching, it would have become an elimination round very quickly."
    m frowntalk talk "Now, let's go eat."

    show mary smile

    c talk "Yes, let's go!"

    show cherry smile

    a talk "Alright..."

    a smile "{nw}"
    
    jump morning2
    
    ######## end contest 1 WIN


    
label week3contest:

    scene stage4far
    with fadee

    $ config.side_image_tag = ""
    
    ann winter "{i}Today, the prep room is eerily quiet.{/i}"

    $ config.side_image_tag = "alice"
        
    a up frowntalk winter "Another week already... I don't know if I'm ready."
    a frown "{nw}"

    show mary up frown winter at center:
        zoom 1.3
        yalign 0.4
    with dissolve
    
    m frowntalk "You'll need to learn to overcome."

    show mary frown
    
    a frowntalk "I guess I’m not as strong-willed as you, Mary. I just don’t like this feeling of my friends leaving me one by one... that and I don’t really feel worthy of advancing."
    a frown "{nw}"

    m frowntalk "Your earlier concern I can understand, but your second concern is unforgivable. By saying that you aren’t worthy, are you trying to tell me that a contestant who’ll be eliminated isn’t worthy either?"
    
    show mary frown

    a frowntalk "That’s not what I mean. I’m saying that they should be here and not me! I mean... if the professional judges’ votes count more than the lay audience, I’m sure I'll be the first to go."
    a frown "{nw}"

    m frowntalk "But are singers always judged in the kind of strict manner you’re suggesting?"

    show mary frown
    
    a frowntalk "Well... no... but..."
    a frown "{nw}"
    
    m frowntalk "Even if we don’t consider the fact that this isn’t even true, being an idol isn’t just about showing off your singing technique. It’s a multi-faceted form of entertainment."
    m "The audience would take to your looks, take to your fashion style, whatever... but that’s just how it is."

    show mary frown
    
    a frowntalk "But don't you think that's unfair?"
    a frown "{nw}"
        
    m frowntalk "Unfair? In what way? You're asking this question like asking whether it’d be unfair for an artist to not be born a scientist instead."
    m "We’re all unique individuals here, with different strengths and weaknesses. It’s up to you to make your strengths shine and defeat your weaknesses."
    
    show mary frown

    a "Even if that means winning an idol contest by... being cute?"
    a frown "{nw}"
        
    m talk "If that’s your strength, then yes. Be the cutest you can be. Develop and maintain a stage personality that engages your audience."
    
    show mary smile

    a down frowntalk "That's... it just feels so shallow..."
    a frown "{nw}"
        
    m frowntalk "I don’t think so. See Jacque? I have deep respect for him, shallow a character as he is. He spends literally hours on his makeup. He even adopted a French stage name just to enhance his stage personality."
    m "You think it’s easy? I think not. He put a lot of hard work into it, all for the sake of entertaining his audience. That’s what an idol should be like."
    m "You may feel like crying on the inside from all the stress upon your shoulders, but under the bright lights, you keep it all in, showing only the smile that your audience wants to see."
    
    show mary frown

    a frowntalk "Is that not just... being fake?"
    a frown "{nw}"
        
    m talk "It’s all about giving the audience something to dream about. When they are watching you, they can forget about the harsh realities they face on a regular basis."
    m "You’re creating a temporary utopia for them. This is where they can just let go and have fun."
    
    show mary frown

    a frowntalk "I... I don't know if I really get it."
    a frown "{nw}"
    
    m talk "You do. You’ve been doing this superbly so far. You may be like this in here, but out on the stage, you really shine."
    
    show mary smile

    a frowntalk "I suppose \"like this\" isn’t exactly a good thing, right?"
    a frown "{nw}"
    
    m talk "Hmm... it’s not idol-like, for sure, but... it’s adorable in its own way."

    show mary smile

    show mary frown at leftt:
        zoom 1.3
        yalign 0.4
    show taylor up frown winter at right:
        zoom 0.98
    with moveinright
    
    ann "{i}Before I get the chance to ask further, Taylor comes out of the change room with a green knitted hat on her head. Mary squints at her.{/i}"
    
    m down frowntalk "Really? That’s all for your outfit?"

    show mary frown
    
    t frowntalk "The theme is winter."

    show taylor frown
    
    m frowntalk "And you’re wearing a t-shirt. The same t-shirt as the intro episode and week 1..."

    show mary frown
    
    t frowntalk "It's different from last week's."

    show taylor frown
    
    m frowntalk "This guy is the one whom you shouldn’t learn from if you want to become an idol, Alice. I'm surprised your lack of style hasn't gotten you eliminated yet on virtue alone."
    
    show mary frown

    t frowntalk "If elimination means I can just leave this place, I’d have sung like I was on helium to get the hell outta here."

    show taylor frown
    
    ann "{i}I wonder why Taylor seems so reluctant to participate in all this. I mean... she did sign up for this on her own accord, right?{/i}"
    
    m frowntalk "I’m not going to ponder why you even applied in the first place, but even now, can’t you just withdraw?"

    show mary frown
    
    t frowntalk "We signed a contract. I would have to pay for damages to that greedy Russian lady if I were to withdraw now."

    show taylor frown
    
    a talk "I’m pretty sure she’s Slovenian, actually... prežganka and all. I looked it up online after she mentioned it."

    a frown "{nw}"
    
    m frowntalk "Stop, you two. We're going off-topic."

    show mary frown
    
    t frowntalk "I don’t see what else I need to say. I’m not rich like you, Mary. I can’t fish out a couple hundred thousand from my pockets."
    
    show taylor frown

    hide taylor with moveoutright

    ann "{i}With that, Taylor just turns around and heads for the stage, leaving all of us staring after her.{/i}"

    show cherry up frown winter at rightt
    with dissolve
    
    c frowntalk "What did you guys just say to her to have her stomp out like that?"

    show cherry frown
    
    m down frowntalk "Nothing. She’s just being her usual unprofessional self, is all."

    show mary up frown
    
    a frowntalk "I wouldn't go that far..."
    a frown "{nw}"
    
    c down frowntalk "I... I just want everybody to get along..."

    show cherry frown
    
    hide cherry
    hide mary
    with dissolve

    $ config.side_image_tag = ""

    scene stage4close
    with dissolve

    show jacques up smile at center:
        zoom 1.35
        yalign 0.35
    with dissolve
    
    j talk "Welcome back to Supernova. This is the third week of our contest where only the best can remain and step up to the throne of your next super idol. As you can see here, this week’s theme is winter!"
    j "Our first contestant to sing for us today is Raisa Cherenkov. Welcome!"

    show jacques smile

    hide jacques with dissolve
    
    a "You're up first?"
    
    c "Yeah. Ms. Dominko decided that I should do the opener for this week..."
    c "It's okay. I'll be fine."
    
    ann "{i}Images of snow drift down to fall on virtual conifers within the globe illuminated on the screen. Cherry walks up to the stage, standing beside where a snowman decoration is placed.{/i}"
    ann "{i}Her pale skin and platinum hair blends into the background, eyes a piercing blue like ice crystals. Still, despite the fragile appearance, Cherry gives off a strength that I’ve never seen from her before.{/i}"
    ann "{i}The song opens with lonely piano notes, then, as what sounds like sleigh bells start ringing, Cherry’s voice joins in.{/i}"
    ann "{i}It’s a whispery, sad tone, like withered branches struggling to withstand the cold. But as smooth, synth strings start filling in the shadows, Cherry’s voice thickens, rich with an entrancing power.{/i}"
    
    an "I thought she only sings children’s songs. Last week, she had to practise a lot to take on that techno pop, but why is she so... in command of this song this week?"
    ann "{i}Cherry closes her eyes. I can see, I can hear that she has completely submerged herself into the melody.{/i}"
    ann "{i}There’s probably nothing else on her mind now, just the lyrics of this song, the words she’s singing for one person, and one person only.{/i}"
    
    show cherry up smile winter at center:
        zoom 1.3
        yalign 0.5
    with dissolve

    c talk "I’m not so small now, you see. Won’t you come and stay with me?"
    c "I can take you to the sky. I was a small bird, but now can fly."
    c "I am strong now, you know? I can hold you, I won’t let go."
    c "So long as you’re here, I have no fear..."

    show cherry smile
    
    ann "{i}She steps up, her white boots leaving barely any sounds on the ground. It’s like she really knows how to fly, her voice rising with the wind.{/i}"
    ann "{i}She lifts her hand upwards, the blue sleeve of her coat drawing a beautiful arc to the side. Reaching out, she turns to face us.{/i}"
    
    c talk "...not summer and the scorching sun, not winter and the freezing snow."
    c "So long as you’re here, I won’t let go, won’t let go..."

    show cherry smile
    
    ann "{i}I clap along with the crowd. The sound we make starts off gently, then becomes deafening. I think I see it now, why Cherry’s singing is always so charming. It’s genuine.{/i}"
    ann "{i}Even though I may not share the same feelings as she is expressing, I become engrossed in understanding them.{/i}"
    ann "{i}When I’m watching her on the stage, it’s as though I’ve stepped into her shoes, walking the paths she has taken, experiencing the emotions filling her heart. They are simple emotions, but they are clear and true.{/i}"
    ann "{i}Cherry doesn’t hide herself. This is who she is, the good and bad, the strong and weak.{/i}"

    hide cherry with dissolve

    ann "{i}It’s a powerful way to sing. There is no performance quite like it.{/i}"

    show jacques up smile at center:
        zoom 1.35
        yalign 0.35
    with dissolve

    j talk "Thank you, Raisa. That was a heartfelt song, indeed."
    j "Our next contestant is Mary Viswanathan. So far, she has displayed a warm image for us on-stage. How will she fare with this week’s winter theme?"
    
    show jacques smile

    hide jacques with dissolve

    ann "{i}Mary, who along with Taylor has been silent throughout Cherry’s performance, gets up to walk onto the stage.{/i}"
    ann "{i}The silver and diamond jewellery makes a strong contrast on her sun-kissed skin, giving her an even more noble look than usual. She’s like the queen of snow.{/i}"
    ann winter "{i}But this just makes her slightly trembling hands seem even more humbling.{/i}"

    scene stage4far
    with dissolve

    $ config.side_image_tag = "alice"
    
    show mary unsure frown winter at center:
        zoom 1.4
        yalign 0.5
    with dissolve

    a frowntalk winter "You okay?"
    a frown "{nw}"
    
    m frowntalk "O-of course. Why wouldn't I be?"

    show mary frown
    
    ann "{i}I want to assure her that it’s okay to be nervous, but how can I do it? Maybe pointing out her current state would only worsen things.{/i}"
    ann smile "{i}I take her hands in mine and give them an affirming squeeze instead.{/i}"
    
    m frowntalk "I..."
    m "It was... a shock, listening to Cherry sing like that. I almost doubted myself."
    m "But I guess, after all, she’s her, I’m me. I’ll have to do things my way."

    show mary frown
    
    a talk "That's okay."
    a "I’ll root for you, no matter what style you choose for your performance."

    a smile "{nw}"
    
    m up talk "Thanks."

    show mary smile

    $ config.side_image_tag = ""

    scene stage4close
    with dissolve
    
    ann "{i}Harps sound in the background, strings plucked one by one. They form a beautiful melody, but it’s thin and sparse, like something is lacking. Mary’s voice fills the gaps, humming, crying.{/i}"
    ann "{i}Her voice, deep, colorful, paints the night sky with the moon and stars. The calm light unveils snowflakes that have been dancing in the frigid air all along, falling upon our shoulders to dust a soft layer of white.{/i}"
    ann "{i}That’s the imagery Mary brings forth. It’s serene. It’s breathtaking. But only then do I realize that she always sounds so detached, from the crowd, from the world, from me, from herself.{/i}"
    ann "{i}It’s unreal. Her warmth in the summer theme, her energy in the techno theme, and now her delicate cold in this winter theme. So well-constructed, yet...{/i}"
    ann "{i}...I somewhat want to hear what the real Mary would sound like.{/i}"
    ann "{i}I’ve always just noticed her perfection, the lady with a good upbringing, smart and beautiful albeit a little self-centered. But who is she, really? What are her motivations? What are her true feelings now?{/i}"
    ann "{i}I wonder, if Mary were not standing on a stage, but just by a bus stop, waiting as snow falls on her umbrella, what kind of tune will she let slip from her lips?{/i}"
    ann "{i}But that is just a pointless musing. Perhaps this is the real Mary. Of course she’s not truly perfect. But she’s a person who tries very hard to be so. She may be nervous this moment. She may be lost. But she doesn’t let it show.{/i}"
    ann "{i}To give the audience a dream to experience, huh?{/i}"
    ann "{i}In her own way, Mary may be a gentle person after all.{/i}"

    show jacques up smile at center:
        zoom 1.35
        yalign 0.35
    with dissolve
    
    j talk "A most beautiful performance from Mary Viswanathan once again. She sang of snow falling under moonlight, calm and entrancing."
    
    show jacques smile

    scene stage4far
    with dissolve

    show taylor up frown winter at rightt
    show mary up frown winter at leftt
    with dissolve

    t frowntalk "It’s a shame you still haven’t opened up your heart, Mary. Such a beautiful voice, only to come to waste."
    
    show taylor frown

    m down frowntalk "You are one to say. If you don’t get serious soon, you’ll be eliminated."

    show mary frown
    
    t frowntalk "I don't know if I'd care..."

    show taylor frown

    scene stage4close
    with dissolve
    
    ann "{i}Taylor doesn’t let the tense atmosphere get to her. The moment she’s on-stage, she’s the cool, collected singer again.{/i}"
    ann "{i}The broad theme opens in the background, her voice easily blending into it along with the bell-like rings of a second melody.{/i}"
    ann "{i}Taylor doesn’t force too much air into her singing, but somehow, she manages to project the clear sounds into the audience. It’s like it doesn’t take any effort. But at the same time, I know that’s just a show of her skills.{/i}"
    ann "{i}I know Taylor is very skillful from day one. However, that skill never actually translates to enhancing the mood of songs that she sings. Instead, she warps every song into something of her own, feeding it with hopeless melancholy.{/i}"
    ann "{i}She does the same with this wintery music. What originally sounds like an innocent walk down a snow-lined sidewalk becomes a walk down memory lane.{/i}"
    ann "{i}I can almost feel my hand, numb from cold, taken in her and led down a path where her steps leave the snow dented. I follow her into the dark, reliving vague regrets threatening to swallow our meager presence.{/i}"
    ann "{i}Summer, techno, winter... all just minor twists to her bleak mentality.{/i}"

    show jacques up smile at center:
        zoom 1.35
        yalign 0.35
    with dissolve
    
    j talk "Thank you, Taylor. You have expressed a desolate face of winter in your song. That was a unique take."
    j "Now, our last contestant, Alice Carroll, will have her take on the theme. Alice, the stage is now yours."
    
    show jacques smile

    ann "{i}Indeed, what is it that I want to express?{/i}"
    ann "{i}What is it that I want to sing?{/i}"

    $ currentScreen = "week3minigame"
    $ waitTime = 4.5
    
    call screen week3minigame
    
label week3win:

    $ config.side_image_tag = ""
    
    ann "{i}Should I be like Cherry, sing for a person who means a lot to her?{/i}"
    ann "{i}Or be like Mary, sing for the crowd that watches her?{/i}"
    ann "{i}Maybe yet, I should sing like Taylor, minding only my own feelings, venting them to my heart’s content?{/i}"
    ann "{i}Only when I step up to the stage do I come to discover that I have never even contemplated this question.{/i}"
    ann "{i}How should I sing?{/i}"
    ann "{i}For what reason do I sing? Who am I singing to?{/i}"
    ann "{i}In the first two weeks, I’ve just been shocked. The moment I stood here, I didn’t know what to do. I just did what I could, trying not to screw up.{/i}"
    ann "{i}Maybe my skill was too low. I had too much going around in my head, just trying to keep up with the beat, to reach every note.{/i}"
    ann "{i}But now I’m getting better. I know I can now command my voice. I have control over the pitch and timbre, the amplitude and texture. I’ve learned a lot from the others.{/i}"
    ann "{i}I’ve developed an arsenal of techniques I can use, maybe even to improvise variations to the melody.{/i}"
    ann "{i}When the piano melody sounds, I wonder how to start. This is important. I’ll be setting the mood for the rest of the song.{/i}"
    ann "{i}But I'm lost. I still don't know how."
    
    a "When the snow falls, my heart will skip again..."
    a "I will remember all our days again."
    a "Those memories will be with me... till I’m old."
    
    ann "{i}It’s strange, because the more I ponder, the harder it becomes.{/i}"
    ann "{i}When I just let go, the song takes me exactly where I should be.{/i}"
    ann "{i}Maybe it’s a sad thing...not having a style that’s mine. I don’t have anything in particular that I want to express. You know, I really wish I could lead my audience, just like Cherry, Mary, and Taylor.{/i}"
    ann "{i}But maybe being led by the song itself isn’t so bad?{/i}"
    ann "{i}The melody takes me deep into someone’s reminiscence. Young days, going to parties, having fun - there are so few constraints to limit her.{/i}"
    ann "{i}Like a caterpillar building its cocoon, everything seems possible. But once locked inside, fear churns.{/i}"
    ann "{i}What if she can’t become anything? What if she always remain an ugly worm while everybody else becomes bright butterflies and take flight into the wide skies above?{/i}"
    ann "{i}Those are the dark nights and cold winters - metaphorical, yes, but so real in her mind.{/i}"
    ann "{i}Then someone takes her hand.{/i}"
    ann "{i}She can’t see, but she can feel the warmth holding her. She’s being dragged out into the light. She can feel her new wings flutter off remnants of her old coat and broaden to their full span.{/i}"
    ann "{i}She is now engulfed in sunlight. It is no longer cold - it is spring. The scent of flowers fills her nostrils. By instinct, she flaps those wings.{/i}"
    ann "{i}By instinct, she flaps those wings.{/i}"
    ann "{i}Winter leaves. Winter comes again. All that’s left are memories. The person who saved her is gone, but she’ll still remember...somewhere in the snow remains her savior’s footsteps. Knowing this, alone, gives her comfort.{/i}"
    ann "{i}She, too, has flown away.{/i}"
    ann "{i}I, too, fly away.{/i}"
    ann "{i}I blink.{/i}"
    ann "{i}The snow is gone. No caterpillars, no cocoon, no butterflies. They were all my imagination, built from the melody of the song, the words that form the lyrics.{/i}"
    ann "{i}I didn’t have a \"self\" when I was singing. I became the protagonist, the story becomes mine.{/i}"
    ann "{i}Who is the audience? I don’t know. The ones in the seats? Behind the TV? My boss, friends, family? Myself?{/i}"
    ann "{i}I don’t think it matters in the end. To me, singing is singing. It’s fun, using my voice to bring meaning to notes and words that aren’t my own.{/i}"
    ann "{i}By singing, I connect with the thoughts of others. I feel what I cannot under normal circumstances.{/i}"
    ann "{i}And is that not the purpose of art? To communicate feelings that are difficult to express, even to people who may not share your experiences, culture, or even language?{/i}"
    ann "{i}It’s something that transcends all boundaries of society. It is art that helps us empathize with each other, brings harmony despite our differences.{/i}"
    ann "{i}Knowing this gives me purpose to continue. I can’t help but smile at the audience, who finally claps after my performance has ended.{/i}"
    
    show jacques up smile at center:
        zoom 1.35
        yalign 0.3
    with dissolve

    j talk "Another nice performance by Alice Carroll. I’m sure we can all relate a little to the themes expressed in this song."
    j "But with four wonderful performances from our contestants, it’ll be a difficult choice to eliminate one of them. Let’s decide during the commercial break. Stay tuned. We’ll be back with the results!"
    
    show jacques smile

    scene stage4far
    with dissolve

    show katja smile at center:
        zoom 1.3
        yalign 0.4
    with dissolve

    $ config.side_image_tag = "alice"

    k talk "You’re actually smiling, Kid."

    show katja smile
    
    ann winter "{i}My boss waits for me at the doorway to the prep room, making me nearly jump in surprise.{/i}"
    
    a talk "I suppose I’m actually happy with my performance?"
    
    a smile "{nw}"

    k talk "Well, it really isn’t bad."

    show katja smile
    
    ann frown "{i}And here I was feeling good about myself - her cold statement doesn’t give me much hope, huh?{/i}"
    
    k frowntalk "Were you perhaps expecting me to praise you?"

    show katja frown
    
    a frowntalk "It wouldn’t hurt, haha."
    
    ann frown "{i}I notice that even my boss’ harsh comments aren’t doing much to sway my mood. I know I did well. It isn’t something that needs to be verified by others.{/i}"
    
    k frowntalk "Rather than your performance, I think your mindset is even more worthy of praising."

    show katja frown
    
    a frowntalk "Mindset?"
    a frown "{nw}"
    
    k frowntalk "In my opinion, an idol is a marketed phenomenon. An idol can be ugly, can lack talent, but so long as you promote her to a divine status, she’ll be loved. The only thing is, she first has to believe this to be possible."
    
    show katja frown

    a frowntalk "You mean... no matter how poor your abilities are, objectively speaking, to still believe you are the best of the best?"
    a frown "{nw}"

    k frowntalk "Something like that. A person with the belief that he is omnipotent can become a god. A god who doesn’t believe himself to be omnipotent, on the other hand, will cease to be revered."
    
    show katja frown

    a frowntalk "That's... philosophical..."
    a frown "{nw}"

    k talk "When you get to my age, you’ll start having some theories about life."

    show katja smile
    
    ann smile "{i}I don’t know if I appreciate that kind of philosophy, but regardless, I’ll try harder.{/i}"

    hide katja with dissolve

    ann "{i}I want to be loved by the audience because of my ability to engage them, not because of some artificial promotion designed to specifically target the crowd’s psych or whatever...{/i}"
    ann "{i}After my conversation with Boss, I join the others in the prep room to wait for the results. Mary and Taylor are still staying quiet from their previous conflict, while Cherry is making some idle chatter with a stage director.{/i}"
    
    show mary unsure frown winter at left
    show cherry up smile winter at center
    show taylor up frown winter at right
    with dissolve

    a talk "So... umm... everybody did well in the performances just now."
    a smile "{nw}"

    m frowntalk "I don’t know about that. I think I could’ve done better."
    
    show mary frown

    t down "Strange to say, but I’m in agreement regarding my own performance."
    
    show taylor frown

    c frowntalk "You don’t have to say that about yourselves..."
    
    show cherry frown

    scene stage4close
    with dissolve

    $ config.side_image_tag = ""

    show jacques up smile at center:
        zoom 1.35
        yalign 0.3
    with dissolve

    j talk "I’m sure we all have had a tough time deciding who will advance, who will be eliminated this week. The results now lie in my hands, and I must say, they are close. Very close!"
    j "The winner of this week is... Raisa Cherenkov!"
    j "Our professional judges and the lay audience on our comment boards both comment on the strong, genuine emotions you’ve expressed in your heartfelt ballad. Congratulations, Raisa. You’ve advanced."
    j "Coming in second place is... well, this is a little unexpected..."
    j "This just goes on to prove how much she has improved... Congratulations, Alice Carroll, you’ve also advanced! The simple take on a highly relatable song has resonated strongly with our audience."
    j "Over the weeks, you’ve developed a unique charm, making you now a forerunner for victory rather than the underdog from when we first started. Great job, Alice!"
    
    show jacques smile

    ann "{i}I don't think I heard him right.{/i}"
    ann "{i}For the first time, I will not be standing on the stage of elimination.{/i}"
    ann "{i}I actually made it to second place. I don’t know how to feel about this.{/i}"

    scene stage4far
    with dissolve

    $ config.side_image_tag = "alice"

    an winter frown "{nw}"

    show mary up smile winter at rightt
    show taylor up frown winter at leftt
    with dissolve
    
    m talk "Be proud, Alice. You deserve it."

    show mary smile
    
    a frowntalk "I... I don't know about that..."
    a frown "{nw}"
    
    t frowntalk "Mary is actually right this time. I can feel the confidence in you. You don’t need to hide it."
    
    show taylor frown

    m frowntalk "Do we look like the type of people to be upset by being jealous?"

    show mary frown
    
    a down frowntalk "Of course not!"
    a up frown "{nw}"
    
    m talk "Then all you have to say is \"Thank you for your support. I’ll continue to work hard\"."

    show mary smile
    
    a talk "I... thank you for your support... I’ll continue... I’ll get better... I’ll work very, very hard in the future."
    
    ann smile "{i}Taylor puts her large hand on my head and ruffles my hair, giving me a rare smile I hardly know she’s capable of showing.{/i}"
    
    t talk "Good. I look forward to seeing your improvement."

    show taylor smile

    $ config.side_image_tag = ""

    scene stage4close
    with dissolve

    show jacques up smile at center:
        zoom 0.96
    show mary up frown winter at left:
        zoom 1.2
        yalign 0.3
    show taylor up frown winter at right:
        zoom 1.1
        yalign 0.35
    with dissolve
    
    j talk "And today, the two facing elimination are our week 1 winner, Taylor Warren, and week 2 winner, Mary Viswanathan. Please come onto the stage, Taylor and Mary."
    j "How do you feel about standing here today?"
    
    show jacques smile

    t frowntalk "Do I really have to answer this question?"

    show taylor frown
    
    ann "{i}Taylor may not be speaking to the mic, but I can still tell that’s exactly what she’s saying. After all, that fits her personality perfectly.{/i}"
    ann "{i}Mary delivers her a glare and takes the mic into her own hands instead.{/i}"
    
    m talk "I thank everybody for the chance to be here..."
    m frowntalk "...is what I should say. I guess at this point, I have revisited my strategy of acting like the idol I have thought people like to see."
    m "In all honesty, I’ve always felt confident about winning. I know I’m skillful and there shouldn’t be anything stopping me. What I haven’t considered is the true meaning of being here."
    m "What are my own feelings about the words I sing? What are the feelings that the songwriters are trying to express? I think maybe those are also things I should’ve considered."
    m talk "If I were to have the chance to return to this stage, that’s what I would like to answer. I know this sounds... idealistic, impractical, but that’s what I really think at this moment."
    
    show mary smile

    ann "{i}Considering how Mary is, I can only imagine how much it took for her to say all this.{/i}"
    ann "{i}She has always valued professionalism above all else. I’m sure at this moment, she probably feels selfish to be using the opportunity to express her thoughts.{/i}"
    ann "{i}Still, she has gathered the courage to say it. She has gathered the courage to revisit her own ideas of what being an idol should be. This truthful side of her can only be described as admirable.{/i}"
    
    m frowntalk "I want to become an idol not just cut out from the same mold as all others. I want to bring something new to the industry."
    m "This may be arrogant of me, but I think there would be no reason for me to become an idol if I have nothing new to offer."
    m talk "Facing elimination made me realize this. For that alone, I’m glad. You guys have given me a wake-up call. I would have no regrets even if I were the one to step down from the stage today."
    
    show mary frown

    j talk "Thank you, Mary. That was very motivational. Do you have anything to add, Taylor?"
    
    show jacques smile

    t talk "No. That was perfect."
    
    show taylor smile

    ann "{i}Taylor looks over to Mary, offering Mary her hand. Mary widens her eyes, but takes it in her grasp.{/i}"
    
    m frowntalk "One of us will have to go, but the memories is something that’ll stay."

    show mary smile
    
    t talk "Agreed."
    
    show taylor smile

    j talk "Alright. Now, I must announce who will be eliminated from week 3 of Supernova. I’m sorry to say..."
    j smile "{cps=40}...{/cps}"

    show mary frown

    j frowntalk "Mary Viswanathan, you have been eliminated."
    
    show jacques smile

    ann "{i}Mary doesn’t look too upset. She calmly steps down the stage.{/i}"

    hide mary with dissolve

    $ renpy.pause(0.5)

    hide taylor
    hide jacques
    with dissolve

    ann "{i}Really, she’s like a queen. She may have lost, but she is not lost. If anything, she knows what she wants even better now.{/i}"
    ann "{i}I wish I could be like that.{/i}"
    ann "{i}If- no, when- Mary becomes an idol in the future, she’ll be an inspiration for many.{/i}"
    
    ###### end contest 3 win
    
label week4contest:

    scene stage5far
    with fadee

    $ config.side_image_tag = "alice"
    
    ann frown edgy "{i}If the prep room was quiet last week, then it’s silent this week.{/i}"

    show director smile at center:
        zoom 1.2
        yalign 0.8
    with dissolve

    di talk "Intie sure looks sad today. Has your friend ditched you?"

    show director smile
    
    a frowntalk "I’m not sad. I’m just thinking."
    a frown "{nw}"
    
    di talk "Thinking about what to do now that your friend is not here to help?"
    
    show director smile

    ann "{i}I would like to rebuke him, but maybe there is some truth to what he is saying. Even if Mary hasn’t been directly guiding me, she still has given me motivation and inspiration. It’s strangely... depressing with her gone.{/i}"
    
    show taylor up frown edgy at right:
        zoom 0.97
        yalign 0.2
    with moveinright

    t frowntalk "I think it's a good thing."

    show taylor frown
    
    di talk "Easier for you to win?"

    show director smile

    show director at leftt:
        zoom 1.2
        yalign 0.8
    with moveinright

    show taylor at right:
        zoom 1.1
        yalign 0.4
    with dissolve
    
    t frowntalk "Oh please. Do I look like I care about that?"

    show taylor frown

    show director at left:
        yalign 0.8
    with moveinleft

    show cherry up frown edgy at center:
        zoom 1.2
        yalign 0.45
    with dissolve
    
    c frowntalk "I know Mary is trying to get Alice and I to become more independent, but..."

    show cherry frown
    
    a frowntalk "It's hard, right?"
    a frown "{nw}"
    
    c down frowntalk "I really only joined because I thought I could watch the show..."

    show cherry frown
    
    di talk "Well, Intie here only joined because she had to."

    show director smile
    
    ann "{i}I roll my eyes in response.{/i}"
    
    a frowntalk "Yeah, that’s right. So please don’t give me an excuse to bail out of this right before the show starts."
    a frown "{nw}"

    di talk "As though you can afford to lose your job and pay for the damages."

    show director smile
    
    a talk "Who knows? I have a rich friend after all. Maybe she’d lend me money."
    
    show taylor smile

    ann smile "{i}Taylor chuckles, clearly amused by how I turned the director’s words back at him.{/i}"

    hide director with dissolve

    ann "{i}I guess that really leaves me no choice but to win this and make sure I don’t have to go back to being an intern...{/i}"
    
    show cherry at leftt:
        yalign 0.45
    with moveinright

    c up frowntalk "It isn’t that I don’t want to become more self-reliant... but it’s easier said than done, huh?"
    
    show cherry frown

    t frowntalk "Maybe it's the process that matters."
    
    show taylor frown

    a frowntalk "Process?"
    a frown "{nw}"

    t frowntalk "You should know all about this, Alice. We’ve all seen your growth throughout the past few weeks."

    show taylor frown
    
    a frowntalk "I admit I have a bit more confidence in my abilities now, but I really have no systematic way of ensuring my own improvement."
    a "I don’t know if I’ll just stall one day, and find that I can’t go further even though I have yet to climb to the top."
    a frown "{nw}"

    c talk "It’s like how my Mom says it’d be impossible for me to cook no matter how much I try."
    
    show cherry smile

    t frowntalk "No. You just have to take the eggs out of the carton and crack the shell before it’s fried."
    
    show taylor frown

    ##ann "{i}Both Taylor and I can recall the disaster of Cherry trying to make an omelette back at our residence.{/i}"
    ann "{i}How can one think that tossing the entire carton of eggs, cardboard and all, onto the pan and assume it’d miraculously cook into anything edible is beyond me.{/i}"
    ann "{i}Lucky thing was, Cherry didn’t even remember (or know how) to turn on the stove. Thank God.{/i}"
    
    show katja smile at left behind cherry:
        xalign -0.1
    with moveinleft

    k talk "The show’s about to start. Ready to head over, guys?"
    
    show katja smile

    ann "{i}What can I say? I never feel ready anyway.{/i}"
    
    a talk "Yes, Boss."
    a smile "{nw}"

    scene stage5close
    with dissolve

    $ config.side_image_tag = ""
    
    show jacques up smile at center:
        zoom 1.35
        yalign 0.3
    with dissolve

    j talk "Welcome to week 4 of Supernova. With only three contestants left, today we will decide who gets the ticket to the grand finale, who will be left behind. Are you ready for the cruel battle to come?"
    j "Of course you are! We have all been waiting for this day since the very beginning. It’s only right that we have a suitable theme to set the stage. Presenting to you the theme of this week..."
    j "Darkness! Yes, darkness will be the theme of this week. How will our contestants portray it with their voices? Let us lend our applause to our first contestant to take on the challenge: Raisa Cherenkov!"
    
    show jacques smile

    hide jacques with dissolve

    ann "{i}A lonely, depressing melody sounds as Cherry takes to the stage, her dark, layered dress dragging behind her. She sings as her heels click down the stage, her voice thin, airy, like an eerie fog drawn across a rural night.{/i}"
    ann "{i}Her skin, so white it’s as though blood doesn’t run beneath it, and eyes a deep blue, Cherry gives off the impression of an ice witch from folklore, immortalized as a marble figurine twirling on an old music box.{/i}"
    ann "{i}With each repetition of the main theme, this illusion becomes more like reality. This is the power of Cherry’s singing.{/i}"
    ann "{i}She possesses a unique timbre and wide vocal range, giving her much needed flexibility for expressing whatever emotions she desires.{/i}"
    ann "{i}She can turn the simplest of melodies to something different and outstanding. It’s like she is some kind of god, shaping the world with mud and giving it life with her breath.{/i}"
    
    scene stage5far
    with dissolve

    $ config.side_image_tag = "alice"

    an frown edgy "{nw}"

    show taylor up frown edgy at rightt
    show katja frown at leftt
    with dissolve

    t frowntalk "But it’s like... something is lacking today. Motivation?"
    
    show taylor frown

    a frowntalk "Sorry?"
    a frown "{nw}"

    k frowntalk "More like inspiration, Taylor."
    
    show katja frown

    t frowntalk "Ah... I can relate to that."
    
    show taylor frown

    a frowntalk "I... can't?"
    a frown "{nw}"

    t frowntalk "If anything, that has always been your strong point, Alice. You may not realize it, but inspiration just flows within you. Overflows, really. That’s how we can all sense it."
    
    show taylor frown

    scene stage5close
    with dissolve

    $ config.side_image_tag = ""

    show jacques up smile at center:
        zoom 1.35
        yalign 0.3
    with dissolve

    j talk "Thank you, Raisa."
    j "Next, we have Alice Carroll. Just listening to this opening should be enough to tell us that she’s going to put a different spin to this week’s theme, right? Alright, Alice. I’ll leave things in your hands."
    
    show jacques smile

    hide jacques with dissolve

    ann "{i}I don’t know if what Taylor said really applies to me. I don’t have time to think over it either.{/i}"
    ann "{i}But the music is on. The game’s mine.{/i}"
    ann "{i}I head onto the stage, a grin filling my face.{/i}"
    
    jump week4minigame
    
label week4win:
    
    ann "{i}While Cherry took a more traditional, ghost story-like approach to the dark theme, I’m spinning it with a modern take at Bach’s Fugue in G Minor.{/i}"
    ann "{i}The song takes off with a strong, pounding rhythm, the pedal point only emphasizing this beat. I move my body with the hard hit of each note, making my voice pulse with it.{/i}"
    ann "{i}The lights are flashing along with my lead, swerving, blinking, changing in rapid succession a vivid array of colors.{/i}"
    ann "{i}Damn it, Director. You may be an ass, but you do make sure the crew does its job right, huh?{/i}"
    ann "{i}I can’t betray all your efforts, I swear.{/i}"
    ann "{i}I mold myself into a gothic ballerina, dancing like my limbs are rigid with death. I imagine fangs growing long within my mouth, and in showing them, the quality of my voice changes to that of a croak, a growl.{/i}"
    ann "{i}My sound deepens, roughens, I’m infected with a virus that makes me into a zombie. I am Dracula and Frankenstein.{/i}"
    ann "{i} As I reach my black-painted nails to the audience, I brush across webs that cling to me like a glove, the spider, a black widow, scurrying up my arm to perch proudly on my shoulder.{/i}"
    ann "{i}Yes, that’s the imagery I’m going for.{/i}"
    ann "{i}Is this the inspiration Taylor was talking about? I don’t know. Maybe I have been so dissatisfied with my life up to this point that I’ve gotten used to filling the hollows with my imagination?{/i}"
    ann "{i}That's a morbid thought.{/i}"
    ann "{i}But even if that were the case, I’m starting to figure out a solution to my dissatisfaction.{/i}"
    ann "{i}When I think I can’t do something, tell myself I can.{/i}"
    ann "{i}When I can’t see an opportunity, go find it.{/i}"
    ann "{i}Standing here on this stage makes me remember all the dreams I’ve tossed out because of my old cowardice.{/i}"
    ann "{i}I thought I was just being realistic when I gave up on pursuing them. In the end, I was just hiding from the possibility of failure.{/i}"
    ann "{i}Who cares if I fail, really? Myself?{/i}"
    ann "{i}So if I can forgive myself in the case I fail, nobody else would have a problem with it, right?{/i}"
    ann "{i}What is there to fear, then?{/i}"
    ann "{i}If we really think about it, fear is often a constructed quality. A figment of our own thoughts and illusions.{/i}"
    ann "{i}That’s why even darkness, no matter how seemingly fearsome at first glance, can be turned on its head to something interesting, amazing, flavorful.{/i}"
    ann "{i}The pedal point pulls the dissonance back to the tonal center. The tension is resolving to consonant harmony.{/i}"
    ann "{i}I pull my hand back, dissolving the imaginary cobwebs, holding the new energy to my chest as my body loses rigidity, moving into an easy, lively dance. Despite the black teardrops painted beneath my eyes, I’m smiling.{/i}"
    ann "{i}I take my voice to a bright climax, giving it all my radiance. The waves of glow sticks beneath the stage follow my lead. We’re breaking through the night, bringing in a new dawn.{/i}"
    ann "{i}It's a celebration!{/i}"

    show jacques up smile at center:
        zoom 1.3
        yalign 0.3
    with dissolve
    
    j talk "Beautiful, beautiful work from Alice Carroll. A big hand for her, please!"

    show jacques smile

    hide jacques with dissolve
    
    scene stage5far
    with dissolve

    show taylor up smile edgy at center:
        zoom 1.12
        yalign 0.2
    with dissolve

    $ config.side_image_tag = "alice"

    an smile edgy "I leave the stage with heart pounding, breath shaking. I have never been so tired, but at the same time, I’ve never been so satisfied with my work. I’m feeling absolutely wonderful."
    
    t talk "That was great, Alice. Really great."
    
    show taylor smile

    a talk "Thanks. I really liked it as well."
    a smile "{nw}"

    show director smile at right with moveinright

    show taylor frown

    di talk "Finally tossing aside your fake modesty?"
    
    show director smile

    a frowntalk "Do you really have to say it like that?"

    ann frown "{i}The director gives a chiding snort.{/i}"
    
    di talk "I like it better when people like you just say exactly what you’re really thinking."
    
    show director smile

    t frowntalk "So you won’t feel left out for being a rude ass?"

    show taylor frown
    
    di talk "You’re one to speak."
    
    show director smile

    j "Now, please lend your warm applause to our final contestant for this evening, Taylor Warren."
    
    t frowntalk "I don’t have time to argue with you anymore. It’s my turn."

    hide director with moveoutright

    t "Alice, just want to give you my thanks. I didn’t really care for this contest at first, hated it even... but now I want to actually try to participate."
    t talk "I feel inspired just listening to you."

    show taylor smile

    $ config.side_image_tag = ""

    scene stage5close
    with dissolve
    
    ann "{i}Taylor still hasn’t changed much.{/i}"
    ann "{i}While Cherry and I both went with the clothes chosen by our production staff, she just put on a simple grey shirt to match her pants. I wasn’t under the impression that she would be taking this seriously.{/i}"
    ann "{i}But the breath she takes to compose herself in front of her audience makes me aware of how wrong I was.{/i}"
    ann "{i}Just the way she’s carrying herself is telling me that she’s going to offer a real, amazing performance this time.{/i}"
    ann "{i}The clicking beats sound. She lifts her head, eyes snapping open while she starts singing.{/i}"
    ann "{i}In all the previous weeks, she has just been venting her sadness with her voice. Tonight, she is different.{/i}"
    ann "{i}There is no hidden grief in the wispy tone she uses. I don’t know how she does it, but she gives a mysterious vibe to the way it rings - I hear it echoing across the room.{/i}"
    ann "{i}I get the sense that something is watching me, in front of me, behind me, to my sides. It’s certainly creepy and fits right into the dark theme.{/i}"
    ann "{i}That’s not all. Taylor layers her voice with vibrato. The first hearing tells a mystery, yes, but that’s only the beginning. The pulses afterwards give some sort of answer, but no resolution.{/i}"
    ann "{i}I feel like I’m tossed into some kind of futuristic conspiracy, a confusing new world order, beautiful on the outside, dystopian within.{/i}"
    ann "{i}The song descends into a rap verse. Her pitch dips down with it, low, whispering.{/i} They’re watching you. They’re all-seeing. They’re listening to your words of despair. There is no praying."
    ann "{i}The melody returns with a fire of change. Taylor cracks a glow stick in her hand to draw an arc of blue-green above her.{/i}"
    ann "{i}There is defiance in her voice. There is strength and determination. I sense the hope within her, like a light in the dark.{/i}"
    ann "{i}She whips the light down like a sword, or maybe it’s more like a gun, ready to shoot laser through an enemy of evil. I’ve been reduced to a little fangirl. I just want to tell her how \"cool\" she looks and sounds!{/i}"
    ann "{i}But beneath the story she’s telling through the melody and lyrics, I sense something more personal. Is this Taylor’s own growth?{/i}"
    ann "{i}Is this...what I’ve inspired her to become?{/i}"
    ann "{i}The darkness she had previously drowned herself in is actually more like a cocoon. Tonight, she has broken free.{/i}"
    ann "{i}It’s like the dystopian society of her song, so established that you cannot take it down in one go else humanity itself would crumble.{/i}"
    ann "{i}But awareness will allow mankind to rationalize right and wrong, bring perception to society’s suffering, thus evolving the world into a better place.{/i}"
    ann "{i}In Taylor’s case, she has begun to evolve towards a more meaningful way of expressing herself.{/i}"
    ann "{i}Whatever her pain is, the way she was venting it wouldn’t go anywhere. We felt what she was trying to portray, but we couldn’t connect with it.{/i}"
    ann "{i}Singing is an art, and art is not only a mode of expression, but also a way to communicate.{/i}"
    ann "{i}It seems that Taylor has finally figured it out. She’s still herself, but she’s also using her inner feelings as motivation towards expressing other ideas, to tell stories that may not be her own.{/i}"
    ann "{i}She’s aware of what’s troubling her, and in singing about them, she comes to confront them on her own will. She ends up defeating them with her song, changing the mindset she originally had.{/i}"
    
    show taylor up frowntalk edgy at center:
        zoom 1.6
        subpixel True
        yalign 1.0
        linear 4.0 yalign 0.2
    with dissolve

    t "In order for the light to shine so brightly, the darkness must be present."
    
    ann "{i}Is this what she’s trying to say about this week’s theme? Is this also her personal discovery?{/i}"

    hide taylor with Dissolve(1.5)

    $ renpy.pause(0.5)

    show jacques up smile at center:
        zoom 1.35
        yalign 0.3
    with dissolve

    j talk "An intriguing performance by Taylor Warren. There’s an elegance to the simplicity of her voice, and yet she manages to convey ideas far deeper and profound. It certainly leaves me with many thoughts."
    j "It looks to be another tough decision this week, my audience. Let us cast our votes during the commercial break, and we’ll be back with the results. Who will make it to the final showdown? We shall see in a moment!"
    
    show jacques smile

    hide jacques with dissolve

    scene stage5far
    with dissolve

    ann "{i}The three of us wait anxiously at the prep room for the results. One of us will have to go while the other two make it to the finals. Would I be the one eliminated?{/i}"
    ann "{i}I don’t want to be the one. I want to stay.{/i}"
    ann "{i}But even if I lose here, I don’t think I’d have any regrets. If not for this show, I wouldn’t have met all these great people. I wouldn’t have met the real me. How else would I be able to face my dreams head-on?{/i}"
    ann "{i}I didn’t think I had the talent to pursue this road, but now, I know talent is something shaped by hard work and circumstances.{/i}"
    ann "{i}To hone a talent, you must seek out a platform for training it, then study and practice till it’s sharp as a sword, shine like a diamond.{/i}"
    ann "{i}I know I’ve done it this time, all thanks to the unforeseen opportunity and my own resilience from backing down.{/i}"
    ann "{i}I’m not afraid of failing, because that doesn’t make me a failure. I still succeeded in many things, for which I should be proud.{/i}"
    
    show director smile at center:
        zoom 1.4
        yalign 0.7
    with dissolve

    $ config.side_image_tag = "alice"

    an frown edgy "Why do I hate that look on his face...?"

    di talk "Time for you three to go."

    show director smile

    show cherry up frown edgy at right:
        zoom 0.97
        yalign 0.4
    show taylor up frown edgy at leftt behind director
    with dissolve
    
    c frowntalk "All three of us?"

    show cherry frown
    
    di talk "Yeah. It's more exciting that way, heh."

    show director smile
    
    scene stage5close
    with dissolve

    show taylor up frown edgy at right
    show cherry up smile edgy at left
    show jacques up smile at center:
        zoom 0.98
    with dissolve
    
    j talk "And we’re back with the results! How do you feel about this, Taylor?"

    show jacques smile
    
    t frowntalk "How should I feel about it?"

    show taylor frown
    
    a frowntalk "I'm nervous."
    a frown "{nw}"
    
    c frowntalk "Me too."

    show cherry frown
    
    j talk "You, Taylor? Are you nervous?"

    show jacques smile
    
    t frowntalk "Who wouldn't be?"
    
    show taylor frown

    j talk "But you look awfully calm about it. What’s your secret?"
    
    show jacques smile

    t talk "Satisfaction."
    t "This show was more than I bargained for. To have learned so much from the others, learned so much about myself... I think it’s already worth it. Going to the final is just icing on the cake."
    
    show taylor frown

    j talk "Still an enticing icing though, is it not?"
    
    show jacques smile

    t talk "I don't mind sweets."
    
    show taylor smile

    j talk "And Raisa, Alice, do you agree with Taylor too?"
    
    show jacques smile
    show cherry smile

    a talk "Yeah. I’m just happy to be here. Even if I have to step down before the final, I think I’ve already gained a lot from this experience."
    
    ann smile "{i}Cherry looks at me and grins, the nervousness finally parting a little to show her inner joy.{/i}"
    
    c talk "Uhm... it has been... really nice."
    c "I’ve always just sung for a single person. This is the first time I’ve sung for somebody else, for strangers I’ve never met."
    c "And though I still don’t know how to do it well, I think I’ve had fun just trying it out."
    c "I’ll try harder in the future! I want to sing for more people, and sing not just about myself, but about other people, other stories."
    
    show cherry smile

    j talk "Alright, and the person who will be eliminated from week 4 of Supernova is..."
    
    show jacques smile

    hide jacques
    hide cherry
    hide taylor
    with dissolve

    $ config.side_image_tag = ""

    ann "{i}{cps=30}The next moment is unreal.{/cps}{/i}"
    ann "{i}{cps=50}It’s all silent in my world as I watch Cherry bow and step down from the stage, leaving Taylor and I standing.{/cps}{/i}"
    ann "{i}{cps=50}I've made it to the finals.{/cps}{/i}"
    ann "{i}I... I...{/i}"
    ann "{i}...I don't know what you say...{/i}"

    show taylor up smile edgy at center:
        zoom 1.5
        yalign 0.3
    with dissolve
    
    t talk "Pleased to be your opponent in the grand finale. I look forward to our battle of voices, Alice."
    
    ######### end week 4 WIN
    
    
    
    
################################################
################ Contest Elimination (weeks 1-4)

label eliminated:
    
    ann "{i}Our performances have ended. Here I am, standing on the stage, facing elimination.{/i}"
    ann "{i}I have worked hard these past weeks. Even though it was an unexpected opportunity to participate in this contest, I think I’ve made the most out of it.{/i}"
    ann "{i}But somewhere deep in my heart, I know I still need a little more of something to push past this round.{/i}"
    ann "{i}A little more skill? A little more enthusiasm? A little more...of myself?{/i}"
    ann "{i}I have yet to find a unique path to the top. There must be something that only my voice can express.{/i}"
    ann "{i}I just haven't found it yet.{/i}"
    
    j "And the person who will be eliminated this week is..."
    j "Sorry, Alice. You have been eliminated."
    
    ann "{i}As I thought, I'm the one to go.{/i}"
    ann "{i}I calmly step down from the stage, its bright lights falling behind me as I move into the darkness.{/i}"
    ann "{i}I would be lying if I say I have no regrets. I do, actually. I know I could’ve done better.{/i}"
    ann "{i}But it’s too late. There’s nothing I can do about this now.{/i}"
    ann "{i}Still, that doesn’t mean I will give up. This experience has made me realize that my dream of becoming an idol is still real as ever.{/i}"
    ann "{i}I clench my fist. I will be back.{/i}"
    ann "{i}I will make my dream come true someday!{/i}"
    
    ##### end elimination weeks 1-4
    
    
##################################################
#################################### FINAL CONTEST

label finalcontest:

    ann "{i}I'm finally here.{/i}"
    ann "{i}The end of the road, the last showdown of this contest.{/i}"
    
    j "Welcome to week 5 of the Supernova idol contest, the final stage of the competition for the coveted throne of your next superstar!"
    j "Taylor Warren, a veteran in the music industry. While she has stayed behind the scenes till now, she is a well-known composer of many songs."
    j "Her audience is spread across the globe, many praising the strong emotions she manages to evoke in her colorful melodies and driving rhythms."
    j "By entering this contest, she has taken off on what she describes as a path of self-discovery. Now, she is not only writing music for us, but also performing it live, showing us exactly the messages she wishes to convey."
    j "What are her inspirations? What are her motivations? Now, she will lay her soul before us. Taylor, the stage is yours!"
    
    ann "{i}We have walked a long way.{/i}"
    ann "{i}Jacque is right. It really has been a month of sweat and tears. We have met many people along the way, but now, this is a path that we must take alone.{/i}"
    ann "{i}The audience is watching us. Our friends and family are watching us. We are surrounded, but the moment you set foot on the stage, you are by yourself. You are in a place where they can’t reach you.{/i}"
    ann "{i}Still, you must shine for them, like the sun and moon, stars and meteors. You are high above the people, but you must make them gravitate towards you, show them the flame that burns in your heart, and use it to warm their hearts too.{/i}"
    ann "{i}That's what Taylor is doing now.{/i}"
    ann "{i}This is the first time I’ve seen her like this. She is no longer the quiet, sarcastic personality she once was, hiding behind a mop of dirty blond and thick glasses.{/i}"
    ann "{i}The creased shirt, pressed collar, crisp, clean lines of her suit - she is positively radiant today. And that’s just her appearance. Her demeanor, her voice, they are all bright and powerful.{/i}"
    ann "{i}She has left her shell far behind her. This is the new Taylor. The real Taylor. And the talent she is showcasing is absolutely amazing!{/i}"
    ann "{i}The guitar riffs are sick. The drums are pounding with my heartbeat. Her voice starts deep and rises like a bird taking flight. Not just any bird. He’s an eagle, soaring high, spreading its wings to glide the azure skies.{/i}"
    ann "{i}The floodlights, reflecting golden off her hair, are like sunshine crowning eagle feathers. It’s so bright that I must squint against her light. This surely is proof of her kingship over the heavens.{/i}"
    ann "{i}Even though Taylor has always been so talented, I think she couldn’t have performed like this without the struggles she has been through over the past weeks.{/i}"
    ann "{i}Only after a long night does the light of dawn appear beautiful. Only after a cold winter does spring feel warm. Without loss, there is no gain. Without falling down, you never learn how to stand back up.{/i}"
    ann "{i}Taylor has regretted. Taylor has second-guessed her own decisions. She wondered whether she should really have been here.{/i}"
    ann "{i}She asked if she were not the one standing on the stage, if someone else took her place instead, would the contest nights be more interesting, more entertaining to watch.{/i}"
    ann "{i}Was she more suitable for standing backstage, watching others sing for her, or should she be the one out there, singing for us?{/i}"
    ann "{i}I’m sure those were tough questions. I think she thought long and hard about them. There were times when her answers took her wandering backwards, regressing to depression and self-pity.{/i}"
    ann "{i}But I’m proud to say that I, along with the others, have helped show her the way.{/i}"
    ann "{i}There is nobody who knows you better than yourself. If you were too afraid to sing your own songs, nobody would be able to do it for you.{/i}"
    ann "{i}Life is full of hardships. We will face pain, we will face loss. But if we back down, we would just be standing in place, trapped where these dark feelings will continue to consume us.{/i}"
    ann "{i}Though moving forward may sometimes feel like clawing through tangles of barbed vines, our bodies may feel like they’re being torn from outside in and inside out, we must continue through these obstacles.{/i}"
    ann "{i}Searing heat, freezing cold, dark nights, uncertain futures - these are all scary images that may flash through our minds, but in overcoming them, we become stronger.{/i}"
    ann "{i}We are swords. We need to be abraded again and again to be polished into sharp blades.{/i}"
    ann "{i}Taylor screams her hopes into the audience. They roar with her, captured by her brilliance. We all want a better world. It is what we as humans are wired to wish for.{/i}"
    ann "{i}Taylor connects these dreams together and gives sound to it, amplifies it for more and more people to hear. It is no longer her personal strength that is sustaining her, but the strength of many, many more of her supporters.{/i}"
    ann "{i}That is what an idol should be. She is not afraid of her own dreams. She shows them to us. She shoulders our dreams along with his.{/i}"
    ann "{i}She makes us one. United by our common desires.{/i}"
    
    j "Thank you very much for your performance, Taylor. A most fitting climax for her month-long journey here at Supernova."
    j "Our remaining contestant is Alice Carroll. Unlike Taylor, she has little formal musical training. That is not to say she is unfamiliar with the industry. According to her, she has always been fascinated with idol groups, just like you and me."
    j "She would sing to their songs and dance to their moves, dress like them and hold her own secret concerts from the top of her bed. Her audience? No one but herself."
    j "Like any rational young person, she saw little chances of succeeding in this competitive industry. Instead of pursuing a career on the stage, she resigned herself to one behind it, interning at a television production company."
    j "Her work was hard, but very mundane and underappreciated. She carried camera cables and lifted heavy equipment, she ran whatever errands were requested of her."
    j "What could prompt her to do all this for the meagre pay she was offered, if not for the slight glimmer of hope that she would one day stand atop the stage for an audience other than herself?"
    j "Finally, she realized that she must grasp this hope else it too would eventually fade. Thus, this is why she is now here to sing for us. Alice, this is now your stage. Please make the most out of it!"
    
    ann "{i}Jacque smiles at me. It’s a little hard to believe that he has made such an impressive speech from the little blurb he requested for me to submit.{/i}"
    ann "{i}Of course, this is his job, but I also know that he managed to speak to my heart because that’s what I’ve shown him with my hard work, with my performances. I’ve spoken to everybody with my voice.{/i}"
    ann "{i}Today, the last fireworks will be set. Regardless of outcome, this will be my last performance at Supernova, but I know it will not be my last public performance ever. I’ve already made up my mind.{/i}"
    ann "{i}No matter what, I’ll not bat down my own dream again. I will pursue it. I will shine for all my fans beneath this stage!{/i}"
    
##########################
############### WIN FINALE
label finalwin:

    ann "{i}I feel more at ease on this stage than I have ever before.{/i}"
    ann "{i}All the pressure of winning is just gone. It’s ironic, considering this is my final performance.{/i}"
    ann "{i}The heavy gown should be weighing me down, but my body feels light. My voice, which needs to be projected to the very back of this room, comes just as easily.{/i}"
    ann "{i}It’s crystal clear, like a cool mountain stream meandering through rocky beds and emerald grasses.{/i}"
    ann "{i}I remember the first time I’ve been here. I remember standing at the way back where it’s difficult to even see who is on the stage.{/i}"
    ann "{i}At that time, I would never have thought I would even get the chance to stand here, and when I was presented with the opportunity, I didn’t even want to accept it.{/i}"
    ann "{i}To accept myself...{/i}"
    ann "{i}I thought I was silly. I thought I was immature. To become an idol? What a joke. That’s like a middle-schooler’s daydream! I’m an adult now. I need realistic goals to ensure that I can make a living for myself.{/i}"
    ann "{i}What I failed to realize was that being an idol is a realistic dream for me.{/i}"
    ann "{i}Sure, not just anybody can do it. It’s a sad and unfortunate thought. But would I, Alice Carroll, be better off with a different occupation? Would I be better suited as a lawyer or doctor or bakery owner?{/i}"
    ann "{i}I’ve always loved to sing. My strength is perseverance. I just so happened to be endowed with the qualities of an idol. All I lacked was the confidence to pursue this career.{/i}"
    ann "{i}Not anymore!{/i}"
    ann "{i}I don’t even need to draw them to me. The audience is naturally drawn.{/i}"
    ann "{i}I can see it in their faces, now not just dark shadows that I don’t quite dare to stare at, but individuals, some of whom I recognize from previous weeks, some who I’m seeing for the first time.{/i}"
    ann "{i}As I braid the melody into the harmony, weaving the sound waves in and out with a flawless beat, I can see my audience’s faces of awe. They are entranced by my voice, so rich and colorful, bright and warm.{/i}"
    ann "{i}I don’t think I’m the same brand of idol as Taylor is. I don’t think I can stand out with the same kind of dominance. But there are some things that only I have.{/i}"
    ann "{i}I can’t shoulder everybody’s dreams, but I have the capability of living my own dream, and giving others the strength to live theirs.{/i}"
    ann "{i}My dancing steps take me to the very edge where I can see Cherry jumping up from the front row, trying to reach me. I can see Mary break into a wide smile, her golden eyes gleaming with delight.{/i}"
    ann "{i}I know, when I’m up here, I become endowed with an energy that overflows the confines of my own self.{/i}"
    ann "{i}Maybe this energy is not solely my own. Maybe it takes many people to make me who I am today. But regardless, this energy becomes something I can grasp, I can amplify and give out to those willing to receive it.{/i}"
    ann "{i}Taylor calls it an inspiration. Perhaps that’s what it is.{/i}"
    ann "{i}I’m not an idol who towers above all. I’m an idol who inspires!{/i}"
    
    a "You can be yourself too!"
    
    ann "{i}I shout into the crowd, holding out my hand. In my mind’s eye, I see flowers blooming from my fingers, so ripe their petals catch the wind and scatter into the seats below.{/i}"
    ann "{i}Pink and white, violet and orange, warm colors fill the room with feelings of spring, a season of new encounters, new beginnings.{/i}"
    ann "{i}The flowers may be imaginary, but the little squares of colored tissue paper that rain down into my hands are not.{/i}"
    
    k "Aren’t you being biased here? I thought you didn’t like her."
    
    di "I’m just giving the audience exactly what they want to see."
    
    k "It is beautiful, seeing the final result of your own creation."
    
    di "I won’t be so arrogant to call her my creation."
    
    k "Not just my sole creation, of course. Idols are created by all their supporters."
    k "Our wishes, our aspirations, all embodied in her very being. We see a piece of ourselves in her, which is why we can’t help but fall in love with her image."
    
    di "Typical self-centered thinking from you, Katja."
    
    k "As though you’re one to speak."
    
    di "You know me too well."
    
    ann "{i}There is no performance that belongs to a single person. To perform, there must be a recipient of what you’re trying to express. Otherwise, it is nothing but an inner musing.{/i}"
    ann "{i}This performance here is not really mine. At least not mine alone. The stage crew, the audience, the makeup artist, the organizers...everybody plays a part.{/i}"
    ann "{i}Then what's my role?{/i}"
    ann "{i}To bring it all together, of course!{/i}"
    ann "{i}Come to think of it, maybe it was wrong to compare idols to light. We aren’t the sun. We’re just objects to be shone upon.{/i}"
    ann "{i}Basked in everybody’s hopes, we become an existence that inspires those watching us to pursue things that they once deemed impossible.{/i}"
    ann "{i}Because they are the ones who made an impossibility like myself become reality.{/i}"
    ann "{i}But these are all just philosophical blurbs that can wait for another day.{/i}"
    ann "{i}At this moment, all I want to do is sing.{/i}"
    ann "{i}Sing to my heart’s content. Sing with everything I have.{/i}"
    ann "{i}The lights are bright. The stage beneath me so large and beautiful.{/i}"
    ann "{i}My audience’s cheers warm me from within. I’m so proud. I’m so proud to be here.{/i}"
    ann "{i}I wish this moment could last forever. I’ve never been so happy.{/i}"
    ann "{i}Thank you, everybody. Thank you for letting me stand here before you. Thank you for giving me your attention.{/i}"
    ann "{i}Thank you for letting me discover myself.{/i}"
    ann "{i}Just being here, singing for you...{/i}"
    ann "{i}It's all I desire now.{/i}"
    
    jump credits
    
    
#####################################
###################### After Credits
    
label epilogue:
    
    ann "{i}Oh shit, I'm gonna be late!{/i}"
    ann "{i}It’s all my own fault. I shouldn’t have been so damn excitable that I couldn’t fall asleep all night, then ended up dozing off on my chair just three hours before showtime!{/i}"
    ann "{i}Boss is so gonna kill me.{/i}"
    
    m frowntalk "Relax, Alice. You fidgeting around like this makes it hard for me to draw your brows."
    
    a "Sorry... I'll try not to."
    
    m frowntalk "Then again, if you weren’t so nervous, the makeup artist would be able to do this in my stead. Seriously, when have I become your personal assistant?"
    
    a "Sorry to always rely on you, Mary. But...you’re the only one who can calm me down, you see, so..."
    
    m frowntalk "I know, I know. Now just sit back and stop curling up like a pillbug. I’ll finish this in no time."
    
    di "You girls done?"
    
    m frowntalk "Just a moment."
    
    di "Yeah, yeah, Superstar. Hurry it up, alright?"
    
    m frowntalk "I'm trying!"
    
    a "I'm so sorry..."
    
    ann "{i}Shortly after the director leaves us, Mary finishes lining my right brow.{/i}"
    
    a "I think it’s good. Both brows are even."
    
    m frowntalk "Aren’t your expectations low..."
    
    a "Can’t help it. I’ve gotta go!"
    
    ann "{i}I give Mary’s hands a squeeze and dash off for the stage, leaving her sighing in exasperation.{/i}"
    ann "{i}I know she just wants the best for me. I’m so lucky to have someone like her by my side.{/i}"
    
    with fade
    
    a "Is it starting?"
    
    k "Made it just before I was about to send out my lackeys to hunt you down, dead or alive."
    
    j "Welcome to season two of your favorite idol show, Supernova! Are you ready for another month of heart-wrenching, blood-boiling struggles for the throne of your next superstar?"
    j "Yes! I know I’m ready! And she is too! Introducing our winner from season one - she will start us off with the first song of this new festival!"
    
    ann "{i}I make my way up the steps. The familiar light falls upon me.{/i}"
    ann "{i}Tay, Mary, Cherry... they’re all watching. I wave to them, feeling their cheers pour energy into my heart.{/i}"
    
    j "This is your idol, Alice Carroll......"
    
    ###### end epilogue
    
    
########################
############ LOSE FINALE
label finallose:    

    ann "{i}The final stage.{/i}"
    ann "{i}After the past few weeks, I feel confident about myself.{/i}"
    ann "{i}I have worked hard. Even though it was an unexpected opportunity to participate in this contest, I think I’ve made the most out of it.{/i}"
    ann "{i}I have the skill. I have the enthusiasm. I should have everything already.{/i}"
    ann "{i}But Taylor's performance really shook me.{/i}"
    ann "{i}How can she find the strength to not only overcome her own personal obstacles, but to also shoulder the audience’s dreams on her back?{/i}"
    ann "{i}I... don't know.{/i}"
    ann "{i}The music comes off easily from my tongue. I feel its melody. I feel its beat. I echo my idealized version of the song into the crowd.{/i}"
    ann "{i}It should be perfect, but for some reason, I still find it lacking...{/i}"
    ann "{i}Where have I gone wrong?{/i}"
    
    j "Thank you, Alice. That was another beautiful performance from you."
    j "Now, we shall hear from the audience. Who is the idol in their hearts? Voting starts now!"
    
    ann "{i}My heart beats heavily. I can hardly breathe as I watch the people in the stands press on their keypads. I’m sure thousands more are currently casting their votes online.{/i}"
    ann "{i}It is a strange feeling, because you know what? I actually already know the result before it is announced.{/i}"
    ann "{i}I’m part of the audience too, afterall. I know what they are thinking.{/i}"
    
    j "And now, the results are in my hands. The winner of your favorite idol show, Supernova, is..."
    j "Taylor Warren!"
    
    ann "{i}I hear the crowd roar in approval. I nod, clapping with them. They have made the right decision.{/i}"
    
    a "That was amazing, Taylor. What you did out here was absolutely amazing."
    
    t "I couldn’t have done it without you."
    
    ann "{i}She grabs my hand and shakes it hard. Her smile is a bright one, but there is something strange about her eyes... is it perhaps disappointment?{/i}"
    ann "{i}At what?{/i}"
    
    a "Taylor, are you okay?"
    
    t "Ahh... I was just thinking about your... nevermind."
    t "I think it was close, the competition between you and me. One day, I’m sure you’ll become a wonderful idol."
    
    ann "{i}That one day is just not today.{/i}"
    
    a "I will try harder from now on. I’m sure I’ll succeed in the future."
    
    t "Yeah. I have faith in you."
    
    ann "{i}I calmly step down from the stage, its bright lights falling behind me as I move into the darkness.{/i}"
    ann "{i}I would be lying if I say I have no regrets. I do, actually. I know I could’ve done better.{/i}"
    ann "{i}But it’s too late. There’s nothing I can do about this now.{/i}"
    ann "{i}Still, that doesn’t mean I will give up. This experience has made me realize that my dream of becoming an idol is still real as ever.{/i}"
    ann "{i}I clench my fist. I will be back.{/i}"
    ann "{i}I will make my dream come true someday!{/i}"
    
    jump credits
    with fade




######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################


###################################     Week 1

default currentScreen = "week1minigame"

screen week1minigame:
    textbutton _("Hello my love") xalign 0.05 yalign 0.2 text_size 40 at word1 action SetVariable("phrase1", True)
    textbutton _("Goodbye my friend") xalign 0.3 yalign 0.4 text_size 40 at word2 action SetVariable("phrase2", True)
    textbutton _("Hello new world") xalign 0.6 yalign 0.6 text_size 40 at word3 action SetVariable("phrase3", True)
    textbutton _("Will I see you again?") xalign 0.9 yalign 0.8 text_size 40 at word4 action SetVariable("phrase4", True), If(phrase1 and phrase2 and phrase3, true = Jump("week1round2"), false = Jump("failed"))

    timer 8.0 action Jump("failed")


label week1round2:
    $ phrase1 = False
    $ phrase2 = False
    $ phrase3 = False
    $ phrase4 = False

    $ currentScreen = "week1minigame2"

    call screen week1minigame2


screen week1minigame2:
    textbutton _("The times are changing") xalign 0.5 yalign 0.2 text_size 40 at word1 action SetVariable("phrase1", True)
    textbutton _("But my heart stands still") xalign 0.5 yalign 0.4 text_size 40 at word2 action SetVariable("phrase2", True)
    textbutton _("Your eyes are listless") xalign 0.5 yalign 0.6 text_size 40 at word3 action SetVariable("phrase3", True)
    textbutton _("Can I change your will?") xalign 0.5 yalign 0.8 text_size 40 at word4 action SetVariable("phrase4", True), If(phrase1 and phrase2 and phrase3, true = Jump("week1round3"), false = Jump("failed"))

    timer 8.0 action Jump("failed")


label week1round3:
    $ phrase1 = False
    $ phrase2 = False
    $ phrase3 = False
    $ phrase4 = False

    $ currentScreen = "week1minigame3"

    call screen week1minigame3


screen week1minigame3:
    textbutton _("The winds are growing stronger") xalign 0.05 yalign 0.25 text_size 40 at word1 action SetVariable("phrase1", True)
    textbutton _("Yet I still remain") xalign 0.3 yalign 0.75 text_size 40 at word2 action SetVariable("phrase2", True)
    textbutton _("If you won't come with me") xalign 0.6 yalign 0.35 text_size 40 at word3 action SetVariable("phrase3", True)
    textbutton _("Then I'll leave you in the rain") xalign 0.9 yalign 0.85 text_size 40 at word4 action SetVariable("phrase4", True), If(phrase1 and phrase2 and phrase3, true = Jump("week1win"), false = Jump("failed"))

    timer 8.0 action Jump("failed")


label failed:
    $ slow += 1

    if slow >= 3:
        jump eliminated
    else:
        $ rand = renpy.random.randint(1,5)

        if rand == 1:
            an "Dammit, that's not right!"
        if rand == 2:
            an "No, no, not the right order!"
        if rand == 3:
            an "Crap, maybe they didn't notice that slip-up-"
        if rand == 4:
            an "Let me try that again!"
        if rand == 5:
            an "Wait, wrong line!"

        call screen currentScreen



######      Week 2 was deleted to cut scope


##############################      Week 3



screen week3minigame:
    textbutton _("The sun has hidden") xalign 0.25 yalign 0.2 text_size 40 at word1 action SetVariable("phrase1", True)
    textbutton _("The skies are gray") xalign 0.05 yalign 0.4 text_size 40 at word2 action SetVariable("phrase2", True)
    textbutton _("I can feel the chill coming") xalign 0.65 yalign 0.6 text_size 40 at word3 action SetVariable("phrase3", True)
    textbutton _("But I'll brace through it all") xalign 0.15 yalign 0.8 text_size 40 at word4 action SetVariable("phrase4", True), If(phrase1 and phrase2 and phrase3, true = Jump("week3round2"), false = Jump("failed"))

    timer 8.0 action Jump("failed")


label week3round2:
    $ phrase1 = False
    $ phrase2 = False
    $ phrase3 = False
    $ phrase4 = False

    $ currentScreen = "week3minigame2"

    call screen week3minigame2


screen week3minigame2:
    textbutton _("I can still hear your voice") xalign 0.1 yalign 0.8 text_size 40 at word1 action SetVariable("phrase1", True)
    textbutton _("Whispering through the wind") xalign 0.7 yalign 0.6 text_size 40 at word2 action SetVariable("phrase2", True)
    textbutton _("The cold air reminds me") xalign 0.15 yalign 0.4 text_size 40 at word3 action SetVariable("phrase3", True)
    textbutton _("Even if we don't meet again...") xalign 0.7 yalign 0.2 text_size 40 at word4 action SetVariable("phrase4", True), If(phrase1 and phrase2 and phrase3, true = Jump("week3round3"), false = Jump("failed"))

    timer 8.0 action Jump("failed")


label week3round3:
    $ phrase1 = False
    $ phrase2 = False
    $ phrase3 = False
    $ phrase4 = False

    $ currentScreen = "week3minigame3"

    call screen week3minigame3


screen week3minigame3:
    textbutton _("When the snow falls") xalign 0.1 yalign 0.1 text_size 40 at word1 action SetVariable("phrase1", True)
    textbutton _("My heart will skip again") xalign 0.25 yalign 0.25 text_size 40 at word2 action SetVariable("phrase2", True)
    textbutton _("I will remember all our days again") xalign 0.1 yalign 0.50 text_size 40 at word3 action SetVariable("phrase3", True)
    textbutton _("Those memories will be with me") xalign 0.35 yalign 0.75 text_size 40 at word4 action SetVariable("phrase4", True)
    textbutton _("Until I'm old") xalign 0.1 yalign 0.95 text_size 40 at word5 action SetVariable("phrase5", True), If(phrase1 and phrase2 and phrase3 and phrase4, true = Jump("week3win"), false = Jump("failed"))

    timer 8.0 action Jump("failed")





#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################





default phrase1 = False
default phrase2 = False
default phrase3 = False
default phrase4 = False
default phrase5 = False


default slow = 0
default waitTime = 5

transform word1:
    alpha 0

    pause 1

    ease 1 alpha 1.0

    pause waitTime

    ease 1 alpha 0

transform word2:
    alpha 0

    pause 2

    ease 1 alpha 1.0

    pause waitTime

    ease 1 alpha 0

transform word3:
    alpha 0

    pause 3

    ease 1 alpha 1.0

    pause waitTime

    ease 1 alpha 0

transform word4:
    alpha 0

    pause 4

    ease 1 alpha 1.0

    pause waitTime

    ease 1 alpha 0

transform word5:
    alpha 0

    pause 5

    ease 1 alpha 1.0

    pause waitTime

    ease 1 alpha 0


screen testMinigame1:
    textbutton _("Hello my love") xalign 0.05 yalign 0.2 text_size 40 at word1 action SetVariable("phrase1", True)
    textbutton _("Goodbye my friend") xalign 0.3 yalign 0.4 text_size 40 at word2 action SetVariable("phrase2", True)
    textbutton _("Hello new world") xalign 0.6 yalign 0.6 text_size 40 at word3 action SetVariable("phrase3", True)
    textbutton _("Will I see you again?") xalign 0.9 yalign 0.8 text_size 40 at word4 action SetVariable("phrase4", True), If(phrase1 and phrase2 and phrase3, true = Jump("testDone"), false = Jump("testfailed"))

    timer 8.0 action Jump("testfailed")

label testDone:
    a talk "I did it!"

    $ phrase1 = False
    $ phrase2 = False
    $ phrase3 = False
    $ phrase4 = False

    return

label testfailed:
    $ slow += 1

    if slow >= 3:
        jump eliminated
    else:
        $ rand = renpy.random.randint(1,5)

        if rand == 1:
            an "Dammit, that's not right!"
        if rand == 2:
            an "No, no, not the right order!"
        if rand == 3:
            an "Crap, maybe they didn't notice that slipup-"
        if rand == 4:
            an "Let me try that again!"
        if rand == 5:
            an "Wait, wrong line!"

        call screen testMinigame1



#######################################################################################################################
#######################################################################################################################



# label testMinigame2:
#     $ ui.timer(8.0, ui.jumps("too_slow"))
    
#     python:
#         line = renpy.input("Hello my love")
#         line = line.strip()
        
#     if line == 'Hello my love':
#         jump line1C
        
#     if line == 'hello my love':
#         jump line1C
        
#     else:
#         jump testMinigame


# label line1C:
#     $ ui.timer(8.0, ui.jumps("too_slow"))
    
#     python:
#         line = renpy.input("Goodbye my friend")
#         line = line.strip()
        
#     if line == 'Goodbye my friend':
#         jump line2C
        
#     if line == 'goodbye my friend':
#         jump line2C
        
#     else:
#         jump line1C


# label line2C:
#     $ ui.timer(8.0, ui.jumps("too_slow"))
    
#     python:
#         line = renpy.input("Hello new world")
#         line = line.strip()
        
#     if line == 'Hello new world':
#         jump line3C
        
#     if line == 'hello new world':
#         jump line3C
        
#     else:
#         jump line2C


# label line3C:
#     #timer 10 action Jump("too_slow")
#     $ ui.timer(8.0, ui.jumps("too_slow"))
    
#     python:
#         line = renpy.input("Will I see you again?")
#         line = line.strip()
        
#     if line == 'Will I see you again?':
#         jump done
        
#     if line == 'will I see you again?':
#         jump done
        
#     if line == 'Will I see you again':
#         jump done
        
#     if line == 'will I see you again':
#         jump done

#     else:
#         jump line3C

# label too_slow:
#     $ slow += 1

#     if slow < 3:
#         a "Ack, I stumbled!"

#         jump testMinigame

#     else:
#         a "Oh no.... I completely failed...."

#         $ renpy.quit()


# label done:
#     a "I... I can't believe it..... I finished the song perfectly!"


