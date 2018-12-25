from collections import deque
import csv

class Exports:
    
    def exporter(self,stock):
        if(stock.qty==0):
            status="CLOSED"
        else:
            status="OPEN"
        #print in tabular format
        output = "{:^6}  {:^6}  {:^6}  {:^1},{:^1} {:^17}".format(str(stock.sid),stock.type ,stock.name,str(stock.initqty),str(stock.qty),status)
        TransactionRoom.printOutput[int(stock.sid)] = output


class Transactor:

    def transact(self,a,b):
        
        if(a.qty>b.qty):
            a.qty=a.qty-b.qty
            b.qty=0
        elif(a.qty<b.qty):
            b.qty=b.qty-a.qty
            a.qty=0
        else:
            a.qty=0
            b.qty=0

class TransactionRoom:
    
    printOutput = {} #dictionary to store all outputs taken place in the room
    
    def __init__(self):
        self.export=Exports()
        self.trs=Transactor()

    def operation(self,company,stock):
        if(stock.type=="Buy"):
            company.buyers.append(stock)
        
        elif (stock.type == "Sell"):
            company.sellers.append(stock)

        #debulk queues in each read
        while(1>0):
                if(company.sellbal.qty==0 and len(company.sellers)>0):
                    company.sellbal = company.sellers.popleft()
                elif(company.sellbal.qty==0 and len(company.sellers)==0):
                    break

                if(company.buybal.qty==0 and len(company.buyers)>0):
                    company.buybal=company.buyers.popleft()
                elif(company.buybal.qty==0 and len(company.buyers)==0):
                    break
                
                #perform transaction
                self.trs.transact(company.sellbal,company.buybal)
                
                #check for closed stocks return them
                if(company.buybal.qty==0):
                    self.export.exporter(company.buybal)
                if(company.sellbal.qty==0):
                    self.export.exporter(company.sellbal)
                  
                
    #to grab all open stocks in the end
    def cleaner(self,company):
        
        while(len(company.buyers)>0):
            temp = company.buyers.popleft()
            self.export.exporter(temp)
        
        while(len(company.sellers)>0):
            temp = company.sellers.popleft()
            self.export.exporter(temp)

        if(company.buybal.qty>0):
            self.export.exporter(company.buybal)

        if(company.sellbal.qty>0):
            self.export.exporter(company.sellbal)

    #to print results / output
    def printer(self):
        troom2 =  sorted(TransactionRoom.printOutput)
        print("\n")
        print("StockID  Side  Company  Quantity  Status")
        print("----------------------------------------")
        for i in troom2:
            print(TransactionRoom.printOutput[i])
        print("\n")


class Stock:

    def __init__(self,sid,qty,typeo,cname,initqty):
        self.sid=sid
        self.qty=qty
        self.type=typeo
        self.initqty=initqty
        self.name=cname


    
class Company:

    def __init__(self,name):
        self.name=name
        self.buyers = deque()
        self.sellers = deque()
        self.buybal = Stock(0, 0, "Buy","",0)
        self.sellbal = Stock(0, 0, "Sell","", 0)



class Companies:

    def __init__(self):
        self.companies = {}

    def insert(self,company,cname):
        self.companies[cname] = company

    def check(self,cname):
        #return the company object if it exists
        if(cname in self.companies): 
            return self.companies[cname]
        else:
            return 0
    



def main():

    companies=Companies()
    tRoom=TransactionRoom()

    with open('data2.csv', 'r') as csvFile: #change file here for input
        reader = csv.reader(csvFile)
        for row in reader:
            sid=int(row[0])
            type=row[1]
            cname=row[2]
            qty=int(row[3])
            #block for new entries
            stock = Stock(sid, qty, type, cname, qty)
            if(companies.check(cname)==0):
                #create new company
                company=Company(cname)
                #insert into companies
                companies.insert(company,cname)
            #block for existing ones
            else:
                company=companies.check(cname)

            tRoom.operation(company,stock)
            
    for i in companies.companies:
        tRoom.cleaner(companies.companies[i])
    
    #print results
    tRoom.printer()
    

if __name__ == '__main__':
    main()






