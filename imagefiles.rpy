#######################################################################################################################
##############################################                              ###########################################
##############################################          Image Files         ###########################################
##############################################                              ###########################################
#######################################################################################################################

layeredimage side alice:

    group body:

        attribute base default:
            "a base.png"
        attribute edgy:
            "a edgy.png"
        attribute princess:
            "a princess.png"
        attribute summer:
            "a summer.png"
        attribute winter:
            "a winter.png"

    group eyebrows:

        attribute up default:
            "a brow1.png"
        attribute down:
            "a brow2.png"

    group mouth:

        attribute smile default:
            "a expression1.png"
        attribute talk:
            "a expression2.png"
        attribute frown:
            "a expression3.png"
        attribute frowntalk:
            "a expression4.png"




layeredimage mary:

    group body:

        attribute base default:
            "m base.png"
        attribute summer:
            "m summer.png"
        attribute winter:
            "m winter.png"

    group eyebrows:

        attribute up default:
            "m brow1.png"
        attribute down:
            "m brow3.png"
        attribute unsure:
            "m brow2.png"

    group mouth:

        attribute smile default:
            "m expression1.png"
        attribute talk:
            "m expression2.png"
        attribute frown:
            "m expression3.png"
        attribute frowntalk:
            "m expression4.png"


layeredimage cherry:

    group body:

        attribute base default:
            "c base.png"
        attribute edgy:
            "c edgy.png"
        attribute winter:
            "c winter.png"
        attribute summer:
            "c summer.png"

    group eyebrows:

        attribute up default:
            "c brow1.png"
        attribute down:
            "c brow2.png"

    group mouth:

        attribute smile default:
            "c expression1.png"
        attribute talk:
            "c expression2.png"
        attribute frown:
            "c expression3.png"
        attribute frowntalk:
            "c expression4.png"


layeredimage taylor:

    group body:

        attribute base default:
            "t base.png"
        attribute edgy:
            "t edgy.png"
        attribute prince:
            "t prince.png"
        attribute summer:
            "t summer.png"
        attribute winter:
            "t winter.png"

    group eyebrows:

        attribute up default:
            "t brow1.png"
        attribute down:
            "t brow2.png"
        attribute upprince:
            "t brow3.png"
        attribute downprince:
            "t brow4.png"

    group mouth:

        attribute smile default:
            "t expression1.png"
        attribute talk:
            "t expression2.png"
        attribute frown:
            "t expression3.png"
        attribute frowntalk:
            "t expression4.png"



layeredimage katja:

    always:

        "k base.png"

    group mouth:

        attribute smile default:
            "k expression1.png"
        attribute talk:
            "k expression2.png"
        attribute frown:
            "k expression3.png"
        attribute frowntalk:
            "k expression4.png"



layeredimage jacques:

    group body:

        attribute base default:
            "j base.png"
        attribute bath:
            "j bath.png"

    group eyebrows:

        attribute up default:
            "j brow1.png"
        attribute down:
            "j brow2.png"

    group mouth:

        attribute smile default:
            "j expression1.png"
        attribute talk:
            "j expression2.png"
        attribute frown:
            "j expression3.png"
        attribute frowntalk:
            "j expression4.png"



layeredimage director:

    always:

        "d base.png"

    group mouth:

        attribute smile default:
            "d expression1.png"
        attribute talk:
            "d expression2.png"



######################################################################################################################
######################################################################################################################
######################################################################################################################



image sparkles1:
    "sparkles.png"
    linear 0.5 alpha 0.0

    "sparkles.png"
    linear 1.6 alpha 1.0

    "sparkles.png"
    linear 1.0 alpha 0.0

    repeat

image sparkles2:
    "sparkles2.png"
    linear 0.2 alpha 0.0

    "sparkles2.png"
    linear 1.0 alpha 1.0

    "sparkles2.png"
    linear 1.3 alpha 0.0

    repeat


image mmconcert:
    subpixel True
    size (1200, 800)
    xalign .5
    yalign .5

    parallel:
        "images/mm.png"

        crop (26, 10, 393, 238)
        pause 1.0
        easeout .9 crop (19, 18, 602, 372)

        crop (88, 500, 189, 121)
        easeout 1.1 crop (91, 467, 474, 280)

        crop (978, 12, 211, 206)
        easein 1.8 crop (611, 43, 467, 318)

        crop (524, 260, 158, 111)
        easein 1.8 crop (509, 239, 500, 287)


        easein 3.5 crop (0, 0, 1200, 800)


image concert1:
    "images/promo.jpg"
    size (1280, 1697)
    alpha 1.0
    yalign 1.0
    linear 10.0 yalign 0.0

image concert2:
    subpixel True
    size (1200, 800)
    xalign .5
    yalign .5

    parallel:
        "images/mm.png"

        crop (92, 444, 231, 152)
        pause 0.5
        easeout 2.5 crop (100, 290, 535, 345)

        crop (393, 4, 157, 98)
        easeout 1.6 crop (372, 6, 373, 248)

        crop (1015, 8, 171, 114)
        easein 2.6 crop (538, 7, 605, 397)

        pause 1.0

        easein 4.5 crop (0, 0, 1200, 800)


image logomm:
    "images/logo.png"
    alpha 0

    pause 9

    "images/logo.png"
    ease 1 alpha 1.0

transform dissolvemm:
    alpha 0

    pause 0.4

    ease 1 alpha 1.0
