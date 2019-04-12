#https://stackoverflow.com/questions/31173113/starting-hiveserver2
#https://www.edureka.co/blog/hive-commands-with-examples
#https://www.tutorialspoint.com/hive/hive_create_table.htm

from pyhive import hive
conn = hive.Connection(host="localhost", port=10000, username="andre")