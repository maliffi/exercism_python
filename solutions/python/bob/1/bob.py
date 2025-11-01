def response(hey_bob):
    hey_bob = hey_bob.strip()
    if len(hey_bob) <=0 :
        return "Fine. Be that way!"
    if hey_bob[-1] == "?":
        if hey_bob.upper() == hey_bob and hey_bob.lower() != hey_bob:
            return "Calm down, I know what I'm doing!" 
        else:
            return "Sure."
    if hey_bob.upper() == hey_bob and hey_bob.lower() != hey_bob:
        return "Whoa, chill out!"
    
    return "Whatever."
    
