import tkinter as tk
import random

class lists:

    fullList = {}
    doneList = {}
    fullListLength = 0
    doneListLength = 0
    
    hiraganaSelected = False

    def __init__(self):
        self.hiragana = {}
        self.katakana = {}

        with open("groups/hiragana.txt", 'r', encoding="utf-8") as file:
            hiragana = file.readlines()

        for kana in hiragana:
            kana = kana.strip()
            kana = kana.split(";")
            self.hiragana[kana[0]] = kana[1].strip().split(",")

        with open("groups/katakana.txt", 'r', encoding="utf-8") as file:
            katakana = file.readlines()

        for kana in katakana:
            kana = kana.strip()
            kana = kana.split(";")
            self.katakana[kana[0]] = kana[1].strip().split(",")

    def selectLists(self, hiragana:bool, katakana:bool):
        self.fullList = {}
        self.doneList = {}
        self.fullListLength = 0
        self.doneListLength = 0
        self.hiraganaSelected = hiragana

        if hiragana == True:
            self.fullList |= self.hiragana

        if katakana == True:
            self.fullList |= self.katakana

        #kanji here

        self.fullListLength = len(self.fullList)

    def randomPick(self):
        if self.fullListLength == 0:
            self.selectLists(self.hiraganaSelected)

        if random.random() < 0.2 and self.doneListLength != 0:
            randomNumber = random.randint(0, self.doneListLength - 1)
            return list(self.doneList.items())[randomNumber]
        else:
            randomNumber = random.randint(0, self.fullListLength - 1)
            selectedPair = list(self.fullList.items())[randomNumber]
            self.fullList.pop(selectedPair[0])
            self.fullListLength -= 1
            self.doneList[selectedPair[0]] = selectedPair[1]
            self.doneListLength += 1
            return selectedPair


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.groups = lists()
        
        self.setup()

        self.root.mainloop()

    def setup(self):
        self.deleteAll()

        self.root.title("Japanese")
        self.root.geometry("600x400")
        self.root.config(bg="gray80")

        self.root.bind("<Escape>", lambda e: self.root.destroy())

        titleLabel = tk.Label(self.root, text="Japanese Learning", font=("Arial", 40, "bold"), bg="gray80")
        titleLabel.pack(pady=0)
        
        self.errorLabel = tk.Label(self.root, text=" ", font=("Arial", 10), bg="gray80", fg="red")
        self.errorLabel.pack(pady=0)
        
        areasLabel = tk.Label(self.root, text="Areas to study", font=("Arial", 20, "bold"), bg="gray80")
        areasLabel.pack(pady=0)

        self.hiraganaRadioVal = tk.BooleanVar(value=True)

        hiraganaCheckButton = tk.Checkbutton(self.root, text="Hiragana", variable=self.hiraganaRadioVal, font=("Arial", 15), bg="gray80")
        hiraganaCheckButton.pack(pady=5)

        self.katakanaRadioVal = tk.BooleanVar(value=True)

        katakanaCheckButton = tk.Checkbutton(self.root, text="Katakana", variable=self.katakanaRadioVal, font=("Arial", 15), bg="gray80")
        katakanaCheckButton.pack(pady=5)

        # kanji checkboxes here

        testTypeLabel = tk.Label(self.root, text="Test Type", font=("Arial", 20, "bold"), bg="gray80")
        testTypeLabel.pack(pady=5)

        testTypesFrame = tk.Frame(self.root, bg="gray80")
        testTypesFrame.pack()

        self.engKanaCheckRadioVal = tk.BooleanVar()

        engKanaCheckCheckButton = tk.Checkbutton(testTypesFrame, text="A ✓ or ✗", variable=self.engKanaCheckRadioVal, font=("Arial", 15, "bold"), bg="gray80")
        engKanaCheckCheckButton.pack(side="left", padx=10)
        

        tk.Label(testTypesFrame, text="|", font=("Arial", 15, "bold"), bg = "gray80", fg="gray").pack(side="left", padx=2)
        self.kanaToEngRadioVal = tk.BooleanVar()

        kanaToEngCheckButton = tk.Checkbutton(testTypesFrame, text="あ  →  A", variable=self.kanaToEngRadioVal, font=("Arial", 15, "bold"), bg="gray80")
        kanaToEngCheckButton.pack(side="left", padx=10)

        self.alwaysOnTopBoolVal = tk.BooleanVar()

        tk.Checkbutton(self.root, text="Always on top", font=("Arial", 10), bg="gray80",variable=self.alwaysOnTopBoolVal, command=self.ToggleAlwaysOnTop).pack()

        startButton = tk.Button(self.root, text="Start", font=("Arial", 15, "bold"), width=8, bg="gray80", command=self.titleStartCheck)
        startButton.pack(pady=20)

    def titleStartCheck(self):
        if self.hiraganaRadioVal.get() == False and self.katakanaRadioVal.get() == False:
            self.errorLabel.config(text="Select an area to study")
            return

        if self.engKanaCheckRadioVal.get() == False and self.kanaToEngRadioVal.get() == False:
            self.errorLabel.config(text="Select a way to test")
            return
        
        self.groups.selectLists(self.hiraganaRadioVal.get(), self.katakanaRadioVal.get())

        self.root.unbind("<Escape>")
        
        self.testScreen()
        
    def testScreen(self):
        self.root.config(bg="gray80")
        self.deleteAll()
        self.root.unbind("<Return>")

        self.root.bind("<Escape>", lambda e: self.exitToTitle())

        self.root.title("Testing")
        numOptions = 1
        if self.engKanaCheckRadioVal.get() == True and self.kanaToEngRadioVal.get() == True:
            numOptions = 2

        choice = 1
        if numOptions == 2:
            if random.random() > 0.5:
                choice = 1
            else:
                choice = 2
        else:
            if self.engKanaCheckRadioVal.get() == True:
                choice = 1
            else:
                choice = 2
        
        kanaChoice = self.groups.randomPick()

        if choice == 1:
            self.kanaCheckTest(kanaChoice[0], kanaChoice[1])
        elif choice == 2:
            self.kanaToEngTest(kanaChoice[0], kanaChoice[1])

    def kanaCheckTest(self, kana:str, engs:list):
        self.root.config(bg="gray80")

        tk.Label(self.root, text="/".join(engs), font=("Arial", 70, "bold"), bg="gray80").pack()

        revealButton = tk.Button(self.root, text="Reveal", font=("Arial", 20, "bold"), bg="gray80")
        revealButton.pack(pady=10)
        
        revealLabel = tk.Label(self.root, text=kana, font= ("UD Digi Kyokasho N", 70, "bold"), bg="black", width=10)
        revealLabel.pack()

        def revealAndUnbind():
            revealLabel.config(bg="gray80")
            self.root.unbind("<Return>")
            self.root.bind("<Return>", lambda e: self.testScreen())

        self.root.bind("<Return>", lambda e: revealAndUnbind())

        def reveal():
            revealLabel.config(bg="gray80")
            self.root.unbind("<Return>")
            self.root.bind("<Return>", lambda e: self.testScreen())

        revealButton.configure(command= reveal)

        tk.Button(self.root, text="Next", font=("Arial", 20, "bold"), bg="gray80", command=self.testScreen).pack(pady=10)
        
    def kanaToEngTest(self, kana:str, engs:list):
        self.root.bind("<Return>", lambda e: self.checkAnswer(kana, engs))

        label = tk.Label(self.root, text=kana, font= ("UD Digi Kyokasho N", 130, "bold"), bg="grey80")
        label.pack(pady=30)

        self.entryBox = tk.Entry(self.root, width=20, font=("Arial", 20, "bold"), justify="center")
        self.entryBox.pack(pady=10)
        self.entryBox.focus_set()

        tk.Button(self.root, text="Check", font=("Arial", 20, "bold"), bg="gray80", command=lambda: self.checkAnswer(kana, engs)).pack(pady=10)      

    def checkAnswer(self, kana, engs):
        self.root.unbind("<Return>")
        self.root.bind("<Return>", lambda e: self.testScreen())
        
        answer = self.entryBox.get().lower().strip()

        self.deleteAll()

        if answer in engs:
            self.root.config(bg="green")
            label = tk.Label(self.root, text=kana, font= ("UD Digi Kyokasho N", 130, "bold"), bg="green")
            label.pack(pady=20)
            label = tk.Label(self.root, text="/".join(engs), font= ("Arial", 30, "bold"), bg="green")
            label.pack()
            tk.Button(self.root, text="Next", font=("Arial", 20, "bold"), bg="gray80", command=self.testScreen).pack(pady=10)

        else:
            self.root.config(bg="red")
            label = tk.Label(self.root, text=kana, font= ("UD Digi Kyokasho N", 120, "bold"), bg="red")
            label.pack()
            label = tk.Label(self.root, text="/".join(engs), font= ("Arial", 40, "bold"), bg="red")
            label.pack()
            label = tk.Label(self.root, text="You Wrote:", font= ("Arial", 20, "bold"), bg="red")
            label.pack()
            label = tk.Label(self.root, text=answer, font= ("Arial", 20, "bold"), bg="red")
            label.pack()
            tk.Button(self.root, text="Next", font=("Arial", 20, "bold"), bg="gray80", command=self.testScreen).pack(pady=10)
        
    def ToggleAlwaysOnTop(self):
        if self.alwaysOnTopBoolVal.get() == True:
            self.root.wm_attributes('-topmost', True)
        else:
            self.root.wm_attributes('-topmost', False)

    def exitToTitle(self):
        self.root.unbind("<Escape>")
        self.setup()

    def deleteAll(self):
        for widget in self.root.winfo_children():
            widget.destroy()


App()