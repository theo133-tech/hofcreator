import requests

bs = "[addbusstop]"
term = "[addterminus]"
fileName = input("Enter the file name(No Extension): ")
f = open(fileName + ".hof",'r')
imgSrc = "https://generator.hkt172.net/canrun/generate?"
    
def downloadWelcomeImage(url,file_name):
    response = requests.get(url)
    with open(file_name,"wb") as f:
        f.write(response.content)

if f.read() != "":
    # print("Really nigga")
    busStopWrite = open("busstoplist.txt",'a')
    write = open(fileName + ".hof","a")
    addbs = True
    while addbs == True:
        isDDU = input("\nIs this for DDU? [Y/N/q]: ")
        if isDDU == "Y":
            dduBname = input("Enter the route number: ")
            dest1 = input("Enter the first destination: ")
            dest2 = input("\nEnter the second destination: ")
            dest1Sec = input("\nEnter the sections for destination 1: ")
            dest2Sec = input("\nEnter the sections for destination 2: ")
            price1 = input("\nEnter the price for dest 1: ")
            price2 = input("\nEnter the price for dest 2: ")
            blankArea1 = 21 - (len(dest1) + len(dest1Sec))
            blankArea2 = 21 - (len(dest2) + len(dest2Sec))
            blankArea1Space = " "
            blankArea2Space = " "
            y1 = blankArea1Space * blankArea1
            y2 = blankArea2Space * blankArea2
            for char in blankArea1Space:
                print(blankArea1Space)
                print(blankArea2Space)
                write.write(bs)
                write.write(dduBname + "\n")
                write.write(dest1 + y1 + dest1Sec + "\n")
                write.write(dest2 + y2 + dest2Sec + "\n")
                write.write("$" + price1 + "\n")
                write.write("$" + price2 + "\n\n")
                busStopWrite.write(dduBname + "\n")
                write.close()
        elif isDDU == "N":
            write.write(bs + "\n")
            bsName = input("Enter the bus stop name: ")
            busStopWrite.write(bsName + "\n_PleaseHoldTheHandrail\n")
            write.write(bsName + "\n")
            stopreName = input("Enter the stopreporter display: ")
            write.write(stopreName + "\n")
            bsTime = input("Enter the busstop time: ")
            write.write(bsTime + "\n")
            isPrice = input("Does this stop has a new section? (Y/N): ")
            if isPrice == "Y":
                bsPrice = input("Enter the price here: ")
                write.write("$" + bsPrice + "\n")
                write.write("$" + bsPrice + "\n\n")
                chinStopName = input("Chinese name for the bus stop: ")
                if len(chinStopName) > 6:
                    split = int(input("Input the place where the word should be split: "))
                    firstGen = imgSrc + "ln0=&ln1=" + chinStopName[0:split] + "&type=6&filename=" + bsName
                    secGen = imgSrc + "ln0=" + chinStopName[0:split] + "&ln1=" + chinStopName[split:len(chinStopName)] + "&type=6&filename=" + bsName
                    
                    if bsName.find("_") != -1:
                        #Replace _xxx -> _!xxx
                        bsName = bsName.replace("_","_!")
                    downloadWelcomeImage(firstGen, "6words\\" + bsName + ".bmp")
                    downloadWelcomeImage(secGen, "6words\\" + bsName + "_2.bmp")
                    if bsName.find("_!") != -1:
                        bsName = bsName.replace("_!","!")
                    downloadWelcomeImage(firstGen, "6words\\" + bsName + ".bmp")
                    downloadWelcomeImage(secGen, "6words\\" + bsName + "_2.bmp")
                    if len(chinStopName) > 8:
                        split8 = int(input("Where do you want to seperate for 8words mon: "))
                        fGen = imgSrc + "ln0=&ln1=" + chinStopName[0:split8] + "&type=8&filename=" + bsName
                        sGen = imgSrc + "ln0=" + chinStopName[0:split8] + "ln1=" + chinStopName[split8:len(chinStopName)] + "&type=8&filename=" + bsName
                        if bsName.find("_") != -1:
                            #Change _xxx -> _!xxx
                            bsName = bsName.replace("_","_!")
                        downloadWelcomeImage(fGen, "8words\\" + bsName + ".bmp")
                        downloadWelcomeImage(sGen, "8words\\" + bsName + "_2.bmp")
                        
                        if bsName.find("_!") != -1:
                            bsName = bsName.replace("_!","!")
                        downloadWelcomeImage(fGen, "8words\\" + bsName + ".bmp")                        
                        downloadWelcomeImage(sGen, "8words\\" + bsName + "_2.bmp")
                    else:
                        gen = imgSrc + "ln0=&ln1=" + chinStopName + "&type=8&filename=" + bsName
                        downloadWelcomeImage(gen, "8words\\" + bsName + ".bmp")
                        if bsName.find("_") != -1:
                            bsName = bsName.replace("_","")
                        downloadWelcomeImage(gen, "8words\\" + bsName + ".bmp")
                else:
                    gen = imgSrc + "ln0=&ln1=" + chinStopName + "&type=6&filename=" + bsName
                    downloadWelcomeImage(gen, "6words\\" + bsName + ".bmp")
                    gen8 = imgSrc + "ln0=&ln1=" + chinStopName + "&type=8&filename=" + bsName
                    downloadWelcomeImage(gen, "8words\\" + bsName + ".bmp")
                    if bsName.find("_") != -1:
                        bsName = bsName.replace("_","")
                    downloadWelcomeImage(gen, "6words\\" + bsName + ".bmp")
                    downloadWelcomeImage(gen, "8words\\" + bsName + ".bmp")
            elif isPrice == "N":
                write.write(bsName + "\n")
                write.write(bsName + "\n")#with underscore
                chinStopName = input("Please enter the Chinese name for the bus stop: ")
                if len(chinStopName) > 6:
                    split = int(input("Input the place where the word should be split: "))
                    firstGen = imgSrc + "ln0=&ln1=" + chinStopName[0:split] + "&type=6&filename=" + bsName
                    secGen = imgSrc + "ln0=" + chinStopName[0:split] + "&ln1=" + chinStopName[split:len(chinStopName)] + "&type=6&filename=" + bsName
                    
                    if bsName.find("_") != -1:
                        #Replace _xxx -> _!xxx
                        bsName = bsName.replace("_","_!")
                    downloadWelcomeImage(firstGen, "6words\\" + bsName + ".bmp")
                    downloadWelcomeImage(secGen, "6words\\" + bsName + "_2.bmp")
                    if bsName.find("_!") != -1:
                        bsName = bsName.replace("_!","!")
                    downloadWelcomeImage(firstGen, "6words\\" + bsName + ".bmp")
                    downloadWelcomeImage(secGen, "6words\\" + bsName + "_2.bmp")
                    if len(chinStopName) > 8:
                        split8 = int(input("Where do you want to seperate for 8words mon: "))
                        fGen = imgSrc + "ln0=&ln1=" + chinStopName[0:split8] + "&type=8&filename=" + bsName
                        sGen = imgSrc + "ln0=" + chinStopName[0:split8] + "ln1=" + chinStopName[split8:len(chinStopName)] + "&type=8&filename=" + bsName
                        if bsName.find("_") != -1:
                            #Change _xxx -> _!xxx
                            bsName = bsName.replace("_","_!")
                        downloadWelcomeImage(fGen, "8words\\" + bsName + ".bmp")
                        downloadWelcomeImage(sGen, "8words\\" + bsName + "_2.bmp")
                        
                        if bsName.find("_!") != -1:
                            bsName = bsName.replace("_!","!")
                        downloadWelcomeImage(fGen, "8words\\" + bsName + ".bmp")                        
                        downloadWelcomeImage(sGen, "8words\\" + bsName + "_2.bmp")
                    else:
                        gen = imgSrc + "ln0=&ln1=" + chinStopName + "&type=8&filename=" + bsName
                        downloadWelcomeImage(gen, "8words\\" + bsName + ".bmp")
                        if bsName.find("_") != -1:
                            bsName = bsName.replace("_","")
                        downloadWelcomeImage(gen, "8words\\" + bsName + ".bmp")
                else:
                    gen = imgSrc + "ln0=&ln1=" + chinStopName + "&type=6&filename=" + bsName
                    downloadWelcomeImage(gen, "6words\\" + bsName + ".bmp")
                    gen8 = imgSrc + "ln0=&ln1=" + chinStopName + "&type=8&filename=" + bsName
                    downloadWelcomeImage(gen, "8words\\" + bsName + ".bmp")
                    if bsName.find("_") != -1:
                        bsName = bsName.replace("_","")
                    downloadWelcomeImage(gen, "6words\\" + bsName + ".bmp")
                    downloadWelcomeImage(gen, "8words\\" + bsName + ".bmp")
                
                #Writing busstop without underscore
                nBsName = bsName[0:len(bsName)]
                busStopWrite.write(nBsName + "\n")
                write.write("\n" + bs + "\n")
                write.write(nBsName + "\n")
                write.write(stopreName + "\n")
                write.write(bsTime + "\n")
                write.write(bsName + "\n")
                write.write(bsName + "\n\n")
        elif isDDU == "q":
            #Write Slot
            write.write("===============================================================================\n")
            write.write("	Slot 1")
            write.write("===============================================================================\n\n")
            write.write("Slot 1\n")
            write.write("-----------------------------------\n\n")
            write.write("[infosystem_trip]\n")
            routeCode = input("Enter the route code: ")
            write.write(routeCode + "\n")
            destination = input("Enter the destination: ")
            write.write(destination + "\n")
            IBIS = input("Enter the IBIS code: ")
            write.write(IBIS + "\n")
            hanoverCode = input("Enter hanover code(e.g. 68MY): ")
            write.write(hanoverCode + "\n\n\n\n[infosystem_busstop_list]\n\n")
            write.write(dduBname + "\n")
        elif isDDU == "":
            write.close()