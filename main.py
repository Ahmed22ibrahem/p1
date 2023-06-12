import pyttsx3                                          #للتعرف علي خصائص الجهاز
import speech_recognition as sr                         #علشان يسمع الصوت "يتصنت"
import webbrowser                                       #لكي نقدر نتعامل مع المتصفح
import time                                             #للتعامل مع الوقت
import datetime                                         #للتعامل مع الوقت والتاريخ من win
import os                                               #للتعامل من اللـ win
from pydub import AudioSegment                          #للتعامل مع الاصوات من خلال استدعائها
from pydub.playback import play                         #لتشغيل الاصوات في الخلفية
import pyautogui                                        #نستخدمها للنشر في الفيس بوك أو رفع علي يوتيوب


wel =pyttsx3.init()                                         #باصيت المكتبة للمتغير
voices =wel.getProperty('voices')
wel.setProperty('voice',voices[0].id)


def Speak(audio):
    wel.say(audio)
    wel.runAndWait()


def TakeCommands():
    commnd=sr.Recognizer()
    with sr.Microphone() as mic :
        print('say commands sir....')
        commnd.phrase_threshold =0.4
        audio =commnd.listen(mic)
        try:
            print('Recording.....')
            query=commnd.recognize_google(audio,language='ar')
            print(f'you say :{query}')
        except Exception:
            return None
        return query.lower()


music =AudioSegment.from_mp3('sounds/welcome.mp3')
play(music)

time.sleep(1)

music1 =AudioSegment.from_mp3('sounds/wecome2.mp3')
play(music1)


while True:

    query =TakeCommands()
    if'صباح الخير' in query:
        b=AudioSegment.from_mp3('sounds/goodmorning.mp3')
        play(b)

    if 'مساء الخير' in query:
        b=AudioSegment.from_mp3('sounds/goodevining.mp3')

        play(b)

    if 'افتح جوجل' in query:
        b = AudioSegment.from_mp3('sounds/google.mp3')
        play(b)
        time.sleep(2)
        webbrowser.open_new_tab('https:/www.google.com')

    if 'مواعيد اليوم' in query:
        b = AudioSegment.from_mp3('sounds/mao3d.mp3')
        play(b)

    if 'اغلق اللاب' in query:
        b = AudioSegment.from_mp3('sounds/closePC.mp3')
        play(b)
        os.system("shutdown /s /t 1")

    if 'نكتب كود' in query:
        b = AudioSegment.from_mp3('sounds/program.mp3')
        play(b)
        cpath ="C:/Users/hahme/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        os.startfile(cpath)

    if 'النشر على فيسبوك' in query:
        b = AudioSegment.from_mp3('sounds/post.mp3')
        play(b)
        post = input('Enter your post  :')
        webbrowser.register('Microsoft Edge',None,
                            webbrowser.BackgroundBrowser("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"))
        pyautogui.hotkey('ctrl ','t')
        link = 'https://www.facebook.com/profile.php?id=100007591931059'

        webbrowser.get('Microsoft Edge').open_new(link)
        time.sleep(10)
        pyautogui.hotkey('ctrl','f')
        time.sleep(3)
        pyautogui.press('ُdelete')
        pyautogui.typewrite("what is in your mind?")
        pyautogui.press('ُEnter')
        time.sleep(3)
        pyautogui.press('Escape')
        pyautogui.press('Enter')
        time.sleep(10)
        pyautogui.typewrite(post)
        time.sleep(3)
        pyautogui.click(670,600)

    command = input()

    if command.lower() == "esc":
        break







