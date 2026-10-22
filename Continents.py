#Allows the user to delete(kill) or re-add(renew) any of the six continents.

#questions:
#Why is southAmerica listed first? Because it was the smallest change, so I did it first in my tests. Duh.
    #the order on the rest is just whatever order I thought of them when I wrote the makeContinent function.
#Why only six? Because this is the only ASCII art of a map I could find.
    #I wanted to do one of the USA with all 50 states. I took what I could get.

underline = "\033[4m" #makes text Underlined
red = "\033[31m" #makes Asia Red
green = "\033[32m" #makes Europe Green
yellow = "\033[33m" #makes Africa yellow
blue = "\033[34m" #makes North America Blue
purple = "\033[35m" #makes South America Purple
cyan = "\033[36m" #makes Oceania Cyan
norm = "\033[0m" #short for normal - resets color


print(f"{underline}BEHOLD - THE WORLD:{norm}")
print(f"        {blue}_,--',{norm}   {green}_._{norm}{red}.--._____{norm}")
print(f" {blue}.--.--';_'-.',{norm} {green}'';{norm}{red}_      {red}_.,-'{norm}")
print(f"{blue}.'--'.  _.'{norm}    {yellow}(`'-;{norm}{red}_ .-.>.'{norm}")
print(f"      {blue}'-{norm}{purple}:_{norm}      {yellow})  /{norm} {red}`' '=.{norm}")
print(f"        {purple}) >{norm}     {yellow}(_/,{norm}     {cyan}/~){norm}")
print(f"        {purple}|/{norm}               {cyan}`^ .'{norm}")

'''
print("        _,--',   _._.--._____   ")
print(" .--.--';_'-.', '';_      _.,-' ")
print(".'--'.  _.'    (`'-;_ .-.>.'    ")
print("      '-:_      )  / `' '=.     ")
print("        ) >     (_/,     /~)    ")
print("        |/               `^ .'  ") '''
print("")

def makeContinents(sA,nA,erope,asi,ocean,afr): #I can reuse the variables for symbols that are in the same continent. small wins.
    if(sA==False): #kills the continent
        sA3=" "
        sA4=" "
        sA5=" "
        sA6=" "
        sA7=" "
        sA8=" "
    else: #gives it the correct characters (the hard part)
        #I had to remove 1 and 2 because I realized they're actually part of NA. whoops
        #But I don't care enough to change the names.
        sA3=f"{purple}:{norm}"
        sA4=f"{purple}_{norm}"
        sA5=f"{purple}){norm}"
        sA6=f"{purple}>{norm}"
        sA7=f"{purple}|{norm}"
        sA8=f"{purple}/{norm}"
    if(nA==False):
        nA1=" "
        nA2=" "
        nA3=" "
        nA4=" "
        nA5=" "
        nA6=" "
    else:
        nA1=f"{blue},{norm}"
        nA2=f"{blue}-{norm}"
        nA3=f"{blue}_{norm}"
        nA4=f"{blue}.{norm}"
        nA5=f"{blue}'{norm}"
        nA6=f"{blue};{norm}"
    if(erope==False):
        ero1=" "
        ero2=" "
        ero3=" "
        ero4=" "
    else:
        ero1=f"{green}'{norm}"
        ero2=f"{green};{norm}"
        ero3=f"{green}_{norm}"
        ero4=f"{green}.{norm}"
    if(asi==False):
        asi1=" "
        asi2=" "
        asi3=" "
        asi4=" "
        asi5=" "
        asi6=" "
        asi7=" "
        asi8=" "
    else:
        asi1=f"{red}.{norm}"
        asi2=f"{red}'{norm}"
        asi3=f"{red}_{norm}"
        asi4=f"{red}`{norm}"
        asi5=f"{red}-{norm}"
        asi6=f"{red}={norm}"
        asi7=f"{red}>{norm}"
        asi8=f"{red},{norm}"
    if(ocean==False):
        oce1=" "
        oce2=" "
        oce3=" "
        oce4=" "
        oce5=" "
        oce6=" "
        oce7=" "
    else:
        oce1=f"{cyan}~{norm}"
        oce2=f"{cyan}){norm}"
        oce3=f"{cyan}`{norm}"
        oce4=f"{cyan}^{norm}"
        oce5=f"{cyan}.{norm}"
        oce6=f"{cyan}'{norm}"
        oce7=f"{cyan}/{norm}"
    if(afr==False):
        af1=" "
        af2=" "
        af3=" "
        af4=" "
        af5=" "
        af6=" "
        af7=" "
        af8=" "
        af9=" "
    else:
        af1=f"{yellow}({norm}"
        af2=f"{yellow}/{norm}"
        af3=f"{yellow}){norm}"
        af4=f"{yellow}_{norm}"
        af5=f"{yellow},{norm}"
        af6=f"{yellow};{norm}"
        af7=f"{yellow}-{norm}"
        af8=f"{yellow}'{norm}"
        af9=f"{yellow}`{norm}"

    print(f"{underline}BEHOLD - THE WORLD:{norm}")
    print(f"        {nA3}{nA1}{nA2}{nA2}{nA5}{nA1}   {ero3}{ero4}{ero3}{asi1}{asi5}{asi5}{asi1}{asi3}{asi3}{asi3}{asi3}{asi3}")
    print(f" {nA4}{nA2}{nA2}{nA4}{nA2}{nA2}{nA5}{nA6}{nA3}{nA5}{nA2}{nA4}{nA5}{nA1} {ero1}{ero1}{ero2}{asi3}      {asi3}{asi1}{asi8}{asi5}{asi2}")
    print(f"{nA4}{nA5}{nA2}{nA2}{nA5}{nA4}  {nA3}{nA4}{nA5}    {af1}{af9}{af8}{af7}{af6}{asi3} {asi1}{asi5}{asi1}{asi7}{asi1}{asi2}")
    print(f"      {nA5}{nA2}{sA3}{sA4}      {af3}  {af2} {asi4}{asi2} {asi2}{asi6}{asi1}")
    print(f"        {sA5} {sA6}     {af1}{af4}{af2}{af5}     {oce7}{oce1}{oce2}")
    print(f"        {sA7}{sA8}               {oce3}{oce4} {oce5}{oce6}")
    print("")


def death(south,north,eu,theBigOne,other,africA): #the continents are always in the same order. Refer to other functions.
    #the names here are more comedic because they can be. (also I did not realize how many names for the same thing I'd need)
    if(south==False):
        south="" #if the continent is already dead, it should not be in the question.
    else:
        south="South America(1) "
    if(north==False):
        north=""
    else:
        north="North America(2) "
    if(eu==False):
        eu=""
    else:
        eu="Europe(3) "
    if(theBigOne==False):
        theBigOne=""
    else:
        theBigOne="Asia(4) "
    if(other==False):
        other=""
    else:
        other="Oceania(5) "
    if(africA==False):
        africA=""
    else:
        africA="Africa(6) "
    if(north=="" and south=="" and eu=="" and africA=="" and other=="" and theBigOne==""):
        choice=(input("You have already killed all the continents! Press ENTER to continue: "))
        choice=0
    else:
        choice=int(input(f"Which continent should die: {south}{north}{eu}{theBigOne}{other}{africA}"))
    print("")
    return choice #choice then becomes user


def renew(downTown,upTown,eeeTown,ayyTown,water7,africaTown): #the continents are always in the same order. Refer to other functions.
    if(downTown==True): #if the continent is NOT dead, it should not be in the question.
        downTown=""
    else:
        downTown="South America(1) "
    if(upTown==True):
        upTown=""
    else:
        upTown="North America(2) "
    if(eeeTown==True):
        eeeTown=""
    else:
        eeeTown="Europe(3) "
    if(ayyTown==True):
        ayyTown=""
    else:
        ayyTown="Asia(4) "
    if(water7==True): #refrence that doesn't really make sense
        water7=""
    else:
        water7="Oceania(5) "
    if(africaTown==True):
        africaTown=""
    else:
        africaTown="Africa(6) "
    if(downTown=="" and upTown=="" and eeeTown=="" and ayyTown=="" and water7=="" and africaTown==""):
        choice=(input("You have not yet killed any continents. Press ENTER to continue: "))
        choice=0
    else:
        choice=int(input(f"Which continent should be renewed: {downTown}{upTown}{eeeTown}{ayyTown}{water7}{africaTown}"))
    print("")
    return choice #choice then becomes user


southAmerica=True
northAmerica=True
europe=True
asia=True
oceania=True
africa=True
i=1 #for the loop

while(i==1):

    user=int(input("Would you like to Kill(1) or Renew(2) a continent? or Settings(0): "))
    if(user==1): #kill
        user = death(southAmerica,northAmerica,europe,asia,oceania,africa)
        if(user==1):
            southAmerica=False
        elif(user==2):
            northAmerica=False
        elif(user==3):
            europe=False
        elif(user==4):
            asia=False
        elif(user==5):
            oceania=False
        elif(user==6):
            africa=False
    elif(user==2):
        user = renew(southAmerica,northAmerica,europe,asia,oceania,africa)
        if(user==1):
            southAmerica=True
        elif(user==2):
            northAmerica=True
        elif(user==3):
            europe=True
        elif(user==4):
            asia=True
        elif(user==5):
            oceania=True
        elif(user==6):
            africa=True
    elif(user==0):
        user=int(input("Quit(0) or See Extras(5): "))
        if(user==0):
            i+=1
            southAmerica=False
            northAmerica=False
            europe=False
            asia=False
            oceania=False
            africa=False
        elif(user==5):
            print("")
            print("Total code is [236 Lines] (including the code for this)")
            print("Work began on [March 14th, 2026] at [5PM]")
            print("Most Recent Update was on: [March 23rd, 2026] at [1PM]")
            stop=input("Press ENTER when you wish to continue: ") #Lets the user have time to read

    makeContinents(southAmerica,northAmerica,europe,asia,oceania,africa)




#If I made bug reports like The Sims 3, one would be 'Africa no longer refuses to die'
#edit: 'Africa no longer stays dead'


'''
#the original ASCII:

#note: the { in africa had to be replaced with (
#note the " in europe had to be replaced with two '
print("        _,--',   _._.--._____   ")
print(" .--.--';_'-.', ";_      _.,-'  ")
print(".'--'.  _.'    {`'-;_ .-.>.'    ")
print("      '-:_      )  / `' '=.     ")
print("        ) >     {_/,     /~)    ")
print("        |/               `^ .'  ")
'''