import csv

def proEOS():
    ftimestamp = open('./tokenList/EOStimestamp.csv')
    lines = ftimestamp.readlines()
    print(112)
    fnew = open('./tokenList/EOSnew.csv', 'w')
    with open("./tokenList/EOS.csv", 'w+r') as feos:
        for i, line in feos:
            print(lines[i])
    ftimestamp.close()

def main():
        proEOS()       

if __name__=="__main__":
    main()       
