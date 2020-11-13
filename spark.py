import pyspark
from pyspark import SparkContext
sc =SparkContext()
print('##############################')
print(sc.parallelize([1,2,3,4]).collect())
