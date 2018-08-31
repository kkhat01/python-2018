import random
import time

responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

name = input ("what is your name:")

while True:
    question = input("what is your question "+name+ "?"" or to quit, type x: ")
    if question.strip() == "x":
        break
    print("Let me see")
    time.sleep(2)
    print("Hmmm")
    time.sleep(2)
    print(random.choice(responses))
    


