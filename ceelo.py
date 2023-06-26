
#Cee-Lo
#Phase 1
from random import randint
try:
     numpl=int(input('Number of players (between 2 and 6): '))
except ValueError:
              print("Something wrong happened: invalid literal for int() with base 10: ''")  
              print("'I'm setting the number of players to 3")
              numpl=3
while not 2<=numpl<=6:
     print('I expected between 2 and 6 players')
     print("'I'm setting the number of players to 3")
     numpl=3
     break
try:
        numc=int(input('Number of coins per player (between 5 and 100): '))
except ValueError:
               print("Something wrong happened: invalid literal for int() with base 10: ''")
               print("I'm setting the number of coins to 10")
               numc=10
while not 5<=numc<=100:
    print('I expected between 5 and 100 coins')
    print("I'm setting the number of coins to 10")
    numc=10
    break
banker=randint(1,numpl)
print('Game starts with' ,numpl, 'players')
print('Each player has',numc,'coins')
print('Player',banker,' is randomly picked as banker')
print()
while numc>0:
 print('Current balance is : ')
 for x in range(1,numpl+1):
        print('Player',x, 'has ',numc,'coins')
 lst=[]
 lst1=[]
 lst2=[]

 b_score=0  
 p_score=0
 print()
 b_a=int(input('Player '+str(banker)+': You are the banker!Please enter a valid bank amount: '))
 lst2.append(b_a)
 if b_a>numc or b_a<=1:
          b_a=int(input('Player '+str(banker)+': You are the banker!Please enter a valid bank amount: '))
 for i in range(1,numpl+1):   
         if i!=banker:
              b_p=int(input('Player '+str(i)+' please enter a valid bet:'))         
              if b_p>numc:
                        b_p=int(input('Player '+str(i)+' please enter a valid bet:'))                    
              elif b_p>b_a:
                        b_p=int(input('Player '+str(i)+' please enter a valid bet:'))                    
              lst.append(b_p) 
              lst1.append(i)
              s=sum(lst)      
              if s==b_a:     
                 break

#Phase 2
 print()
 print("Round starts")
 for k in range(len(lst1)):
              if k==banker: 
                   print('Player '+str(banker)+' :Banker with bank amount='+str(b_a))

         
              if s!=b_a:
                   print('Player ',str(lst1[k]),' has bet',str(lst[k]),' :')
              elif s==b_a:               
                   for e in range(i+1,banker-1):
                      
                        print('Player ',str(e),' has bet 0 :')
                   for k in range(banker+1,numpl+1):
                        print('Player ',str(k),' has bet 0 :')               
                   print('Player '+str(banker)+' :Banker with bank amount='+str(b_a))
                   break
 print()
 l=input('Banker press ENTER to roll dice')
 r=[randint(1,6) for t in range(3)]
 print('Banker rolled',r)

 if (4 in r) and (5 in r) and (6 in r):
               print('Automatic Win! Banker wins all bets! Round ends!')                  
               lst2.append(s)
               s2=sum(lst2)
               b_score=6
 elif r[0]==r[1]==r[2]:        
               print('Automatic Win! Banker wins all bets! Round ends!')                  
               lst2.append(s)
               s2=sum(lst2)
               b_score=6    
 elif (6 in r) and (r[0]==r[1]
               or r[1]==r[2]
               or r[2]==r[0]):        
               print('Automatic Win! Banker wins all bets! Round ends!')                  
               lst2.append(s)
               s2=sum(lst2)
               b_score=6        
 elif (1 in r) and (2 in r) and (3 in r):        
               print('Automatic Lose! Banker lose all  the bets and the bank! Round ends!')                  
               b_score=1
 elif (1 in r) and (r[0]==r[1]
               or r[1]==r[2]
               or r[2]==r[0]):       
               print('Automatic Lose! Banker lose all  the bets and the bank! Round ends!')                  
               b_score=1        
 elif r[0]==r[1]:
          b_score=r[2]
 elif r[1]==r[2]:
          b_score=r[0]
 elif r[0]==r[2]:
               b_score=r[1]
 if b_score!=1 and b_score!=6 and b_score!=0:
               print('Banker scored ',str(b_score),'points')
 while b_score==0:
               print('Banker rolls again')
               r=[randint(1,6) for t in range(3)]
               print('Banker rolled',r)
               b_score=0
               if (4 in r) and (5 in r) and (6 in r):
                    print('Automatic Win! Banker wins all bets! Round ends!')                    
                    lst2.append(s)
                    s2=sum(lst2)
                    b_score=6
               elif r[0]==r[1]==r[2]:        
                    print('Automatic Win! Banker wins all bets! Round ends!')
                    lst2.append(s)
                    s2=sum(lst2) 
                    b_score=6   
               elif (6 in r) and (r[0]==r[1]
                              or r[1]==r[2]
                              or r[2]==r[0]):        
                         print('Automatic Win! Banker wins all bets! Round ends!')                          
                         lst2.append(s)
                         s2=sum(lst2)
                         b_score=6        
               elif (1 in r) and (2 in r) and (3 in r):        
                    print('Automatic Lose! Banker lose all  the bets and the bank! Round ends!')                     
                    b_score=1
               elif (1 in r) and (r[0]==r[1]
                              or r[1]==r[2]
                              or r[2]==r[0]):       
                         print('Automatic Lose! Banker lose all  the bets and the bank! Round ends!')                          
                         b_score=1        
               elif r[0]==r[1]:
                         b_score=r[2]
               elif r[1]==r[2]:
                         b_score=r[0]
               elif r[0]==r[2]:
                         b_score=r[1]
               if b_score!=1 and b_score!=6 and b_score!=0:
                    print('Banker scored ',str(b_score),'points')
 for j in range(1,numpl+1):
     if j!=banker and b_score!=6 and b_score!=1:
          print()
          m=input('Player '+str(j)+' press ENTER to roll dice')
          rp=[randint(1,6) for t in range(3)]
          print('Player '+str(j)+' rolled :',rp)
          if (4 in rp) and (5 in rp) and (6 in rp):
                                   print('Player '+str(j)+' beats the banker')
                                   p_score=6                                       
          elif rp[0]==rp[1]==rp[2]:
                                   print('Player '+str(j)+' beats the banker')
                                   p_score=6                                       
          elif (1 in rp) and (2 in rp) and (3 in rp):        
                    print('Automatic Lose!Player '+str(j)+'  lose ')
                    p_score=1
          elif (1 in rp) and (rp[0]==rp[1]
                          or rp[1]==rp[2]
                          or rp[2]==rp[0]):       
                         print('Automatic Lose!Player '+str(j)+'  lose ')
                         p_score=1
          elif rp[0]==rp[1]:
                         p_score=rp[2]
          elif rp[1]==rp[2]:
                         p_score=rp[0]
          elif rp[0]==rp[2]:
                         p_score=rp[1]
          elif rp[0]!=rp[1]!=rp!=[2]:
                              p_score=0
          if p_score!=1 and p_score!=6 and p_score!=0:
                                   print('Player '+str(j)+ ' scored '+str(p_score)+' points')
                                   if b_score>p_score:
                                             print('Banker wins')                                             
                                   elif b_score<p_score:
                                             print('Player '+str(j)+ ' beats the banker')                                             
                                   else:
                                          print("It's a tie between the banker and the player!")
          while p_score==0:
                         print('Player '+str(j)+' rolls again')
                         rp=[randint(1,6) for t in range(3)]
                         print('Player '+str(j)+' rolled :',rp)                   
                         if (4 in rp) and (5 in rp) and (6 in rp):
                                       print('Player '+str(j)+' beats the banker')
                                       p_score=6                                       
                         elif rp[0]==rp[1]==rp[2]:
                                       print('Player '+str(j)+' beats the banker')
                                       p_score=6                                       
                         elif (1 in rp) and (2 in rp) and (3 in rp):        
                               print('Automatic Lose!Player '+str(j)+'  lose ')
                               p_score=1
                         elif (1 in rp) and (rp[0]==rp[1]
                                        or rp[1]==rp[2]
                                        or rp[2]==rp[0]):       
                                    print('Automatic Lose!Player '+str(j)+'  lose ')
                                    p_score=1
                         elif rp[0]==rp[1]:
                                         p_score=rp[2]
                         elif rp[1]==rp[2]:
                                        p_score=rp[0]
                         elif rp[0]==rp[2]:
                                        p_score=rp[1]
                         elif rp[0]!=rp[1]!=rp!=[2]:
                                        p_score=0
                         if p_score!=1 and p_score!=6 and p_score!=0:
                                             print('Player '+str(j)+ ' scored '+str(p_score)+' points')
                                             if b_score>p_score:
                                                  print('Banker wins')                                                  
                                             elif b_score<p_score:
                                                  print('Player' +str(j)+ ' beats the banker')                                                  
                                             else:
                                               print("It's a tie between the banker and the player!")

