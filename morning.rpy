
#######################################################################################################################
##############################################                              ###########################################
##############################################           Mornings           ###########################################
##############################################                              ###########################################
#######################################################################################################################



######################### Normal Wake-up

label normal:
        
    scene bedaliceday
    with fade
    
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
        

label hopeful:
    
    scene bedaliceday
    with fade
    
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