from re import L
from fpdf import FPDF
from datetime import date
today = date.today()
from data import generate_random_name
from data import generateRandomDate
from data import generate_random_contact
from data import generate_random_gender
from data import generate_random_address    
from data import generate_random_id    
from data import generate_random_medical_department    


list_name = ['patient name', 'patient', 'full name', 'prescribed to', 'name', 'name of patient', "patient's name"]
list_dob =['dateofbirth', 'date of birth', 'dob', 'birthdate','age']
list_contact=['mobile no', 'contact no', 'personal contact', 'phone number', 'cell phone number']
list_gender =['sex', 'gender', 'male/female', 'biological sex', 'assigned gender', 'sexual classification']
list_address=['address', 'residence', 'domicile', 'location', 'home location', 'place of residence', 'residential address', 'house address', 'street address', 'housing details']

file_path = 'my_list.txt'
list_pdf_name =[]

class PDF(FPDF):
    def header(self):
        d2 = today.strftime("%B %d, %Y")
        # Logo
        # self.image('logo1.png', 0, 0,220,18)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        
        # self.set_font("Helvetica", size=15)

        # Move to the right
        self.cell(150)
        # Title

        self.text(60,12, 'Late Baliram Kashyap Memorial Govt')

        self.text(60,20, 'Medical College Jagdalpur')

        self.text(50,28, 'BASTAR,CHHATTISGARH,Pin: 494001')

        self.text(155,5,d2)
        # Line break
        self.ln(10)

        # self.line(10,28,210,25)
        self.line(10,30,210,30)
    


    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8 
        self.set_font('Arial', 'I', 8)
        # self.image('footer.png', -1, 285,212,14)

        # Page number
        # self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def generate_pdf():
    
    
    for name in list_name :
        for dob in list_dob :
            for contact in list_contact :
                for gender in list_gender:
                    for address in list_address:
                        pdf = PDF()
                        pdf.alias_nb_pages()
                        pdf.add_page()
                        pdf.set_font('Times', 'B', 18)
                        pdf.text(10,38,"Patient Details")
                        pdf.set_font('Times', 'B', 15)
                        
                        i=47
                        file_name = generate_random_name(8)
                        pdf.text(10,i ,"patient id : "+generate_random_id())
                        pdf.text(10,i+8 , ""+name +" : "+ generate_random_name())
                        pdf.text(10,i+16,""+dob +" : "+ generateRandomDate())
                        pdf.text(10,i+24,""+contact +" : "+ generate_random_contact())
                        pdf.text(10,i+32,""+gender +" : "+ generate_random_gender())
                        pdf.text(10,i+40,""+address +" : "+ generate_random_address())

                        pdf.text(120,i, "department : "+generate_random_medical_department())
                        pdf.text(120,i+8,"Registration Number : "+ generate_random_id())
                        pdf.text(120,i+16,"Doctor's name : "+ generate_random_name())
                        pdf.text(120,i+24,"Patiet Type : "+ generate_random_name())
                        pdf.line(10,93,210,93)
                        pdf.line(10,94,210,94)
                        
                        pdf_file_name = f"""./pdfs/{file_name}.pdf"""
                        list_pdf_name.append(pdf_file_name)
                        
                        pdf.output(pdf_file_name, 'F')
    print(len(list_pdf_name))
    with open(file_path, 'w') as file:
        file.write(str(list_pdf_name))
    return
    
generate_pdf()