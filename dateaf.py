import datefinder
import winsound
import datetime


def alarm(text):
    DTimeA=datefinder.find_dates(text)
    for mat in DTimeA:
        print(mat)
    stringA=str(mat)
    timeA=stringA[11:]
    print(timeA)
    hourA=timeA[:-6]
    hourA=int(hourA)
    minuteA=int(timeA[3:-3])
    # minuteA=int(timeA)
    
    while True:
        print("Your alarm is set now")
        if hourA==datetime.datetime.now().hour:
            if(minuteA==datetime.datetime.now().minute):
                print("Alarm is running")
                winsound.PlaySound("./Alarm-Fast-High-Pitch-B1-www.fesliyanstudios.com.mp3",winsound.SND_LOOP)
            elif minuteA>datetime.datetime.now().minute:
                break
            
                
        
   
    
    
    
# alarm("set alarm at 9:59:00 am")