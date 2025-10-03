questions=[['Which country have highest population in world?','USA','INDIA','CHINA','RUSSIA',3],
['Which is the powerful country in the world?','ISRAEL','RUSSIA','CHINA','USA',4],
['who is the father of nation india?','JAWAHAR LAL NEHRU','MAHATMA GANDHI','DR.B.R. AMBEDKAR','SARDAR WALLABH BHAI PATEL',2],
['What does not grow on tree according to a popular Hindi saying?','Money','Flowers','Leaves','Fruits',1],
['Who wrote Indian National Anthem?','RabindranathTagore','Lal Bahadur Shastri','Chetan Bhagat','RKNarayan',1],
['Which city is known as the Pink City of India?','Banglore','Maysore','Jaipur','Kochi',3]]
levels=[1000,5000,10000,20000,30000,50000]
for i in range(0,len(questions)):
    question=questions[i][0]
    print(question)
    print('1.',questions[i][1]     ,  '2.',questions[i][2])
    print('3.',questions[i][3]     ,   '4.',questions[i][4])
    answer=int(input('Choose a correct option: '))

    if answer==questions[i][-1]:
        print(f"Congratulations! you won Rs{levels[i]}.")
    else:
        print("Sorry:(, you lose.")
