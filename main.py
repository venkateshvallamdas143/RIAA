from fpdf import FPDF,HTMLMixin
from os.path import join
from os import getcwd
from PIL import ImageColor
import sys
import os
import PyPDF2
import math
from datetime import date

cwd = os.path.dirname(__file__) 

pwd = os.getcwd()

class MyFPDF(FPDF, HTMLMixin):
    pass

def px2MM(val):
  # Sauce: https://www.figma.com/community/plugin/841435609952260079/Unit-Converter
  return val * (25.4 / 72)

def mm2PX(val):
  # Sauce: https://www.figma.com/community/plugin/841435609952260079/Unit-Converter
  return val * (72 / 25.4)

def hex2RGB(val):
  return list(ImageColor.getcolor(val, "RGB"))

pdf= FPDF('P','mm','A4')


# If saving path which is /pdf not exists. Create one.
pdf_exists = os.path.exists(join(pwd,"generated_pdf")) and os.path.isdir(join(pwd,"generated_pdf"))
if pdf_exists != True:
    print(pdf_exists)
    os.mkdir(join(pwd,"generated_pdf"))

"""Deleting Pkl"""
try:
    LGpkl_file_path = os.path.join(cwd,'assets','fonts','Calibri')
    del_pkl = [x for x in os.listdir(LGpkl_file_path) if x.endswith('.pkl')]
    for file in del_pkl:os.remove(os.path.join(LGpkl_file_path,file))
    print('Deleting all .pkl files....')
except FileNotFoundError:
    print('.pkl files not exists in assets folder. No Need To Delete')
"""Deleting Pkl"""


def pdf_creator(pdf):
    pdf = FPDF()
    pdf.set_auto_page_break(False)
    
    # cwd = os.getcwd()
    pdf.add_font('Calibri', "",join(cwd,'assets','fonts','Calibri','Calibri.ttf'),uni=True)
    pdf.add_font('CalibriBold', "",join(cwd,'assets','fonts','Calibri','calibrib.ttf'),uni=True)

    page1(pdf)
    page2(pdf)
    page3(pdf)
    page4(pdf)
    page5(pdf)
    page6(pdf)
    page7(pdf)
    page8(pdf)
    page9(pdf)
    page10(pdf)
    page11(pdf)

    filename = sys.argv[6]
    # directory = join(sys.argv[7],filename)
    directory = join(pwd,'generated_pdf',filename)
    

    pdf.output(directory)
    print('PDF Genrated Inside ', join(pwd,"generated_pdf") ,"Folder")
    
def img_add(pdf):
    img = join(cwd,'assets','images','stampandsign2.jpg')
    pdf.image(img,px2MM(435), px2MM(770),px2MM(120), px2MM(55))

def page1(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'DF')
    
    y = mm2PX(pdf.get_y()) + 12
    pdf.set_xy(px2MM(0), px2MM(y + 32))
    pdf.set_font('CalibriBold', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(600), px2MM(16),'Member Agreement Synopsis',align='C')
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(80), px2MM(y+16))
    pdf.set_font('CalibriBold', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(110), px2MM(14),"Parties",align='L')
    
    y = mm2PX(pdf.get_y())
    
    pdf.set_xy(px2MM(80), px2MM(y+22))
    pdf.set_font('Calibri', size=11)
    pdf.cell(px2MM(45), px2MM(14),f"The agreement is between 1 Finance (SEBI Registered Investment Advisor) and you (the Member).")
   
    y = mm2PX(pdf.get_y())
    pdf.set_font('CalibriBold', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.set_xy(px2MM(80), px2MM(y+22))
    pdf.cell(px2MM(110), px2MM(14),"Appointment",align='L')
    
    
    y = mm2PX(pdf.get_y())+22
    pdf.set_font('Calibri', size=11)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(354), px2MM(14),"The member appoints 1 Finance to provide financial advisory services as per RIA regulations.")

    y = mm2PX(pdf.get_y())
    pdf.set_font('CalibriBold', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.set_xy(px2MM(80), px2MM(y+22))
    pdf.cell(px2MM(110), px2MM(14),"Services",align='L')
    
    y = mm2PX(pdf.get_y())+22
    pdf.set_font('Calibri', size=11)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(45), px2MM(14),"The agreement specifies the details of the services that we offer exclusively to the members.")

    y = mm2PX(pdf.get_y())
    pdf.set_font('CalibriBold', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.set_xy(px2MM(80), px2MM(y+20))
    pdf.cell(px2MM(110), px2MM(14),"Fees",align='L')

    y = mm2PX(pdf.get_y())+22
    pdf.set_font('Calibri', size=11)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(45), px2MM(14),"A flat fee of INR 2499.00 per consultation")

    y = mm2PX(pdf.get_y())
    pdf.set_font('CalibriBold', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.set_xy(px2MM(80), px2MM(y + 20))
    pdf.cell(px2MM(110), px2MM(14),"Consent",align='L')
    
    y = mm2PX(pdf.get_y())+22
    pdf.set_font('Calibri', size=11)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(450), px2MM(14),"The member consents to availing services and agreeing to the terms and conditions of the agreement.")

    y = mm2PX(pdf.get_y())
    pdf.set_font('CalibriBold', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.set_xy(px2MM(80), px2MM(y + 8))
    pdf.cell(px2MM(110), px2MM(14),"Confidentiality",align='L')
    
    y = mm2PX(pdf.get_y())+22
    pdf.set_font('Calibri', size=11)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(45), px2MM(14),"The agreement binds 1 Finance to keep the member's data confidential and safe.")

    y = mm2PX(pdf.get_y())
    pdf.set_font('CalibriBold', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.set_xy(px2MM(80), px2MM(y+20))
    pdf.cell(px2MM(110), px2MM(14),"Termination & arbitration",align='L')
    
    y = mm2PX(pdf.get_y())+18
    pdf.set_font('Calibri', size=11)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(450), px2MM(14),"You have the right to terminate this agreement without specifying any reason, and if there is any dispute, you can settle it through Arbitration.")

def page2(pdf):
    
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'DF')
    
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y+38))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"1 Finance Private Limited, a registered investment advisor with SEBI Registration No. INA000017523",align='L')
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"having {' '}corporate {' '}office at {' '}Unit No. {' '}1101{'  '} &{' '} {' '}{' '}1102,{' '} {' '}11th{' '} Floor, {' '}B-Wing,{' '} Lotus{' '} Corporate{' '} Park,",align='L')
    
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"Goregaon (E), Mumbai-400063 and registered office at{' '} ‘Marwadi Financial Plaza’, {' '}Nana Mava Main",align='L')
    
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"Road, Off {' '} 150ft Ring Road, Rajkot- 360001, {' '} Gujarat, (hereinafter{' '}  referred to as the “INVESTMENT",align='L')
    
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"ADVISOR” or “1 FINANCE” which expression shall unless excluded by or repugnant to the context,be",align='L')
    
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"deemed to include its administrators and permitted assigns) of the FIRST PART",align='L')
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 28))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"1 Finance {' '} provides{' '}  financial{' '}  advisory{' '}{' '}  services{' '}  through{' '}  its {' '} mobile{' '}  application{' '}  and{' '}website,",align='L')
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"www.1finance.co.in, under the brand name of 1 Finance.",align='L')
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 28))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"And",align='L')
    
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 28))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"The Client ({' '} Hereinafter {' '} referred to as the “CLIENT / Member” which expression shall, unless  it be",align='L')
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"repugnant{' '}  to{' '}  the context  or be deemed to mean and include  its administrators{' '}  and{' '}  permitted",align='L')
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"assigns), of the SECOND PART;",align='L')


    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 28))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"Both{' '}{' '} 1{' '} Finance{' '} and the{' '}{' '} client{' '}{' '} shall{' '}{' '} also{' '}{' '} hereinafter{' '}{' '} be{' '} individually{' '}referred{' '}{' '} to as party and",align='L')
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"collectively as parties.",align='L')

    
        
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 22))
    pdf.set_font('CalibriBold', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"Definitions:",align='L')
    
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 22))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"“Investment Advisor” or “Investment Adviser” means any person, who for consideration, is engaged",align='L')
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"""in{' '} the business of providing{' '} investment{' '} advice to clients or other persons or groups of persons and""",align='L')
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"""includes{' '}{' '} any{' '}{' '} person{' '} who holds{' '}{' '} out {' '}himself as{' '}{' '} an {' '}investment {' '}advisor{' '}/{' '}{' '}investment adviser, by""",align='L')
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"""whatever name called;""",align='L')
    
    # Definitions End...
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 22))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"""“Client {' '}or Member” {' '}means{' '} any{' '} individual, {' '}group{' '} of{' '} individuals, {' '}partnership, {' '}trust, or{' '} company,""",align='L')    

    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.set_font('Calibri', size=11)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(450), px2MM(14),f"""including, without limit, a fund for whom the advisor acts as an investment advisor.""",align='L')    


    # Main Para End ...

    # y = mm2PX(pdf.get_y())+28
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y + 28))
    pdf.cell(px2MM(10), px2MM(14),"1.") 

    y = mm2PX(pdf.get_y())
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(420), px2MM(14),"Appointment of the Investment Advisor")
    
    y = mm2PX(pdf.get_y())+22
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"1.1")
    
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""In accordance with the applicable laws, the client hereby appoints, entirely at his / her / its risk, the investment advisor to provide the required services in accordance with the terms and conditions of the agreement as mandated under Regulation 19(1)(d) of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013.""")
    
    
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.cell(px2MM(10), px2MM(14),"2.") 
    
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(80), px2MM(y + 14))
    pdf.cell(px2MM(420), px2MM(14),"Consent of the Client")
    
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y + 22))
    pdf.cell(px2MM(420), px2MM(14),"The client hereby consents to the following:")
    
    y = mm2PX(pdf.get_y())+22
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"2.1")
    
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""I / We have read and understood the terms and conditions of investment advisory services provided by the investment advisor along with the fee structure and mechanism for charging and payment of fee.""")
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 10))
    pdf.cell(px2MM(10), px2MM(14),"2.2")
    
    pdf.set_xy(px2MM(90), px2MM(y + 10))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Based on our written request to the investment advisor, an opportunity was provided by the investment advisor to ask questions and interact with the ‘person(s) associated with the investment advice.""")
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 10))
    pdf.cell(px2MM(10), px2MM(14),"2.3")

    pdf.set_xy(px2MM(90), px2MM(y + 10))
    pdf.multi_cell(px2MM(400), px2MM(14),"""That my risk profiling is completed.""")
    
    # 3
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y + 10))
    pdf.cell(px2MM(10), px2MM(14),"3.") 

    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(80), px2MM(y + 10))
    pdf.cell(px2MM(430), px2MM(14),"Declaration from the Investment Advisor")

    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y + 22))
    pdf.cell(px2MM(430), px2MM(14),"Investment advisor hereby declares the following:")

def page3(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')
    

    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y + 38))
    pdf.cell(px2MM(10), px2MM(14),"3.1")
    

    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y + 38))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Investment advisor shall neither render any investment advice nor charge any fee until the client has signed this agreement.""")
    
     
    y = mm2PX(pdf.get_y())+8
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"3.2")
    
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Investment advisor shall not manage funds and securities on behalf of the client and it shall only receive such sums of monies from the client as are necessary to discharge the client’s liability towards fees owed to the investment advisor.""")

    
    
    y = mm2PX(pdf.get_y())+8
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"3.3")
    
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Investment advisor shall not, in the course of performing its services to the client, hold out any investment advice implying any assured returns or minimum returns or target return or percentage accuracy or service provision till achievement of target returns or any other nomenclature that gives the impression to the client that the investment advice is risk-free and/or not susceptible to market risks and or that it can generate returns with any level of assurance.""")

    
    


    # # 4


    y = mm2PX(pdf.get_y())+8
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"4.") 

    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Fees Specified under the Investment Advisor Regulations and Relevant Circulars Issued Thereunder""")

    #Bullets
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70),px2MM(y + 10))
    pdf.cell(px2MM(10),px2MM(14),'4.1')

    point4_para1 = """The Client(s) shall pay the investment advisor fees for the services rendered as provided in the 1 Finance Mobile Application. The fees can be paid using the payment modes available on the platform."""
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),point4_para1)
    

    #Bullets
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70),px2MM(y + 10))
    pdf.cell(px2MM(10),px2MM(14),'4.2')

    point4_para2 = """In accordance with SEBI (Investment Advisor) regulations, circulars, and guidelines, the maximum fees that can be charged to clients under Asset under Advice mode shall not exceed 2.5 percent of AUA per annum per client and under fixed fee – shall not exceed INR 1,25,000/- per annum per Client."""
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),point4_para2)
    

    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"5.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.cell(px2MM(430), px2MM(14),"""Fees Charged to the Client""")
    
    pdf.set_font('Calibri',size=11) 
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 28))
    pdf.cell(px2MM(10), px2MM(14),"5.1")
    
    y = mm2PX(pdf.get_y()) 
    pdf.set_xy(px2MM(70), px2MM(y + 28))
    pdf.cell(px2MM(10), px2MM(14),"5.2")
    
    y = mm2PX(pdf.get_y()) + 70
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"5.3")
    
    # y = mm2PX(pdf.get_y()) + 56
    # pdf.set_xy(px2MM(70), px2MM(y))
    # pdf.cell(px2MM(10), px2MM(14),"5.4")
    
    pt5_text = ("""The client agrees to pay the advisory fee in the manner specified above.""",
                """Fees must be paid in any manner that allows for the traceability of the fund /amount paid. The modalities of payments may include account payee crossed cheques/Demand drafts, as well as a direct credit to bank accounts via NEFT/RTGS/IMPS/UPI or any other manner specified by SEBI from time to time. The fees, however, must not be paid in cash.""",
                """In the event of premature termination of the advisory services as per the terms of the agreement, the client shall be refunded the fees for the unexpired period. However, investment advisor may retain a maximum advisory fee of one-quarter.""")
    
    y = mm2PX(pdf.get_y()) - 28 - 70
    # y = mm2PX(pdf.get_y())+28
    for i in range(3):
        if i == 4:
            pdf.set_xy(px2MM(90), px2MM(y))
            pdf.multi_cell(px2MM(430), px2MM(14),pt5_text[i])
            y = mm2PX(pdf.get_y())+14
        else:
            pdf.set_xy(px2MM(90), px2MM(y))
            pdf.multi_cell(px2MM(430), px2MM(14),pt5_text[i])
            y = mm2PX(pdf.get_y())+14
        
        

    # 6 Point
    y = mm2PX(pdf.get_y())
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.cell(px2MM(10), px2MM(14),"6.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y + 14))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Scope of Services""")
    
    pt6_text = """Defining the Financial Behaviour Score of the client."""
    
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y + 14))
    pdf.multi_cell(px2MM(430), px2MM(14),pt6_text)

    
    pdf.set_xy(px2MM(70), px2MM(y + 14))
    pdf.cell(px2MM(10), px2MM(14),f"6.1")


    pt6_text = (
                """Defining the important financial ratios for the client.""",
                """Aggregation of the client Assets & liability under 1View.""",
    )
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 22))
    pdf.cell(px2MM(10), px2MM(14),f"6.2")
    y = mm2PX(pdf.get_y())

    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),pt6_text[0])
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 8))
    pdf.cell(px2MM(10), px2MM(14),f"6.3")

    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y + 8))
    pdf.cell(px2MM(430), px2MM(14),pt6_text[1])
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 22))
    pdf.cell(px2MM(10), px2MM(14),f"6.4")

    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y + 22))
    pdf.multi_cell(px2MM(430), px2MM(14),"Providing the overall financial plan along with the financial advisory on the various Financial Instruments.")

    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 8))
    pdf.cell(px2MM(10), px2MM(14),f"6.5")

    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y + 8))
    pdf.multi_cell(px2MM(430), px2MM(14),"The client shall be provided with a risk profile based on the set of questions and other information of a client, required for providing the investment advisory.")

    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(70), px2MM(y + 8))
    pdf.cell(px2MM(10), px2MM(14),f"6.6")

    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y + 8))
    pdf.multi_cell(px2MM(430), px2MM(14),"The advisory, financial plan, financial behaviour score, and recommendation will be provided only to the client.")

def page4(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')
    
    pt6_text = (
                """The client has sole discretion to decide on whether to act on the advice of the investment advisor or not based on the client’s own independent assessment of risk and reward of the investment. The investment advisor shall have no rights, power or responsibility, or any obligation to ensure that the client act upon the advice of the investment advisor.""",
                """The investment advisor shall use its best judgement and efforts in rendering the advice to the client under this agreement and in the performance of all its duties under this agreement""",
                """The investment advisor along with its promoter, director, or employee will never execute any transaction on behalf of the client nor will represent a client in any way for any negotiation or transaction of purchase or sale of securities or any assets. The client will be solely responsible for the execution of advice rendered by the investment advisor. """,
                """ The services rendered by the investment advisor shall be subject to the activities permitted under the Securities and Exchange Board of India (investment advisors) regulation, 2013.""",
                )
    y = mm2PX(pdf.get_y())+22
    pdf.set_font('Calibri',size=11)
    for i in range(1,5):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"6.{i+6}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt6_text[i-5])
        
        y = mm2PX(pdf.get_y())+14

    #####
        
    #Point 7
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=11)

    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"7.")
    
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Duties & Functions of the Investment Advisor""")

    
    """Uncomment This"""
    pt7_text = (
        """Investment advisor shall be in compliance with the SEBI (Investment Advisor) Regulations, 2013 and its amendments, rules, circulars, and notifications. """,
        """Investment advisor shall be in compliance with the eligibility criteria as specified under the IA Regulations at all times. """,
        """Investment advisor shall conduct an audit as per the SEBI (Investment Advisor) Regulations, 2013. """,
        """Investment advisor shall provide the report to the client on potential and current investments.""",
        """Investment advisor shall be responsible for the risk assessment procedure of the client including their risk capacity and risk aversion before offering any recommendation or advice to the client.""",
        f"""Investment advisor shall provide investment advisory services to the client during the term of this agreement on investment in all financial/investment products under all regulated authorities as is permitted under applicable laws and regulations governing investment advisor. The services rendered by the investment advisor are non-binding in nature and the final decision on the type{' '} of instruments; the proportion {' '}of exposure{' '} and the tenure of the investments shall be taken by the client at their sole discretion."""
    )

    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=11)
    # for i in range(1,8): # OG
    for i in range(1,7):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"7.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt7_text[i-1])
        y = mm2PX(pdf.get_y())+10
    """Uncomment This"""
    pt7_text2 = (
        """Investment advisor shall act in a fiduciary capacity as one of the advisers to the client with respect to managing its investment-related portfolio holistically. The investment-advisor shall act in a bona fide manner for the benefit and in the interest of the client.""",
        """Investment advisor shall maintain records of client-wise KYC, advice, risk assessment, analysis reports of investment advice and suitability, terms and conditions document, the rationale of advice, related books of accounts, and register containing a list of clients along with dated investment advice in compliance with the SEBI (Investment Advisors) Regulations, 2013.""",
        """Investment advisor undertakes to abide by the Code of Conduct as specified in the Third Schedule of the SEBI (Investment Advisors) Regulations, 2013."""
    )
      
    y = mm2PX(pdf.get_y())+12
    pdf.set_font('Calibri',size=11)
    # for i in range(8,10):
    for i in range(8,11):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"7.{i - 1}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt7_text2[i-8])
        
        y = mm2PX(pdf.get_y())+10

    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"8.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Investment Objectives and Guidelines""")

def page5(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')


    pt8_text = (
        """Investment advisor undertakes to recommend direct implementation of advice i.e. through direct schemes/direct codes,and other client specifications/restrictions on investments, if any.""",
        """The investment advisor shall recommend and advise the client based on the risk profile of the client. The client can choose on their own any other investment product which is not recommended as per the risk profile.""",
        """The client shall take independent advice of its own from an independent tax advisor on the impact of taxation in the investment advice given by the investment advisor."""
    )
    
    pdf.set_font('Calibri',size=11)
    y = mm2PX(pdf.get_y())+40
    for i in range(1,4):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"8.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt8_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
        
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"9.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Risk Factors""")

    #Bullets
    y = mm2PX(pdf.get_y())+6
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.1')
    
    y = mm2PX(pdf.get_y()) + 70
    pdf.set_xy(px2MM(70),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.2')
    
    y = mm2PX(pdf.get_y()) + 56
    pdf.set_xy(px2MM(70),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.3')
    
    y = mm2PX(pdf.get_y()) + 56
    pdf.set_xy(px2MM(70),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.4')
    
    y = mm2PX(pdf.get_y()) + 84
    pdf.set_xy(px2MM(70),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.5')
    
    pt9_text= (
        """The investment advisor will not be liable to the client for any loss or damage financially or otherwise due to any of the advice or recommendation by the investment advisor to the client. The client also expressly agrees not to hold the investment advisor liable for any financial loss or otherwise.""",
        """The investments are subject to market risks, and there is no assurance or guarantee that the goal of the investments will be met. Additionally, the investment advisor's past performance does not ensure its future success.""",
        """Changes in government regulations, general interest rate levels, and hazards related to trading volume, liquidity, and settlement systems in the equities and debt markets could all have an impact on performance of the investments/products.""",
        """Investments in the products that the clients have chosen are subject to a wide range of risks, including but not limited to the economic slowdown, stock market volatility and illiquidity, poor corporate performance, changes in the government's and its policies, economic policies, acts of God, acts of war, civil unrest, sovereign action, and/or other events that are beyond the control of the investment advisor or any of its associates.""",
        """In no way do the names of the products or the types of investments imply their prospects or returns. The performance of specific businesses, alterations in the market, and industry-specific and macroeconomic issues all have the potential to negatively impact the performance of the invested asset."""
    )
    y = mm2PX(pdf.get_y()) - 70 - 56 - 56 - 84
    pdf.set_font('Calibri',size=11)
    for i in range(5):
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt9_text[i])
        y = mm2PX(pdf.get_y())+14
    

    
    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"10.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Validity of Advisory Services""")

    pt10_text = (
        """The advisory service agreement will be valid from the date of signing this agreement.""",
        """The agreement will be auto renewed subject to the payment of fees by the client.""",
        """The client or the investment advisor can terminate this agreement by giving 30 days’ notice to the other party."""
    )
    pdf.set_font('Calibri',size=10)
    # y = mm2PX(pdf.get_y())+32 #Og
    y = mm2PX(pdf.get_y())+10
    for i in range(1,4):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"10.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt10_text[i-1])
        
        y = mm2PX(pdf.get_y())+5
    
    y = mm2PX(pdf.get_y())+12
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"11.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Amendments""")

    pdf.set_font('Calibri',size=11)
    y = mm2PX(pdf.get_y())+12
    
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),f"11.1")

    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""With the mutual consent of both parties the agreement can be amended and after amendment, the amended clause shall form a part of this agreement and constitute a legal binding between the parties.""")

    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"12.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Termination""")

    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(mm2PX(pdf.get_y())+8))
    pdf.multi_cell(px2MM(430), px2MM(14),"This agreement may be terminated under the following circumstances:")
    
def page6(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')

        
    y = mm2PX(pdf.get_y())+38
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"12.1")
    
    pdf.set_xy(px2MM(92), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"Voluntary termination: Either party may terminate this agreement by giving 30 days prior written notice to another party without stating any specific reason for termination.")
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"12.2")
    
    pdf.set_xy(px2MM(92), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(12),"""Mandatory termination by client: client can mandatorily terminate this agreement without giving anynotice to the investment advisor upon the occurrence of any of the following events:""")
    
    chr = ('i.','ii.','iii.','iv.')
    texts = (
        """Any breach of terms by the investment advisor""",
        """If the advisor is barred by any government authority or SEBI or by order of the court to not act as an investment advisor.""",
        """If the investment advisor files for insolvency or becomes insolvent or enters into liquidation.""",
        """If the investment advisor ceases to hold the statutory license required to provide the service of investment advisory."""
    )
    y = mm2PX(pdf.get_y())+14
    for i in range(4):
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(16), px2MM(14),chr[i],border=0)
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(430 - 15), px2MM(14),texts[i])
        
        y = mm2PX(pdf.get_y())+10
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"12.3")
    
    pdf.set_xy(px2MM(95), px2MM(y))
    pdf.multi_cell(px2MM(425), px2MM(12),"""Mandatory termination by investment advisor: Investment advisor can terminate this agreement without giving any notice to the client upon the occurrence of any of the following events:""")
    
    texts = (
        """If the client commits a breach of any of the terms and conditions of this agreement.""",
        """If the client becomes insolvent or files for insolvency or enters into a liquidation""",
        """If the client gets barred or restricted by any of the regulatory bodies including SEBI."""
    )  
    y = mm2PX(pdf.get_y())+10
    for i in range(3):
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(16), px2MM(14),chr[i],border=0)
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(430 - 15), px2MM(14),texts[i]) 
        
        y = mm2PX(pdf.get_y())+10
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"12.4")
    
    pdf.set_xy(px2MM(93), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""In the event of suspension of the registration certificate of the investment advisor by SEBI, the client may choose to terminate this agreement.""")

    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"12.5")
    
    pdf.set_xy(px2MM(92), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""In the event the client chooses to delete the account/profile from the 1 Finance Mobile Application, the deletion of the account/profile will be treated as the closure of the agreement.""")
    

    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"13.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Implications of Amendments and Termination""")

    pdf.set_font('Calibri',size=11)
    y = mm2PX(pdf.get_y())+10
    
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(16), px2MM(14),f"13.1")
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),f""" Notwithstanding any such termination,{' '} all rights, liabilities,{' '} and obligations of the parties arising out of or in respect of transactions entered into prior to the termination of this relationship shall continue to subsist and vest in/be binding on the respective parties or his/its respective heirs, executors, administrators, legal representatives or successors, as the case may be;""")

    pt13_text = (
        """In case the clients are not satisfied with the services being provided by the investment advisor and wish to terminate/ stop investment advisory services, the client shall have a right to terminate the investment advisory relationship at any time subject (adhering to termination clause of this agreement) to refund of advisory fee after deducting one-quarter fee as breakage fee in case the termination is initiated by the clients.""",
        """ In case the investment advisor transfers/sells/assigns its business to any other third party in such event the investment advisor will ensure that the client is provided the services by such new assignee / transferee on the same terms and conditions as stipulated in this agreement.""",
        """ If the termination is due to suspension/cancellation of registration or due to any other action taken by other regulatory body/government authority then the fees will be refunded on a pro-rata basis."""
    )
    y = mm2PX(pdf.get_y())+10
    for i in range(2,5):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"13.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt13_text[i-2])
        
        y = mm2PX(pdf.get_y())+10
    
def page7(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')

    
    pdf.set_font('Calibri',size=11)
    y = mm2PX(pdf.get_y())+38
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(16), px2MM(14),f"13.5")
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),f""" The investment advisor would provide transition support, if requested by the client and
subsequently approved by management, to the client in the event of termination.""")

   
    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('Calibri',size=11)
    pdf.cell(px2MM(10), px2MM(14),"14.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Relationship with Related Parties""")
    
    pt14_text=(
        """ Investment advisor will carry out its activities independently at arm's-length, from all other activities performed by the investment advisor or by any of the investment advisor's group companies.""",
        """ Investment advisor does not have any conflict of interest of the investment advisory activities with its relationship with related parties, such conflict of interest shall be disclosed to the client as and when they arise."""
    )
    pdf.set_font('Calibri',size=11)
    y = mm2PX(pdf.get_y())+10

    for i in range(1,3):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(16), px2MM(14),f"14.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt14_text[i-1])
        
        y = mm2PX(pdf.get_y())+8
        
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('Calibri',size=10)
    pdf.cell(px2MM(10), px2MM(14),"15.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Investment Advisor Engaged in Other Activities""")
    
    pt15_text=(
        """The investment advisor hereby represents that it shall not provide to the client any commission-based distribution services, for securities and investment products, either directly or through its group companies.""",
        """The investment advisor hereby confirms that it shall not provide the investment advisory services for securities and investment products directly or through its group companies to the client who is availing of any commission-based distribution service."""
    )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    for i in range(1,3):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(16), px2MM(14),f"15.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt15_text[i-1])
        
        y = mm2PX(pdf.get_y())+4
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('Calibri',size=11)
    pdf.cell(px2MM(14), px2MM(14),"16.")
    
    pdf.set_font('CalibriBold', size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""No Right to Seek Power of Attorney""")
    
    y = mm2PX(pdf.get_y())+6
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"Investment advisor clearly declares that it shall not seek any power of attorney or authorizations from its clients for the implementation of investment advice.")

    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(14), px2MM(14),"17.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""Representation to Client""")

    point17_text = """The investment advisor represents to the client that it will take all consents and permissions from the client prior to undertaking any actions in relation to the securities or investment product advised by the investment advisor.""" 
    y = mm2PX(pdf.get_y())+6
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),point17_text)

    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"18.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""No Conflict of Interest""")

       
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""The investment advisor does hereby disclose that it does not have any conflict of interest with the client as on date and will disclose any such conflict of interest to the client as and when they arise. The investment advisor also declares that it will not derive any direct or indirect benefit out of the client’s securities or investment product.""")

     
 
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"19.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Maintenance of Accounts and Confidentiality""")

    pt19_text=(
        """ Investment advisor shall be responsible for maintenance of client accounts and data as mandated under the SEBI (Investment Advisors) Regulations, 2013. """,
        """ Investment advisor shall not divulge any confidential information about its client, which has come to its knowledge, without taking prior permission of its client, except where such disclosures are required to be made in compliance with any law for the time being in force.""",
        """ The client agrees and acknowledges that, pursuant to this agreement or otherwise, the investment advisor may receive confidential information about the client."""
    )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    for i in range(1,4):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"19.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt19_text[i-1])
        
        y = mm2PX(pdf.get_y())+10
    
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(12), px2MM(14),"20.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Liability of Investment Advisor""")

def page8(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')
   
    #Bullets
    pdf.set_font('Calibri',size=11)
    y = mm2PX(pdf.get_y()) + 38
    pdf.set_xy(px2MM(70),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'20.1')
    
   
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),""" It is hereby agreed by the client that the investment advisor shall not incur any liability by reason of any loss, which a client may suffer by reason of any depletion in the value of the assets under advice, which may result by reason of fluctuation in asset value, or by reason of non-performance or under-performance of the securities/funds or any other market conditions.""")
    
    #BULLETS
    y = mm2PX(pdf.get_y()) + 10
    pdf.set_xy(px2MM(70),px2MM(y))
    pdf.cell(px2MM(14),px2MM(14),'20.2')

    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),""" The client hereby understands that the responsibility of an investment advisor is to provide financial advice that is best suited to the client based on the information and details of a client available with an investment advisor. Client relying on the advice of an investment advisor is solely a decision of the client.""")
       
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"21.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Representations and Covenants""") 

    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"21.1")
    
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),""" The parties hereto represent, warrant and covenant to each other as under:""")
    
    chr = ('i.','ii.','iii.','iv.')
    # chr = ('a.','b.','iii.','iv.')
    texts = (
       """Each party has the relevant power, capacity, and authority to execute, deliver and perform this agreement and has taken necessary action to authorise the execution and performance of this agreement.""",
       """Each party has required approval, license, permissions, and clearances which are necessary and required for entering into this agreement.""",
       """The investment advisor represents the client, that the investment advisor has the requisite skills, knowledge, experience, infrastructure, and capabilities along with the experienced and trained persons who have required qualification and skill set for performing the functions mentioned in this agreement."""
    )
    y = mm2PX(pdf.get_y())+10
    for i in range(2):
        pdf.set_xy(px2MM(88), px2MM(y))
        pdf.multi_cell(px2MM(15), px2MM(14),chr[i])
        
        pdf.set_xy(px2MM(100), px2MM(y))
        pdf.multi_cell(px2MM(420), px2MM(14),texts[i])
        
        y = mm2PX(pdf.get_y())+8
        
    
    chr = ('iii.','iv','v.','vi.','vii.','viii.')
    # chr = ('c.','d.','e.','f.','g.','h.')
    texts = (
       """The investment advisor represents the client, that the investment advisor has the requisite skills, knowledge, experience, infrastructure, and capabilities along with the experienced and trained persons who have required qualification and skill set for performing the functions mentioned in this agreement.""",
        """The investment advisor represents that the advisor will not derive any direct or indirect benefit out of the client’s securities or investment product.""",
        """The investment advisor will not manage any funds or security, on behalf of the client under the investment advisory agreement""",
        """The investment advisor represents that the advisor, principal officer and person associated with investment advice shall maintain a requisite qualification and certification throughout the validity of this agreement.""",
        """The client represents that he has read and understood the agreement, fee structure, and modes of payment of fees and he is aware of the risks associated with the nature of services and the transaction involved in this agreement.""",
        """ The client represents that he/she will keep himself /herself aware of the policies, terms and conditions, regulations, guidelines, and other relevant information related to the investment advisor."""
    )
    y = mm2PX(pdf.get_y())+10
    for i in range(6):
        pdf.set_xy(px2MM(88), px2MM(y))
        pdf.multi_cell(px2MM(22), px2MM(14),chr[i])
        
        pdf.set_xy(px2MM(100), px2MM(y))
        pdf.multi_cell(px2MM(420), px2MM(14),texts[i])
        
        y = mm2PX(pdf.get_y())+8
     
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('Calibri',size=11)
    pdf.cell(px2MM(10), px2MM(14),"22.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Death or Disability of Client""")

    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),"""The provisions of this agreement will not automatically end or modify if the Client passes away, becomes disabled, or becomes physically or mentally incompetent. The client's legal heirs or another authorised representative may agree to modify the terms of this agreement or terminate it, provided that doing so is not forbidden by law""")

    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('Calibri',size=11)

    pdf.cell(px2MM(10), px2MM(14),"23.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Notices""")
     
def page9(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')
    
    pdf.set_font('Calibri',size=11)
    y = mm2PX(pdf.get_y())+38
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.multi_cell(px2MM(455), px2MM(14),"""Any notice communication or documents to be given to the other party shall be delivered electronically or may be given by personal delivery, courier, registered post or fax or at the address hereinafter mentioned.""")
    
    y = mm2PX(pdf.get_y()) + 22
    pdf.rect(px2MM(65), px2MM(y-12),px2MM(230), px2MM(20),'FD') #
    pdf.set_font('Calibribold',size=11)
    pdf.set_xy(px2MM(70), px2MM(y -10))
    pdf.multi_cell(px2MM(210), px2MM(14),"""If to the client:""")
    
    pdf.rect(px2MM(280 + 10), px2MM(y-12),px2MM(233), px2MM(20),'FD') #
    pdf.set_xy(px2MM(290 + 5), px2MM(y - 10))
    pdf.multi_cell(px2MM(210), px2MM(14),"""If to 1 Finance:""")
    
    y = mm2PX(pdf.get_y()) + 14
    pdf.set_font('Calibri',size=11)
    pdf.rect(px2MM(65), px2MM(y-10),px2MM(225), px2MM(60),'FD')
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(70), px2MM(y - 5))
    pdf.multi_cell(px2MM(210), px2MM(14),"""The address and email provided by the client""")
    """
    # pdf.set_xy(px2MM(80), px2MM(y + 5))
    # pdf.multi_cell(px2MM(180), px2MM(14),sys.argv[4]) # Email
    
    # y1 = mm2PX(pdf.get_y()) + 3
    
    # pdf.set_xy(px2MM(80), px2MM(y1 - 3))
    # pdf.multi_cell(px2MM(180), px2MM(9),sys.argv[2]) #Address
    """
    pdf.rect(px2MM(280 + 10), px2MM(y-10),px2MM(233), px2MM(60),'FD')
    pdf.set_xy(px2MM(290 + 5), px2MM(y - 5))
    pdf.multi_cell(px2MM(210), px2MM(14),"""The address mentioned in the agreement""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(290 + 5), px2MM(y))
    pdf.multi_cell(px2MM(210), px2MM(14),"""Email: compliance@1finance.co.in""")
    
    y = mm2PX(pdf.get_y()) + 32
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('Calibri',size=11)

    pdf.cell(px2MM(10), px2MM(14),"24.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Settlement of Disputes and Provision for Arbitration""")
    
    pt24_text=(
        """ No suit, prosecution or other legal proceeding shall lie against the investment advisor for any damage caused or likely to be caused by anything which is done in good faith or intended to be done under the provisions of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013.""",
        """Any grievance or complaint of the client will be redressed by the investment advisor in compliance with the provision of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013.""",
        """No suit, prosecution, or other legal proceedings shall lie against the investment advisor for any damage caused or likely to be caused by anything which is done in good faith or intended to be done under the provisions of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013."""
    )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    for i in range(1):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"24.{i+1}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt24_text[i-1])
        
        y = mm2PX(pdf.get_y())+10

    pdf.set_font('Calibri',size=11)
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),f"24.2")
    text = """Any grievance or complaint of the client will be redressed by the investment advisor in compliance with the provision of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013."""
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),text)

    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),f"24.3")
    text2 = """All disputes, differences, claims, and questions whatsoever arising from this agreement between the client and investment advisor and/or their respective representatives touching these presents shall be in accordance with and subject to the provisions of The Arbitration and Conciliation Act, 1996, or any statutory modification or re-enactment thereof for the time being in force. Such arbitration proceedings shall be held in Mumbai, and the language of Arbitration will be English."""
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),text2)

    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('CalibriBold',size=11)

    pdf.cell(px2MM(10), px2MM(14),"25.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Adherence to Grievance Redressal Timelines""")

    pt25_text=(
        """ Investment advisor shall be responsible to resolve the grievances within the timelines specified under SEBI circulars issued from time to time.""",
        """ The Client understands and confirms to send all the complaints and queries in case of any grievance or complaint arising out of and in the course of this agreement, on the email address at grievance@1finance.co.in."""
    )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    for i in range(1,3):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"25.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt25_text[i-1])
        
        y = mm2PX(pdf.get_y())+10

    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('CalibriBold',size=11)
    pdf.cell(px2MM(10), px2MM(14),"26.") 
        
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Indemnity""")

    pt26_text=(
        """The client hereby agrees that he has understood the risks associated with investments and is fully conscious of the same. It is hereby agreed that investment advisor shall not be liable in respect of any loss resulting from such risks.""",
        """ Investment advisor shall not be responsible for any loss or damage occasioned as a result of any factor whatsoever other than fraud or gross and willful negligence on its part. Without prejudice to the above, the client specifically agrees not to hold investment advisor responsible for any loss or damage occasioned by adverse market conditions, force majeure circumstances, delays on the part of companies or other authorities including government authorities in registering transfer of shares and securities, errors of judgement on investment advisor’s part or other factors beyond its control. Notwithstanding the generality of the foregoing, investment advisor shall not be liable if any or all of the securities and/or shares become illiquid due to force"""
        )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    for i in range(1,3):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"26.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(13),pt26_text[i-1])
        
        y = mm2PX(pdf.get_y())+8

def page10(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')

    page9_remaining_val = """majeure circumstance, adverse market conditions, court statutory or regulatory injunctions, attachments or other prohibitions affecting them and/or other factors beyond their control."""

    y = mm2PX(pdf.get_y())+38
    pdf.set_font('Calibri',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),page9_remaining_val)
        
    
    y = mm2PX(pdf.get_y())+8
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('Calibri',size=11)

    pdf.cell(px2MM(10), px2MM(14),"27.") 
        
    pdf.set_font('CalibriBold', size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Severability""")
    
    y = mm2PX(pdf.get_y())+8
    pdf.set_font('Calibri',size=11)

    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"27.1")
    
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(430), px2MM(14),""" If any provision of this agreement shall be held or made invalid by a court decision, statute, rule or otherwise, the remainder of this agreement shall not be affected thereby.""")
    
    
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('Calibri',size=11)

    pdf.cell(px2MM(10), px2MM(14),"28.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Force Majeure""")
    
    pt28_text=(
        """ The investment advisor shall not be liable for delays or errors occurring by reason of circumstances beyond its control, including but not limited to acts of civil or military authority, national emergencies, work stoppages, fire, flood, catastrophe, acts of God, insurrection, war, riot, or failure of communication or power supply.""",
    """ The investment advisor shall not be liable in the event of equipment breakdowns beyond its control, the investment advisor shall take reasonable steps to minimise service interruptions but shall have no liability with respect thereto."""
    )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    for i in range(1,3):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"28.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt28_text[i-1])
        
        y = mm2PX(pdf.get_y())+8

    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.set_font('Calibri',size=11)

    pdf.cell(px2MM(10), px2MM(14),"29.")
    
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(90), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Miscellaneous""")

    pt29_text=(
        """ All payments made under this agreement will be made in INR.""",
    """ No failure on the part of any party to exercise, and no delay on its part in exercising any right or remedy under this agreement will operate as a waiver thereof, nor will any single or partial exercise of any right. """
    )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    for i in range(1,3):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"29.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt29_text[i-1])
        
        y = mm2PX(pdf.get_y())+10
    
    pt29_text=(

       """ The advice or recommendations given to the client are intended to the benefit of client only, no other person shall be entitled to rely on such information.""",
       """ Other than as specifically permitted under this agreement, the client shall not publish or broadcast advertisements, circulars, or other publicity material referring to the investment advisor without the prior written consent of the investment advisor.""",
       """ Each party agrees to perform such further actions and execute such further agreements as are necessary to effectuate the purposes hereof."""
       
    )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=11)
    for i in range(3,6):
        pdf.set_xy(px2MM(70), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"29.{i}")
        
        pdf.set_xy(px2MM(90), px2MM(y))
        pdf.multi_cell(px2MM(430), px2MM(14),pt29_text[i-3])
        
        y = mm2PX(pdf.get_y())+10

    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(70), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"Agreed and Accepted by Client & 1 Finance",align='L')

    y = mm2PX(pdf.get_y())+8
    
    #### Details of Investment Advisers ####
    pdf.set_font('CalibriBold',size=11)
    pdf.set_xy(px2MM(70),px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"Details of Investment Advisor")

    # Table Start
    x = 74
    y = mm2PX(pdf.get_y()) + 8
    
    """Col 1 Vals"""
    
    col1_vals = ['Name as registered with SEBI','Brand name','Type of registration','Registration Number ','Validity of registration','Corporate Office Address', 'Principal Officer', 'Contact details',
    'Corresponding SEBI regional/local \noffice address']

    for i in range(9 - 1):  # Excluding last value which is moved to next page.
        if i == 0:
            pdf.set_font('Calibri',size=11)
            pdf.set_xy(px2MM(x),px2MM(y + 3))
            pdf.rect(px2MM(65 + 2), px2MM(math.floor(y)), px2MM(170), px2MM(20),'D')
            pdf.multi_cell(px2MM(400), px2MM(14),col1_vals[i])

        elif i == 5:
            pdf.rect(px2MM(65 + 2), px2MM(math.floor(y)), px2MM(170), px2MM(60),'D')
            pdf.set_font('Calibri',size=11)
            pdf.set_xy(px2MM(x),px2MM(y + 6))
            pdf.multi_cell(px2MM(400), px2MM(14),col1_vals[i])
            y  += 40
        elif i == 8:
            pdf.rect(px2MM(65 + 2), px2MM(math.floor(y)), px2MM(170), px2MM(65),'D')
            pdf.set_font('Calibri',size=11)
            pdf.set_xy(px2MM(x),px2MM(y + 6))
            pdf.multi_cell(px2MM(400), px2MM(14),col1_vals[i])
            y += 45
        else:
            pdf.set_font('Calibri',size=11)
            pdf.set_xy(px2MM(x),px2MM(y + 3))
            pdf.rect(px2MM(65 + 2), px2MM(math.floor(y)), px2MM(170), px2MM(20),'D')
            pdf.multi_cell(px2MM(400), px2MM(14),col1_vals[i])
        y += 20
    
    y = 94 #Resseting y to the begining of the table
    # Col2 ######################################3
    col2_vals = ['1 Finance Private Limited','1 Finance','Non-Individual', 'INA000017523','December 22, 2022 - Perpetual','Unit No. 1101 & 1102, 11th Floor, B-Wing, Lotus \nCorporate Park, Goregaon (E), Mumbai-400063','Mr. Akhil Rathi','po@1finance.co.in','Securities and Exchange Board of India, \nSEBI Bhavan II, Plot No: C7, “G” Block, \nBandra Kurla Complex, Bandra (East), Mumbai-400051']

    # x = 241 - 4.1
    x = mm2PX(pdf.get_x() + 74)
    y = 94 + 494 - 14
    # y = mm2PX(pdf.get_y() + 7)

    for i in range(9 - 1 ): # Excluding last value which is moved to next page.
        pdf.set_font("Calibri",  size=11)
        pdf.set_text_color(*hex2RGB('#000000'))

        if i == 0 or i == 1 or i == 2 or i == 3:
            pdf.set_font('Calibri',size=11)
            pdf.set_xy(px2MM(x),px2MM(y + 3))
            pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(40))
            pdf.multi_cell(px2MM(400), px2MM(14),col2_vals[i])

        elif i == 5:
            pdf.set_font('Calibri',size=11)
            pdf.set_xy(px2MM(x),px2MM(y + 6))
            pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(60))
            pdf.multi_cell(px2MM(280), px2MM(14),col2_vals[i])
            y += 40

        elif i == 7:
                pdf.set_font("Calibri",style = "U" , size=11)   
                pdf.set_xy(px2MM(x),px2MM(y + 3))
                pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(20))
                # pdf.set_text_color(*hex2RGB('#0000FF')) # Initially It was set to Blue
                pdf.set_text_color(*hex2RGB('#000000'))
                pdf.multi_cell(px2MM(280), px2MM(14),col2_vals[i])

        elif i == 8:
            pdf.set_font('Calibri',size=11)
            pdf.set_xy(px2MM(x),px2MM(y + 6))
            pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(65))
            pdf.multi_cell(px2MM(280), px2MM(14),col2_vals[i])
            y += 45
        else:   
            pdf.set_font('Calibri',size=11)
            pdf.set_xy(px2MM(x),px2MM(y + 3))
            pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(20))
            pdf.multi_cell(px2MM(400), px2MM(14),col2_vals[i])
        y += 20
        
def page11(pdf):

    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')

    
    # Table Start
    x = 74
    y = mm2PX(pdf.get_y()) + 52
    
    """Col 1 Vals"""
    
    col1_vals = ['Corresponding SEBI regional/local \noffice address']

    for i in range(len(col1_vals)):
        pdf.rect(px2MM(65 + 2.1), px2MM(math.floor(y)), px2MM(170), px2MM(80),'D')
        pdf.set_font('Calibri',size=11)
        pdf.set_xy(px2MM(x),px2MM(y + 6))
        pdf.multi_cell(px2MM(400), px2MM(14),col1_vals[i])
    
    # Col2 ######################################
    col2_vals = ['Securities and Exchange Board of India, \nSEBI Bhavan II, Plot No: C7, “G” Block, \nBandra Kurla Complex, Bandra (East), Mumbai-400051']

    x = mm2PX(pdf.get_x() + 74)

    y = mm2PX(pdf.get_y()) - 34.2
    


    for i in range(len(col2_vals)):
        pdf.set_font("Calibri",  size=11)
        pdf.set_text_color(*hex2RGB('#000000'))

        pdf.set_font('Calibri',size=11)
        pdf.set_xy(px2MM(x),px2MM(y + 6.5))
        pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(80))
        pdf.multi_cell(px2MM(200), px2MM(16),col2_vals[i])
    

    

### Details Of Client Table ####

    y = mm2PX(pdf.get_y()) + 38

    pdf.set_font("CalibriBold",style="U",size=11)
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.multi_cell(px2MM(600), px2MM(14),"Details of Client:")

    # extract current local date
    today = date.today()
    # show date in different format
    # today = today.strftime("%Y-%m-%d")
    today = today.strftime("%d-%m-%Y")

    table2_c1_val = ['Name','Address','PAN','Email ID','Mobile Number','Agreement Execution Date']
    
    name, address, pan,email, mobile , agreement_execution_date = sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],today

    table2_col2_vals = (name , address, pan,email, mobile , agreement_execution_date)

    tab2_counter = y + 30
    tab2_col1_vals_counter = y + 35
    for i in range(7-1):
        pdf.set_font("Calibri",  size=11)
        x =  len(table2_col2_vals[i]) / 50
        if x < int(x):
            x+=1
        else:
            x+=1
        x=int(x)
        if i == 5:
            pdf.set_font("CalibriBold",  size=11)
            pdf.rect(px2MM(80), px2MM(tab2_counter), px2MM(160), px2MM(x*20),'D')
            pdf.set_xy(px2MM(80),px2MM(tab2_col1_vals_counter))
            pdf.multi_cell(px2MM(400), px2MM(12),table2_c1_val[i])
        else:
            pdf.rect(px2MM(80), px2MM(tab2_counter), px2MM(160), px2MM(x*20),'D')
            pdf.set_xy(px2MM(80),px2MM(tab2_col1_vals_counter))
            pdf.multi_cell(px2MM(400), px2MM(12),table2_c1_val[i])


        # Table 2 Col 2
        pdf.rect(px2MM(240), px2MM(tab2_counter), px2MM(230), px2MM(x*20),'D')
        pdf.set_xy(px2MM(245),px2MM(tab2_col1_vals_counter))
        pdf.multi_cell(px2MM(220), px2MM(12),table2_col2_vals[i],border = 0)
        tab2_counter += x*20
        tab2_col1_vals_counter += x*20

    y = mm2PX(pdf.get_y()) # Use This Always to Reset the value of Y.

pdf_creator(pdf)