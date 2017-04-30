# Off timing responses
def below10_accel():
    return "There's this thing called music, check it out sometime."
def onequarter_accel():
    return  "Do you even know what a chorus is?"
def onehalf_accel():
    return  "That was pretty good, if you were trying to dab before anyone else."
def threequarters_accel():
    return "I mean, I've seen worse. Just get the timing right, ok?"
def top_ten_accel():
    return "Yaz dab queen."

# Incorrect movement responses
def below10_orient_gyro():
    return "I honestly don't know if you just sneezed or tried to dance."
def onequarter_orient_gyro():
    return  "This isn't the chicken dance."
def onehalf_orient_gyro():
    return  "I can tell what you're trying to do, but if anyone asks we don't know each other, ok?"
def threequarters_orient_gyro():
    return "Hmm....not terrible. Practice that form a bit more and you'll be in good shape."
def top_ten_orient_gyro():
    return "Yaz dab queen."


# Generate response for dab
def in_depth_rate_dab(orient_gyro, accel):
    response = "In terms of your timing: "
    if accel < 10:
        response += below10_accel()
    elif accel < 25:
        response += onequarter_accel()
    elif accel < 50:
        response += onehalf_accel()
    elif accel < 75:
        response += threequarters_accel()
    else:
        response += top_ten_accel()
    response += " As for your dabbing: "
    if orient_gyro < 10:
        response += below10_orient_gyro()
    elif orient_gyro < 25:
        response += onequarter_orient_gyro()
    elif orient_gyro < 50:
        response += onehalf_orient_gyro()
    elif orient_gyro < 75:
        response += threequarters_orient_gyro()
    else:
        response += top_ten_orient_gyro()
    return response

def rate_dab(orient_gyro, accel):
    print "orient_gyro: "+str(orient_gyro)
    print "accel: "+str(accel)
    print "rating: "
    if orient_gyro + accel > 180:
        response = "You fucking rock, dabstar."
    elif orient_gyro + accel < 50:
        response = "Honestly, get the fuck out the club."
    else:
        response = in_depth_rate_dab(orient_gyro, accel)
    print response
    return response

#### Testing these bad boys out ####

rate_dab(34,86)
rate_dab(55,100)
rate_dab(2,1)
rate_dab(66,28)
rate_dab(90,30)
rate_dab(80,95)

import pyttsx
engine = pyttsx.init()
engine.say('Good morning.')
engine.runAndWait()
