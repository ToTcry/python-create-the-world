from pyspark import SparkConf,SparkContext
import os

# 初始化
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)



rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def func(data):
     return data * 10

rdd2 = rdd1.map(func)
print(rdd2.collect())

rdd3 = rdd2.map(lambda x:x+5)
print(rdd3.collect())


# 输出文件
rdd1.saveAsTextFile("D:/文档/深造/编程/Python/课堂练习/课堂练习/output1")
rdd2.saveAsTextFile("D:/文档/深造/编程/Python/课堂练习/课堂练习/output2")
rdd3.saveAsTextFile("D:/文档/深造/编程/Python/课堂练习/课堂练习/output3")

