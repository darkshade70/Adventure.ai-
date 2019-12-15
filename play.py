import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
print("Setup complete!")

history = "It is always a bad idea to talk to the ancient ones."


def isContext(text):  # is a iece of textthis a context change? (i.e. moving to a new room)
    if "you are" in text or "we are" in text or "this is" in text or '''you're''' in text:  # context change
        return True
    else:
        return False


# lets us detect a loop condition where the game just replies "taken" or "done" to everything
def isTakeLoop(playerAction, result):
    if "done" in result.lower() or ("take" in result.lower() and "take" not in playerAction.lower()):
        return True
    else:
        return False


# gpt is trying to move the player when they didn't specify they wanted to move
def isInvalidMove(playerAction, result):
    if ("go ") in playerAction:
        return False
    else:
        if isContext(result):
            return True
        else:
            return False


# This text defines where your character starts! You can make it anything!

# Change to True to make the game a bit more coherent, but possibly a bit less interesting
STRICT_MODE = True

locContext = ""
alreadyDone = ""
prompt = ""
action = ""
# for the first response (generating the initial setting) we want to impose less strict restrictions on output
firstRun = True
while True:
    newprompt = "no response"
    gpo = gpt2.generate(sess, temperature=0.1, prefix=history, run_name='run1',
                        length=100, return_as_list=True, nsamples=3, batch_size=3, top_p=0.99)
    for candidate in gpo:
        goodCandidate = False
        result = candidate
        splitup = result.split("\n")
        newprompt = ""
        hasContext = False
        for item in splitup:
            words = item.split(" ")
            # avoid repeating things we've said in this or previous responses. If a response is very short (i.e. "taken" when you pick up an item) it's ok to repeat.
            if (item not in alreadyDone or len(words) <= 2) and item not in newprompt and (isTakeLoop(action, item) == False) and (isInvalidMove(action, item) == False or firstRun):
                # If it's a next player action, then stop, otherwise keep going
                if ("." in item or "?" in item or "!" in item) and (hasContext == False or isContext(item) == False):
                    newprompt = newprompt+item
                    goodCandidate = True
                    if isContext(item):
                        hasContext = True
                else:
                    if goodCandidate and STRICT_MODE:  # This prevents GPT from taking actions on our behalf. If strict mode is on actions are never taken, if it is off they are taklen but not shown to us. Strict mode on can make the game more playable at the expense of less interesting descriptions
                        break
        if goodCandidate:
            break
    if len(newprompt) > 3:  # this will be blank if GPT couldn't come up with anything
        if isContext(newprompt):  # This is updating the location context
            locContext = newprompt
        print(newprompt.replace(".", "\n").upper())
        prompt = newprompt
        action = input()
        firstRun = False
        history = locContext+"\n"+prompt+"\n"+action
        alreadyDone = alreadyDone+prompt+"\n"+action
    else:
        print("I don't know how to do that".upper())
        newaction = input()
        history = locContext+"\n"+prompt+"\n"+newaction
        alreadyDone = alreadyDone+"\n"+newaction
