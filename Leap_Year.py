#Leap Year Concept

#https://www.youtube.com/watch?v=YCnZ474mFbU

a=2080
# leap year/4=0  AND leap year/100 not equal to 0     If satiesfies both the condition then we get leap year eg(2080)
# leap year/4=0  AND leap year/100 =0 AND leap Year/400=0   If satiesfies the all 3 condition then we also get leap year(eg 2000)
b=a%4
c=a%100
d=a%400
if(b!=0):
 print("Its not a leap year")
while(b==0):
     if(b==0 and c!=0):
       print("Its a leap year")
       break;
     elif((c==0) and (d==0)):
      print("Its a leap year")
      break;
     else:
      print("Its not a leap year")
      break;