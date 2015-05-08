# Hadoop streaming and pig query

## Introduction
* Use hadoop streaming to compare with pig query with the same job. 
* Customer dataset: each line contains: CustID, Name, Age, CountryCode, Salary.
* Transactions dataset: each line contains: TransID, CustID, TransTotal, TransNumItems, TransDesc.
* Objective: reports	for	every	customer,	the	number	of	transactions	that	each	customer	did	and	the	total	sum	of	these	transactions. 

## Conclusion
* Hadoop streaming is faster than Pig. This is just because in hadoop streaming, one mapreduce job can accomplish the whole thing. At the reducer part of Hadoop streaming, it does both the aggregation and join. 
* In pig query, however, it transformed this job into two mapreduce job. One for join and one for aggregation. So there is extra overhead to sort, shuffle, read and wirite the intermediate results. 
