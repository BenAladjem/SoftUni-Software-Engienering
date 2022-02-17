def say(times):
    if times == 0:
        return
    print("I say something")
    say(times - 1)

say(10)
