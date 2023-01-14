import socket
import random
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 5000

server.bind((ip, port))

server.listen()
clients = []
names = []

print("SERVER CONNECTED!!")

questions = [
    "Who was the original drummer for the beatles? \n a. Ringo Star \n b. Pete Best \n c. John Lennon \n d. George Harrison",
    "Who from the following was in one direction? \n a. Luke Hemmings \n b. Ed sheeran \n c. Louis Tomlinson \n d. Bradley Simpson",
    "How many memebers are there in BTS? \n a. 9 \n b. 4 \n c. 5 \n d. 7",
    "What is the best selling single of all time? \n a. White Christmas by Bing Crosby \n b. Shape of you by Ed Sheeran \n c. Something Just like this by The chainsmokers & Coldplay \n d. Perfect by Ed Sheeran ",
    "Who is the best selling female artist of all time? \n a. Adele \n b. Madonna \n c. Taylor Swift \n d. Katy Perry",
    "Who is the oldest female artist to reach no. 1 with the longest gap between hits? \n a. Kate bush \n b. Miley Cyrus \n c. Katy Perry \n d. Madonna",
    "Which song stayed 1 on Billboard for 15 weeks? \n a. Old Town Road by Lil Nas X \n b. All I want for christmas is you by Mariah Carey \n c. As it was by Harry Styles \n d. Macarena by Los Del Rio",
    "Who is the youngest person to win 'triple crown' film music award? \n a. Louis Tomlinson \n b. Billie Eillish \n c. Conan Gray \n d. Olivia Rodrigo",
    "Who is the first group to debut at no. 1 with their first 4 albums in the US? \n a. BTS \n b. The Beatles \n c. One Direction \n d. Backstreet Boys",
    "Which singer has most Guiness World Records? \n a. Asha Bhosle \n b. Taylor Swift \n c. Madonna \n d. Lata Mangeshkar",
    "Who is top listened artist? \n a. Just Bieber \n b. Drake \n c. BTS \n d. Taylor Swift"
]

answers = ['b', 'c', 'd', 'a', 'b', 'a', 'c', 'b', 'c', 'a', 'd']

def clientThread(con, names):
    score = 0
    con.send("Welcome to this quiz!".encode('utf-8'))
    con.send("You will recieve a question along with some options, choose the correct one.".encode('utf-8'))
    con.send("All the best!!\n\n".encode('utf-8'))

    index, question, answer = get_random_question_ans(con)
    while True:
        try:
            message = con.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score += 1
                    con.send("Bravo!\nYour score is {score}\n\n".encode('utf-8'))
                else:
                    con.send("Incorrect answer!\nBetter luck next time\n\n".encode('utf-8'))

                removeQuestion(index)
                index, question, answer = get_random_question_ans(con)
            else:
                remove(con)
        except:
            continue

def get_random_question_ans(con):
    random_index = random.randint(0, len(questions)-1)
    random_question = questions[random_index]
    random_ans = answers[random_index]
    con.send(random_question.encode('utf-8'))
    return random_index, random_question, random_ans
    

def removeQuestion(index):
    questions.pop(index)
    answers.pop(index)

def remove(con):
    if con in clients:
        clients.remove(con)

while True:
    con, addr = server.accept()
    con.send('nickname'.encode("utf-8"))
    nickname = con.recv(2048).decode("utf-8")
    clients.append(con)
    names.append(nickname)
    print(nickname+" connected")
    newThread = Thread(target=clientThread, args=(con, nickname))
    newThread.start()
