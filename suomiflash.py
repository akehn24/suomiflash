import csv
import googletrans
import textblob
from googletrans import Translator
from tkinter import *
from tkinter import ttk, messagebox
from random import randint


### Title Splash Screen ################################
title_screen = Tk()
title_screen.attributes('-topmost',True)
# hide title bar
title_screen.overrideredirect(True)

root_label = Label(title_screen, text="SuomiFlash", font=("Arial", 50))
root_label.pack(pady=30)

# main screen size
app_width = 650
app_height = 550

# use these to center your windows
screen_width = title_screen.winfo_screenwidth()
screen_height = title_screen.winfo_screenheight()
x_coord = int((screen_width / 2) - (app_width / 2))
y_coord = int((screen_height / 2) - (app_height / 2))

title_screen.geometry(f"300x100+{x_coord + 175}+{y_coord + 200}")
########################################################


### Functions ##########################################
vocab_files = {
    "Choose Your Vocab": "", 
    "General Vocab": "/Users/akehn/Documents/repos/suomiflash/vocab_files/general_vocab.csv", 
    "People": "/Users/akehn/Documents/repos/suomiflash/vocab_files/people_vocab.csv", 
    "Animals": "/Users/akehn/Documents/repos/suomiflash/vocab_files/animal_vocab.csv", 
    "Colors": "/Users/akehn/Documents/repos/suomiflash/vocab_files/color_vocab.csv", 
    "Calendar": "/Users/akehn/Documents/repos/suomiflash/vocab_files/calendar_vocab.csv", 
    "Numbers": "/Users/akehn/Documents/repos/suomiflash/vocab_files/number_vocab.csv", 
}
global vocab
def get_vocab(vocab_file):
    global vocab
    vocab = []
    vocab_file = vocab_file.get()

    filepath = vocab_files[vocab_file]
    if filepath:
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
    Runs the vocab game.
    '''
    game_screen = Toplevel()
    game_screen.title("Suomi Flash - Finnish Language Learning App")
    # iconbitmap to be added later...
    # game_screen.iconbitmap("/Users/akehn/Documents/repos/suomiflash/window_icon.ico")

    # create app's main window
    game_screen.geometry(f"{app_width}x{app_height}+{x_coord}+{y_coord}")
    game_screen.attributes('-topmost',True)


    ### Notebook Tabs #########################
    game_notebook = ttk.Notebook(game_screen)
    game_notebook.pack(fill="both")

    game_frame = Frame(game_notebook, width=app_width, height=app_height)
    game_frame.pack(fill="both", expand=1)

    translator_frame = Frame(game_notebook, width=app_width, height=app_height)
    translator_frame.pack(fill="both", expand=1)

    game_notebook.add(game_frame, text="SuomiFlash")
    game_notebook.add(translator_frame, text="Translator")
    ###########################################


    ### Game Functions ########################
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
        global vocab
        global rand_word
        rand_word = randint(0, len(vocab)-1)

        # update label with the random word
        vocab_word.config(text=vocab[rand_word][0])


    def return_answer(event):
        answer()

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
    ###########################################


    ### Game GUI ##############################
    # Word Label
    vocab_word = Label(game_frame, text="", font=("Arial", 36))
    vocab_word.pack(pady=20)

    # Answer Label
    ans_label = Label(game_frame, text="", font=("Helvetica", 20))
    ans_label.pack(pady=20)

    # Hint Label
    hint_label = Label(game_frame, text="", font=("Arial", 15))
    hint_label.pack()

    # Answer Entry Box
    entry_box = Entry(game_frame, font=("Arial", 18))
    entry_box.pack(pady=20)
    entry_box.bind("<Return>", return_answer)

    # Button Frame
    button_frame = Frame(game_frame)
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
    score_label = Label(game_frame, text="", font=("Arial", 20))
    score_label.pack(pady=20)

    # Back Button
    back_button = Button(game_frame, text="Back to Menu", command=game_screen.destroy)
    back_button.pack()
    ###########################################


    ### Translator Functions ##################
    languages = googletrans.LANGUAGES
    language_list = list(languages.values())

    def clear_language():
        text_to_translate.delete(1.0, END)
        translated_text.delete(1.0, END)


    def translate_text():
        # delete previous translation
        translated_text.delete(1.0, END)
        g_translator = Translator()

        try:
            # get language code
            for key, value in languages.items():
                if value == language_to_translate.get():
                    lang_to_trans_code = key

            for key, value in languages.items():
                if value == translate_to_language.get():
                    trans_to_lang_code = key

            text_translated = g_translator.translate(text_to_translate.get(1.0, END), src=lang_to_trans_code, dest=trans_to_lang_code)
            translated_text.insert(1.0, text_translated.text)

        except Exception as e:
            messagebox.showerror("Translator", e, parent=game_screen)
            print(e)
    ###########################################


    ### Translator GUI ########################
    text_to_translate = Text(translator_frame, width=30, height=20)
    text_to_translate.grid(row=0, column=0, pady=20, padx=10)

    translate_button = Button(translator_frame, text="Translate", font=("Arial", 24), command=translate_text)
    translate_button.grid(row=0, column=1)

    translated_text = Text(translator_frame, width=30, height=20)
    translated_text.grid(row=0, column=2, pady=20, padx=10)

    language_to_translate = ttk.Combobox(translator_frame, width=10, value=language_list)
    language_to_translate.current(21)  # english = 21
    language_to_translate.grid(row=1, column=0)

    translate_to_language = ttk.Combobox(translator_frame, width=10, value=language_list)
    translate_to_language.current(25)  # finnish = 25
    translate_to_language.grid(row=1, column=2)

    clear_button = Button(translator_frame, text="Clear", command=clear_language)
    clear_button.grid(row=2, column=1)
    ###########################################

    next()
########################################################


### Main Menu ##########################################
def main_menu():
    '''
    Main Menu Screen
    '''
    title_screen.destroy()

    root = Tk()
    root.title("Suomi Flash - Finnish Language Learning App")
    root.iconbitmap("/Users/akehn/Documents/repos/suomiflash/suomiflash.py")

    # create app's main window
    root.geometry(f"{app_width}x{app_height}+{x_coord}+{y_coord}")
    root.attributes('-topmost',True)


    def on_select_vocab(selection):
        if selection.get() != "Choose Your Vocab":
            get_vocab(vocab_file)


    ### Menu Buttons/Labels ###################
    # Title Label
    title_label = Label(root, text="SuomiFlash", font=("Arial", 36))
    title_label.pack(pady=20)

    # Choose Your Vocab Label
    choose_label = Label(root, text="Choose your vocab:", font=("Arial", 20))
    choose_label.pack(pady=20)

    # Vocab Dropdown
    vocab_file_options = ["Choose Your Vocab", "General Vocab", "People", "Animals", "Colors", "Calendar", "Numbers",]
    vocab_file = StringVar()
    vocab_file.set(vocab_file_options[0])
    vocab_dropdown = OptionMenu(root, vocab_file, *vocab_file_options, command=lambda x:(on_select_vocab(vocab_file)))
    vocab_dropdown.pack()

    # # Button Frame
    button_frame = Frame(root)
    button_frame.pack(pady=10)

    # Start Button
    start_button = Button(root, text="Start", command=game_screen)
    start_button.pack(pady=20)

    # Quit Button
    quit_button = Button(root, text="Quit", command=root.quit)
    quit_button.pack()
    ###########################################
########################################################


########################################################

title_screen.after(2000, main_menu)

mainloop()