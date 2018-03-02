import MySQLdb
import matplotlib.pyplot as plt
from matplotlib import  style

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="secret",  # your password
                     db="abhivasu")        # name of the data base
style.use("ggplot")
cur = db.cursor()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
n,m = input("enter value of interval ").split(' ')
n=int(n)
m=int(m)
x=[]; y=[]
for i in range(n,m+1) :
    cur.execute("select value from averagedata where hour = %s",(i,))
    row = cur.fetchone()
    lastrec = row[0]
    x.append(i)
    y.append(lastrec)
ax1.plot(x, y)
plt.show()

