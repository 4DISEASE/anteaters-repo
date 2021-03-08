import billboard

def format():
    hot100=billboard.ChartData('hot-100')
    artist100 = billboard.ChartData('artist-100')
    billboard200 = billboard.ChartData('billboard-200')

    count=0
    number = 1
    global nicetexthot100, nicetextartist100, nicetext200
    nicetexthot100 = ''
    nicetextartist100=''
    nicetext200 = ""
    while count<100:
        nicetexthot100 = nicetexthot100 + str(number) + ". " + str(hot100.entries[count]) + "</br>"
        count +=1
        number +=1

    count=0
    number = 1
    while count<100:
        nicetextartist100 = nicetextartist100 + str(number) + ". " + str(artist100.entries[count]) + "</br>"
        count +=1
        number +=1

    count=0
    number = 1
    while count<200:
        nicetext200 = nicetext200 + str(number) + ". " + str(billboard200.entries[count]) + "</br>"
        count +=1
        number +=1

hot100=billboard.ChartData('hot-100')
format()

def billboarddata():
    billboarddict={"hot100data": nicetexthot100,
                   "artist100data": nicetextartist100,
                   "billboard200data": nicetext200}
    return billboarddict
