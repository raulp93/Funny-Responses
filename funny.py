import time
import random


def choose(result):
    file_name = f"text-files\\{result}.txt"
    number = random.randint(1, 6)
    responses = open(file_name, "r").readlines()
    response = responses[number].strip()
    print(response)


def sendit(message):
    with open("request.txt", "w") as outfile:
        outfile.write(message)



while True:
    time.sleep(0.15)
    with open("request.txt", "r") as infile:
        check = infile.read()
    
    if check == "send a message":
        open("request.txt", "w").close()
            
        with open("result.txt", "r") as infile:
            check = infile.read()
    
        if check == 'lost':
            message = choose('lost')
        
        elif check == 'won':
            message = choose('won')

        elif check == "'draw":
            message = choose('draw')

        sendit(message)

        












