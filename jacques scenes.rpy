##“Jacques Gets Deep Over Coffee” scene

label lounge:

    label jacquescoffee:

        scene loungeday
        with fade

        $ config.side_image_tag = ""

        an "For some reason, I’m not feeling especially hungry right now."
        an "But still, the atmosphere of the lounge seems like exactly what I need."
        an "As I step into the room, I see Jacques staring out the window, holding a cup of coffee."

        menu:
            "Morning, Jacques!":
                jump jacquescoffeechat1

            "Uh...{i}Bon matin{/i}?":
                jump jacquescoffeechat2

            "Where’d you get that coffee?":
                jump jacquescoffeechat3

        label jacquescoffeechat1:

            $ config.side_image_tag = "alice"

            an "Jacques turns towards me."

            show jacques down smile at center:
                zoom 1.2
                yalign 0.3
            with dissolve

            j down talk "Good morning, Alice."
            j up "And what a {i}lovely{/i} morning it is!"

            show jacques smile

            a down talk "Well, the weather {i}does{/i} seem pretty nice out."
            a up "But I still think I’ll be staying inside for a while."
            a smile "{nw}"

            j down talk "Looking after your skin? Or just taking a little rest?"

            menu:
                "I don’t want to get sunburned.":
                    jump jacqueschatskincare

                "I’m conserving my energy.":
                    jump jacqueschathobby

                "Inside is where the food is.":
                    jump jacqueschatmillenialle

            label jacqueschatskincare:

                j down talk "{i}Vraiment?{/i} Well, that’s certainly very mature of you."
                j up frowntalk "Too many people these days forget about the kind of damage the sun can do, especially when you’re not properly prepared."

                show jacques frown

                an down frown "Is he...giving me a lecture on skincare?"

                j talk "Nevertheless, I’m sure you’ve heard all this stuff before."
                j "I won’t waste your time with the full TIM Talk."

                show jacques smile

                a up talk "I appreciate that."
                a smile "{nw}"

                jump jacquesmorningpart1

            label jacqueschathobby:

                j down frowntalk "Hmm, {i}pas mal{/i}."
                j up "It makes sense that you’d want to save your energy for the big contest, {i}non{/i}?"
                j "But at the same time, it can also be a good idea to spread your wings and try something new."
                j "I believe Taylor, for example, has been going on morning jogs to keep herself active."
                j "Miss Mary has been taking the occasional shopping trip to sharpen her sense of style."
                j "And of course, Ma Belle Cherry has been, ah..."
                j "Actually, I think she’s mostly spending time with the animals, and sort of...{i}meandering{/i} around the grounds."
                j "Perhaps you need to find yourself your own little hobby, just for when you don’t feel like practicing."

                show jacques smile

                an down frown "Hmm...he’s got a point."

                jump jacquesmorningpart1

            label jacqueschatmillenialle:

                j down frowntalk "That was...unusually honest."
                j up talk "But I suppose that’s {i}Une Millenialle{/i} thing, isn’t it?"
                j "Always talking about food and sleep and whatnot?"

                show jacques smile

                a down frowntalk "Hey, {i}everyone{/i} needs to eat and sleep."
                a up talk "And also, I’m 99/%/ sure \”Millenialle\” isn’t even a real French word."
                a smile "{nw}"

                j talk "Hmm, very true."

                show jacques smile

                jump jacquesmorningpart1

        label jacquescoffeechat2:

            $ config.side_image_tag = "alice"

            an "Jacques turns around, smiling, but raises a finger."

            show jacques down smile at center:
                zoom 1.2
                yalign 0.3
            with dissolve

            j talk "Actually, \”{i}bonjour{/i}\” works better, here."

            show jacques up smile

            a down frowntalk "Oh? I thought I read somewhere that \”matin\” means \”morning\”..."
            a down frown "{nw}"

            j talk "True, but in French, most people say \”bonjour\”, unless it’s later in the evening."

            a down talk "Huh. The more you know, I guess."
            a up smile "{nw}"

            jump jacquesmorningpart1

        label jacquescoffeechat3:

            $ config.side_image_tag = "alice"

            an "Jacques turns around, raising his cup."

            show jacques down smile at center:
                zoom 1.2
                yalign 0.3
            with dissolve

            j down talk "Oh, this?"
            j up "This is my morning {i}Noisette{/i}, Alice."
            j "~It’s like sunrise in a cup.~"
            j "And to answer your question, I made it myself."

            show jacques smile

            an down frown "{i}N...Nwazzit?{/i} I’ve never heard of it before."

            a down frowntalk "Ah, what {i}is{/i} it, though? Like, what type of coffee?"
            a down frown "{nw}"

            j down talk "{i}Noisette?{/i} It means \”hazelnut\”."
            j "It’s a shot of espresso, with four drops of pure, organic cream."

            show jacques up smile

            an down frown "Wait, I think I’ve heard of that before."

            a up talk "Isn’t that called a Macchiato?"
            a smile "{nw}"

            show jacques down frown

            an down frown "Jacques looks almost offended."

            j down frowntalk "{i}Macchiato{/i} is Italian. {i}Noisette{/i} is French."

            show jacques down frown

            a down frowntalk "And what’s the difference?"
            a frown "{nw}"

            j up talk "It’s {i}French.{/i}"

            show jacques up smile

            a down talk "Oh. Okay."
            a up smile "{nw}"

            jump jacquesmorningpart1

        label jacquesmorningpart1:

            j up talk "Anyway, how’re you doing this morning?"

            show jacques smile

            a down talk "Well..."
            a "To be honest, I’m still a bit overwhelmed by this whole thing."
            a frown "{nw}"

            j down frowntalk "The contest, you mean?"

            show jacques frown

            a up talk "Yeah. Some days I still can’t believe that I’m a finalist on {i}Supernova{/i}."
            a smile "{nw}"

            j up talk "Well, sometimes show business can feel like a fairy tale."
            j "~The lowly, wallflower intern who’s {i}miraculously{/i} given a chance to shine...~"
            j "It’s almost like {i}Cinderella, non?{/i}"

            show jacques smile

            an down frown "At least he didn’t say {i}Alice in Wonderland...{/i}"

            j down talk "But you {i}do{/i} seem a little {i}out of sorts{/i}...If you like, I could stand to sit and chat for a while."

            menu:
                "It might be nice to sit and talk for a while...":
                    jump jacqueschat2

                "Actually, I’m inspired to go outside for some reason.":
                    jump jacqueschat2end

            label jacqueschat2:

                j up talk "So, what exactly has been on your mind?"

                show jacques smile

                a down frowntalk "Hmm..."

                menu:
                    "I’m worried about Mary.":
                        jump somethingaboutmary

                    "I’ve been thinking about Cherry.":
                        jump shesmycherrypie

                    "I just don’t {i}get{/i} Taylor.":
                        jump letstalktaylor

                label somethingaboutmary:

                    a down frowntalk "Actually, I’ve been thinking about Mary, lately."
                    a frown "{nw}"

                    j down frowntalk "Oh?"

                    show jacques down smile

                    a frowntalk "Well, she just seems so {i}serious{/i} about this."
                    a frown "{nw}"

                    j up talk "Aren’t you all?"

                    show jacques smile

                    a frowntalk "Well, yeah. But Mary seems...different."
                    a "Maybe it’s just me, but I feel like she’s got a {i}lot{/i} riding on the contest."
                    a "She seems so determined to win that...I’m almost afraid to find out how she’ll react if she doesn’t."
                    a frown "{nw}"

                    j down talk "You think she might have a Good Old Fashioned Reality TV Breakdown?"

                    show jacques smile

                    a frowntalk "..."

                    menu:
                        "Yes.":
                            jump marybreakdownyes

                        "No.":
                            jump marybreakdownno

                        "I’m not sure.":
                            jump marybreakdownmaybe

                    label marybreakdownyes:

                        a down frowntalk "I’m afraid she’s going to go {i}nuclear{/i}."
                        a frown "{nw}"

                        an "Jacques raises his eyebrows."

                        show jacques down frown

                        j frowntalk "Flipping tables, throwing chairs, that sort of thing?"

                        show jacques frown

                        an "I nod."

                        j frowntalk "Well, as much as it {i}would{/i} make for {i}fantastic{/i} television..."
                        j up talk "I believe Miss Mary is actually a lot more...even keeled than you might suspect."
                        j down "Sure, she’s a bit of a...{i}princess{/i}, shall we say..."
                        j up "But I think that losing may actually be good for her, in the end."

                        show jacques smile

                        a frowntalk "You mean...losing might actually make her happier?"
                        a "I’d...never really thought of it like that."
                        a frown "{nw}"

                        j talk "Mmm-hmm. Not that I want {i}any{/i} of my Dear Contestants to fail, after all."
                        j "It’s my job to support you all equally, as your host {i}sans pareil{/i}."

                        show jacques smile

                        jump jacqueschat2part2

                    label marybreakdownno:

                        a down talk "I don’t think she’ll have a {i}breakdown{/i}, I just..."
                        a frowntalk "I don’t want to see her get her feelings hurt."
                        a frown "{nw}"

                        j down frowntalk "That’s...very considerate, considering she’s your competitor."

                        show jacques frown

                        a up frowntalk "Hey, just because we’re competing doesn’t mean we’re not friends."
                        a frown "{nw}"

                        j up talk "Do you think {i}she{/i} sees you as a friend?"

                        show jacques smile

                        a up talk "Maybe."
                        a down frowntalk "Then again, maybe not."
                        a up talk "But either way, I’m {i}still{/i} going to be nice to her."
                        a smile "{nw}"

                        j down frowntalk  "Well, that’s very...{i}professionel{/i} of you."

                        show jacques up smile

                        an "He winks."

                        j talk "You’re acting like a star already."

                        show jacques smile

                        a down talk "Was that...{i}sarcasm{/i}?"
                        a up smile "{nw}"

                        j talk  "Oh, I’m {i}never{/i} sarcastic. I simply call them how I see them."

                        show jacques smile

                        a talk "Always the dazzling host, eh?"
                        a smile "{nw}"

                        j talk "{i}Exactement{/i}."

                        show jacques smile

                        jump jacqueschat2part2

                    label marybreakdownmaybe:

                        a down frowntalk "I...honestly don’t know what she’s going to do."
                        a "I just hope that she’s going to be {i}okay{/i}."
                        a frown "{nw}"

                        j down frowntalk "That’s very sweet of you, worrying about your competitor like that."

                        show jacques frown

                        a frowntalk "Well, honestly...When we’re not on stage, I kind of {i}forget{/i} that we’re competing."
                        a frown "{nw}"

                        j frowntalk "You just see her as a random girl you’ve recently met?"

                        show jacques frown

                        a frowntalk "Sort of, yeah."
                        a up "When we’re eating breakfast, or if I run into her at the house, it doesn’t even occur to me that we’re trying to beat each other."
                        a frown "{nw}"

                        j up talk "Well, I suppose that’s a good thing, being able to draw a line between work and play."

                        show jacques smile

                        a down frowntalk "/”Play/”?"
                        a frown "{nw}"

                        j talk "Compared to performing in front of thousands? I’d say sitting around drinking tea and walking the gardens is {i}definitely{/i} play."
                        j "I myself am always {i}très{/i} appreciative of the time I get to spend at this lovely little mini-mansion."

                        show jacques smile

                        a up talk "Because \”All work and no play makes Jacques a dull boy?\”"
                        a smile "{nw}"

                        an "Jacques stares at me for a moment."

                        j frowntalk "Do me a favor, mademoiselle."

                        show jacques frown

                        a down frowntalk "Yeah?"
                        a frown "{nw}"

                        j talk "Stick to singing."
                        j "That joke was so cheesy I could serve it on a charcuterie board."

                        show jacques smile

                        a down frowntalk "Hey, so was {i}that{/i}!"
                        a frown "{nw}"

                        j talk "Yes, but {i}I’m{/i} a professional entertainer. The cheese is part of the charm."

                        show jacques smile

                        a up talk "I guess..."
                        a smile "{nw}"

                        jump jacqueschat2part2

                label shesmycherrypie:

                    a down frowntalk "I’m... a little concerned about Cherry, to be honest."
                    a frown "{nw}"

                    j down frowntalk "Really?"

                    show jacques frown

                    a frowntalk "Yeah."
                    a "I just... she seems {i}really{/i} sweet, but I’m worried about how this contest is going to affect her."
                    a frown "{nw}"

                    j frowntalk "You think she can’t handle the pressure?"

                    show jacques frown

                    a frowntalk "Well..."

                    menu:
                        "I don’t think she’s cut out for this.":
                            jump cherryshouldntbehere

                        "I actually think she might win.":
                            jump ibelieveincherry

                        "She {i}can{/i} handle it, but {i}will{/i} she?":
                            jump comeoncherry

                    label cherryshouldntbehere:

                        an "I take a deep breath."

                        a frowntalk "I mean, it’s not just me, right?"
                        a "Cherry seems {i}totally wrong{/i} for this kind of thing."
                        a "I mean she’s honest, and good-natured, and so down-to-Earth."
                        a "She’s not {i}like{/i}..."
                        a frown "{nw}"

                        j up talk "Not like all us awful showbiz people?"

                        show jacques smile

                        a up frowntalk "..."
                        a "...I’m being a jerk, aren’t I?"
                        a frown "{nw}"

                        j frowntalk "To very many people, yes."
                        j "But...I don’t think that’s how you feel deep down."
                        j "I think this little...bug that you have up your {i}derrière{/i} is, well..."
                        j "I think you’re overthinking about what Cherry thinks."

                        show jacques frown

                        a down frowntalk "Yeah?"
                        a frown "{nw}"

                        j talk "But you know, if you’re {i}really{/i} worried about her, you should just {i}ask{/i} her how she feels about it."

                        show jacques smile

                        a frown "You...may actually have a point, there."
                        a frown "{nw}"

                        jump jacqueschat2part2

                    label ibelieveincherry:

                        a up talk "Actually, I think Cherry has a good chance of winning."
                        a "Her voice is {i}amazing{/i}."
                        a smile "{nw}"

                        j talk "I’m sure she’d appreciate the compliment."

                        show jacques smile

                        a down frowntalk "But what I {i}am{/i} worried about is, if she {i}does{/i} win, what then?"
                        a "A {i}lot{/i} of people who win these reality singing shows only stay famous for a year or two..."
                        a "Some of them stick around, but others just...stop making music, I guess."
                        a frown "{nw}"

                        j frowntalk "En réalité, it’s more like they stop making {i}money{/i}, Alice."

                        show jacques frown

                        an down "...{i}Ouch.{/i}"

                        a frowntalk "Because showbiz is hard?"
                        a frown "{nw}"

                        j talk "Because showbiz is {i}fickle{/i}."
                        j "One moment, you could be on top of the world with a best-selling album and a viral music video..."
                        j frowntalk "And then your star can just...{i}fizzle out{/i}, Alice."

                        show jacques frown

                        an "He frowns to himself."

                        j down frowntalk "All of a sudden, people on the street are wondering what happened to you, as if you’d died or disappeared."

                        show jacques frown

                        a down frowntalk "Wow..."
                        a frown "{nw}"

                        an "Now {i}that’s{/i} a depressing thought."

                        j up talk "As for Cherry, well..."
                        j "I think she’d do alright."
                        j "Whether she wins and becomes the world’s idol, or she ends up a one-hit wonder..."
                        j "Either way, I’m sure she’ll find her footing."

                        show jacques smile

                        a up talk "That’s...actually really encouraging."
                        a "Thanks, Jacques."
                        a smile "{nw}"

                        jump jacqueschat2part2

                    label comeoncherry:

                        a up talk "I think she can handle the pressure."
                        a down frowntalk "I just don’t know if she {i}will{/i}."
                        a frown "{nw}"

                        an "Jacques raises an eyebrow."

                        show jacques down frown

                        j frowntalk "{i}Vraiment?{/i} Well..."
                        j "As much as I can understand why you’re worried about her...Maybe you should worry about yourself?"
                        j "This {i}is{/i} a competition, after all."
                        j "Or were you planning on quietly letting yourself lose, so the other girls can shine?"
                        j "Because let me tell you, {i}mademoiselle{/i}, that’s simply {i}not{/i} good television."

                        show jacques frown

                        menu:
                            "I’m here to win.":
                                jump iwanttobetheverybest

                            "I don’t deserve to win.":
                                jump imbadandishouldfeelbad

                        label iwanttobetheverybest:

                            an "I shake my head."

                            a up frowntalk "I’m here to win, or at least, to do my best."
                            a "I mean, if I {i}didn’t{/i} push myself, I’d regret it for the rest of my life."
                            a frown "{nw}"

                            j down frowntalk "Very true, very true."

                            show jacques smile

                            a down talk "Still, just because I want to win doesn’t mean I don’t care about the others."
                            a smile "{nw}"

                            j up talk "A fierce competitor with a heart of gold, huh?"

                            show jacques smile

                            jump jacquesportrayal

                        label imbadandishouldfeelbad:

                            a down frowntalk "...I don’t deserve to be here, Jacques."
                            a frown "{nw}"

                            j down frowntalk "You don’t want to be on the show?"

                            show jacques frown

                            a frowntalk "It’s not that I don’t {i}want{/i} to be, it’s just..."
                            a "I didn’t {i}earn{/i} it."
                            a frown "{nw}"

                            j frowntalk "Alice, you must be joking. That performance you gave was {i}spectacular{/i},just like the other three!"

                            show jacques frown

                            a frowntalk "Yeah, but...they got through official channels, whereas I’m just a technicality."
                            a frown "{nw}"

                            j up talk "Hmmm...a girl with a once-in-a-lifetime opportunity, but filled with self-doubt..."

                            show jacques smile

                            jump jacquesportrayal

                        label jacquesportrayal:

                            j talk "Or at least, that’s how they might portray you."

                            show jacques smile

                            a down frowntalk "Wait, \”portray\”?"
                            a frown "{nw}"

                            j talk "Alice, this is a {i}reality show{/i} after all."
                            j "When it’s time for the DVDs to come out, or even the TV airing, well..."
                            j "The show’s executives will have found nice little character arcs for all of you."

                            show jacques smile

                            a up frowntalk "You mean they’re going to lie about us?"
                            a frown "{nw}"

                            j down frowntalk "Not lie {i}per se{/i}, just...tie together the footage in a way that’s more {i}cinematic{/i}."

                            show jacques down smile

                            a down frowntalk "That’s kind of bizarre."
                            a frown "{nw}"

                            j up talk "That’s show-business."

                            show jacques smile

                            a up talk "Touché."
                            a smile "{nw}"

                            jump jacqueschat2part2

                    label letstalktaylor:

                        a down frowntalk "It’s Taylor."
                        a frown "{nw}"

                        j down frowntalk "Oh?"

                        show jacques frown

                        a frowntalk "I just...don’t {i}understand{/i} her."
                        a "She’s so {i}serious{/i} about this, more than any of us."
                        a "It’s really impressive, but at the same time, I’m kind of worried about her."
                        a frown "{nw}"

                        j up talk "Are you sure you’re not just jealous?"

                        show jacques smile

                        a frowntalk "What do you mean?"
                        a frown "{nw}"

                        j talk "Well...let me ask you something else."
                        j "Have you ever had a dream; something you wanted to do more than {i}anything{/i}?"

                        show jacques smile

                        a talk "I..."

                        menu:
                            "I’ve wanted to be famous my whole life.":
                                jump alicewantstheworld

                            "My dreams were pretty boring...":
                                jump alicewantsnormality

                            "Actually, I don’t remember...":
                                jump alicewantstosleep

                        label alicewantstosleep:

                            a up frown "Hmm..."

                            an "I shrug."

                            a frowntalk "I’m not sure."
                            a "I mean, when I was a {i}really{/i} little kid, I wanted to be a princess, and a space captain, and a {i}tree{/i}..."
                            a "But if we’re talking career-wise, I just don’t remember."
                            a "I don’t think there’s {i}any{/i} job that’s been my \”dream\”."
                            a frown "{nw}"

                            j down frown "Hmm..."
                            j up frowntalk "Well, that {i}might{/i} explain why you ended up an Intern."
                            j talk "It’s an excellent job for someone with no hopes or aspirations."

                            show jacques smile

                            an down "What the hell?"
                            an frowntalk "I open my mouth to protest, but Jacques raises a hand."

                            j talk "Before you cut me off, can you honestly tell me that you {i}liked{/i} doing errands all day?"

                            show jacques smile

                            an up frown "...Shit. He’s got me there."

                            a down frowntalk "Still, you don’t have to put it like that..."
                            a frown "{nw}"

                            j talk "Well, despite your {i}laissez-faire{/i} attitude to, well, {i}everything{/i}, it seems like part of you still wants to sing, {i}non{/i}?"

                            show jacques smile

                            a up talk "Yeah, you’re right."
                            a smile "{nw}"

                            j talk "Well, in that case..."

                            show jacques smile

                            jump jacqueschatdream

                        label alicewantsnormality:

                            a up talk "Actually, I never thought I’d get into showbiz."
                            a "I mean, everyone {i}fantasizes{/i} about being a famous singer, or a writer, or a movie star..."
                            a "But I never really put much hope into it. Before now, anyway."
                            a "Back in high school, I {i}thought{/i} I was going to be a journalist, or some kind of teacher."
                            a smile "{nw}"

                            j talk "...{i}But?{/i}"

                            show jacques smile

                            a talk "But when I managed to get the right grades to go to Presley, there was {i}no way{/i} I could say no."
                            a smile "{nw}"

                            j talk "{i}Pourquoi?{?i}"

                            show jacques smile

                            a down frown "..."

                            an "Why {i}did{/i} I go to Presley, if I never thought I could be famous?"

                            a frowntalk "Maybe because, deep down, I was still {i}hoping{/i} I could do something artistic."
                            a frown "{nw}"

                            j talk "And here you are, making art, {i}non{/i}?"

                            show jacques smile

                            a up talk "...We’re {i}making{/i} reality TV."
                            a frown "{nw}"

                            j talk "Which is, of course, the {i}highest{/i} {i}forme d’art{/i}."

                            show jacques smile

                            an "He gestures at the air dramatically."
                            an "This whole conversation feels ridiculous."
                            an "That said...maybe he’s right."

                            j talk "You want to know what I think?"

                            show jacques smile

                            a talk "Sure."
                            a smile "{nw}"

                            jump jacqueschatdream

                        label alicewantstheworld:

                            a down frown "..."

                            an "I take a deep breath."
                            an "My mouth goes dry for a moment as I try to find the words."
                            an "How can I {i}say{/i} this without coming off like some stuck-up primadonna?"
                            an "...I guess I just have to say it."

                            a up frowntalk "My dream is to sing."
                            a frown "{nw}"

                            j down frowntalk "On the show? Like this?"

                            show jacques frown

                            an "I shake my head."

                            a talk "Not just on a show, but...everywhere."
                            a "I want to sing at small, crowded bars. I want to sing at grand concert halls."
                            a "I want to star in music videos, and travel to exotic places..."
                            a "I want to be a {i}star{/i}."
                            a smile "{nw}"

                            j up talk "...And yet, you {i}never{/i} studied music at your school?"

                            show jacques smile

                            a talk "I studied a {i}bit{/i}."
                            a "But the music program there is {i}really{/i} competitive, and I didn’t want to get my hopes up."
                            a smile "{nw}"

                            j frown "Hmmm..."

                            jump jacqueschatdream

                        label jacqueschatdream:

                            j up talk "It seems like you and Taylor have the same dream."
                            j "Except that {i}she{/i} has spent every waking moment fighting to {i}achieve{/i} that dream."

                            show jacques smile

                            an down frown "Hearing those weirds feels like a bucket of cold water being thrown in my face."
                            an "Thinking back, every time I’ve seen Taylor, she’s been doing {i}something{/i} to help herself improve..."
                            an "She really is in a whole other league."

                            a down frowntalk "...I don’t deserve to be competing with her, do I?"
                            a frown "{nw}"

                            an "Jacques chuckles."

                            j down talk "Life isn’t about {i}deserving{/i} things, Alice. It’s about putting on a show!"
                            j up "Still, I hope that helps you realize just why our dear Taylor is ah, {i}burning the candle at both ends{/i}."

                            show jacques smile

                            a up talk "Yeah, I think I understand."
                            a talk "You know...I never realized just how impressive she really is."
                            a smile "{nw}"

                            j talk "Would you like me to let you in on one last little secret?"

                            show jacques smile

                            menu:
                                "Uh, sure.":
                                    jump whatsyoursecretjacques

                                "Nah, I think I’d better go.":
                                    jump idontcarejacques

                            label idontcarejacques:

                                a talk "Actually, if it’s alright with you, I think I’ll head out."
                                a smile "{nw}"

                                j talk "{i}Mais bien sûr.{/i}"

                                show jacques smile

                                a down talk "I’m...going to assume that means yes."
                                a smile "{nw}"

                                an up "I wave awkwardly at Jacques, and head out of the room."

                                jump jacqueschat2end

                            label whatsyoursecretjacques:

                                an "You know what? This could be {i}good{/i}."

                                a down talk "What’s the secret?"
                                a smile "{nw}"

                                j talk "I’m glad you asked."

                                show jacques smile

                                an up "He takes a deep breath, almost like he’s about to give a speech."
                                an "While he’s psyching himself up (or is he trying to psych {i}me{/i} up?), I grab a small pastry that’s sitting on a table near the window."
                                an "Oh hey, a croissant."

                                j frown "..."

                                an "I take a small bite."
                                an "It tastes...{i}French.{/i}"

                                j talk "Believe it or not, my dream wasn’t always obvious to me."
                                j "I didn’t always want to be an entertainer."

                                show jacques smile

                                an down frown "Wait, what? {i}Jacques?{/i}"
                                an "I can’t imagine him as anything {i}but{/i} a sparkly, melodramatic TV host."

                                j talk "It’s true."
                                j "I wanted to be...a {i}writer{/i}."

                                show jacques smile

                                an up "That was...{i}not{/i} the reveal I was expecting."

                                a talk "Are you {i}serious?{/i}"
                                a smile "{nw}"

                                an "He nods."

                                j talk "{i}C’est vrai!{/i} I used to want...{i}to write love stories{/i}."
                                j "Epic, {i}beautiful{/i} love stories about young, passionate lovers in revolutionary France!"

                                show jacques smile

                                a talk "Uh...cool?"
                                a smile "{nw}"

                                j talk "It was {i}very{/i} cool."
                                j "But then, one day, I realized something."
                                j "I’d much rather be {i}on{/i} the stage than behind the scenes."
                                j "I didn’t have to just {i}write{/i} about glamour and glitz, I could {i}live{/i} a life of romance!"

                                show jacques smile

                                an "That is {i}so{/i} incredibly cheesy."

                                j talk "So, your Bellvance Industry Pro Tip of the morning is this."
                                j "Go! Sing! Live a life of love and luxury!"

                                show jacques smile

                                a talk "...Can I finish my croissant, first?"
                                a smile "{nw}"

                                j down talk "...You may."

                                show jacques up smile

                                a talk "Great!"
                                a smile "{nw}"

                                an "And with that, I decide to head somewhere else, nibbling on my breakfast snack as I walk."

                                jump jacqueschat2end

                    label jacqueschat2part2:

                        an "Jacques clears his throat."

                        j up talk "Well, in any case, I hope this little chat helped."
                        j "As for me, I’ve got some things I need to get done."

                        show jacques smile

                        a down talk "Oh? What kind of things?"
                        a smile "{nw}"

                        j talk "{i}Host Things{/i}"

                        show jacques smile

                        an up frown "I have no idea what that means, but okay."

                        a talk "Have fun, Jacques."
                        a smile "{nw}"

                        j talk "I always do."

                        show jacques smile

                        hide jacques with dissolve

                        an "With that, he strides out of the room, coffee still in hand."
                        an "I kind of wonder, though."
                        an "If {i}I{/i} spend the rest of my life doing showbiz-y things, will {i}I{/i} end up walking around in a cloud of sparkles?"
                        an "...I guess I’ll just have to wait and see."

                    label jacqueschat2end:

                        jump nightSwitch

                    ## end scene


    label jacquesinterview:

        an "You know what? I think I need to stretch my legs for a while..."
        an "I’ll take a walk around the grounds and see if I can clear my head."

        scene fountainday
        with fade

        an "As I step outside, the gravel crunches softly under my feet."
        an "It’s crunching much {i}less{/i} softly as a tall, harried figure paces back and forth on the other side of the fountain."
        an "I peek my head around."

        $ config.side_image_tag = "alice"

        a frowntalk "...{i}Jacques{/i}?"
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
                jump jacquessceneoneend

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
            an "I hadn’t thought about it until now, but {i}Supernova{/i} was the first time I’d seen Jacques Bellevance in {i}years{/i}."
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
            j talk "The press always want to ask the same old boring questions."
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

            jump nightSwitch



######################################################################################################################

##“Oxwood? Redblood?” scene


    label paulgetscolorful:

        scene loungeafternoon
        with fade

        $ config.side_image_tag = "alice"

        a up smile "Mmm..."

        an "I yawn into the back of my hand, glancing around me."

        a "..."
        a talk "What {i}time{/i} is it?"
        a smile "{nw}"

        an "It feels like I’ve been here for maybe an hour, but the sky outside is {i}decidedly{/i} dark."
        an "Did I really space out that much? Or did I fall asleep without noticing?"
        an "...Either way, I should probably head to my room."
        an "I stretch a little, and start heading towards the doorway."
        an "And then a figure appears."
        an "The man in front of me is tall, tanned, and painfully stylish, sporting one of those \”pseudo-casual\” ensembles."
        an "You know, the kind of clothes that {i}look{/i} like they’re from a thrift store, but cost hundreds of dollars apiece?"
        an "Yeah, those sorts of clothes."

        na "Alice, thank god you’re here."

        a down talk "Huh?"
        a smile "{nw}"

        an "The man looks down at me, frowning."

        na "We. Are In. A {i}Crisis{/i} Situation, Alice."

        a up smile "..."

        an "...I have {i}no{/i} idea what he’s talking about."
        an "...Hold on."
        an "I {i}know{/i} him."

        na "Hey, are you listening?"

        an "Paul’s an intern, like me. Well, not {i}much{/i} like me, but we both work for Katja."
        an "He’s been working with her since...I think about a year or so before I joined?"

        p "Honey?"

        an "He’s a pretty cool guy...I {i}think{/i}. We never really got to talk much because, well, {i}work{/i}."

        p "Hey..."

        an "Paul taps me on the shoulder and I flinch."

        a up talk "Oh, sorry, Paul."
        a smile "{nw}"

        an "He rolls his eyes."

        p "It’s fine. I just...{i}really{/i} need your help right now."

        a down talk "Yeah?"
        a smile "{nw}"

        p "Yeah. Can you help me?"

        a up talk "Well..."
        a smile "{nw}"

        menu:
            "Sure.":
                jump yeshelppaul

            "I’d rather not.":
                jump noheckoffpaul

            "Help you with what?":
                jump tellmepaul1

        label tellmepaul1:

            a talk "What do you need me to help with?"
            a smile "{nw}"

            p "A {i}thing{/i}, Alice. A very {i}big{/i} thing."
            p "Well, the actual thing I need you to help with isn’t {i}actually{/i} that hard..."
            p "But there {i}could{/i} be big consequences..."

            a down "...For you, or for me?"
            a smile "{nw}"

            p "Yes."

            a frown "..."

            p "Come on, honey. It’ll only take maybe...thirty seconds, tops."

            menu:
                "Okay, I’ll help.":
                    jump yeshelppaul

                "I’m just too busy right now.":
                    jump noheckoffpaul

            a down frowntalk "I’m sorry, Paul, but whatever it is, I don’t have time right now."
            a up "I need to focus on the {i}contest{/i}."
            a smile "{nw}"

            p "And you don’t suppose that {i}maybe{/i} this has something to do with that?"

            a down frowntalk "Huh?"

            p "Honey, I’m not here just to bug you about what SelfiPix filter looks best on me."
            p "I want you to help me with something show-related."
            p "And don’t worry, it’s not like I’m helping you cheat or anything."
            p "Really, it’s just a minor detail, but...you were the only person I could think of to help with this."

            a up frowntalk "Hmm..."

            menu:
                "Alright, I’ll see what I can do.":
                    jump yeshelppaul

                "I’m sorry, I just can’t.":
                    jump nomeansnopaul

            label nomeansnopaul:

                a down frowntalk "Look, I’m sure that whatever you’re doing is important, but..."
                a "I {i}really{/i} need to get some sleep."
                a "If I don’t, it might even affect how I do in the next contest."
                a frown "{nw}"

                an "Paul lets out a defeated sigh."

                p "Alright, I can see you don’t want to do this."
                p "I guess I’ll go ask one of the staff, or something..."

                a up talk "Thanks, Paul. I’m glad you understand."
                a smile "{nw}"

                an "And with that, I step around Paul and head towards my room."
                an "I’ve got a lot to do tomorrow, after all..."

                jump paulcolorsceneend

            label yeshelppaul:

                a up talk "Alright, you’ve convinced me. What can I do to help?"
                a smile "{nw}"

                an "Paul’s eyes light up."

                p "I’m {i}so{/i} glad you asked."

                an "He strides over to me, then scoots around to my side, so he’s half-leaning over me."
                an "Paul reaches into his jacket pocket, and pulls out a smartphone."
                an "With a few deft gestures, he pulls up an image folder and taps on a thumbnail."

                a down frowntalk "Umm..."
                a frown "{nw}"

                an "The image now filling up the screen is..."
                an "Okay, I don’t actually know {i}what{/i} it is."
                an "It’s a reddish-brown {i}splotch{/i} on a checkerboard background."

                a frown "..."

                p "Okay, {i}so{/i}."
                p "Which of these two do you prefer?"
                p "{i}This...{/i}"
                p "Orrrrrrr.... {i}this{/i}?"

                an "He swipes his thumb right, bringing up another picture."
                an "Wait, the {i}same{/i} picture? Maybe?"

                a "..."

                an "I squint at the \”new\” image."
                an "Nope. Still a splotch."

                a frowntalk "Are...these different, Paul?"
                a frown "{nw}"

                an "He rolls his eyes."

                p "The {i}color{/i}, Alice. I need you to tell me which color seems more...{i}dynamic{/i}."

                a "They’re both the same color, though?"
                a frowntalk "{nw}"

                an "It’s sort of a...vibrant maroon, I guess? Like a cross between dried blood and red wine."

                p "Come on, Alice. You’re in {i}show business{/i} for goodness’ sake."
                p "Or are you going to tell me you’ve been colorblind this whole time?"

                a up frowntalk "I’m not."
                a frown "{nw}"

                an "Or at least, I didn’t {i}think{/i} so until today."
                an "Paul swipes his thumb left and right a few times, like we’re doing some kind of weird eye exam."
                an "..."
                an "I seriously can’t see any difference."
                an up "Wait. Hold on."
                an "There {i}is{/i} a difference."
                an "{i}The filenames.{/i}"
                an "Whenever Paul switches pictures, the filename pops up for about half a second."
                an "The color that Paul showed me first is labelled \”Oxwood.png\”."
                an "The other one is \”Redblood\”..."

                p "So, any thoughts?"

                a up talk "Well..."

                menu:
                    "Oxwood is {i}clearly{/i} the superior choice.":
                        jump oxwood1

                    "Redblood. Duh.":
                        jump redblood1

                    "Which do {i}you{/i} like best, Paul?":
                        jump paulspreferences

                    "What’s this {i}for{/i}, anyway?":
                        jump whyareyoudoingthistomepaul

                label paulspreferences:

                    a up talk "Well, I {i}know{/i} we’re both in show business, Paul..."
                    a "But you’re so much more {i}experienced{/i} than I am."
                    a "Maybe you could give me your thoughts before I decide?"
                    a smile "{nw}"

                    an "Paul frowns a little."

                    p "You really wanna know what {i}I{/i}think?"

                    a talk "Yeah."
                    a smile "{nw}"

                    an "He strokes his chin for a moment."

                    p "{i}Well...{/i}"
                    p "Oxwood is definitely the more {i}traditional{/i} choice."
                    p "I’ve got an Oxwood phone case that I like to use whenever I’m going to a job interview."
                    p "Makes me seem a little {i}classier,{/i} y’know?"

                    a down talk "Uh, sure."
                    a smile "{nw}"

                    p "But {i}Redblood{/i} is bold. Agressive, even."
                    p "Redblood’s a color that says \”I don’t give a crap what you think\”."
                    p "If dragons were real, and they peed, it would be this color."
                    p "Oh, and it’s a Winter, of course."

                    a frowntalk "...Of course."
                    a frown "{nw}"

                    an "That... didn’t explain {i}anything{/i}."
                    an "If anything, I may be even {i}more{/i} confused, now."
                    an "It’s like he’s talking about two {i}completely{/i} different colors!"
                    an "While I’m trying to wrap my head around this, Paul keeps swiping back and forth between the two images."
                    an "...Or maybe he’s just refreshing the {i}same{/i} image?"
                    an "Honestly, I’m starting to wonder if this is some kind of prank that one of the other contestants put him up to..."

                    p "So, Alice. Which do you think we should go with?"

                    menu:
                        "Oxwood makes the most sense.":
                            jump oxblood1

                        "Let’s be bold, do Redblood.":
                            jump redblood1

                        "Ox...blood?":
                            jump oxblood1

                        "What exactly are you trying to decide the color {i}of{/i}?":
                            jump whyareyoudoingthistomepaul

                label whyareyoudoingthistomepaul:

                    a up talk "Paul, maybe it’d help a little if you told me what these colors are gonna be {i}used for.{/i}"
                    a smile "{nw}"

                    p "Nuh-uh. Can’t do it."
                    p "She {i}told{/i} me not to let you know. Said you’d overthink it too much."
                    p "Can’t let it \”color your decisions\” or whatever."

                    a down frowntalk "..."

                    menu:
                        "Was that a pun?":
                            jump verypunnypaul

                        "Please tell me?":
                            jump comeonpaulbecool

                        "Wait, {i}who{/i} told you to ask me?":
                            jump nicegoingpaul

                    label verypunnypaul:

                        p "Hmmm, maybe."
                        p "But anyway, just give me your pick, okay?"
                        p "You don’t even have to think about it too much."
                        p "Just go with your gut feeling."

                        a frown "Hmmm..."

                        label colorchoice2:

                            menu:
                                "Oxwood sounds good.":
                                    jump colorstuff2

                                "Let’s go with Redblood.":
                                    jump colorstuff2

                                "I like Oxblood the best.":
                                    jump thatsnotacolor

                                "Redwood, for sure!":
                                    jump thatsnotacolor

                    label comeonpaulbecool:

                        p "{i]Look{/i}, Alice."
                        p "The whole {i}point{/i} of this is to get your honest, unbiased opinion."
                        p "The less you know, the better your answer will be."

                        a up frowntalk "That makes {i}no{/i} sense."
                        a frown "{nw}"

                        p "Well, art of often {i}doesn’t{/i} make sense."
                        p "It doesn’t really matter what it’s {i}for.{/i}"
                        p "Maybe it’s a piece of set dressing, or a costume, or a flyer...or maybe Katja just wants to buy herself a new {i}car{/i} or something."
                        p "It’s not like any of us ever know what that woman’s {i}thinking{/i}."

                        an down smile "Wait, \”Katja\”?"

                        p "Just tell me which color looks best to {i}you{/i}."

                        jump colorchoice2

                    label nicegoingpaul:

                        a up frowntalk "Alright, fess up. Who put you up to this?"
                        a frown "{nw}"

                        an "Paul clicks his tongue."

                        p "{i}Crap.{/i} I was {i}not{/i} supposed to let that slip."
                        p "Look, let’s just pretend that {i}nobody{/i} told me to do this."
                        p "{i}Especially{/i} not Katja, okay?"

                        an "..."

                        a talk "So, it’s super-duper {i}definitely{/i} Katja’s idea, but if she knew you told me, you’d be fired?"
                        a smile "{nw}"

                        p "Bin-{i}go{/i}, Alice."

                        an "I sigh."
                        an "Seriously, Katja? Why can’t you just {i}tell{/i} me these things?"
                        an "And besides..."

                        a talk "I have no idea why Katja’d have you ask {i}me{/i} this stuff."
                        a "I have, like, the {i}least{/i} aesthetic sense out of anyone here..."
                        a smile "{nw}"

                        an "Except maybe Jacques. But that’s another story."

                        p "I think that’s actually {i}why{/i} she wanted me to ask you."
                        p "There are dozens of people working on this show with degrees in art, and fashion, and stage design..."
                        p "But it’s a {i}reality{/i} show. It’s {i}trashy{/i}, and {i}melodramatic{/i}, the kind of thing that’s not {i}aimed{/i} at \”artistic\” types."
                        p "It’s a show for normal, everyday, average human beings."
                        p "If we want to reach those people, we don’t need an expert opinion. We need a Normal Person Opinion."

                        an "...I’m honestly not sure if I should be offended right now."

                        p "So, Miss Normal Person. Which of these two {i}magnificent{/i} colors has caught your Normal Eyes?"

                        a talk "Well..."

                        jump colorchoice2

                    label thatsnotacolor:

                        p "Seriously, Alice?"
                        p "Look, I know you don’t really {i}care{/i} about this, but {i}wow{/i}."

                        an down frown "That...{i}thing{/i} I just said wasn’t an option, was it?"

                        a up talk "I’m sorry, Paul."
                        a "I just...really don’t think I can help with this."
                        a smile "{nw}"

                        p "No, it’s fine."
                        p "I’ll go ask one of the kitchen staff or something."

                        an "Paul walks off, looking dejected."
                        an "Hopefully, he’s not too mad at me."
                        an "Anyway, I need to go get some sleep"

                        jump paulcolorsceneend

                    label colorstuff2:

                        p "You think so?"

                        a down talk "Y-yeah."
                        a smile "{nw}"

                        an "He frowns for a moment, swiping back and forth a few times."

                        p "..."
                        p "You’re absolutely right, Alice."
                        p "Okay, now I need to get back to work."

                        an up "He turns on his heel and strides out of the room, heading down the hallway."
                        an "He calls over his shoulder."

                        p "Thanks, Alice!"

                        a "No problem! Oh, and goodnight!"
                        a smile "{nw}"

                        an "In a few moments, he’s out of sight."

                        a "Well, I guess I can finally get some sleep."
                        a smile "{nw}"

                        jump paulcolorsceneend

                label oxwood1:

                    a up talk "Oxwood, definitely."
                    a smile "{nw}"

                    p "{i}Really{/i}?"

                    a down frowntalk "Yeah? Is that...not what you were hoping for?"
                    a frown "{nw}"

                    p "Oh, no. It’s just that’s what {i}I’d{/i} picked, too."
                    p "Guess I know it’s the right choice."
                    p "Thanks, Alice."

                    a up talk "You’re welcome. Although I’m still not really sure what I {i}did{/i}."
                    a smile "{nw}"

                    p "You {i}helped{/i}, is what you did."
                    p "Anyway, I guess that means I’ve got my work cut out for me."

                    an "With that, Paul heads out of the room, and starts walking down the hallway."
                    an "He looks...relieved."
                    an "I’m glad."

                    a "..."
                    a "Anyway, I think it’s finally time for me to get some sleep."

                    jump paulcolorsceneend

                label redblood1:

                    a up talk "Hmm, I think I like Redblood the best."
                    a "I mean, they look pretty similar, but there’s something about Redblood that speaks to me."
                    a smile "{nw}"

                    an "...I’m not going to tell him that what \”speaks to me\” is the ridiculously bizarre name."
                    an "It sounds like the title of a fighting game or something..."

                    p "Hmm..."
                    p "Well, {i}my{/i} vote was for Oxwood, but now that you mention it..."

                    an "He nods."

                    p "Redblood it is."
                    p "You’re absolutely right that it’s more evocative."

                    an "I didn’t say that, but okay."

                    p "Thanks, Alice. You’ve been a massive help."

                    an "He slips his phone back into his jacket pocket."

                    p "Anyway, now that {i}that’s{/i} settled, I’ve got about five hundred {i}other{/i} things that Katja wanted me to do."

                    an "Wait, Katja?"
                    an "...It’s probably best not to think about it too much. Who knows what she’s up to?"

                    a talk "You’re welcome, Paul."
                    a "Can I go to bed now?"
                    a smile "{nw}"

                    p "Of course!"

                    an "I step away from him and walk out to the hallway."

                    p "Goodnight, Alice!"

                    a talk "Night, Paul!"
                    a smile "{nw}"

                    an "Well, now that’s over and done with, I can hopefully get some sleep..."

                    jump paulcolorsceneend

                label paulcolorsceneend:

                    jump nightSwitch

                    ## end scene



