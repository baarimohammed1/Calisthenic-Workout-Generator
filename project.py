from tabulate import tabulate
import random

def main():
    check_1 = explain_menu()
    muscle_group = choose_body_parts(check_1)
    difficulty = choose_difficulty(check_1)
    list_exercises = generate_exercises(muscle_group)
    sets = generate_sets(difficulty)
    print(generate_workout(list_exercises, sets))


def explain_menu():
    header = "Calisthenics Workout Generator"
    welcome ="Generate personalized Calesthenics\nworkout based on your experience \nand the body group you would like\nto train!"
    next = "Press X to Start Your Journey!"
    #print(tabulate({None, headers, tablefmt="grid"))
    print(tabulate({header: [welcome]}, headers="keys", tablefmt="fancy_grid"))
    while True:
        try:
            str = input("Enter X to continue: ").lower()
            if "x" == str:
                return "continue"
        except (KeyError, ValueError):
            print("Invalid Character, Press X to begin")
        pass



def choose_body_parts(str):
    if str == "continue":
            header = "Calisthenics Workout Generator"
    muscle_group ="Choose which group of muscle to \ntarget! \nEnter L for Lower Body. \nEnter U for Upper Body. \nEnter F for Full Body."
    print(tabulate({header: [muscle_group]}, headers="keys", tablefmt="fancy_grid"))
    while True:
        try:
            str = input("Enter L,U, or F to continue: ").lower()
            if "l" == str:
                return str
            if "u" == str:
                return str
            if "f" == str:
                return str
        except (KeyError, ValueError):
            print("Invalid Character, Enter either L,U, or F to continue")
        pass

def choose_difficulty(str):
        if str == "continue":
            header = "Calisthenics Workout Generator"
            difficulty_txt ="Choose the diffuclty of your workout.\nEnter B for Beginner. \nEnter I for Intermediate. \nEnter A for Advanced."
            print(tabulate({header: [difficulty_txt]}, headers="keys", tablefmt="fancy_grid"))
            while True:
                try:
                    str_1 = input("Enter B,I, or L to continue: ").lower()
                    if "b" == str_1:
                        return str_1
                    if "i" == str_1:
                        return str_1
                    if "a" == str_1:
                        return str_1
                except (KeyError, ValueError):
                    print("Invalid Character, Enter either B,I, or L to continue")
                pass

def generate_sets(difficulty):
    if difficulty == "b":
        sets = "3x8"
    if difficulty == "i":
        sets = "4x12"
    if difficulty == "a":
        sets = "5x15"
    return sets

def generate_exercises(muscle_group):
    upper = ["Pushups", "Diamond Pushups", "Pullups", "Pike Pushups", "Chinups", "Wide-grip Pushups", "Wide-grip Pullups"]
    lower = ["Squats", "Lunges", "Knee-tuck Jumps", "Calf Raises", "Jump Squats", "Box Jumps"]
    if muscle_group == "u":
        e_1 = random.choice(upper)
        e_2 = random.choice(upper)
        e_3 = random.choice(upper)
        e_4 = random.choice(upper)
    if muscle_group == "l":
        e_1 = random.choice(lower)
        e_2 = random.choice(lower)
        e_3 = random.choice(lower)
        e_4 = random.choice(lower)
    if muscle_group == "f":
        e_1 = random.choice(upper)
        e_2 = random.choice(upper)
        e_3 = random.choice(lower)
        e_4 = random.choice(lower)
    all_exercises = [e_1, e_2, e_3, e_4]
    return all_exercises


def generate_workout(all_exersises, sets):
    header = "Calisthenics Workout Generator"
    return(tabulate({header: [tabulate({"Exersise": all_exersises, "Sets" :[sets,sets,sets,sets]}, headers="keys", tablefmt="simplechp")]}, headers="keys", tablefmt="fancy_grid"))



if __name__ == "__main__":
    main()
