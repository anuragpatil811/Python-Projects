##Python code for QR code generator for UPIpayments
import qrcode

#Taking UPI ID as a input
upi_id = input("Enter your UPI ID:")
#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE 

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#Creating QR Codes for each payment app 
phonepe_qr = qrcode.make(phonepe_url)
#Save the QR code to image file(optional)
phonepe_qr.save('phonepe_qr.png')
#Display the QR codes
phonepe_qr.show()