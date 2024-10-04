import csv
from tkinter import *
# import pandas as pd
from random import randint


root = Tk()
root.title("Suomi Flash - Finnish Language Learning App")
root.iconbitmap("/Users/akehn/Documents/repos/suomiflash/suomiflash.py")
root.geometry("550x450")


### Vocab Lists ########################################
vocab = [
    (("Hei"), ("Hi")), 
    (("Heihei"), ("Bye")),
    (("Kiitos"), ("Thank you")),
    (("Anteeksi"), ("Sorry")),
    (("Terve"), ("Hello")), 
    (("Tervetuloa"), ("Welcome")), 
    (("Kuka"), ("Who")), 
    (("Mukava"), ("Nice")), 
    (("Hauska"), ("Funny")), 
    (("Kaunis"), ("Beautiful")), 
    (("Komea"), ("Handsome")), 
    (("Kippis"), ("Cheers")), 
    (("Joo"), ("Yes")), 
    (("Kyllä"), ("Yes")), 
    (("Ei"), ("No")), 
    (("Paljon"), ("Lots")), 
    (("Onnea"), ("Good luck")), 
    (("Jee"), ("Yay")), 
    (("Ja"), ("And")), 
    (("Minä olen"), ("I am")), 
    (("Sinä olet"), ("You are")), 
    (("Aina"), ("Always")), 
    (("Mies"), ("Man")), 
    (("Nainen"), ("Woman")), 
    (("Ihminen"), ("Human")), 
    (("On"), ("Is")), 
    (("Hän"), ("He/She")), 
    (("Lapsi"), ("Child")), 
    (("Valkoinen"), ("White")), 
    (("Harmaa"), ("Grey")), 
    (("Ruskea"), ("Brown")), 
    (("Purppura"), ("Purple")), 
    (("Violetti"), ("Purple")), 
    (("Sininen"), ("Blue")), 
    (("Vihreä"), ("Green")), 
    (("Keltainen"), ("Yellow")), 
    (("Oranssi"), ("Orange")), 
    (("Punainen"), ("Red")), 
    (("Vaaleanpunainen"), ("Pink")), 
    (("Pinki"), ("Pink")), 
    (("Musta"), ("Black")), 
    (("Ujo"), ("Shy")), 
    (("Hiljainen"), ("Quiet")), 
    (("Ystävä"), ("Friend")), 
    (("Rehellinen"), ("Honest")), 
    (("Tyttö"), ("Girl")), 
    (("Poika"), ("Boy")), 
    (("Sisko"), ("Sister")), 
    (("Herra"), ("Mr")), 
    (("Suomi"), ("Finland")), 
    (("Suomeksi"), ("In Finnish")), 
    (("Suomea"), ("Finnish")), 
    (("Tämä"), ("This")), 
    (("Maa"), ("Country")), 
    (("Hyvä"), ("Good")), 
    (("Todella"), ("Very")), 
    (("Rouva"), ("Mrs")), 
    (("Isä"), ("Father")), 
    (("Maanantai"), ("Monday")), 
    (("Tiistai"), ("Tuesday")), 
    (("Keskiviikko"), ("Wednesday")), 
    (("Torstai"), ("Thursday")), 
    (("Perjantai"), ("Friday")), 
    (("Lauantai"), ("Saturday")), 
    (("Sunnuntai"), ("Sunday")), 
    (("Tammikuu"), ("January")), 
    (("Helmikuu"), ("February")), 
    (("Maaliskuu"), ("March")), 
    (("Huhtikuu"), ("April")), 
    (("Toukokuu"), ("May")), 
    (("Kesäkuu"), ("June")), 
    (("Heinakuu"), ("July")), 
    (("Elokuu"), ("August")), 
    (("Syyskuu"), ("September")), 
    (("Lokakuu"), ("October")), 
    (("Marraskuu"), ("November")), 
    (("Joulukuu"), ("December")), 
    (("Maalit"), ("Goals")), 
    (("Maali"), ("Goal")), 
    (("Tehdä"), ("To do")), 
    (("Syntymäpäivä"), ("Birthday")),
    (("Syntymäpäivät"), ("Birthdays")),  
    (("Kuu"), ("Moon")), 
    (("Kuukaudet"), ("Months")), 
    (("Viikonpäivät"), ("Days of the week")), 
    (("Huomenta"), ("Morning")), 
    (("Nähdään"), ("See you")), 
    (("Ole hyvä"), ("You're welcome")), 
    (("Ei kestä"), ("Don't mention it")),  
    (("Ei se mitään"), ("It's nothing")), 
    (("Okei"), ("Ok")), 
    (("Selva"), ("Ok")), 
    (("Mennään"), ("Let's go")), 
    (("Hitaammin"), ("Slower")), 
    (("Opiskelen"), ("I study")), 
    (("Koira"), ("Dog")), 
    (("Kissa"), ("Cat")), 
    (("Järvi"), ("Lake")), 
    # ((""), ("")), 
    # ((""), ("")), 
]
# vocab = []

# def get_vocab():
#     paths = ["/Users/akehn/Documents/repos/suomiflash/vocab_files/general_vocab.csv"]
#     for path in paths:
#         df = pd.read_csv(path, na_filter=False, encoding = 'utf-8')

#         # check the column headers
#         # pd.set_option('display.max_columns', None)
#         # print(df.head())
#         # return

#         for index, word in df.iterrows():
#             vocab.append(word)
#     return

vocab = []
def get_vocab():
    filepath = "/Users/akehn/Documents/repos/suomiflash/vocab_files/general_vocab.csv"
    with open(filepath, newline='') as vocab_csv:
        vocab_reader = csv.reader(vocab_csv, delimiter=',')
        for word in vocab_reader:
            vocab.append(word)
########################################################


### Functions ##########################################
def next():
    '''
    Next Function
    Generates a random int to get a random word from the vocab list and sets the label
    to this word.
    '''
    global hint_string, hint_count

    # clear previous word/answer
    ans_label.config(text="")
    entry_box.delete(0, END)
    # reset hint
    hint_label.config(text="")
    hint_string = ""
    hint_count = 0

    # create random int/word
    global rand_word
    rand_word = randint(0, len(vocab)-1)

    # update label with the random word
    vocab_word.config(text=vocab[rand_word][0])


def answer():
    '''
    Answer Function
    Takes the user's input and checks if their translation is correct. 
    '''
    print(entry_box.get().capitalize())

    if entry_box.get().capitalize() == vocab[rand_word][1]:
        ans_label.config(text=f"Correct! {vocab[rand_word][0]} translates to {vocab[rand_word][1]}.", fg="#34eba1")
    else:
        ans_label.config(text=f"Incorrect! {vocab[rand_word][0]} translates to {(vocab[rand_word][1]).capitalize()}.", fg="#eb345b")


# keeping track of the hints given
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


########################################################
# Word Label
vocab_word = Label(root, text="", font=("Arial", 36))
vocab_word.pack(pady=50)

# Answer Label
ans_label = Label(root, text="")
ans_label.pack(pady=20)

# Answer Entry Box
entry_box = Entry(root, font=("Arial", 18))
entry_box.pack(pady=20)

# Button Frame
button_frame = Frame(root)
button_frame.pack(pady=20)

# Answer Button
ans_button = Button(button_frame, text="Check", command=answer)
ans_button.grid(row=0, column=1, padx=20)

# Next Button
next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=1, column=2)

# Hint Button
hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=1, column=0)

# Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)
########################################################


# program start
get_vocab()
next()

root.mainloop()