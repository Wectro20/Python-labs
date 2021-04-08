# Python-labs

## Lab 5
  - Count the total size of image files of each type (at the end of the query tape should be the end of png, jpg) 
  - Resources which were successfully returned to customers (query type - GET or POST) 
  - Between 05 / Mar / 2004: 17: 04: 44 to 12 / Mar / 2004: 15: 21: 28
  - Log file: https://github.com/elastic/examples/blob/master/Common%20Data%20Formats/apache_logs/apache_logs 

### To run:
  - Clone/Download lab5 branch
  - Go into repo folder
  - Type `./main.py` or `python3 main.py

### How to use:
  ```
    counter = ResBytesCounter("NAME_OF_FILE")
    counter.search_period("17/May/2015:10:05:03", "17/May/2015:10:05:43")
  ```
  - NAME_OF_FILE replace for your log file
  - search_period this method search your period in log file
  ```
    a, b = counter.ok_img()
    counter.calc_size_resource_of_request(a)
    counter.calc_size_resource_of_request(b)
  ```
  - ok_img method which return two lists 
  - First with ok request of jpg resource in example list a 
  - Second with ok request of png resource in example list b
