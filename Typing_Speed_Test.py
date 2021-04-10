import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from timeit import default_timer as timer
from PIL import ImageTk , Image
import random
import sqlite3

conn = sqlite3.connect('leaderboard.db')
cur = conn.cursor()
print("Opened database successfully")

"""
CREATE TABLE leaderboard (
    id   INTEGER PRIMARY KEY
                 UNIQUE
                 NOT NULL,
    name VARCHAR NOT NULL,
    wpm  DOUBLE
);
"""


windows = Tk()
windows.geometry( "600x600" )
windows.resizable( 0 , 0 )
windows.title( "Typing Speed Test" )
windows.configure( background='mint cream' )
windows.iconbitmap('./keyboard.ico')

def login ():
    frame1 = Frame( windows )
    img = ImageTk.PhotoImage( Image.open( "./bg.jpg" ) )
    image = tk.Label( frame1 , image=img )
    image.image = img
    image.place( x=0 , y=0 )
    frame1.place( height=600 , width=600 , x=0 , y=0 )

    Welcome_Message = Label( frame1 , text="Welcome to Typing Speed Test!!" , bg= '#eaeceb' ,
                             font=("Copperplate Gothic Bold" , "20" ,) , fg='navy' )
    Welcome_Message.place( x=60 , y=175 )

    frame_login = Frame( frame1 )
    img = ImageTk.PhotoImage( Image.open( "./n1.jpg" ) )
    image = tk.Label( frame_login,image=img )
    image.image = img
    image.place( x=0,y=0 )
    frame_login.pack()
    frame_login.place( height=115 , width=275 , x=150 , y=275 )

    def click ( *args ):
        name.delete( 0 , 'end' )

    myFont = font.Font( family='Helvetica' , size=10 , weight='bold' )
    myFont1 = font.Font( family='Candara',size=12 )
    name = Entry( frame_login , width=25 )
    name[ 'font' ] = myFont1
    name.pack( pady=30 )
    name.place( x=20 , y=20,height=30 )
    name.insert( 0 , 'Enter Your Name:' )
    name.bind( "<Button-1>" , click )

    def Save_Details ( name ):
        if name == '':
            messagebox.showerror( 'ERROR' , 'Name field cannot be empty' )
        elif name == 'Enter Your Name:':
            messagebox.showerror( 'ERROR' , 'Please Enter your Name' )
        else:
            frame1.destroy()
            test = Test_Window( name )

    button_enter = Button( frame_login , text='Save Details' , bg='snow' , command=lambda: Save_Details( name.get() ) ,
                           padx=1 ,
                           pady=1 )
    button_enter[ 'font' ] = myFont
    button_enter.pack()
    button_enter.place( x=20 , y=70 )


def Test_Window ( username ):
    start = timer()  # Starting the timer when window is displayed
    wpm = 0
    Frame_test = Frame( windows )
    img = ImageTk.PhotoImage( Image.open( "./bg1.jpg" ) )
    image = tk.Label( Frame_test,image=img )
    image.image = img
    image.place( x=0,y=0 )
    Frame_test.place( height=700 , width=600 , x=0 , y=0 )

    welcome = font.Font( family='Verdana' , size=15 , weight='bold' )
    Welcome_User = Label( Frame_test , text="Welcome " + username , bg='#e6e8f4' )
    Welcome_User[ 'font' ] = welcome
    Welcome_User.place( x=0 , y=50 )
    Statement = Label( Frame_test , text="Type this:" , bg='#eeeef6' , font=('Rockwell' , 13, 'bold') )
    Statement.place( x=0 , y=100 )

    sentences = [ 'The quick brown fox jumps over the lazy dog' ,
                  'A bird in the hand is worth two in the bush' ,
                  'Dont count your chickens before they hatch' ,
                  'The sharper the berry the sweeter the wine' ,
                  'A weed is no more than a flower in disguise' ]

    sentence_index = random.randint( 0 , len( sentences ) - 1 )

    Ques = Label( Frame_test , text='"' + sentences[ sentence_index ] + '"' , bg='#f4f3f8' ,fg='navy', font=('Lucida Console' , '14','bold') )
    Ques.place( x=20 , y=150 )

    def click ( *args ):
        Answer.delete( 0 , 'end' )

    Answer = Entry( Frame_test , width=45 )
    myFont1 = font.Font( family='Candara',size=16 )
    Answer[ 'font' ] = myFont1
    Answer.pack()
    Answer.place( x=30 , y=200 , height=40 )
    Answer.insert( 0 , 'Type your answer here:' )
    Answer.bind( "<Button-1>" , click )

    def Submit ():
        if Answer.get() == '':
            messagebox.showwarning( 'WARNING' , 'Answer field is empty' )
        elif Answer.get() == 'Type your answer here:':
            messagebox.showwarning( 'WARNING' , 'Please enter proper answer' )
        else:
            end = timer()
            time_taken = int( end - start )

            User_answer = Answer.get()
            Ques_displayed = sentences[ sentence_index ]

            index_ques = 0
            correct_char = 0
            for char in User_answer:
                if (Ques_displayed[ index_ques ] == char):
                    correct_char += 1
                index_ques += 1

            Accuracy = (correct_char * 100) / len( Ques_displayed )
            wpm = (len( (User_answer).split(" ") ) * 60) / (time_taken)
            cursor = cur.execute('select * from leaderboard;')
            id = len(cursor.fetchall())
            
            cur.execute("INSERT INTO leaderboard (id,name,wpm) VALUES (? , ? , ? );",(id+1,username,wpm))
            conn.commit()
            ranks = cur.execute("SELECT name, RANK () OVER (ORDER BY wpm DESC) leaderboardRank FROM leaderboard;")
            for item in ranks:
                if(item[0] == username):
                    rank = item[1]

            Result=Label(Frame_test,text="RESULTS :",bg='#e3d5da',font=('Arial Black','16'))
            Result.place( x=20,y=355 )
            Result_1 = Label( Frame_test ,
                            text="\nTime: {:.2f} seconds \n\nAccuracy: {:0.2f}%\n\nWords Per Minute : {:0.1f}\n\nLeaderboard Rank : {}".format( time_taken ,
                                                                                                           Accuracy ,
                                                                                                           wpm,
                                                                                                           rank) ,
                            bg='#e3d5da',font=('Times' , '14','bold') )
            Result_1.place(x=20,y=385)

    myFont = font.Font( family='Courier New' , size=10 , weight='bold' )
    Submit_button = Button( Frame_test , text='Submit' , bg='#414d67' ,fg='white', command=Submit , padx=20 , pady=1 )
    Submit_button[ 'font' ] = myFont
    Submit_button.place( x=30 , y=275 )

    def Reset ():
        Test_Window( username )

    Reset_button = Button( Frame_test , text='Reset' , bg='#414d67' ,fg='white', command=Reset , padx=30 , pady=1 )
    Reset_button[ 'font' ] = myFont
    Reset_button.place( x=180 , y=275 )


login()
windows.mainloop()
