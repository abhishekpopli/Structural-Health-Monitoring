# Structural-Health-Monitoring
Python - Matlab project for offshore ocean structures
One of my projects done in summer internship at IIT Madras in June-July 2017

**Structural Health Monitoring or Conditional Monitoring** refers to digitally monitoring the conditions of the structure. Its goal is predictive maintenance i.e., detecting and warning about any fault or machine failures with sufficient accuracy to enable repair before breakdown.<br />
To achieve this, sensor data is collected from the structure/vehicle and transferred to the desired computer for analyzing the conditions. The sensor data was stored in the SQL Database on the web server which leads to analyze the past conditions of the structure also.<br />
The following work was done in the fulfillment of the Condition monitoring:<br />
•**Live Graph:**
A Live graph of the sensors data was plotted with the actual original readings of the sensor, with the time duration between 2 sensor readings being 6.67 milliseconds. Implemented in **live_plot.py**<br />
•	**SQL Server handling for sensor data:**
The data of sensors was continuously stored on the SQL database on the server, which was used to analyze not only the present conditions but also of the past conditions of the structure.  <br />
•	**Plotting data of the past time:**
The data stored in SQL database was used to plot the hourly average sensor readings between the desired interval of hours taken input from the user. Implemented in **manual_plot_hour_data.py**  <br />
•	**GUI  designing using Tkinter:**
Python programming language was used to make the software implementing the above all said plotting of graphs. TKINTER Library of Python was used for GUI designing in the software.<br />
•	SMS notification of exceeding value of sensors
<br />
** You only need to run **plot_hour_data.py**  which automatically calls **live_plot.py**.
**Working:**
Every 6.67 millisecond, one row from excel sheet is being entered in the “sensors” table in SQL using the python program excel_sql.py discussed in the next chapter. Another python program “liveplot.py” is simultaneously executed which plots the live graph. At the starting, this program has two empty arrays which represent time and value to be plotted. So, it checks for any value in the table which has time greater than  the time the program  was started and stored those values in the two arrays and stores the time of the last row it plotted.<br />
Now, Every 6.67 millisec, this program checks for any new row entered in the table by comparing the maximum time in the table with the time of the last row it plotted. If there is any new row added, it collects those rows and appends that in the array and also, removes the same amount of rows added in the array from the starting of the array. This way a constant number of points are being plotted on the screen 
<br />
**Analyze and Visualize stored data**
The user enters the desired range of hours to see the average of each hour between that interval through graph. A seperate table is stored in the database which stores average sensor data of each hour and is updated every hour. 
<br />
The experiment for Sensor Networking was performed with accelerometer sensor used in the underwater crude extracting machine with the sensor embedded on one of its three legs and sensor’s readings were transmitted using Raspberry Microcontroller in the underwater vehicle connected wirelessly to a web server SQL database.
<br />
**The Python code for transferring data from excel sheet to the SQL database is given in excel_sql.py**
<br />
WAY2SMS  API was used to send SMS from web server to the desired phone.  It was embedded in a seperate site . The code is available in sms.py
<br />
	The WAY2SMS API receives data through GET request from the program.
<br />
	The program makes connection to the API whenever called.
<br />
