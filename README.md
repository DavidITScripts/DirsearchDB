# DirsearchDB
To report to a database, do the following:
1.  Change the database parameters in the ./lib/reports/DBReport.py script to match your DB
2.  use the --database-report=outputfile.txt
Example:
python3 dirsearch.py --database-report=outputfile.txt -L URLList.txt -w wordlist.txt -e php
