from tkinter import Label

class BackGround(Label):
    class Constants:
       width=1000
       height=1000

    def __init__ (self,master,x,y,width,image):
        self.__label=Label(master,image=image,width=width)
        #self.__label.configure(width=self.Constants.width,height=self.Constants.height)
        self.__label.place(x=x,y=y)