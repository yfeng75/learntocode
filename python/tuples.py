welcom = 'Welcome to my nightmare',"Alice Cooper",1975
bad="Bad Company" "Bad Company",1974
budgie = "Nightglight", "Budgie",1981
imelda="More Mayhem", "Emilda May", 2011,(
    (1,"pulling the rug"),(2,"Psycho"),(3,"Mayhem"),(4,"Kentish Town Waltz"))
print(imelda)

title, artist,year,tracks=imelda
print(title,artist,year)
# print(artist)
# print(year)
for char in tracks:
    print("\t" +str(char))



