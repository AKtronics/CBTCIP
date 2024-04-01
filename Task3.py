
'''CREATING PAYMENT RECEIPT
Creating payment receipts is a pretty common task, be it an e-commerce website or any local store for that matter.
Here, you have to create our own transaction receipts just by using python. We would be using reportlab to generate the PDFs. Generally, it comes as a built-in package but sometimes it might not be present too. If it’s not present, then simply type the following in your terminal
'''

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib import colors 

Cr1 = input("Enter first course name: ")
Dat1 = input("Enter the date of Purchase: ")
Su1 = input("Enter term of subscription: ")
Pr1 = float(input("Enter price: "))

Cr2 = input("Enter second course name: ")
Dat2 = input("Enter the date of Purchase: ")
Su2 = input("Enter term of subscription: ")
Pr2 = float(input("Enter price: "))

Cr3 = input("Enter third course name: ")
Dat3 = input("Enter the date of Purchase: ")
Su3 = input("Enter term of subscription: ")
Pr3 = float(input("Enter price: "))

subt = (Pr1 + Pr2 + Pr3)
subt = round(subt,2)

disc = (-0.2*(Pr1 + Pr2 + Pr3))
disc = round(disc,2)

tot = (Pr1 + Pr2 + Pr3)-0.2*(Pr1 + Pr2 + Pr3)
tot = round(tot,2)

table_data = [ 

	[ "Date" , "Course name", "Subscription", "Price (Rs.)" ], 
    [Dat1 , Cr1 , Su1 , str(Pr1) + "/-"],
    [Dat2 , Cr2 , Su2 , str(Pr2) + "/-"],
    [Dat3 , Cr3 , Su3 , str(Pr3) + "/-"],
    [ "Sub Total", "", "", str(subt) + "/-"], 
	[ "Discount", "", "", str(disc) + "/-"], 
	[ "Total", "", "", str(tot) + "/-"],

] 

receipt = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 


styles = getSampleStyleSheet() 


title_style = styles[ "Heading3" ] 


title_style.alignment = 1


title = Paragraph( "CipherByte Technologies" , title_style ) 


style = TableStyle( 
	[ 
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.whitesmoke ), 
		( "GRID" , ( 0, 0 ), ( 3 , 3 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 4 ), ( 6 , 6 ), 1 , colors.black ),
		( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.orange ), 
		( "TEXTCOLOR" , ( 0, 0 ), ( 3, 0 ), colors.black ),
        ( "TEXTCOLOR" , ( 0, 1 ), ( -1, -1 ), colors.darkblue ),
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.azure ), 
	] 
) 

table = Table( table_data , style = style ) 

receipt.build([ title , table ]) 
