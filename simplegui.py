#! hashbing yo
#
#simple gui
#by joe

import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        #Reference Text Box
        #self.entryVariable = Tkinter.StringVar()
        #self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        #self.entry.grid(column=1,row=1,sticky='EW')
        #self.entry.bind("<Return>", self.OnPressEnter)
        #self.entryVariable.set(u"Enter text here.")

        #Reference Button
        #button = Tkinter.Button(self,text=u"Click me !",
        #                        command=self.OnButtonClick)
        #button.grid(column=3,row=1)

        #workaround for sides
        self.labelHiddenSpace = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelHiddenSpace, anchor="e")
        label.grid(column=0, row=1, columnspan=1, sticky='EW',)
        
        label = Tkinter.Label(self, textvariable=self.labelHiddenSpace,
                                    anchor="e")
        label.grid(column=9, row=1, columnspan=1, sticky='EW',)
        
        self.labelHiddenSpace.set(u"   ")        


        #Reference Label
        #self.labelVariable = Tkinter.StringVar()
        #label = Tkinter.Label(self, textvariable=self.labelVariable,
        #                      anchor="w",fg="white",bg="blue")
        #label.grid(column=1,row=2,columnspan=2,sticky='EW')
        #self.labelVariable.set(u"Hello !")


        #Label for Top Entry
        self.labelTopEntry = Tkinter.StringVar()
        labelTopEntry = Tkinter.Label(self, textvariable=self.labelTopEntry,
                                      anchor="w")
        labelTopEntry.grid(column=1, row=1, sticky="SW")
        self.labelTopEntry.set(u"String to Convert: ")

        #Top Entry Box
        self.entryTop= Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryTop)
        self.entry.grid(column=2,row=1, columnspan=6, sticky='EW')
        self.entryTop.set(u"")

        #Label for Bottom Entry
        self.labelBotEntry = Tkinter.StringVar()
        labelBotEntry = Tkinter.Label(self, textvariable=self.labelBotEntry,
                                      anchor="w")
        labelBotEntry.grid(column=1, row=3, sticky="SW")
        self.labelBotEntry.set(u"String to Revert: ")

        #Bottom Entry Box
        self.entryBot= Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryBot)
        self.entry.grid(column=2,row=3, columnspan=6, sticky='EW')
        self.entryBot.set(u"")

        #Convert Button
        button = Tkinter.Button(self,text=u" Convert! ",
                                command=self.OnButtonConvertClick)
        button.grid(column=1, row=5, columnspan=2)

        #Revert Button
        button = Tkinter.Button(self,text=u"  Revert!  "  ,
                                command=self.OnButtonRevertClick)
        button.grid(column=4, row=5, columnspan=3)

        #Workaround for Top, Mid and Bottom
        label = Tkinter.Label(self,anchor="w")
        label.grid(column=1,row=0,columnspan=3, sticky='W')
        label = Tkinter.Label(self,anchor="w")
        label.grid(column=1,row=4,columnspan=3, sticky='W')
        label = Tkinter.Label(self)
        label.grid(column=0,row=8,columnspan=6,sticky='W')

        #Stuff
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)



    #Event Handlers:

    def OnButtonConvertClick(self):
        strConvert = str(self.entryTop.get)
        print strConvert
        self.entryBot.set(strConvert.replace(" ", "q1x1"))

    def OnButtonRevertClick(self):
        pass



        

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('My App')
    app.mainloop()





