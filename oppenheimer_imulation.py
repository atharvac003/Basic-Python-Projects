import os
print("Welcome to the Oppenheimer Simulation Game! Based on the bestselling movie adaptation by Christopher Nolan!")
print("NOTE: Make sure all your responses are in terms of Y or N ONLY for the game to work as intended! Thank you for your cooperation!")
user_response=input("\nIn this game you make choices as Oppenheimer based on your own judgement." + "\nAre you ready? Type Y (for Yes) or N (for No): ")


if user_response=="Y" or user_response=="y":
  start_game=input("\nLet's begin Dr. Oppenheimer.\n\nYou are approached by Lewis Strauss to appear before the government to talk about an arms shipment.\nDo you accept? ")
  
  if start_game=="Y" or start_game=="y":
      strauss_ans=input("You have a chance to call out his shipment program in front of the government. However,in doing so, you will humiliate him.\nDo you call it out? ")
      if strauss_ans=="Y" or strauss_ans=="y":
          strauss=1
      elif strauss_ans=="N" or strauss_ans=="n":
          strauss=0
      
      print("Lewis will remember your decision!")
      
      #os.system('clear')
      
      jean_ans=input('''\nYou are invited to a party by your brother Frank. You discover that the party has important members of the Communist Movement present.\nAmong them a woman catches your eye. She introduces herself as Jean Tatlock.\nSoon after you two start talking she asks you to join the Communist Party.\nDo you accept? ''')
      
      if jean_ans=="Y" or jean_ans=="y":
          jean=1
      elif jean_ans=="N" or jean_ans=="n":
          jean_updated_ans=input("She continues insisting in front of everyone present at the party.\nDo you accept? ")
          if jean_updated_ans=="Y" or jean_updated_ans=="y":
           jean=1
          elif jean_updated_ans=="N" or jean_updated_ans=="n":
           jean=0
           
      chevalier=input("\nAt the same party, Frank's girlfriend introduces you to a man named Chevalier who seems very eager to meet you.\nDo you befriend him? ")
      if chevalier=="Y" or chevalier=="y":
            chevalier=1
            print("After talking to him for a bit, he leaves in a rush informing you that he would definitely stay in touch.")
      elif chevalier=="N" or chevalier=="n":
            chevalier=0
      
      
      kitty_ans=input("\nA few weeks after, at another gathering, you happen to encounter a beautiful woman. She introduces herself as Kitty Puening.\nMonths after talking to her, Kitty asks you to marry her.\nDo you accept? ")
      if kitty_ans=="Y" or kitty_ans=="y":
            kitty=1
            print("The two of you get married in a beautiful ceremony.")
      elif kitty_ans=="N" or kitty_ans=="n":
            kitty=0
            print("Years after being with Jean, the two of you decide to get married.")
      
      #os.system('clear')
 
            
      leslie_ans=input("\n\nWhile you are working on your quantum mechanic theories at Pasadena, a man walks into your chamber one day.\nHe introduces himself as Colonel Leslie Grove. He asks you to work on the Manhattan Project.\nDo you accept? ")
      if leslie_ans=="Y" or leslie_ans=="y":
            print("\nCongratulations! On this note, Leslie has appointed you as the 'Director' of the Manhattan Project.\nIt is a secret project headed by the US government, in order to build a weapon to use against Germany in World War 2.")
            #insert a time delay here
            
            teller_ans=input("\nYou are assigned a group of the most brilliant scientists from across the country. Amongst these is the promising Edward Teller.\nTeller informs you that he has been researching on the possiblity of builiding an H-bomb.\nHe asks you for permission and resources to continue this research.\nDo you allow it? ")
            
            if teller_ans=="Y" or teller_ans=="y":
             teller=1
            
            elif teller_ans=="N" or teller_ans=="n":
             teller=0
            
            print("Teller will remember your decision!")
            
            #clear screen
            
            if kitty==1:
            
             print("\nA few months into the Manhattan Project, you receive news that Jean Tatlock has killed herself.\nHowever, you manage to pull yourself together with support from your wife Kitty.")
            
            #clear screen
             
             if chevalier==1:
                   sleep_ans=input("\n\nSomeone at Los Alamos as tipped you off that Chevalier, who you brought on to the project might be a spy.\nYou head over to Pasadena the next day and tell a senior professor there about your findings.\nHe offers you bed and board at the university until the matter gets sorted out, however you feel uneasy.\nDo you decide to sleep? ")
                
                   if sleep_ans=="Y" or sleep_ans=="y":
                       
                     sleep=1
                     print("\nYou wake up the next morning feeling refreshed.")
                   
                   elif sleep_ans=="N" or sleep_ans=="n":
                       
                     sleep=0
                     print("\nYou stay awake the whole night and feel incredibly groggy as the sun rises")
                   
                   pash_ans=input("\nThere is a knock on your university room. You are informed that you have a visitor.\nWhen you go to find out who it is, the individual reveals himself to be Colonel Pash.\nHe asks you to take a seat and begins questioning you.\nHe asks you if you are a part of the Communist Party.\nWhat do you tell him? ")
                   
                   if pash_ans=="y" or pash_ans=="Y":
                       pash=1
                   else:
                       pash=0
                       
                   if pash==jean:
                       truth=1
                   else:
                       truth=0
                   
                   print("\nHe further asks you about your findings regarding Chevalier")
                   
                   if sleep==1:
                       print("Having rested well the night before, you give a clear account of your relation with Chevalier.")
                       
                   elif sleep==0:
                       print("Due to your lack of sleep, you groggily blurt out an unclear account of your relation with Chevalier.")
                      
                   print("After receiving somewhat satsifactory answers, Colonel Pash leaves the room.")
                   
                   #clear space here
                   
                   if truth==0:
                       print("\nColonel Pash finds out that you have lied about your involvement in the Communist Party.\nYou are turned into the US government effective immediately!")
                       
                   elif truth==1:
                       print("\nDespite Colonel Pash finding your account of the Chevalier incident unsatisfactory enough to rule you out as a security threat, Leslie steps in to defend you.\nHe is able to back you up due to the clear account you provided to Colonel Pash. Unbeknownst to most, he transfers Colonel Pash to another country.")
                       
                       if teller==1:
                           teller_final1 = input("Meanwhile at Los Almanos, Teller approaches you, informing you that thanks to your resources he has finished his research.\nHe is now asking for final approval to begin the actual groundwork on the H-bomb, as soon as testing on the atomic bomb ends.\nDo you allow it? ")
                           
                       elif teller==0:
                           teller_final2 = input("Meanwhile at Los Almanos, Teller approaches you. You notice that he seems resentful, after having rejected his plea for the research.\nDespite this, he is now asking for final approval to begin the actual groundwork on the H-bomb, as soon as testing on the atomic bomb ends.\nDo you allow it? ")
                          
                       choice1=teller_final1
                       choice2=teller_final2
                       
                       if choice1=="Y" or choice1=="y" or choice22=="Y" or choice2=="y":
                               print("nice work")
                       else:
                               print("really nice work")
                               
                       
                           
                   
    
             else:
                   print("The rest of the Edward teller story continues in progression:")
            
            elif kitty==0:
                
             print("\nA few months into the Manhattan Project, you receive news that Jean Tatlock has killed herself.\nWith no one else by your side to comfort you, in immense grief and desperation you end your life.") 
      
            
      elif leslie_ans=="N" or leslie_ans=="n":
            print("Unique ending")
            
     
       

      
          
     


  elif start_game=="N" or start_game=="n": print("You have to engage in a conversation with Strauss!")

  
  
  
  
  
  
  
elif user_response=="N" or user_response=='n':
    print("\nThe makers of the game have found enough evidence to imprison you for the attempted murder of Blackett using a poisoned apple!")
    
else:
    print("\nPlease make a valid choice!\nRun the game and try again!")
