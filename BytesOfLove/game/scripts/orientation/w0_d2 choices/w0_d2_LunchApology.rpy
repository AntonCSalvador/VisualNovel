label w0_d2_LunchApology:
    p "Hey JavaScript!"
    p "Is it if we join you?"
    js "Yeah sure!"
    mc "Lunch was good, I am glad that we got to eat some good food."

    menu w0_d2_LunchApologyC:
        "Collectively apologize and smooth things over":
            mc "Hey, now that we are all together,"
            mc "I just want to apologize one more time for what happened on the tour."
            mc "I think that we could all be good friends."
            mc "I am excited to get to know you guys better in the future."

            jump w0_d2_LunchFlirtDecision

        "Don't collectively apologize":
            jump w0_d2_AfterLunch

menu w0_d2_LunchFlirtDecision:
    "Flirt":
        jump w0_d2_LunchFlirt
        
    "Don't Flirt":
        js "I totally agree, [mc]!"
        js "I think we can be good friends in the future as well."
        p "Yeah, and it’s so good that we are all computer science majors."
        p "Hopefully we will have a lot of classes together."
        jump w0_d2_AfterLunch