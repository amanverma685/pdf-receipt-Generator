from re import L
from fpdf import FPDF
from datetime import date
today = date.today()

from event import event


class PDF(FPDF):
    def header(self):
        d2 = today.strftime("%B %d, %Y")
        # Logo
        self.image('logo1.png', 0, 0,220,18)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)

        # Move to the right
        self.cell(150)
        # Title
        self.text(80,12, 'Payment Receipt')

        self.text(155,5,d2)
        # Line break
        self.ln(10)

        self.line(0,18,210,18)
        self.line(0,19,210,19)
    


    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8 
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def generate_pdf():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    background_image = 'background.jpeg'  # Specify the path to your background image
    pdf.set_font('Times', 'B', 14)
    # reduce_image_opacity(background_image, background_image, opacity=0.5)  # Adjust the opacity value

    pdf.image(background_image, x=0, y=18, w=210, h=297)  # Adjust x, y, w, h as needed

    
    pdf.text(4,24,"User Details:")
    pdf.set_font('Times', '', 12)
    pdf.text(4,29 ,"Name :- " +event.get("booking_details")['primary_driver'])
    pdf.text(4,34,"Pickup:- "+ event.get('booking_details')['pick_up_location'])
    pdf.text(4,39,"Drop-off:- " + event.get('booking_details')['drop_off_location'])
    pdf.text(4,44,"Car Name:- " + event.get('car_details')['name'] +" / "+ event.get('car_details')['type'] +" / "+ event.get('car_details')['model_year'] +" / "+ str(1 if event.get('car_details')['sitting_capacity']==None else event.get('car_details')['sitting_capacity'])+" Passengers")
    pdf.set_font('Times', 'B', 14)
    
    pdf.text(120,24,"Journey Details")
    pdf.set_font('Times', '', 12)
    pdf.text(120,29 ,"Booking Id :- " +event.get("booking_id"))
    pdf.text(120,34,"Pickup Date-Time:- "+ event.get('booking_details')['trip_start_date_time'])
    pdf.text(120,39,"Drop-off Date-Time :- " + event.get('booking_details')['trip_end_date_time'])

    pdf.set_font('Times', '', 12)

    pdf.set_font('Times', 'B', 14)
    
    pdf.text(4,52,"Payment Summary:-")

    pdf.set_font('Times', '', 12)

    pdf.text(4,61, "Rental Duration")

    pdf.text(100,61,str(event.get('payment_details')['rental_duration']) + " Days" if event.get('payment_details')['rental_duration'] >1 else " Day" )

    pdf.line(0, 54, 220, 54)
    pdf.line(0, 63, 220, 63)

    pdf.text(4,68, "Price Per Day")

    for i in range (len(event.get('payment_details')['pay_per_day'])):
        pdf.text(100,68+i*7,"$ "+ str(event.get('payment_details')['pay_per_day'][i]['no_of_day'])+"x"+ " $ "+str(event.get('payment_details')['pay_per_day'][i]['price']))
        pdf.text(185,68+i*7, "$ "+ str( event.get('payment_details')['pay_per_day'][i]['no_of_day'] * event.get('payment_details')['pay_per_day'][i]['price'])+".00")
        
    i=i+1
    pdf.line(0, 63+(i)*7, 220, 63+(i)*7)

    pdf.text(4,68+i*7,"Pickup Location Cost")
    pdf.text(185,68+i*7, "$ "+ str( event.get('payment_details')['pickUp_location_cost'])+".00")

    i=i+1
    pdf.line(0, 63+(i)*7, 220, 63+(i)*7)

    pdf.text(4,68+i*7,"Drop-off Location Cost")
    pdf.text(185,68+i*7, "$ "+ str( event.get('payment_details')['dropoff_location_cost'])+".00")
    
    i=i+1
    pdf.line(0, 63+(i)*7, 220, 63+(i)*7)
    
    pdf.text(4,68+i*7,"Cleaning Fee")
    pdf.text(185,68+i*7, "$ "+ str( event.get('payment_details')['cleaning_fee'])+".00")

    i=i+1
    pdf.line(0, 63+(i)*7, 220, 63+(i)*7)

    pdf.text(4,68+i*7, "Resources Fee")
    i=i+1
    for j in range (len(event.get('booking_details')['resources'])):
        
        pdf.text(4,68+i*7,str(event.get('booking_details')['resources'][j]['resource_name']))
        pdf.text(100,68+i*7,str(event.get('booking_details')['resources'][j]['resource_price'])+" x "+ str(event.get('booking_details')['resources'][j]['no_of_day']) +" ("+ str(event.get('booking_details')['resources'][j]['resource_duration'])+ ") ")
        pdf.text(185,68+i*7, "$ "+str(event.get('booking_details')['resources'][j]['total_resource_cost']) +".00")
        i=i+1
        if(68+i*7 > 280) :
            i=-5
            pdf.add_page()

        
    pdf.line(0, 63+i*7, 220, 63+i*7)

    pdf.text(4,68+i*7,"Admin Fee")
    pdf.text(185,68+i*7, "$ "+ str( event.get('payment_details')['admin_fee'])+".00")
    i=i+1
    pdf.line(0, 63+i*7, 220, 63+i*7)

    pdf.set_font('Times', 'B', 13)

    pdf.text(4,68+i*7,"Sub Total")
    pdf.text(185,68+i*7, "$ "+ str( event.get('payment_details')['net_fare'])+".00")
    i=i+1
    pdf.line(0, 63+i*7, 220, 63+i*7)
    pdf.set_font('Times', '', 12)


    pdf.text(4,68+i*7,"Tax" +" ("+ str( event.get('payment_details')['tax_percentage'])+" %" +") " )
    pdf.text(185,68+i*7, "$ "+ str( event.get('payment_details')['tax']))

    i=i+1
    pdf.line(0, 63+i*7, 220, 63+i*7)

    pdf.set_font('Times', 'B', 14)

    pdf.text(4,68+i*7,"Total Price" )
    pdf.text(185,68+i*7, "$ "+ str( event.get('payment_details')['total_fare']))
    i=i+2
    pdf.image('thanku.jpg',80, 68+i*7, 50,50)
    
    

    pdf_file_name = "generatedPDF.pdf"
    pdf.output(pdf_file_name, 'F')

    return pdf_file_name
    
generate_pdf()