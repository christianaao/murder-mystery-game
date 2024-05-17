import sys, time, random

def typingprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)

def typinginput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  value = input()  
  return value   

#global variables
Analyst_Skill = 0
Cunning_Skill = 0
Fighting_Skill = 0
year = ["1841", "1928", "1979", "2024"]
inventory = []

#start game function
def start_game():
    print("""
████████╗██╗███╗   ███╗███████╗                                  
╚══██╔══╝██║████╗ ████║██╔════╝                                  
   ██║   ██║██╔████╔██║█████╗                                    
   ██║   ██║██║╚██╔╝██║██╔══╝                                    
   ██║   ██║██║ ╚═╝ ██║███████╗                                  
   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝                                  
████████╗██████╗  █████╗ ██╗   ██╗███████╗██╗                    
╚══██╔══╝██╔══██╗██╔══██╗██║   ██║██╔════╝██║                    
   ██║   ██████╔╝███████║██║   ██║█████╗  ██║                    
   ██║   ██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║                    
   ██║   ██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗               
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝               
███╗   ███╗██╗   ██╗██████╗ ██████╗ ███████╗██████╗              
████╗ ████║██║   ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗             
██╔████╔██║██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝             
██║╚██╔╝██║██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗             
██║ ╚═╝ ██║╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║             
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝             
███╗   ███╗██╗   ██╗███████╗████████╗███████╗██████╗ ██╗   ██╗██╗
████╗ ████║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚██╗ ██╔╝██║
██╔████╔██║ ╚████╔╝ ███████╗   ██║   █████╗  ██████╔╝ ╚████╔╝ ██║
██║╚██╔╝██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗  ╚██╔╝  ╚═╝
██║ ╚═╝ ██║   ██║   ███████║   ██║   ███████╗██║  ██║   ██║   ██╗
╚═╝     ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝
        """)
    typingprint("Welcome to Time Travel Murder Mystery!")
    print()
    start = typinginput("Would you like to continue? Type 'Yes' or 'No': ").lower()
    print()
    if start == "Yes".lower():
        intro()
    elif start == "No".lower():
        typingprint("The game will now end.")
        print()
        time.sleep(3)
        sys.exit()
    else:
       typingprint("Invalid. Please try again.")
       print()
       start_game()

#game intro and beginning stats
def intro():
    global player
    global Analyst_Skill
    global Cunning_Skill
    global Fighting_Skill
    Analyst_Skill = dice_roll(1, 6)
    Cunning_Skill = dice_roll(1, 6)
    Fighting_Skill = dice_roll(1, 6)
    typingprint("In this game, you will play the role of a Detective. Your task is to navigate your way through the different timelnes, collecting evidence and increasing your stats as you go along to prepare you for the final showdown...")
    print()
    player = typinginput("What is your name, Detective? Please type in your chosen Surname: ").strip().lower().capitalize()
    print()
    typinginput("Roll the dice to determine your stats. Press Enter to roll the dice. ")
    print()
    typingprint(f"Detective {player}'s Analyst Skill: {Analyst_Skill}")
    print()
    typingprint(f"Detective {player}'s Cunning Skill: {Cunning_Skill}")
    print()
    typingprint(f"Detective {player}'s Fighting Skill: {Fighting_Skill}")
    print()
    typingprint("Your skillset seems to be a bit low... Well, there's no better way to learn than on the job, Detective. As you progress through the game, you will make decisions which will impact the rest of the game and affect your skill level.")
    print()
    year_chooser()

# end of game screen **add colour here
def game_over():
    typingprint("""
 ███████████ █████   █████ ██████████    ██████████ ██████   █████ ██████████  
░█░░░███░░░█░░███   ░░███ ░░███░░░░░█   ░░███░░░░░█░░██████ ░░███ ░░███░░░░███ 
░   ░███  ░  ░███    ░███  ░███  █ ░     ░███  █ ░  ░███░███ ░███  ░███   ░░███
    ░███     ░███████████  ░██████       ░██████    ░███░░███░███  ░███    ░███
    ░███     ░███░░░░░███  ░███░░█       ░███░░█    ░███ ░░██████  ░███    ░███
    ░███     ░███    ░███  ░███ ░   █    ░███ ░   █ ░███  ░░█████  ░███    ███ 
    █████    █████   █████ ██████████    ██████████ █████  ░░█████ ██████████  
   ░░░░░    ░░░░░   ░░░░░ ░░░░░░░░░░    ░░░░░░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░   """)
    print()
    print()
    typingprint("FROM TEAM 2, THANK YOU FOR PLAYING!")
    print()
    print("Team 2 Members: Amna, Ehinomen, Michael, Nigel, Olamide :)")
    print()
    quit(" ~ The game will now disconnect ~ ")

# game over screen **add colour here
def you_lose():
    typingprint("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   """)
    print()
    print()
    typingprint("FROM TEAM 2, THANK YOU FOR PLAYING!")
    print()
    print()
    print("Team 2 Members: Amna, Ehinomen, Michael, Nigel, Olamide :)")
    print()
    quit(" ~ The game will now disconnect ~ ")


#dice roll function to generate random numbers between the min and max range
def dice_roll(min, max):
    from random import randint
    roll_outcome = randint(min, max)
    return(roll_outcome)

# 1841 storylines
def year_1841():
    typingprint("You are out on a stroll on a sunny Sunday evening...Suddenly, you notice something. You are startled by the blasphemous sight of a naked person. Outraged, you go over to investigate it. As you bend over the body, etching closer to get a better view at the unholy sight you are witnessing, you are spotted by two other constables in uniform. ")
    print()
    typingprint("They shout out, assuming you are the culprit and arrest you.")
    print()
    typingprint("Option A: Demand to be released")
    print()
    typingprint("Option B: Co-operate with the constables")
    print()
    option = scenario_choice()
    if option == "A":
        year_1841_result("A")
    elif option == "B":
        year_1841_result("B")
    year_chooser()

def year_1841_result(option):
    story_A = "You cooperate - after being questioned at the station, you are later released on a witness' testimonies. You go to the dissection venue to learn from the anatomists' findings from the body. You find markings on the body that show an unholy wound, as if to have been torn apart by a beast. The anatomist informs you that the wound is nothing like he has seen before. You go back to the police department to check catalogues of crimes, but there is nothing useful there. So you decide to go to analyse the scene where the body was found."
    story_B = "You are accused and taken to prison - as you sit in your cell contemplating your decision, you hear a conversation between the other constables. 'The body is unlike anything I have witnessed before. Even the anatomist could not provide a concrete explanation of how they died. I must be insane to say, but I do not believe that the corpse belongs here'. 'What does he mean by “here”?', you think to youself. 'Was the corpse of a spy?' You test the cell bars for any loose bars. You pull on it and manage to dislodge one of them. You squeeze through and quickly make your way to the report room,  careful not to be discovered. You find a report of the body on one of the constables' desks, and you take it."
    if option =="A":
        typingprint(story_A)
        print()
        typingprint("Your discoveries lead you to an underground club by the train station. ")
        print()
        typingprint("Option A: Go inside the underground club.")
        print()
        typingprint("Option B: Do not go inside the underground club.")
        print()
        option = scenario_choice()
        if option == "A":
            year_1841_resultA("A")
        elif option == "B":
            year_1841_resultB("B")
    elif option =="B":
        typingprint(story_B)
        print()
        typingprint("Your discoveries lead you to an underground club by the train station. ")
        print()
        typingprint("Option A: Go inside the underground club.")
        print()
        typingprint("Option B: Do not go inside the underground club.")
        print()
        option = scenario_choice()
        if option == "A":
            year_1841_resultA("A")
        elif option == "B":
            year_1841_resultB("B")

def year_1841_resultA(option):
    global Analyst_Skill
    global Cunning_Skill
    global Fighting_Skill
    global inventory
    story_A = "You go in and notice a man across the room, camouflaged into the shadows, who beacons you closer. As you approach him, you try to scan his face, but the room is dark and his top hat casts a dark silhouette across his face leaving just his jaw exposed, which reveals a scar that runs from his chin towards his left ear. As the man begins to speak, you become more and more perplexed. “I have made a terrible mistake. I should not have been there, and now the timespace is broken. What have I done…Forgive me, please.” He drops to his knees, catching his head in his hands. His body shudders as he breaks down in tears. 'Timespace? What is this gibberish this man speaks of?' you think. You edge away from him. 'This man must be insane, but why does it sound familiar?' Before you have time to ask any questions, the man leaps to his feet and runs for the door. You try to stop him, but he pushes you back, knocking you against the wall. He darts out of the club and vanishes. You notice his hat on the floor, which fell from his head when he knocked you back. There is an inscription on the hem of the hat, a signature: 'M. L. Hubert.'"
    if option =="A":
        typingprint(story_A)
        print()
        analyst_increase = 2
        cunning_increase = 0
        fight_increase = 0
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = "Custom-made top hat"
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory} ")
            print()
    typingprint("You have completed this storyline and will now be exported.")
    print()
    typingprint("""
 _____                             _ 
|__  /__ _  __ _ _ __  _ __  _ __ | |
  / // _` |/ _` | '_ || '_ \| '_ \| |
 / /| (_| | (_| | |_) | |_) | |_) |_|
/____\__,_|\__,_| .__/| .__/| .__/(_)
                |_|   |_|   |_|      """)
    print()
    print()
    year_chooser()

def year_1841_resultB(option):
    global Analyst_Skill
    global Cunning_Skill
    global Fighting_Skill
    global inventory
    story_B = "As you approach the club, you feel anxious. 'Why do I feel as though I have been here before?' you think to yourself. As you reach for the door handle, you feel a shiver down your spine. You hesitate. Suddenly, the door swings open, nearly hitting you. Adrenaline is pumping in your veins as you leap backwards. A slender man emerges from the darkness of the club. His face is covered by his large top hat, only to reveal his jawline, where you notice a scar that travels from his left ear down to his chin. The man reaches his hand out and rests it on your shoulder. Unexpecting, you resist but his grip is firm on your shoulder. You fear he will attack you and reach for your musket. However, he begins to speak in a low, gentle voice tinted with remorse: “I have made a terrible mistake. I should not have been there, and now the times-pace is broken. For this, I do not deserve your forgiveness.” You stammer backwards. “Who are you?!” you shout. The man walks past you, and as he slips onto a side street, he says, “I am your biggest regret”."
    if option =="B":
        typingprint(story_B)
        print()
        analyst_increase = 1
        cunning_increase = 2
        fight_increase = 0
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = "Constable report"
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory} ")
            print()
    typingprint("You have completed this storyline and will now be exported.")
    print()
    typingprint("""
 _____                             _ 
|__  /__ _  __ _ _ __  _ __  _ __ | |
  / // _` |/ _` | '_ \| '_ \| '_ \| |
 / /| (_| | (_| | |_) | |_) | |_) |_|
/____\__,_|\__,_| .__/| .__/| .__/(_)
                |_|   |_|   |_|      """)
    print()
    print()
    year_chooser()

# 1928 storylines
def year_1928():
    typingprint("It is night time, and you are on your way home after work.")
    print()
    typingprint("Scenario: You walk past a well known Speakeasy.")
    print()
    typingprint("Option A: Go inside the Speakeasy")
    print()
    typingprint("Option B: Walk past the Speakeasy")
    print()
    option = scenario_choice()
    if option == "A":
        year_1928_result("A")
    elif option == "B":
        year_1928_result("B")
    year_chooser()

def year_1928_result(option):
    
    story_A = "You go inside the speakeasy and get a drink and see a mysterious woman sitting in the corner of the room. You walk over to talk to them. She reveals information about a body being found near the station. You think that she is bluffing but she hands you some information about the victim's blood type, which makes you suspect her even more. 'This is some very advanced serology', you think to yourself. You head over to the alleged location of the body. You find the body and investigate it."
    story_B = "You walk away from the speakeasy. A couple of drunk customers stumble out of the Speakeasy and unknowingly walk into you. Drunk and riled up, they start to sneer foul language at you. As you are not in uniform, they do not know that you are a detective. You try to show them your badge but they mistake this as a reach for a weapon and one of them throws a punch. You try to defend yourself but you are overtaken by the drunken thugs due to a disadvantage in numbers. When they reach for your wallet to try and steal from you, they realise that your are a detective and they flee, leaving you on the ground, unconscious..."
    if option =="A":
        typingprint(story_A)
        print()
        typingprint("As you wait for the police squad to arrive after discovering the body just as they said, you notice the mysterious woman from Speakeasy gliding past into a dark alley. You call out to her to find out how she knew about the body, but she does not stop.")
        print()
        typingprint("Option A: Run after the mysterious woman")
        print()
        typingprint("Option B: Wait for the police to arrive at the crime scene")
        print()
        option = scenario_choice()
        if option == "A":
            year_1928_resultA("A")
        elif option == "B":
            year_1928_resultA("B")
    elif option =="B":
        typingprint(story_B)
        print()
        typingprint(" * * * ")
        print()
        typingprint("You begin to come to, with blurred vision and coughing blood. Your head is pounding. You try to stand but you stumble and fall forward on your face. As you are falling in and out of consciousness, you see a naked person lying on the ground across from the Train Station, which startles you. Something is not right…")
        print()
        typingprint("Option A: get up and help the person")
        print()
        typingprint("Option B: ignore the drunken idiot and go home")
        print()
        option = scenario_choice()
        if option == "A":
            year_1928_resultB("A")
        elif option == "B":
            year_1928_resultB("B")

def year_1928_resultA(option):
    global Analyst_Skill
    global Cunning_Skill
    global Fighting_Skill
    global inventory
    story_A = "You go after her, and as you are running, you notice that she has quickened her pace. You shout out that you are a Detective and you are ordering for her to stop, but she keeps going. Finally, you see her run into an alleyway that you know is a deadend. 'I've got you know', you think to yourself. But once you turn onto the alleyway, you find that she is not there, as if she had vanished into thin air. All you see is a piece of paper on the ground. You analyse it, and are shocked, as you read text in a writing that is too uniform to be handwritten yet too elegant to have come from a typewriter. It says: “All the bodies are related, and you are the key.” You are in shock. 'What does she mean by “all the bodies…”'"
    story_B = "You wait for the police squad. It's been more than 25 minutes, but you know that it does not take that long to get here from the station, they are probably still smoking cigars in the Detective's pub, another Speakeasy under the guise of a “Hero's Haven”. You scan the crime scene area, and notice on the body that the there is a strange marking on it. Your eyes grow wide as you realise that the marking is a birthmark on their inner thigh, in the shape of a crescent moon. 'How can it be, they have the same birthmark as me?' You reach for your vest pocket camera and take a picture."
    if option =="A":
        typingprint(story_A)
        print()
        analyst_increase = 1
        cunning_increase = 2
        fight_increase = 0
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = "Typed note"
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory} ")
            print()
    elif option =="B":
        typingprint(story_B)
        print()
        analyst_increase = 2
        cunning_increase = 2
        fight_increase = 0
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = "Photograph of birthmark"
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory} ")
            print()
    typingprint("You have completed this storyline and will now be exported.")
    print()
    typingprint("""
 _____                             _ 
|__  /__ _  __ _ _ __  _ __  _ __ | |
  / // _` |/ _` | '_ \| '_ \| '_ \| |
 / /| (_| | (_| | |_) | |_) | |_) |_|
/____\__,_|\__,_| .__/| .__/| .__/(_)
                |_|   |_|   |_|      """)
    print()
    print()
    year_chooser()

def year_1928_resultB(option):
    global Analyst_Skill
    global Cunning_Skill
    global Fighting_Skill
    global inventory
    scenario_A = "You get up, swaying from side to side, to investigate. As you get closer to the body, you notice that its face is disfigured, from what seems to be a brutal artillery wound. The sight of this gruesome attack snaps you back into Detective mode. You blow your whistle to call for backup. As you do so, you notice something, a marking on the body's thigh. Your eyes grow wide as you realises that the marking is a birthmark in the shape of a crescent moon. 'How can it be, they have the same birthmark as me?' You reach for your vest pocket camera and take a picture."
    scenario_B = "You get up, swaying from side to side. You collect your belongings from the ground and slowly stumble home. The next morning, you are woken by the constant ringing of your stick phone. You answer it to find your superior shouting down the phone; “we need you at the station now! A body was discovered by the Train Station, and a witness has identified you at the scene, along with two others. Get here, now!” You get dressed and head over to the police station. You document everything that happened last night, but as you were unconscious from the fight, you cannot provide much information. However, the witness corroborats your story and you are released from duty for the day. You reflect on your decisions.'Why didn't I just check the body last night…?'"
    if option =="A":
        typingprint(scenario_A)
        print()
        analyst_increase = 1
        cunning_increase = 0
        fight_increase = 1
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = "Photograph of birthmark"
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory} ")
            print()
    elif option =="B":
        typingprint(scenario_B)
        print()
        analyst_increase = 0
        cunning_increase = 0
        fight_increase = 1
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = ""
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory} ")
            print()
    typingprint("You have completed this storyline and will now be exported.")
    print()
    typingprint("""
 _____                             _ 
|__  /__ _  __ _ _ __  _ __  _ __ | |
  / // _` |/ _` | '_ \| '_ \| '_ \| |
 / /| (_| | (_| | |_) | |_) | |_) |_|
/____\__,_|\__,_| .__/| .__/| .__/(_)
                |_|   |_|   |_|      """)
    print()
    print()
    year_chooser()

# 1979 storyline
def year_1979():
    global Analyst_Skill
    global Cunning_Skill
    global Fighting_Skill
    global inventory
    typingprint("You are making your way to the train station for the Divisional On-the-Job Training Programme held in New South Wales. You are already running late for the train when you hear a commotion a few blocks away from the station.")
    print()
    typingprint("Scenario: You see a crowd making a big commotion.")
    print()
    typingprint("Option A: Go and see what is happening")
    print()
    typingprint("Option B: Go to the train station")
    print()
    scenario_A = "You investigate what all the commotion is about. There is a large crowd gathered around. As you walk closer he sees a red puddle on the ground. It's blood. There is a trail leading to an alleyway. You push past the crowd towards the source of the blood.The blood appears to be flowing down from an alleyway. You shout to the crowd to stay back and for someone to call the police. You follow the stream of blood, which leads to a naked body lying on the ground. You rush over to check if they're alive but you are shocked with the gruesome defacement of the body. Blood is pouring from the ghastly wound. This was a recent attack. Who could have committed such a heinous crime?!"
    scenario_B = f"You ignore the commotion and continue on with the journey. You arrive at the train station, just a minute before your train is due. 25 minutes pass and your train still has not arrived. You get frustrated and stomp over to the train conductor's office. As you reach for the handle, an announcement is broadcasted throughout the station: “Due to unforeseen circumstances, the train has been cancelled. You sigh and leave the station. As you leave, your cell phone rings. It is your superior: “We have been informed of a body by the train station. All our members are either on duty elsewhere or at the Training Programme. Please tell me you have not left yet, {player}?”. I scoff, “no, the bloody trains are so unreliable, I won't be getting anywhere tonight. I'll get right on it”. You realise then that the crowd you saw earlier must have been gathered around the body. You head over to where the crowd was and see a stream of dried blood, there is a crowd of people there, larger than before, people screaming and shouting at the gruesome disfigurement on the body. You wave the crowd back with your Detective badge as you get closer to examine the issue. The body does not have any clothes on, aside from a long coat that a stranger from the crowd threw over to dignify the corpse. You put on your gloves and remove the coat to search around the body. You notice a sleek, black device under the corpse's hip. You reach for it. It is a device like never seen before, a sleek and portable rectangular device with no buttons, made of metal and glass. On the metal side of the device, there is what appears to be multiple miniature camera lenses on the surface, while the glass has a crack it. As you pick it up for a closer look, the screen turns on. You gasp, nearly dropping the device. Your eyes grow wide as you read from the screen:"
    option = scenario_choice()
    if option == "A":
        typingprint(scenario_A)
        print()
        analyst_increase = 1
        cunning_increase = 0
        fight_increase = 0
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = "Strange device"
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()        
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory} ")
            print()
    elif option == "B":
        typingprint(scenario_B)
        print()
        typingprint("    ------------------------------------------")
        print()
        typingprint("    |   13:57                                |")
        print()
        typingprint("    |   14/05/54                             |")
        print()
        typingprint(f"    |   Welcome, Detective {player}         |")
        print()
        typingprint("    |                                        |")
        print()
        typingprint("    ------------------------------------------")#MAYBE BETTER TO DO WITH ASCII
        print()
        analyst_increase = 1
        cunning_increase = 0
        fight_increase = 0
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = "Strange device"
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()        
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory} ")
            print()
    typingprint("You have completed this storyline and will now be exported.")
    print()
    typingprint("""
 _____                             _ 
|__  /__ _  __ _ _ __  _ __  _ __ | |
  / // _` |/ _` | '_ \| '_ \| '_ \| |
 / /| (_| | (_| | |_) | |_) | |_) |_|
/____\__,_|\__,_| .__/| .__/| .__/(_)
                |_|   |_|   |_|      """)
    print()
    print()
    year_chooser()

# 2024 storyline
def year_2024():
    typingprint(f"You are awoken by your phone ringing. It's the Police Captain, they inform you that a mysterious dead body has been found. You turn on the TV. The news is broadcasting a breaking story about a naked body, with its head violently disfigured, that has appeared just a couple streets down from Mayfield Depot Train Station. You rush down to the crime scene to you meet your superior. “The body has already been taken away by forensics, where have you been?” he glares at you. You stammer, trying to come up with a good excuse for why you overslept. “Anyway, we will discuss this later. For now, I need you to take a witness statement.” Your superior nods over to a teenage boy who is sat by the ambulance van. You approach the teenager. “My name is Detective {player}. Can you tell me your name?” The boy sits there, trembling, tears flooding his eyes. “I know that this has been a horrific experience for you, but can you tell me what you saw?” The boy whimpers, “I was walking down the street to meet up with me mates, and then I saw one of the streetlamps exploded, I thought one of my friends had lit up a firework so I went to go check it out, and that's when I saw…” He begins to cry. “They were just lying there, I got scared and ran away. I don't know how it got there. I don't know anything. They were just lying there”.")
    print()
    typingprint("After speaking with the witness, you approach your superior and inform him about what was said. “That kid knows more than he's letting on, do your job and find out what happened”, your superior scoffs.")
    print()
    typingprint("Option A: Co-operate with the Sergeant")
    print()
    typingprint("Option B: Leave the teenager alone")
    print()
    option = scenario_choice()
    if option == "A":
        year_2024_result("A")
    elif option == "B":
        year_2024_result("B")
    year_chooser()

def year_2024_result(option):
    story_A = "You reluctantly agree and go back to the boy. “Why were you there by yourself, where were you coming from?” The boy shrugs “I was coming home from school and gonna see me mates”. Something tells you that he is hiding something. You look behind him, into the ambulance van. There is a paramedic there. “Wait here” you instruct the boy, as you approach the paramedic. “What's this kid been treated for?” you ask. “He was mostly in a state of shock from what he had seen, the poor thing. Though there was some concern about the bruises he had on his arm. I've done plenty of injections to tell you what a bad job looks like…But there were also some old bruises, it seems like he's been a victim of assault.” You nod your head in concern, looking back at the boy. “What about his parents?” you ask the paramedic. “We've been trying to ring them for a while now, but have not been able to get in touch and he won't tell us anything.” You sigh, “We cannot legally question him without his parents or a legal advisor present. Might be worth getting in touch with child services and legal aid.”"
    story_B = "You clench your jaw, “the boy is frightened to death, have you even called his parents yet?”. “Of course we have, but they haven't picked up, probably a bunch of junkies on a bender by the state of the kid, probably done him a favour and calling Child Protective Services.” You glare at him, your temper quickly rising. “You don't even care about this kid!” you shout. Your superior smirks at you, “what's it to me if he's in the social, better than him winding up on the streets as another homeless crackhead or terrorist wannabe. I'm only doing my job here. Did you not hear him before, saying “fireworks”, yeah right”. As you hear the words come out of his mouth, you clench your fist. Without thinking, you extend your arm, connecting your fist to his jaw. *POW!* Your superior falls back in shock, but quickly recovers and returns a punch. You break out into a fight until another police officer separates you both. You are taken into the station for starting the fight, where you find the teenage boy is also there, waiting for further questioning."
    if option =="A":
        typingprint(story_A)
        print()
        typingprint("Option A: Call child services")
        print()
        typingprint("Option B: Talk to the teenager")
        print()
        option = scenario_choice()
        if option == "A":
            year_2024_resultA("A")
        elif option == "B":
            year_2024_resultA("B")
    elif option =="B":
        typingprint(story_B)
        print()
        typingprint("Option A: Approach the teenager")
        print()
        typingprint("Option B: Stay where you are")
        print()
        option = scenario_choice()
        if option == "A":
            year_2024_resultB("A")
        elif option == "B":
            year_2024_resultB("B")

def year_2024_resultA(option):
    global Analyst_Skill
    global Cunning_Skill
    global Fighting_Skill
    global inventory
    story_A = "You call child services, inform them of the situation and request that they provide legal aid for the child. Child services comes and the boy is taken away. You feel conflicted about your decision."
    story_B = "You go back to the boy and press him about his parents. “If we can't get in touch with your parents, we will be forced to call child services. Do you know where they are?” The boy shrugs, “I've not seen them since 2 months ago, they said they were going on a camping trip and won't come back”. You scratch your head as you think. Damn.  “Alright, I'm going to make sure you're well looked after”. You approach your Sergeant and inform him of what the nurse and the boy said. Your Sergeant calls child services. As you wait with the boy for child services to arrive, the holds your hand. You look down at him, and he is already looking at you, “i know you wanted better for me” he says. “I wished better for you but i failed you”. You narrow your eyes in confusion, “what do you mean?” you ask. “I should have been there for you more, and not let your mother's death destroy our family.” Before you can say anything else, the Sergeant comes to take the teenager to child services. You look back at the paramedic, wondering if the boy was still experiencing shock, but the paramedic was not there."
    if option =="A":
        typingprint(story_A)
        print()
        analyst_increase = 1
        cunning_increase = 2
        fight_increase = 0
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = ""
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory}")
            print()
    elif option =="B":
        typingprint(story_B)
        print()
        analyst_increase = 4
        cunning_increase = 1
        fight_increase = 0
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = ""
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
        else:
            inventory.append(evidence)
            typingprint(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory}")
            print()
    typingprint("You have completed this storyline and will now be exported.")
    print()
    typingprint("""
 _____                             _ 
|__  /__ _  __ _ _ __  _ __  _ __ | |
  / // _` |/ _` | '_ \| '_ \| '_ \| |
 / /| (_| | (_| | |_) | |_) | |_) |_|
/____\__,_|\__,_| .__/| .__/| .__/(_)
                |_|   |_|   |_|      """)
    print()
    print()
    year_chooser()

def year_2024_resultB(option):
    global Analyst_Skill
    global Cunning_Skill
    global Fighting_Skill
    global inventory
    story_A = "You wait for the Captain to summon you. While you try to figure out how you are going to word your account of what happened, you see the boy get taken away for questioning by your superior. You stand up, “where are you taking him? Aren't you meant to be waiting for the Captain too?”. His eyes cut towards your direction. “I've already spoken with the Captain, been let off with a slap on the wrist. Can't say the same will happen for you, considering you started the stupid fight. So as far as I'm concerned, you've got bigger problems than where I take him.” You know he is about to hand the child over to Child Services. You rapidly knock on the Captain's door. “Come in” a tired voice echoes from the room. You swing the door open, “I know we are due about to talk, but the Sergeant's just taken that boy to Child Services but we're not done questioning him. He could be getting put into even more danger and we don't know if his parents are still out there.” The Police Captain slams his fist on his desk, “that bloody shit shouldn't be doing anything without my approval, he's lucky I haven't asked for his badge for the amount of misconducts he's committed today!” With a heavy groan, the Police Captain emerges to his feet, waddling out of the office. His forehead is covered in beads of sweat just from moving from one room into the next. 'Is this what desk duty does to you?' you think to yourself. 'This guy needs to get back into the field and lose a few pounds'. “You”, the Captain points to one of the police officers in the office, “go get that Sergeant and bring him and the boy back here now. And tell him I want to see him in my office straight away!” The Captain turns to me, “you can go into my office now, we have a lot to discuss…”"
    story_B = f"While you wait to be called in by the Police Captain, you decide to sneak over to the teenager. “Are you okay?” you ask. The boy nods, as he wipes snot from his nose with the back of his hand. “Thank you for sticking up for me before. I saw you fighting that copper”. You laugh, “yeah but now I'm in heaps of trouble for that”. The boy looks at you with wide eyes; “it's okay. It's in your nature. You always were one to stand up for what's right, that's how we brought you up. It's a shame really how it ended” You narrow your eyes at the boy, “I don't think I follow…?” The boy looks at you, “it's alright love, you'll figure it out in the end.” The boy places an open locket in your hand. Inside is a picture of a vibrant young man, with a striking resemblance to the teenager, holding a baby close to his chest. You look up at him, confused and with so many questions. “I always keep you with me, and now you can keep me with you too”. Before you can say any more, the Police Captain shouts your name; “Detective {player}, what are you doing over there, you are in enough trouble without me adding witness tampering to the list, get into my office now!” You walk to the office, stuffing the locket into your pocket. As you look back, the teenage boy is no longer there. Instead, the man from the photo in the locket is there, only this time, he looks paler and malnourished, trembling and scratching his arms. “You got a spare cig on ya mate?” he asks one of the police officers."
    if option =="A":
        typingprint(story_A)
        print()
        analyst_increase = 0
        cunning_increase = 0
        fight_increase = 2
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = ""
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()
        else:
            inventory.append(evidence)
            print(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory}")
            print()
    elif option =="B":
        typingprint(story_B)
        print()
        analyst_increase = 1
        cunning_increase = 0
        fight_increase = 2
        Analyst_Skill += analyst_increase
        Cunning_Skill += cunning_increase
        Fighting_Skill += fight_increase
        evidence = "Locket"
        typingprint(f"You have gained {analyst_increase} Analyst Skill point(s). Total Analyst Skill points: {Analyst_Skill}")
        print()
        typingprint(f"You have gained {cunning_increase} Cunning Skill point(s). Total Cunning Skill points: {Cunning_Skill}")
        print()
        typingprint(f"You have gained {fight_increase} Fighting Skill points. Total Fighting Skill points: {Fighting_Skill}")
        print()
        if evidence == "":
            typingprint(f"You did not collect any evidence. The items in your inventory are: {inventory}")
            print()
        else:
            inventory.append(evidence)
            print(f"You have gained an item in your inventory: {evidence}. The items in your inventory are: {inventory}")
            print()
    typingprint("You have completed this storyline and will now be exported.")
    print()
    typingprint("""
 _____                             _ 
|__  /__ _  __ _ _ __  _ __  _ __ | |
  / // _` |/ _` | '_ \| '_ \| '_ \| |
 / /| (_| | (_| | |_) | |_) | |_) |_|
/____\__,_|\__,_| .__/| .__/| .__/(_)
                |_|   |_|   |_|      """)
    print()
    print()
    year_chooser()

# 2054 storyline endgame storyline
def year_2054():
    global Analyst_Skill
    global Cunning_Skill
    global Fighting_Skill
    print()
    typingprint("“Ugh, what happened? Where am I, what's going on?” You wake up with a slight headache.")
    print()
    typingprint("A nurse enters the room")
    print()
    typingprint("“Oh, you're awake? I'll go grab the Doctor, I'm sure you have lots of questions. He will be able to answer them for you.”")
    print()
    typingprint("The Doctor enters the room")
    print()
    typingprint(f"“Hello {player}, glad to see you are awake now and that our team managed to rescue what we could of your mind and its functions. Tell me, what do you remember?”")
    print()
    typingprint("“What happened to me?”")
    print()
    typingprint("The Doctor explains what happened: 'Well, after we were informed that you had joined the rise up raid against Hubert, we went to help, only to find you on the floor with blood gushing out of your ears. We tried to perform rapid CPR but you had major damage to your brain from whatever he did to you.”")
    print()
    typingprint("“So, we decided that the best way to save you was to keep your brain active by making you to recover your memories while we worked on the rest of your body. We initiated a new device in its testing phase and induced your brain into a coma. It is suppose to help stimulate the brain via scenarios and allow for the user to slowly repair their brain functions through its use. It is desinged to help those with Alzheimer's Disease.”")
    print()
    typingprint("“So, do you remeber anything?” the Doctor asks.")
    print()
    typingprint("“I remeber seeing that woman from before, the nurse.”")
    print()
    typingprint("“...Ahh yes. Unfortunately, we had to send her in to try and speed up the healing process.”")
    print()
    typingprint("After a talk with the Doctor about the past lives you experienced, the Doctor has suggests for you to rest. He leaves the room. However, you are struggling to let go of the feeling of wanting to know more about what happened.")
    print()
    typingprint("Option A: Rest in knowledge the villain has been defeated")
    print()
    typingprint("Option B: investigate the information you have collected")
    print()
    scenario_A = "You close your eyes knowing the danger is done. You take your much deserved rest to allow your body to heal. But then... you hear someone say: “sorry, but you know too much to be left alive.” Suddenly, you start to feel yourself slipping away, as your heart rate slows...until you see.....black..."
    scenario_B = "You jump out of the bed and sneak out of the facility. You head for the closest abandoned building to give yourself time and space to figure things out. As you do this, you notice that the pieces of evidence you had been collecting in your dreams all seem to suggest that the villain, known as M. L. Hubert was not in control over what had happened. And that someone had been forcing him to act and create the Time Travel device. Suddenly, you experience a flashback: a memory from when the accident happened, and how the Doctor immediately came in the moment the accident occurred. How was he there so fast? Was it coincidence? Your head begins to throb. How long have I been asleep for? As you rub your forehead, you notice a patient band on your wrist with information written on it, which informs you of the date. You gasp in shock. 'I have been asleep for 4 years?!'"
    option = scenario_choice()
    if option == "A":
        typingprint(scenario_A)
        you_lose()
    elif option == "B":
        typingprint(scenario_B)
        print()
        typingprint("Your face hardens and your heart is beating harder than your head is throbbing. You want to confront the Doctor but feel that you might be too weak to do so.")
        print()
        typingprint("Option A: Confront the Doctor?")
        print()
        typingprint("Option B: Go back and rest.")
        print()
        scenario_A = "You leave the abandoned building and go back to the facility to confront the Doctor about the possibility of him being behind everything. You search each room until you finally find him standing in front of a large, device made of titanium and other rare materials you have never seen before. “What is that?” you ask. The Doctor laughs.“It is unfortunate that you will never get to know what you have allowed me to do, but I need to get rid of you now as you know too much for my plans to succeed”. The Doctor pulls out a syringe."
        scenario_B = "You go back to your hospital bed inside the facility. You get into bed and close your eyes. You start to dream about a figure who you had not previously noticed, but in your dreams you realise that the figure had been in the background of every event you experienced while you were in a coma. The Doctor! You snap your eyes wide open, only to find the Doctor injecting something into your arm. You find that you are unable to move. You start to feel drowsy, struggling to keep your eyelids open. As you begin to slip away, you hear him say: “That's for getting in the way of my work the first time”. You close your eyes, never to open them again..."
        option = scenario_choice()
        if option == "A":
            typingprint(scenario_A)
            print()
            input("Your Cunning Skills and Fighting Skills will derermine the outcome of the game. Press Enter to continue.")
            typingprint(f"Detective {player}'s Cunning Skill: {Cunning_Skill}")
            print()
            typingprint(f"Detective {player}'s Fighting Skill: {Fighting_Skill}")
            print()
            if Fighting_Skill + Cunning_Skill < 13: #if stats are high enough, player will win battle
                typingprint("You start to struggle against the Doctor, but his strength surprises you and he is able to over power you and inject you with a syringe, causing you to stumble and fall backwards, as your heart beats for the last time...")
                you_lose()
            else:
                typingprint("You successfully manoeuvre around the Doctor, grab him by the arm and stab him with the very syringe he was trying to attacking you with. You watch as the Doctor's heart rate begins to slow until it completely stops beating. As he lays there, lifeless on the ground, you destroy the device he was about to use before leaving the facility, on a a new journey to find your next adventure...")
                game_over()
        elif option == "B":
            typingprint(scenario_B)
            you_lose()

#scenario choice generator - will take player's choice between A/B and return to year function to play the scenario
def scenario_choice():
    typingprint("What will you do next?")
    print()
    player_choice = input("Type 'A' to choose Option A, or type 'B' to choose Option B. ").strip().upper()
    typingprint(f"You have chosen option {player_choice}.")
    print()
    if player_choice == "A":
        return "A"
    elif player_choice == "B":
        return "B"
    else:
        typingprint("That is not a valid option. Please try again.")
        scenario_choice()

#year chooser - let's player navigate between the different years
def year_chooser():
    if year == []: #if storyline ends, player will be transported to 2054 storyline automatically
        typingprint(f"Excellent work Detective {player}, you have completed the storyline!")
        print()
        typingprint("But...Wait...What is happening to me??!")
        print()
        year_2054()
    else:
        print(f"Remaining years to travel to: {year}")
    player_chosen_year = input(f"Which year would you like to travel to, Detective {player}? ") #player chooses year to travel to
    if player_chosen_year == "1841":
        year.remove("1841")
        year_1841()
    elif player_chosen_year == "1928":
        year.remove("1928")
        year_1928()
    elif player_chosen_year == "1979":
        year.remove("1979")
        year_1979()
    elif player_chosen_year == "2024":
        year.remove("2024")
        year_2024()
    else:
        typingprint("That is not a valid year, or it may have already been chosen. Please try again")
        year_chooser()

#game starts here
start_game()

#Extras - ASCII ART, Colorama, typewriter effect