import pyautogui as pg
import time
import webbrowser

points=0

answer = pg.prompt(
"""
Where would you rather be?

a)laser tag
b)museum
c)shooting range
d)watching a football game 

"""

)

if answer == "a":
    points +=1
elif answer == "b":
    points+=2
elif answer== "c":
    points+=3
elif answer== "d":
    points+=4
answer = pg.prompt(
"""
Where would you like to live?

a)alone in a big apartment
b)with your best friends in an apartment in the city 
c)in canada
d)house in suburbs 

"""

)

if answer == "a":
    points +=1
elif answer == "b":
    points+=2
elif answer== "c":
    points+=3
elif answer== "d":
    points+=4

answer = pg.prompt(
"""
What is your dream profession?

a)working for a high pay corporal job
b)an architect
c)a television reporter
d)an enviromental lawyer

"""

)

if answer == "a":
    points +=1
elif answer == "b":
    points+=2
elif answer== "c":
    points+=3
elif answer== "d":
    points+=4
    
answer = pg.prompt(
"""
Whats your favorite song?

a)you give love a bad name 
b)star wars theme song 
c)lets go to the mall
d)500 miles

"""

)

if answer == "a":
    points +=1
elif answer == "b":
    points+=2
elif answer== "c":
    points+=3
elif answer== "d":
    points+=4


#END OF SURVEY
pg.alert("you are...")

#Barney Stinson
if points are>= 5:
    pg.alert("barney Stinson")
    webbrowswer.open("https://vignette.wikia.nocookie.net/himym/images/8/83/Rc0JG.jpg/revision/latest?cb=20130113174854")
#Ted Mosby
if points are>= 6 and points <9:
    pg.alert("ted mosby")
    webbrowser.open("https://vignette.wikia.nocookie.net/himym/images/1/14/WB0rq.jpg/revision/latest?cb=20130113174836")
#Robin Sherbatsky
if points are>= 9 and points <14:
    pg.alert ("Robin Sherbatsky")
    webbrowser.open("https://vignette.wikia.nocookie.net/himym/images/9/97/O5wDi.jpg/revision/latest?cb=20150304053526")
#Marshal Erikson
if points are>=14 and points <16:
    pg.alert ("marshal erikson")
    webbrowser.open("https://vignette.wikia.nocookie.net/himym/images/5/50/PlcCt.jpg/revision/latest?cb=20130113174817")
