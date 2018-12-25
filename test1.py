import unittest
import main

import csv


class Test_TestStocks(unittest.TestCase):
    
    def test_transact(self):
        trans = main.Transactor()
        a = main.Stock(0,10,0,0,0)
        b = main.Stock(0,4,0,0,0)
        
        #a>b
        trans.transact(a,b)
        self.assertEqual(a.qty,6)
        self.assertEqual(b.qty,0)

        #a<b
        a.qty=3
        b.qty=10
        trans.transact(a,b)
        self.assertEqual(a.qty,0)
        self.assertEqual(b.qty,7)

        #a=b

        a.qty=6
        b.qty=6
        trans.transact(a,b)
        self.assertEqual(a.qty,0)
        self.assertEqual(b.qty,0)

    def test_operation(self):


        #test for given inputs
        companies=main.Companies()
        tRoom=main.TransactionRoom() 
        with open('data.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                sid=int(row[0])
                type=row[1]
                cname=row[2]
                qty=int(row[3])
                stock = main.Stock(sid, qty, type, cname, qty)
                if(companies.check(cname)==0):
                    company=main.Company(cname)
                    companies.insert(company,cname)
                else:
                    company=companies.check(cname)

                tRoom.operation(company,stock)

        for i in range(len(companies.cnames)):
            tRoom.cleaner(companies.companies[i])
        
        expected_output = {1: '1 Buy ABC 10,0 CLOSED', 4: '4 Buy XYZ 10,0 CLOSED', 2: '2 Sell XYZ 15,0 CLOSED', 3: '3 Sell ABC 13,3 OPEN', 5: '5 Buy XYZ 8,3 OPEN'}
        self.assertEqual(tRoom.printOutput,expected_output)

        #test when only buy or sell stocks available
        companies=main.Companies()
        tRoom=main.TransactionRoom() 
        with open('data3.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                sid=int(row[0])
                type=row[1]
                cname=row[2]
                qty=int(row[3])
                stock = main.Stock(sid, qty, type, cname, qty)
                if(companies.check(cname)==0):
                    company=main.Company(cname)
                    companies.insert(company,cname)
                else:
                    company=companies.check(cname)

                tRoom.operation(company,stock)

        for i in range(len(companies.cnames)):
            tRoom.cleaner(companies.companies[i])

        expected_output = {3: '3 Sell ABC 80,80 OPEN', 5: '5 Sell ABC 10,10 OPEN', 1: '1 Sell ABC 10,10 OPEN', 2: '2 Sell ADS 10,10 OPEN', 4: '4 Sell XYZ 10,10 OPEN', 6: '6 Sell WQY 90,90 OPEN'}
        self.assertEqual(tRoom.printOutput,expected_output)


    def test_exporter(self):
        exp = main.Exports()

        #quantity = 0

        stock = main.Stock(3,0,"Buy","ABC",10)
        exp.exporter(stock)
        self.assertEqual(main.TransactionRoom.printOutput[3],"3 Buy ABC 10,0 CLOSED")

        #quantity !=0

        stock = main.Stock(3,4,"Buy","ABC",10)
        exp.exporter(stock)
        self.assertEqual(main.TransactionRoom.printOutput[3],"3 Buy ABC 10,4 OPEN")






if __name__ == '__main__':
    unittest.main()
    
