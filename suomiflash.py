import csv
from tkinter import *
from random import randint


# title splash screen
title_screen = Tk()
title_screen.attributes('-topmost',True)
# hide title bar
title_screen.overrideredirect(True)

root_label = Label(title_screen, text="SuomiFlash", font=("Arial", 50))
root_label.pack(pady=30)

# main screen size
app_width = 550
app_height = 450

# center screens in the middle of the screen
screen_width = title_screen.winfo_screenwidth()
screen_height = title_screen.winfo_screenheight()
x_coord = int((screen_width / 2) - (app_width / 2))
y_coord = int((screen_height / 2) - (app_height / 2))

title_screen.geometry(f"300x100+{x_coord + 125}+{y_coord + 100}")


### Functions ##########################################
vocab_files = {
    "General Vocab": "/Users/akehn/Documents/repos/suomiflash/vocab_files/general_vocab.csv", 
    "": "", 
}
vocab = []
def get_vocab():
    filepath = "/Users/akehn/Documents/repos/suomiflash/vocab_files/general_vocab.csv"
    with open(filepath, newline='') as vocab_csv:
        vocab_reader = csv.reader(vocab_csv, delimiter=',')
        for word in vocab_reader:
            vocab.append(word)


def button_enter(event):
    event.widget["fg"] = "#375efa"


def button_leave(event):
    event.widget["fg"] = "#000000"
########################################################


### Game Screen ########################################
def game_screen():
    '''
    Main Game Screen
    - This is going to be the screen that runs the game, formerly root.
    - Second function for the main menu.
    - Add a back button that goes back to the main menu.
    '''
    title_screen.destroy()

    root = Tk()
    root.title("Suomi Flash - Finnish Language Learning App")
    root.iconbitmap("/Users/akehn/Documents/repos/suomiflash/suomiflash.py")

    # create app's main window
    root.geometry(f"{app_width}x{app_height}+{x_coord}+{y_coord}")
    root.attributes('-topmost',True)


    ### Main Game Functions ################################
    def clear_answers():
        global hint_string, hint_count

        # clear previous word/answer
        ans_label.config(text="")
        entry_box.delete(0, END)

        # reset hint
        hint_label.config(text="")
        hint_string = ""
        hint_count = 0


    def next():
        '''
        Next Function
        Generates a random int to get a random word from the vocab list and sets the label
        to this word.
        '''
        clear_answers()

        # create random int/word
        global rand_word
        rand_word = randint(0, len(vocab)-1)

        # update label with the random word
        vocab_word.config(text=vocab[rand_word][0])


    global score
    score = 0
    def answer():
        '''
        Answer Function
        Takes the user's input and checks if their translation is correct. 
        '''
        global score

        if entry_box.get().capitalize() == vocab[rand_word][1]:
            ans_label.config(text=f"Correct! {vocab[rand_word][0]} translates to {vocab[rand_word][1]}.", fg="#34eba1")
            score += 1
        else:
            ans_label.config(text=f"Incorrect! {vocab[rand_word][0]} translates to {(vocab[rand_word][1]).capitalize()}.", fg="#eb345b")
            score = 0
        score_label.config(text=f"Score = {score}")


    # keeping track of the hints given
    global hint_string
    global hint_count
    hint_string = ""
    hint_count = 0
    def hint():
        '''
        Hint Function
        Provides the user with a hint to the answer, one letter at a time.
        '''
        global hint_string
        global hint_count

        word_length = len(vocab[rand_word][1])

        if hint_count < word_length:
            # keep giving hints
            hint_string = hint_string + vocab[rand_word][1][hint_count]
            hint_label.config(text=hint_string)
            hint_count += 1
    ########################################################

    ### Game Buttons #######################################
    # Word Label
    vocab_word = Label(root, text="", font=("Arial", 36))
    vocab_word.pack(pady=20)

    # Answer Label
    ans_label = Label(root, text="", font=("Helvetica", 20))
    ans_label.pack(pady=20)

    # Hint Label
    hint_label = Label(root, text="", font=("Arial", 15))
    hint_label.pack()

    # Answer Entry Box
    entry_box = Entry(root, font=("Arial", 18))
    entry_box.pack(pady=20)

    # Button Frame
    button_frame = Frame(root)
    button_frame.pack(pady=10)

    # Answer Button
    ans_button = Button(button_frame, text="Answer", command=answer, fg="#000000")
    ans_button.grid(row=0, column=1, padx=20)
    ans_button.bind("<Enter>", button_enter)
    ans_button.bind("<Leave>", button_leave)

    # Next Button
    next_button = Button(button_frame, text="Next", command=next, fg="#000000")
    next_button.grid(row=1, column=2)
    next_button.bind("<Enter>", button_enter)
    next_button.bind("<Leave>", button_leave)

    # Hint Button
    hint_button = Button(button_frame, text="Hint", command=hint, fg="#000000")
    hint_button.grid(row=1, column=0)
    hint_button.bind("<Enter>", button_enter)
    hint_button.bind("<Leave>", button_leave)

    # Score Label
    score_label = Label(root, text="", font=("Arial", 20))
    score_label.pack(pady=20)
    ########################################################

    get_vocab()
    next()

########################################################


### Main Menu ##########################################
def main_menu():
    '''
    Main Menu Screen
    '''
    pass
########################################################


########################################################
########################################################

title_screen.after(2000, game_screen)

mainloop()