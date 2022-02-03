#Voice script start
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__== "__main__":
    speak("Welcome to the smart calculator")

#Calculator script start

def calc(na, nb, formula):
    if formula== '+':
        return na + nb
    elif formula== '-':
        return na - nb
    elif formula== '*':
        return na * nb
    elif formula== '/':
        return na / nb
    #special formula
    elif formula== 'x':
        return na * nb

print("Enter The First Number")
speak("Enter The First Number")
na = float(input())
print("Enter The Second Number")
speak("Enter The Second Number")
nb = float(input())
print("What Formula Do You Want, +, -, *, x, / ?")
speak("What Formula Do You Want?")
formula = input()
answer = calc(na, nb, formula)
print(answer)
speak(answer)
speak("Thank you")