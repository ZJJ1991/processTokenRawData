import csv

def testCre(fileName):
    # db stores the balance of different accounts
    db = {}
    with open("./tokenList/BNT.csv") as f:
        for line in f:
            sender = line.split(",")[1]
            receiver = line.split(",")[2]
            amount = float(line.split(",")[3])
            if sender in db:
                db[sender] = db[sender] - amount
            else:
                db[sender] = 0-amount
            if receiver in db:
    			db[receiver] = db[receiver]+amount
            else:
                db[receiver] = 0+amount
                print('amount of money: ',amount)

    aa = sum(db.values())
    print ("aa", aa)
    total = db['0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C']
    print('total created: ', -total)

def main():
    testCre("./tokenList/BAT.csv")

if __name__=="__main__":
 	main()