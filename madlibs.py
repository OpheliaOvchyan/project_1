print("Welkome to our game")
print()

while True:
    try:
        num = int(input("Enter a number from 1 to 3: "))
        if 0 < num <  4:
            break
    except ValueError:
        print("Enter a valid number from 1 to 3: ")


def story(questions, text):
        answers = []
        for i in questions:
            while True:
                answer = input(i).strip()

                if answer == "":
                    print("Input cannot be empty. Try again.")
                    continue

                if "number" in i.lower():
                    try:
                        int(answer)  
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                answers.append(answer)
                break

        return text.format(*answers)


if num == 1:
    questions= [
                "Enter a number: ", 
                "Enter Measure of time: ",
                "Enter a Mode of Transportation: ",
                "Enter a Adjective: ",
                "Enter a Adjective: ",
                "Enter a none: ", 
                "Enter a color: ", 
                "Enter a part of the body: ", 
                "Enter a verb: ", 
                "Enter a number: ", 
                "Enter a none: ", 
                "Enter a none: ", 
                "Enter a part of the body: ", 
                "Enter a verb: ", 
                "Enter a none: ", 
                "Enter a Adjective: ",
                "Enter a Silly Word: ", 
                "Enter a none: "
            ]

        


    text = """
        The hospital is a/an {} place, there are a lot of {} {} here.
        There are nurses here who have {} {}.
        If someone wants to come into my room I told them that they have to {} first.
        I've decorated my room with {} {}.
        Today I talked to a doctor and they were wearing a {} on their {}.
        I heard that all doctors {} {} every day for breakfast.
        The most {} thing about being in the hospital is the {} {}!
        """    


elif num == 2:
    questions = [
                "Enter a person's name: ",
                "Enter a noun: ",
                "Enter an adjective (feeling): ",
                "Enter a verb: ",
                "Enter another adjective (feeling): ",
                "Enter an animal: ",
                "Enter a verb: ",
                "Enter a color: ",
                "Enter a verb ending in -ing: ",
                "Enter an adverb : ",
                "Enter a number: ",
                "Enter a measure of time: ",
                "Enter a color: ",
                "Enter another animal: ",
                "Enter a number: ",
                "Enter a silly word: ",
                "Enter a noun: "
            ]            


    text = """
        This weekend I am going camping with {}. I packed my lantern, sleeping bag, and {}.
        I am so {} to {} in a tent. I am {} we might see a(n) {}, I hear they’re kind of dangerous.
        While we’re camping, we are going to hike, fish, and {}.
        I have heard that the {} lake is great for {}.
        Then we will {} hike through the forest for {} {}.
        If I see a {} {} while hiking, I am going to bring it home as a pet!
        At night we will tell {} {} stories and roast {} around the campfire!
        """    



elif num == 3:
    questions = [
                "Enter a person's name: ",
                "Enter an adjective: ",
                "Enter a color: ",
                "Enter an animal: ",
                "Enter a place: ",
                "Enter an adjective: ",
                "Enter a magical creature (plural): ",
                "Enter another adjective: ",
                "Enter another magical creature (plural): ",
                "Enter a room in a house: ",
                "Enter a noun: ",
                "Enter a noun: ",
                "Enter a plural noun: ",
                "Enter an adjective: ",
                "Enter another plural noun: ",
                "Enter a number: ",
                "Enter a measure of time: ",
                "Enter a verb ending in -ing: ",
                "Enter an adjective: ",
                "Enter a noun: "
            ]                    



    text = """
        Dear {}, I am writing to you from a {} castle in an enchanted forest.
        I found myself here one day after going for a ride on a {} {} in {}.
        There are {} {} and {} {} here!
        In the {} there is a pool full of {}.
        I fall asleep each night on a {} of {} and dream of {} {}.
        It feels as though I have lived here for {} {}.
        I hope one day you can visit, although the only way to get here now is {} on a {} {}!
        """                

final_text = story(questions, text)
print(final_text)
        