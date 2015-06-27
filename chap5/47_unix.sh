#! /bin/bash

if [ ! -e ./47.dat ]; then
    python 47.py > 47.dat
fi

echo 'Top 50 frequent predicate'
cut -f1 47.dat | sort | uniq -c | sort -rnk1

echo 'Top 50 frequent combinations of predicate and particle'
cut -f1,2 47.dat | sort | uniq -c | sort -rnk1
