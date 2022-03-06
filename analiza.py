import random
import string
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

counter=(''.join(random.choices(string.ascii_uppercase, k=3)))

def choose_file():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(initialdir='./', initialfile='*.txt', \
    filetypes=[("*.TXT", "*.txt")]) # show an "Open" dialog box and return the path to the selected file
    return filename

def welcome():
    komunikat="Witaj w programie analizy statystycznej"
    spaces=0
    for chars in range(len(komunikat)):
        if komunikat[chars]==' ':
            spaces+=1
    print("="*(len(komunikat)+spaces+1))
    print("=",komunikat,"=")
    print("="*(len(komunikat)+spaces+1))

def analysis():
    file_path=choose_file()
    if file_path:
        file=open(file_path, "r")
        f_content=file.read()
        f_content=f_content.replace(" ", "")
        f_content=f_content.lower()

        letters=string.ascii_lowercase
        dict=[]
        for h in letters:
            dict.append(h)

        for i in range(0,26):
            litery=''
            if f_content.count(dict[i])>1:
                litery+=dict[i]
                print(dict[i]+"|",int(f_content.count(dict[i]))*"x ")
        rozdzialka=''
        for x in range(1,76):
            x=str(x)
            rozdzialka=str(rozdzialka+x+" ")
            if int(x)==75:
                print(int(x)*"===")
        print(2*" ",rozdzialka)
    else:
        print("Błąd wybierania pliku tekstowego")
        return 0

welcome()
analysis()

end=input("Aby zakonczyc wcisnij enter")
