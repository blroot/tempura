__author__ = 'Bruno Lottero'


def main():
    chunksize = 1000
    accesslog_parser(chunksize)


def accesslog_parser(chunksize):
    chunk = []
    with open('access.log', 'r') as accesslog:
        for line in accesslog:
            chunk.append(line.split())
            if len(chunk) == chunksize:
                print 'Printing a chunk \n'
                print chunk
                #process(chunk) // Do something with this chunk
                chunk = []

