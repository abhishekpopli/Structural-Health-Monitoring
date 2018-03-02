import urllib.request
import urllib.parse as pam
y=0.62391
x=1.266
def smsdata(x,y):
	message = "hello...The reading of sensor A crossed the limits. The last exceeded value was "+str(y)+" at time "+str(x)
	url = "https://www.drsekaran-dynamics.com/sms/sendsms.php?message="+ pam.quote_plus(message)
	resp = urllib.request.urlopen(url)
	respData = resp.read()
	print(respData)
smsdata(x,y)