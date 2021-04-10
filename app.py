from datetime import datetime
import time

print("Test Your Typing Speed!")

def start():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sentence = "The quick brown fox jumps over the lazy dog"
    solution = [sentence.lower().count(item) for item in letters]
    words = sentence.split(" ")
    for i in range(3):
        print("Ready In ",3-i)
        time.sleep(1)
    start_time = datetime.now()
    print("Type the following sentence and press Enter")
    print(sentence)
    user_sentence = input()
    user_input = user_sentence.split()
    end_time = datetime.now()
    time_taken = end_time-start_time
    microseconds = time_taken.microseconds
    seconds = time_taken.seconds
    minutes = int(str(time_taken)[-12:-10])
    total_time = (minutes) + (seconds/60) + (microseconds/60000000)
    speed = len(words)/total_time
    err_count = 0
    total_count = 0
    sentence = sentence.replace(" ","")
    user_sentence = user_sentence.replace(" ","")
    user_solution = [user_sentence.lower().count(item) for item in letters]
    for i in range(len(solution)):
        if (solution[i] < user_solution[i]):
            err_count+=1
        total_count += solution[i]
    accuracy = ((total_count-err_count)/total_count)*100
    print("Accuracy : {}\nTotal Count : {}\nErrors Made : {}".format(accuracy,total_count,err_count))
    print("Words per minute : ",speed)

start()
    
    
