import csv


# dataFiles = ["AE","AION","BAT","BNT","BTM","CENNZ","CTXC","DGD", "ELF", "EOS",
# "GNT", "ICX", "IOST", "KIN", "LRC", "MKR", "NAS", "OMG", "REP", "RHOC",
# "SNT", "VEN", "WTC", "ZIL", "ZRX"];

dataFiles = ["AION", "ICX", "VEN"]
create = {"AION": "0x0000000000000000000000000000000000000000",
          # "DGD": "Unknown",
          "ICX": "0xE16fd9B95758fe8f3A478EF9B750A64513bF2E80",
          "VEN": "0x0000000000000000000000000000000000000000"}
delete = {"VEN": "0x000000000000000000000000000000000000dEaD"}


def exfile(fileName):
    db = {}
    topAccounts = []
    with open("./tokenList/"+str(fileName)+".csv") as f:
        for line in f:
            sender = line.split(";")[1]
            print(sender)
            receiver = line.split(";")[2]
            # print(receiver)
            money = float(line.split(";")[3])
            # print(money)
            if sender in db:
                db[sender] = db[sender]-money
            else:
                db[sender] = 0-money
            if receiver in db:
                db[receiver] = db[receiver]+money
            else:
                db[receiver] = 0+money
                # print(money)

    aa = sum(db.values())
    created = db[create[fileName]]
    if fileName == 'VEN':
        deleted = db[delete[fileName]]
        db[delete[fileName]] = -1
        # print("sum")
        # print(aa -db["0x0000000000000000000000000000000000000000"] - db['0x000000000000000000000000000000000000dEaD'])
        balance = -created - deleted
    else:
        balance = -created
    # print(balance)
    l = sorted(db.items(), key=lambda db: db[1])
    print(l[-1])
    print(l[-51:])

    for accounts in l[-51:-1]:
        topAccounts.append(accounts[0])
        topAccounts.reverse()
    return (balance, topAccounts)


def calDailyBal1(fileName):
    db = {}
    topAccounts = []
    with open("./tokenList/"+str(fileName)+".csv") as f:
        for line in f:
            sender = line.split(";")[1]
            receiver = line.split(";")[2]
            money = float(line.split(";")[3])
            if sender in db:
                db[sender] = db[sender]-money
            else:
                db[sender] = 0-money
            if receiver in db:
                db[receiver] = db[receiver]+money
            else:
                db[receiver] = 0+money
            # print(money)

    aa = sum(db.values())
    l = sorted(db.items(), key=lambda db: db[1])
    # print(l)
    # print(l[-51:])
    balf = open("./tokenList/"+str(fileName)+"bal.csv", 'w')
    for item in db.items():
        balf.write(item[0]+','+str(item[1])+'\n')
    balf.close()

    if len(l) < 50:
        for accounts in l[-len(l):-1]:
            topAccounts.append(accounts[0])
        topAccounts.reverse()
	return (topAccounts)
    else:
        for accounts in l[-51:-1]:
            topAccounts.append(accounts[0])
            topAccounts.reverse()
    return (topAccounts)


def dailyBalanceVariation(fileName):
    with open("./tokenList/"+str(fileName)+".csv") as f:
		lines = f.readlines()
    firstLine = lines[0]
    initialTime = firstLine.split(";")[6]
    print("initial time: "+initialTime)
    newFileName = fileName+'days'
    output_new = open('./tokenList/'+newFileName+'.csv', 'w')
    topAccountsFile = open('./tokenList/'+fileName+'final.csv', 'w')
    lastIndex = len(lines)-1
    timeGap = float(lines[lastIndex].split(";")[6]) - \
        float(lines[0].split(";")[6])
    days = float(timeGap)/86400
    print("days: ", days)
    for line in lines:
        if float(line.split(";")[6]) < float(initialTime) + 86400:
            output_new.write(line)
    topAccounts = calDailyBal1(newFileName)
    for account in topAccounts:
        topAccountsFile.write(account+",")


def main():
    final = []
    for fileName in dataFiles:
        # deleteFirstLine(fileName)
        (supply, topAccounts) = exfile(fileName)
        # print(len(topAccounts))
        row = [fileName, supply, topAccounts]
        print(len(topAccounts))
        final.append(row)
        with open("final.csv", "w") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["Token", "Balance", "Account"])
            writer.writerows(final)

def correctDecimal1(fileName):
    fnew = open("./tokenList/"+str(fileName)+"new.csv", 'w') 
    with open("./tokenList/"+str(fileName)+".csv") as f:
        for index, line in enumerate(f):
            money = float(line.split(";")[3])
            # print(money)
            fnew.write(
                line.split(";")[0]+','+
                line.split(";")[1]+','+
                line.split(";")[2]+','+
                str(float(line.split(";")[3]))+','+
                line.split(";")[4]+','+
                line.split(";")[5]+','+
                line.split(";")[6]
                )

def correctDecimal2(fileName):
    fnew = open("./tokenList/"+str(fileName)+"new.csv", 'w') 
    with open("./tokenList/"+str(fileName)+".csv") as f:
        for index, line in enumerate(f):
            money = float(line.split(",")[2])/(1000000000000000000)
            # print(money)
            fnew.write(
                str(index+1)+','+
                line.split(",")[0]+','+
                line.split(",")[1]+','+
                # line.split(";")[2]+','+
                str(float(line.split(",")[2])/(1000000000000000000))+','+
                line.split(",")[3]+','+
                line.split(",")[4]+','+
                line.split(",")[5]
                )

def calDailyBal2(fileName):
    db = {}
    topAccounts = []
    with open("./tokenList/"+str(fileName)+".csv") as f:
        for line in f:
            sender = line.split(",")[1]
            receiver = line.split(",")[2]
            money = float(line.split(",")[3])
            if sender in db:
                db[sender] = db[sender]-money
            else:
                db[sender] = 0-money
            if receiver in db:
                db[receiver] = db[receiver]+money
            else:
                db[receiver] = 0+money
            # print(money)

    aa = sum(db.values())
    l = sorted(db.items(), key=lambda db: db[1])
    # print(l)
    # print(l[-51:])
    balf = open("./tokenList/"+str(fileName)+"bal.csv", 'w')
    for item in db.items():
        balf.write(item[0]+','+str(item[1])+'\n')
    balf.close()

    if len(l) < 50:
        for accounts in l[-len(l):-1]:
            topAccounts.append(accounts[0])
        topAccounts.reverse()
	return (topAccounts)
    else:
        for accounts in l[-51:-1]:
            topAccounts.append(accounts[0])
            topAccounts.reverse()
    return (topAccounts)

if __name__ == "__main__":
    correctDecimal2("BAT")
    # calDailyBal2("AEnew")