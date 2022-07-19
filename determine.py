def determine_cuteness(animal):
    if animal in ["Maja", "Obi"]:
        return "Extremely"

    if animal in ["cat", "dog", "turtle", "otter", "cow", "penguin", "seal", "bunny", "tapir"]:
        return "Very"
    
    if animal in ["bear", "lion"]:
        return "Danger-cute"
    
    return "Probably"