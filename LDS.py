import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data = pd.read_csv("/Users/charliegray/Library/Mobile Documents/com~apple~CloudDocs/programming/LDSAnalyser/Pearson Edexcel GCE AS and AL Mathematics data set (5).csv",sep='delimiter', header=None, encoding = "ISO-8859-1")


print(data[0][2918])


ignoredVal = ["n/a", "#n/a", "-", "na"]

length = 247-63

placesMap = [["CAMBORNE", 63, 1018], ["HEATHROW", 254, 1209], ["HURN", 445, 1400], ["LEEMING", 636, 1591], ["LEUCHARS", 827, 1782], ["BEIJING", 1973, 2162], ["JACKSONVILLE", 2351, 2540], ["PERTH", 2729, 2918]]

def plot(collumn, placesMap, data, ignoredVal, length, increment):

    if collumn in [5, 12, 14]:
        return "not shown, data is qualitative"

    if not (0 < collumn < 14):
        return "not a viable collumn"

    yearInd = 0
    count = 1
    while yearInd < 2:
        plt.figure()
        count = 1
        for index in range(0, 5):

            x = []
            y = []

            for i in range(0, length):

                val = data[0][placesMap[index][yearInd+1]+i+1].split(',')[collumn]

                if val.lower() in ignoredVal:
                    continue
                elif val.lower() == "tr":
                    x.append(i)
                    y.append(0.05)
                else:
                    x.append(i)
                    y.append(float(val))

            plt.subplot(2,3,count)
            year = "1987"
            if yearInd == 1:
                year = "2015"
            plt.title(f"{placesMap[index][0]} {year}")
            plt.plot(x, y)

            plt.yticks(np.arange(min(y), max(y), increment))

            count += 1

        plt.suptitle(f"{data[0][placesMap[0][1]].split(',')[collumn]} VS days after 01/05/{year}")
        

        yearInd += 1

    UKGlobalColMap = {1:1, 2:2, 10:3, 4:4}
    if collumn not in [1, 2, 10, 4]:
        plt.show(block=False)
        return "shown"

    collumn = UKGlobalColMap[collumn]

    yearInd = 0
    count = 1
    while yearInd < 2:
        plt.figure()
        count = 1
        for index in range(5, len(placesMap)):

            x = []
            y = []

            for i in range(0, length):

                val = data[0][placesMap[index][yearInd+1]+i+1].split(',')[collumn]

                if val.lower() in ignoredVal:
                    continue
                elif val.lower() == "tr":
                    x.append(i)
                    y.append(0.05)
                else:
                    x.append(i)
                    y.append(float(val))

            plt.subplot(1, 3, count)
            year = "1987"
            if yearInd == 1:
                year = "2015"
            plt.title(f"{placesMap[index][0]} {year}")
            plt.plot(x, y)

            plt.yticks(np.arange(min(y), max(y), increment))

            count += 1

        plt.suptitle(f"{data[0][placesMap[0][1]].split(',')[collumn]} VS days after 01/05/{year}")

        yearInd += 1


    plt.show(block=False)
    return "shown"

increments = [0, 2, 5, 2, 4, 0, 6, 5 ,1 ,1000, 10, 100, 0, 100, 0]