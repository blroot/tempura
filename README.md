# tempura

This project is intented to be a simple and fast solution for
parsing SQUID accesslog files and saving records to DB

- It is recommended running under PyPy for more speed
- Multi Threading is a desired feature

Usage atm:
- tempura.py [single|multi] [chunk_size] [threads]

Some tests so far

> time python tempura.py single 1000

real    0m3.215s
user    0m3.064s
sys     0m0.140s

> time python tempura.py multi 1000 8

real    0m1.541s
user    0m5.720s
sys     0m0.144s

Not bad, bear in mind that this results involves just reading the file and storing lines in a list of tuples
for further processing, but we are not actually doing anything else in this test, not even printing those chunked
list of tuples, because printing to STDOUT will slow the fuck down the process
