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

