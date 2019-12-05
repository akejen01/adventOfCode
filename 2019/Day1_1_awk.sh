awk '{ s+= int($1 / 3) - 2 } END {print s}' Day1_1_data.txt
