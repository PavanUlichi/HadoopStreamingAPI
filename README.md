# HadoopStreamingAPI

## Below are the instructions for data analysis on hadoop server which supports HadoopStreamingAPI

Go to home directory

First, clone these repository either using https or ssh on to the hadoop server

After successful clone, you can see both mapper.py and reducer.py programs

Then run the below command on hadoop cluster by making small modifications in  output path where you want to store  

 hadoop jar  /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input  /data/nyc/nyc-traffic.csv   -output /users-cloud-16fs/ulichitr/job-out  -mapper ~/mapper.py   -reducer ~/reducer.py  -file ~/{mapper,reducer}.py
 
After successful execution of hadoop jobs, the output statistics can be viewed in hdfs using below command
 
hadoop fs -cat /users-cloud-16fs/ulichitr/job-out/part-00000
  
here we used nyc-traffic.csv file as input and below are the text summary statistics for that data
  
AMBULANCE	3713

BICYCLE	24153

BUS	25871

FIRE TRUCK	1333

LARGE COM VEH(6 OR MORE TIRES)	27981

LIVERY VEHICLE	17775

MOTORCYCLE	10029

OTHER	51360

PASSENGER VEHICLE	1005162

PEDICAB	123

PICK-UP TRUCK	26281

SCOOTER	534

SMALL COM VEH(4 TIRES)	30048

SPORT UTILITY / STATION WAGON	363209

TAXI	63892

UNKNOWN	105481

VAN	51666
