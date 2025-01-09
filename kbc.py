import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("21-Kbc Background-MobCup.vip.mp3")

questions = {  "1.Who is known as the Father of the Nation in India?": "a) Mahatma Gandhi, b) Jawaharlal Nehru, c) Subhas Chandra Bose, d) Sardar Vallabhbhai Patel,",
    "2.What is the national flower of India?": "a) Lotus, b) Rose, c) Jasmine, d) Sunflower,",
    "3.Which city is the capital of India?": "a) New Delhi, b) Mumbai, c) Kolkata, d) Chennai,",
    "4.Which river is considered the holiest in India?": "a) Ganga, b) Yamuna, c) Godavari, d) Brahmaputra,",
    "5.Which monument is known as the symbol of India's freedom struggle?": "a) India Gate, b) Red Fort, c) Gateway of India, d) Charminar,",
    "6.Which is the national animal of India?": "a) Tiger, b) Lion, c) Elephant, d) Rhinoceros,",
    "7.Who was the first Indian to win a Nobel Prize?": "a) Rabindranath Tagore, b) C. V. Raman, c) Har Gobind Khorana, d) Mother Teresa,",
    "8.Which city is known as the 'Silicon Valley of India'?": "a) Bengaluru, b) Hyderabad, c) Chennai, d) Pune,",
    "9.Which is the largest state in India by area?": "a) Rajasthan, b) Uttar Pradesh, c) Madhya Pradesh, d) Maharashtra,",
    "10.Which of the following is the national bird of India?": "a) Peacock, b) Sparrow, c) Eagle, d) Dove,"
}
answer = {
    1: "a", 
    2: "a", 
    3: "a", 
    4: "a", 
    5: "b", 
    6: "a", 
    7: "a", 
    8: "a", 
    9: "a", 
    10: "a"
}
print("\n🙏🙏🙏WELCOME TO KAUN BANEGA CROREPATI🙏🙏🙏\n")
question_number =1
total_money = 0
money = 1000
for question in questions.keys():
    total_money = money-1000
    print(f"Question {question_number} ,  Amount :{money}:\n")
    print(question)
    options_list = questions[question].split(",")
    for option in options_list:
        print(option)
    selected_option = input("enter the option among a / b / c / d : ")
    if selected_option == answer[question_number]:
        print(f"👏👏👏WONDERFUL ! YOU ARE ABSOLUTELY CORRECT , YOU WON {money} RUPEES👏👏👏\n")
        pygame.mixer.music.play()
        time.sleep(2)
        pygame.mixer.music.stop()
        conti = input("TYPE 1 TO MOVE TO NEXT QUESTION OR TYPE 0 TO QUIT\n")
        if conti == 0:
             print(f"🙏🙏🙏YOU ARE QUITTING THE GAME , FINALLY YOU WON {total_money}🙏🙏🙏\n")
    else:
        print(f"😞😞😞SORRY , YOU ARE WRONG,😞😞😞\n")
        print(f"🙏🙏🙏  YOU WON RUPEES {total_money} , THANK YOU FOR PARTICIPATING IN KBC🙏🙏🙏\n")
        break
    money = money + 1000
    question_number = question_number +1 