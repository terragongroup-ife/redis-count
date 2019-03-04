
import redis
import logging
import time
import csv


index_name = 'id'
redis_server = '127.0.0.1'
redis_port = '6379'
r = redis.Redis(
    host=redis_server,
    port=redis_port)
readCSV = ""

# To use logging module to log Info/Debug message properly
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger('redis_setup')

# To calculate total time to get required result.
t = time.process_time()

# clear the hset
r.flushall("ID")


def checkId(checker):
    with open('redis_data.csv') as data:
        readCSV = csv.reader(data,delimiter = ',')
        for row in readCSV:
            if (r.hexists("ID", checker)):
                print("Exists")
                return 1
            else:
                return


with open('redis_data.csv') as data:
    readCSV = csv.reader(data, delimiter = ',')
    line_count = 0
    for row in readCSV:
        if (line_count == 0):
            logger.info(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if r.hexists("ID", row[5]):
                r.hincrby("ID",row[5],1)

            else:
                r.hset("ID",row[5],1)


            line_count += 1



    print(r.hgetall("ID"))
    print(line_count)

checker = input("Enter an Id: ")
checkId(checker)


