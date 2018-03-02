import MySQLdb
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import urllib.request
import urllib.parse
from matplotlib import  style

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="secret",  # your password
                     db="abhivasu")        # name of the data base
style.use("ggplot")
cur = db.cursor()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
lasttime = 0.0
xar = []
yar = []
style.use("ggplot")
#first time // initailising
cur.execute("SELECT max(milisec) FROM sensors;")
row = cur.fetchone()
lastrec= row[0]
if  lastrec >= lasttime :
    row = cur.execute("""SELECT * FROM sensors where milisec > %s """, (lasttime,))
    for row in cur.fetchall():
        #if len(row) > 1 :
        x, y = row[0], row[1]
        xar.append(x)
        yar.append(y)
    size1 = int(len(xar))
    del xar[:size1-20]
    del yar[:size1-20]
#lasttime = lastrec

ax1.plot(xar, yar)
'''
size1 = int(len(xar)/2)
size2 = int(len(yar)/2)
del xar[:size1]
del yar[:size2]

def func(x,y):
    message = "The reading of sensor crossed the limits. The exceeded value is " +str(y) +"   at time  " + str(x)
    url = "https://www.drsekaran-dynamics.com/sms/sendsms.php?message=" + message
    resp = urllib.request.urlopen(url)
    respData = resp.read()
    print(respData)
'''
def animate(i):

    db.begin()
    global lasttime

    cur.execute("select max(milisec) FROM sensors;")
    row = cur.fetchone()
    lastrec = row[0]
    if  lastrec  > lasttime :
        cur.execute("""select * FROM sensors where milisec >%s """ , (lasttime,))

        n = cur.rowcount
        for row in cur.fetchall():
            x, y = row[0],row[1]
            xar.append(x)
            yar.append(y)

        lasttime = x
            #n+=1
        del xar[:n]
        del yar[:n]
        ax1.clear()
        ax1.plot(xar, yar)
        plt.ylim(
            [-0.2, 0.2])

        time.sleep(50.0 / 1000.0)

ani = animation.FuncAnimation(fig, animate,frames=10, interval=200)
plt.show()