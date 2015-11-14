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


def main():
    """
    Main Function
    :return:
    """
    workers = 4
    chunksize = 1000                                               # Chunk Norris :-)
    accesslog_parser(chunksize)


def accesslog_parser(chunksize):
    """
    Parses the access.log file
    :param chunksize:
    :return:
    """
    chunk = []
    with open('access.log', 'r') as accesslog:
        for line in accesslog:
            chunk.append(line.split())
            if len(chunk) == chunksize:
                print 'Printing a chunk \n'
                print chunk
                #process(chunk) # Do something with this chunk
                chunk = []                                         # Once processed, destroy


def file_block(accesslog, workers):
    """
    Seek the file length and return the block size to be processed by a single worker
    :param accesslog:
    :param workers:
    :return:
    """
    accesslog.seek(0,2)                                            # Seek until EOF
    accesslog_size = accesslog.tell()
    accesslog_block = accesslog_size / workers

    return accesslog_block
