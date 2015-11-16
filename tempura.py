"""
Tempura SQUID log processor
Copyright (C) 2015  Bruno Lottero

This file is part of Tempura.

Tempura is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License

Tempura is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Tempura.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'Bruno Lottero'

from multiprocessing import Pool
import sys


def main():
    """
    Main Function
    :return:
    """
    workers = 4
    chunk_size = 1000                                                               # Chunk Norris :-) Amount of lines to process simultaneously
    accesslog_parser_multi_threaded(workers, chunk_size)


def accesslog_parser_single_threaded(chunk_size):
    """
    Parses the access.log file
    :param chunksize:
    :return:
    """
    chunk = []
    with open('access.log.1', 'r') as accesslog:
        for line in accesslog:
            chunk.append(tuple(line.split()))
            if len(chunk) == chunk_size:
                print 'Printing a chunk \n'
                print chunk
                #process(chunk) # Do something with this chunk
                chunk = []                                                          # Once processed, destroy
        if chunk:                                                                   # check if there's something left
            print 'Printing a chunk \n'
            print chunk
            #process(chunk) # Do something with this chunk
            chunk = []


def accesslog_parser_multi_threaded(workers):
    """
    Parses the access.log file
    :param chunksize:
    :return:
    """
    pool = Pool(processes=workers)
    pool.map(spawn_worker, range(workers))


def spawn_worker(worker_number):
    chunk = []
    #workers = int(sys.argv[3])
    #chunk_size = int(sys.argv[2])
    workers = 2
    chunk_size = 4
    with open('access.log.1', 'r') as accesslog:
        for line in file_block(accesslog, workers, worker_number):
            chunk.append(tuple(line.split()))
            if len(chunk) == chunk_size:
                    print 'Worker ' + str(worker_number) + '\n'
                    #print chunk
                    #process(chunk) # Do something with this chunk
                    chunk = []
    if chunk:                                                                   # check if there's something left
        print '\n Printing garbage chunk \n'
        #print chunk
        #process(chunk) # Do something with this chunk
        #chunk = []
        chunk = []


def file_block(accesslog, workers, worker):
    """
    A generator that splits a file into blocks and iterates
    over the lines of one of the blocks.
    Inspired by:
    https://xor0110.wordpress.com/2013/04/13/how-to-read-a-chunk-of-lines-from-a-file-in-python/
    :param accesslog:
    :param workers:
    :param worker:
    :return:
    """
    assert 0 <= worker and worker < workers
    assert 0 < workers

    accesslog.seek(0,2)
    file_size = accesslog.tell()

    ini = file_size * worker / workers
    end = file_size * (1 + worker) / workers

    if ini <= 0:
        accesslog.seek(0)
    else:
        accesslog.seek(ini-1)
        accesslog.readline()

    while accesslog.tell() < end:
        yield accesslog.readline()

if __name__ == '__main__':
    """
    Main Function
    :return:
    """
    workers = int(sys.argv[3])
    chunk_size = int(sys.argv[2])                                                               # Chunk Norris :-) Amount of lines to process simultaneously
    if sys.argv[1] == 'multi':                                                               # Chunk Norris :-) Amount of lines to process simultaneously
        accesslog_parser_multi_threaded(workers)
    if sys.argv[1] == 'single':
        accesslog_parser_single_threaded(chunk_size)
