import pyttsx3

def hello():
    engine = pyttsx3.init()
    print("Hello😊, I Am Spark, How Can I Help You!")
    engine.say("Hello, I Am Spark, How Can I Help You")
    engine.runAndWait()