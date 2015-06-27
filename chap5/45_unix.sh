#! /bin/bash

if [ ! -e ./45.dat ]; then
    python 45.py > 45.dat
fi

echo 'Top 50 frequent combinations of predicate and case patterns'
sort 45.dat | uniq -c | sort -rnk1 | head -n 50
echo

echo 'Top 10 case patterns that have "する"'
grep '^する\t' 45.dat | uniq -c | sort -rnk1 | head -n 10
echo

echo 'Top 10 case patterns that have "見る"'
grep '^見る\t' 45.dat | uniq -c | sort -rnk1 | head -n 10
echo

echo 'Top 10 case patterns that have "与える"'
grep '^与える\t' 45.dat | uniq -c | sort -rnk1 | head -n 10
echo
