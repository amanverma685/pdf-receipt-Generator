from re import L
from fpdf import FPDF
from datetime import date
today = date.today()

from event import event

class PDF(FPDF):
    def header(self):
        d2 = today.strftime("%B %d, %Y")
        # Logo
        # self.image('logo1.png', 10, 10,190,18)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        
        # self.set_font("Helvetica", size=15)

        # Move to the right
        self.cell(150)
        # Title

        # self.text(80,12, 'Payment Receipt')

        self.text(155,5,d2)
        # Line break
        self.ln(10)

        # self.line(10,18,210,18)
        # self.line(10,19,210,19)
    


    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        # self.set_y(-15)
        # Arial italic 8 
        self.set_font('Arial', 'I', 8)
        self.image('footer.png',x=60, y=280, w=100, h=10)

        # Page number
        # self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def generate_pdf():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    background_image = 'back1.png'  # Specify the path to your background image
    pdf.set_font('Times', 'B', 14)
    pdf.image(background_image, x=0, y=0, w=210, h=270)  # Adjust x, y, w, h as needed
    pdf.set_font('Times', '',8)

    pdf.image('logo2.png', 15, 15,80,20)

    pdf.set_font('Times', 'B', 14)
    pdf.text(120,15,"Invoice")

    pdf.set_font('Times', '', 9)

    pdf.text(120,20,"17503 Hankar Way,Richmond,TX77407 United States")
    # pdf.text(122,22,"")
    pdf.text(120,24,"+1(346) 558-3658")
    pdf.text(120,28,"orionventuresgroupllc@gmail.com")
    pdf.text(120,32,"www.cheapvehiclesrentals.com")

    j=45
    pdf.set_font('Times', 'B', 12)
    pdf.text(10,j,"Customer Details")
    pdf.set_font('Times', '', 11)
    pdf.text(10,j+5 ,"Name : " +event.get("booking_details")['primary_driver'] )
    pdf.text(10,j+10,"Pickup : "+ event.get('booking_details')['pick_up_location'])
    pdf.text(10,j+15,"Drop-off : " + event.get('booking_details')['drop_off_location'])
    pdf.text(10,j+21,"Car Name : " + event.get('car_details')['name'] +" / "+ event.get('car_details')['type'] +" / "+ event.get('car_details')['model_year'] +" / "+ str(1 if event.get('car_details')['sitting_capacity']==None else event.get('car_details')['sitting_capacity'])+" Passengers")
    pdf.set_font('Times', 'B', 12)
    
    pdf.text(120,j,"Booking Details")
    pdf.set_font('Times', '', 11)
    pdf.text(120,j+5 ,"Booking Id : " +event.get("booking_id"))
    pdf.text(120,j+10,"Pickup Date-Time :  "+ event.get('booking_details')['trip_start_date_time'])
    pdf.text(120,j+15,"Drop-off Date-Time : " + event.get('booking_details')['trip_end_date_time'])

    pdf.set_font('Times', '', 12)

    pdf.set_font('Times', 'B', 14)
    
    pdf.text(10,j+28,"Payment Summary ")

    pdf.set_font('Times', 'B', 12)

    pdf.text(20,j+35, "Rental Duration")

    pdf.set_font('Times', '', 12)

    pdf.text(100,j+34,str(event.get('payment_details')['rental_duration']) + " Days" if event.get('payment_details')['rental_duration'] >1 else " Day" )

    pdf.line(18, j+36, 190, j+36)
    pdf.line(18,89, 190, 89)
    k=88
    l=83
    pdf.set_font('Times', 'B', 12)
    
    pdf.text(20,k, "Price Per Day")

    pdf.set_font('Times', '', 12)

    for i in range (len(event.get('payment_details')['pay_per_day'])):
        pdf.text(100,k+i*7,"$ "+ str(event.get('payment_details')['pay_per_day'][i]['no_of_day'])+"x"+ " $ "+str(event.get('payment_details')['pay_per_day'][i]['price']))
        pdf.text(170,k+i*7, "$ "+ str( event.get('payment_details')['pay_per_day'][i]['no_of_day'] * event.get('payment_details')['pay_per_day'][i]['price'])+".00")
        
    i=i+1
    pdf.line(18, l+(i)*7, 190, l+(i)*7)

    pdf.set_font('Times', 'B', 12)

    pdf.text(20,k+i*7,"Pickup Location Cost")
    
    pdf.set_font('Times', '', 12)

    pdf.text(170,k+i*7, "$ "+ str( event.get('payment_details')['pickUp_location_cost'])+".00")

    i=i+1
    pdf.line(18, l+(i)*7, 190, l+(i)*7)

    pdf.set_font('Times', 'B', 12)

    pdf.text(20,k+i*7,"Drop-off Location Cost")
    
    pdf.set_font('Times', '', 12)

    pdf.text(170,k+i*7, "$ "+ str( event.get('payment_details')['dropoff_location_cost'])+".00")
    
    i=i+1
    pdf.line(18, l+(i)*7, 190, l+(i)*7)
    
    pdf.set_font('Times', 'B', 12)

    pdf.text(20,k+i*7,"Cleaning Fee")
    
    pdf.set_font('Times', '', 12)

    pdf.text(170,k+i*7, "$ "+ str( event.get('payment_details')['cleaning_fee'])+".00")

    i=i+1
    pdf.line(18, l+(i)*7, 190, l+(i)*7)
    pdf.set_font('Times', 'B', 12)

    pdf.text(20,k+i*7, "Resources Fee")
    pdf.set_font('Times', '', 12)

    i=i+1
    for j in range (len(event.get('booking_details')['resources'])):
        
        pdf.text(20,k+i*7,str(event.get('booking_details')['resources'][j]['resource_name']))
        pdf.text(100,k+i*7,str(event.get('booking_details')['resources'][j]['resource_price'])+" x "+ str(event.get('booking_details')['resources'][j]['no_of_day']) +" ("+ str(event.get('booking_details')['resources'][j]['resource_duration'])+ ") ")
        pdf.text(170,k+i*7, "$ "+str(event.get('booking_details')['resources'][j]['total_resource_cost']) +".00")
        i=i+1
        if(k+i*7 > 280) :
            i=-5
            pdf.add_page()
            background_image = 'back1.png'  # Specify the path to your background image
            pdf.image(background_image, x=0, y=54, w=210, h=270)

    
    pdf.line(18, l+i*7, 190, l+i*7)

    pdf.set_font('Times', 'B', 12)

    pdf.text(20,k+i*7,"Admin Fee")
    pdf.text(170,k+i*7, "$ "+ str( event.get('payment_details')['admin_fee'])+".00")
    i=i+1
    pdf.line(18, l+i*7, 190, l+i*7)

    pdf.set_font('Times', 'B', 14)

    pdf.text(20,k+i*7,"Sub Total")
    pdf.text(170,k+i*7, "$ "+ str( event.get('payment_details')['net_fare'])+".00")
    i=i+1
    pdf.line(18, l+i*7, 190, l+i*7)
    pdf.set_font('Times', '', 12)


    pdf.text(20,k+i*7,"Tax" +" ("+ str( event.get('payment_details')['tax_percentage'])+" %" +") " )
    pdf.text(170,k+i*7, "$ "+ str( event.get('payment_details')['tax']))

    i=i+1
    pdf.line(18, l+i*7, 190, l+i*7)

    pdf.set_font('Times', 'B', 14)

    pdf.text(20,k+i*7,"Total Price" )
    pdf.text(170,k+i*7, "$ "+ str( event.get('payment_details')['total_fare']))
    i=i+2
    pdf.image('thnk.png',80, k+i*7, 50,50)
    
    

    pdf_file_name = "generatedPDF.pdf"
    pdf.output(pdf_file_name, 'F')

    return pdf_file_name
    
generate_pdf()