def exporter(self,stock):
        output = "{} {} {} {},{} {}".format(str(stock.sid),stock.type ,stock.name,str(stock.initqty),str(stock.qty),"CLOSED")
        TransactionRoom.printOutput[int(stock.sid)] = output