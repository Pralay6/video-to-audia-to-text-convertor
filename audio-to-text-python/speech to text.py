import pytube
import tkinter
from tkinter import filedialog 
from tkinter import *
from pytube import YouTube
import os
import speech_recognition as sr
import datetime
from googletrans import Translator
translator = Translator()
c = 210
try:
    os.remove("output.mp4")
except:
    pass
try:
    os.remove("audiofile_mp3.mp3")
except:
    pass
try:
    os.remove("audiofile_wav.wav")
except:
    pass




def search_for_file_path ():
    currdir = os.getcwd()
    file_path_variable_return = filedialog.askopenfilenames(parent=root, initialdir=currdir, filetypes=(("MP4 Files","*.mp4"),), title='Please select a directory')
    if len(file_path_variable_return) > 0:
        print ("You chose: %s" % file_path_variable_return)
    return file_path_variable_return

def get_url():
    video_urll.place(x=25, y=150)
    video_urll.insert(0, "Enter youtube URL")


    myButton3 = Button(root, text = "Enter",command=conversion2, width=20, anchor=CENTER)
    myButton3.place(x=450, y=150)
    video_url = video_urll.get()





def conversion1():
    global c
    x = datetime.datetime.now()
    date_time = str(x.strftime("%d")+"_"+x.strftime("%b")+"_"+x.strftime("%Y")+"_"+x.strftime("%H")+"_"+x.strftime("%M")+"_"+x.strftime("%S"))

    try:
        os.remove("output.mp4")
    except:
        pass
    try:
        os.remove("audiofile_mp3.mp3")
    except:
        pass
    try:
        os.remove("audiofile_wav.wav")
    except:
        pass
    try:
        myLabel60.config(text="")
        myLabel5.config(text="")
        myLabel3.config(text="")
    except:
        pass
    file_path_variable_return = search_for_file_path()
    file_path_variable = file_path_variable_return[0]
    # print ("\nfile_path_variable = ", file_path_variable)
    file_path_variablee = '"'+file_path_variable+'"'

    #Checking if OS is Windows
    if os.name == 'nt':
        path = os.getcwd() + '\\'
        print("[+] Operating System Windows Confirmed")
        myLabel9= Label(root, text = "[+] Operating System Windows Confirmed",padx=40, fg="green")
        myLabel9.place(y=c)
        c+=30
    else:
        path = os.getcwd() + '/'
    
    #using the ffmpeg to convert
    #print("ffmpeg -i "+ file_path_variablee+" output3.mp3")
    command2mp3 = "ffmpeg -i "+ file_path_variablee+" audiofile_mp3.mp3"
    command2wav = "ffmpeg -i audiofile_mp3.mp3 audiofile_wav.wav"

    #Using the OS to fulfill both Commands

    os.system(command2mp3)
    os.system(command2wav)

    myLabel3= Label(root, text = "[+] Sucessfully Created MP3 and WAV AudioFiles",padx=40, fg="green")
    myLabel3.place(y=c)
    c+=30
    print("[+] Sucessfully Created MP3 and WAV AudioFiles")
    
    r = sr.Recognizer()
    audio = 'audiofile_wav.wav'

    with sr.AudioFile(audio) as source:
        audio = r.record(source)


#Using the Try and Catch Block
    textt = []
    t=0
    try:
        text1 = r.recognize_google(audio, language = "mr-IN")
        textt.append(text1)
    except:
        t+=1
    try:
        text2 = r.recognize_google(audio, language = "fr-FR")
        textt.append(text2)
    except:
        t+=1
    try:
        text3 = r.recognize_google(audio, language = "hi-IN")
        textt.append(text3)
    except:
        t+=1
    try:
        text4 = r.recognize_google(audio, language = "es-ES")
        textt.append(text4)
    except:
        t+=1
    if(t==4):
        myLabel6= Label(root, text = "[+] Video is Too Long and has many Disturbances",padx=40,fg="red")
        myLabel6.place(y=c)
        c+=30
        print("[+] Video is Too Long and has many Disturbances")
        exit()
    text =  max(textt, key=len)
    text = translator.translate(text)
    text = text.text
    name = 'Video-to-Text_'+ date_time + ".txt"
    with open(name, mode ='w') as file: 
        file.write("Recognized Speech:") 
        file.write("\n") 
        file.write(text)
        myLabel4= Label(root, text = "[+] Text file created Successfully",padx=40, fg="green")
        myLabel4.place(y=c)
        c+=30
        myLabe25= Label(root, text = "-----------x----------x-------------",padx=40, fg="red")
        myLabe25.place(y=c)
        c+=30
        print("[+] Text file created Successfully")
    
def conversion2():
    global c
    try:   
        myLabel6.config(text="")
        myLabel4.config(text="")
        myLabel2.config(text="")
        myLabel8.config(text="")
    except:
        pass
    x = datetime.datetime.now()
    date_time = str(x.strftime("%d")+"_"+x.strftime("%b")+"_"+x.strftime("%Y")+"_"+x.strftime("%H")+"_"+x.strftime("%M")+"_"+x.strftime("%S"))

    try:
        os.remove("output.mp4")
    except:
        pass
    try:
        os.remove("audiofile_mp3.mp3")
    except:
        pass
    try:
        os.remove("audiofile_wav.wav")
    except:
        pass
    # The URl of Youtube Video
    video_url = video_urll.get()

    #Checking if OS is Windows
    if os.name == 'nt':
        path = os.getcwd() + '\\'
        print("[+] Operating System Windows Confirmed")
        myLabel8= Label(root, text = "[+] Operating System Windows Confirmed",padx=40, fg="green")
        myLabel8.place(y= c)
        c+=30
    else:
        path = os.getcwd() + '/'

   #Specifying the Output File name (MP4)
    name="output.mp4"
    YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name)
    location = path + name + '.mp4'
    renametomp3 = path + name + '.mp3'

    if os.name == 'nt':
        os.system('ren {0} {1}'. format(location, renametomp3))
    file_path_variablee = "output.mp4"
        
    
    #using the ffmpeg to convert
    #print("ffmpeg -i "+ file_path_variablee+" output3.mp3")
    command2mp3 = "ffmpeg -i "+ file_path_variablee+" audiofile_mp3.mp3"
    command2wav = "ffmpeg -i audiofile_mp3.mp3 audiofile_wav.wav"

    #Using the OS to fulfill both Commands

    os.system(command2mp3)
    os.system(command2wav)

    myLabel2= Label(root, text = "[+] Sucessfully Created MP3 and WAV AudioFiles",padx=40, fg="green")
    myLabel2.place(y=c)
    c+=30
    print("[+] Sucessfully Created MP3 and WAV AudioFiles")
    r = sr.Recognizer()
    audio = 'audiofile_wav.wav'

    with sr.AudioFile(audio) as source:
        audio = r.record(source)

#Using the Try and Catch Block
    textt = []
    t=0
    try:
        text1 = r.recognize_google(audio, language = "mr-IN")
        textt.append(text1)
    except:
        t+=1
    try:
        text2 = r.recognize_google(audio, language = "fr-FR")
        textt.append(text2)
    except:
        t+=1
    try:
        text3 = r.recognize_google(audio, language = "hi-IN")
        textt.append(text3)
    except:
        t+=1
    try:
        text4 = r.recognize_google(audio, language = "es-ES")
        textt.append(text4)
    except:
        t+=1
    if(t==4):
        myLabel6= Label(root, text = "[+] Video is Too Long and has many Disturbances",padx=40,fg="red")
        myLabel6.place(y=c)
        c+=30
        print("[+] Video is Too Long and has many Disturbances")
        exit()
    text =  max(textt, key=len)
    text = translator.translate(text)
    text = text.text
    name = 'Video-to-Text_'+ date_time + ".txt"
    with open(name, mode ='w') as file: 
        file.write("Recognized Speech:") 
        file.write("\n") 
        file.write(text)
        myLabel4= Label(root, text = "[+] Text file created Successfully",padx=40, fg="green")
        myLabel4.place(y=c)
        c+=30
        myLabe24= Label(root, text = "-----------x----------x-------------",padx=40, fg="red")
        myLabe24.place(y=c)
        c+=30
        print("[+] Text file created Successfully")

    #except Exception as e:
        #print(e)
   #     myLabel6= Label(root, text = "[+] Video is Too Long and has many Disturbances",padx=40,fg="red")
  #      myLabel6.place(y=300)
 #       print("[+] Video is Too Long and has many Disturbances")




root = tkinter.Tk()
#root.withdraw() #use to hide tkinter window
root.title("Speech to Text Converter in Python")
root.geometry("630x720")

myLabel = Label(root, text = "Helloworld")
#myLabel.pack()

myButton = Button(root, text = "Upload video from Computer", width=30, command = conversion1, anchor=CENTER)
myButton.place(x=75, y=50)
#myButton1 = Button(root, text = "Enter Youtube URL", width=30, command = get_url, anchor=CENTER)
#myButton1.place(x=345, y=50)
video_urll = Entry(root,width=55)

#myButton.grid(row=0, column=0)
#myButton1.grid(row=0, column=1)
clicked = StringVar()
clicked.set("Select Video Language")


root.mainloop()
# Using to Redirect to Main Method
