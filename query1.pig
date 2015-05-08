/* customer = LOAD '/proj2/customer.txt' USING PigStorage(',') AS (id:int, name:chararray, age:int, countrycode:int, salary:float); */

transactions = LOAD '/proj2/Transactions.txt' USING PigStorage(',') AS (transid:int, custid:int, transtotal:float, transnumitems:int, transdesc:chararray);

clean1 = FOREACH transactions GENERATE custid, transtotal;

customer_group = GROUP clean1 BY custid; 

output1 = FOREACH customer_group GENERATE group, COUNT(clean1), SUM(clean1.transtotal);

STORE output1 INTO 'query1_output.csv' USING PigStorage(','); 

