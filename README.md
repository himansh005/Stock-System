# Stock-System
Stock order execution system developed as a part of assignment given by Sahaj Software

SOLID, YAGNI and KISS principles have been applied to the best of my knowledge and ability in the program.

>implemented in Python3

>for running the program:
>python main.py

>for running the tests:
>python tests.py

### Object-Oriented Design Components

- **Exports** : contains the exporter method to store all results in a specified format in a data structure of choice
- **Transactor** : contains the transact method to perform transaction on 2 quantities
- **TransactionRoom**: contains the printOutput dictionary, provides method operation for each stock entry, method cleaner to     empty the queues at the end and method printer to print the results.
- **Stock** : represents each individual stock
- **Company** : represents each company providing their stock for buying or selling
- **Companies** : represents the collection of companies present

### Algorithm

```
 1. create new companies object
 2. create a transaction_room object = tRoom
 3. for each row or line in input file
 
        a. create stock object
        b. check if current(company) exists in companies
                if(yes) return the company object
                else    return 0 and insert new company object in the companies list
                
        c. perform tRoom.operation(company,stock)

                if(stock.type==Buy) [add to buyers Queue]
                if(stock.type==Sell) [add to sellers Queue]

                while(buyer or seller queue is NOT empty):

                    if(buy_balance==0):
                        deque new buyer from buyers Queue
                    if(sell_balance==0):
                        deque new seller from sellers queue
                    
                    transact(buy_balance,sell_balance)
                    collect results

        d. deque and collect remaining open stock in queue and balance

4. sort by stock id print all results

```
### Complexities

    1. Time Complexity  

            a. Iterating over each result takes n computations
            b. searching for a company in dictionary - O(1) since its a hashmap
            c. inserting a company in the dictionary - o(1) since all companies are unique => no collisions
            d. enqueue and deque take O(1) each
                    
                    Here, for each party, maximum of n-1 opposite parties need to be dequed
                    (example, if queue has n-1 sellers waiting, and buyers queue is empty, and new buyer comes
                    with buying power greater than or equal to sum of all selling power, maximum deques = n-1)
                    But, in this case, total computations are 1*(n-1) = n-1
            
            e. transact takes - O(1)
            f. dequeing takes - O(n)
            
            Considering having read all data points into the queue:
            
            Let, x - number of sellers in queue
                 y - number of buyers in queue
            
            where: x+y = n
            
            Let B(x) = total sum of queue x
                B(y) = total sum of queue y
                
            Also, total number of iteraitons is dependent on the queue which has smallest running sum.
    
            Now, the following case formulation holds while each transaction:
                    If B(y) >= B(x):
                    
                       1. y=1 buyer and x sellers: 1.x = x iterations
                       2. y=2 buyers and x sellers: 1.m + 1.(x-m) = x iterations
                       .
                       .
                       Similarily, considerig division of x into k chunks, hence a1+a2+...+ak = x
                       
                       Therfore, for y buyers and x sellers: 1.a1 + 1.a2 + 1.a3 + ..... + 1.ak,(y times)
                                                          = a1 + a2 +a3 + ..... +ak = x
                       
                    Else If B(y) <= B(x):
                                 for y buyers and x sellers: 1.a1 + 1.a2 + 1.a3 + ..... + 1.al,(y times)
                                                          = a1 + a2 +a3 + ..... +al = z (z<x)
                                                          
             Hence, z<x<n. Therefore, maximum iterations are n-1. 
             Therefore, the time complexity is linear: O(n)
    
    2. Space Complexity - linear

### Efficiency

Since, the algorithm computes on the go, i.e., along with reading the file, it keeps emptying the queues
and calculating the results, space and time are optimally utilised 


            
