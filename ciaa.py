from fpdf import FPDF,HTMLMixin
from os.path import join
from os import getcwd
from PIL import ImageColor
import sys
import os
import PyPDF2
import math
from datetime import date
"""Deleting Pkl"""
cwd = os.path.dirname(__file__) 
# cwd = os.getcwd()
# cwd = sys.argv[7]

# LGpkl_file = os.path.join(cwd,'assets','fonts','Calibri')
# test = os.listdir(LGpkl_file)
# for item in test:
#     if item.endswith(".pkl"):
#         os.remove(os.path.join(LGpkl_file, item))
# """Sometimes we pkl files are created in curr dir too, so we are deleting that here"""
# test = os.listdir(cwd)
# for item in test:
#     if item.endswith(".pkl"):
#         os.remove(item)
# """Deleting Pkl"""

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
    
    # filename = sys.argv[4]+'.pdf'    
    # directory = join(sys.argv[5],filename)  
    # pdf.output(directory)
    
    filename = sys.argv[6]
    directory = join(sys.argv[7],filename)
    pdf.output(directory)
    print('pdf genrated')
    
def img_add(pdf):
    # cwd = os.getcwd()      
    # img = join(cwd,'assets','images','stampandsign.jpeg')
    img = join(cwd,'assets','images','stampandsign2.jpg')
    pdf.image(img,px2MM(435), px2MM(770),px2MM(120), px2MM(55))

def page1(pdf):
    
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'DF')
    
    
    pdf.set_xy(px2MM(0), px2MM(50))
    pdf.set_font('CalibriBold',style='U', size=12)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(600), px2MM(16),'1 Finance Investment Advisory Agreement',align='C')
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(80), px2MM(y+32))
    pdf.set_font('CalibriBold', size=10)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(110), px2MM(14),"1 Finance Private Limited,",align='L')
    
    pdf.set_xy(px2MM(190), px2MM(y+32))
    pdf.set_font('Calibri', size=10.1)
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.cell(px2MM(310), px2MM(14),f'{" "}a registered Investment advisor with SEBI Registration No. INA000017523')
    
    
    y = mm2PX(pdf.get_y())
    
    pdf.set_xy(px2MM(80), px2MM(y+12))
    pdf.set_font('Calibri', size=10.1)
    pdf.multi_cell(px2MM(420), px2MM(14),f"having a corporate office at Unit No. 1101 & 1102, 11th Floor, B-Wing, Lotus Corporate Park, Goregaon (E), Mumbai-400063 and a registered office at 'Marwadi Financial Plaza', Nana Mava Main {' '}Road, Off {' '}150ft{' '} {' '}Ring Road,{' '} Rajkot- 360001, {' '}Gujarat,{' '} (hereinafter referred to as the")
    
    y = mm2PX(pdf.get_y())
    pdf.set_font('CalibriBold', size=10)
    pdf.set_xy(px2MM(433), px2MM(y-14))
    pdf.cell(px2MM(420), px2MM(14),"“INVESTMENT")
    
    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(80), px2MM(y+14))
    pdf.cell(px2MM(110), px2MM(14),"ADVISOR” or “1 FINANCE”",align='L')
    
    pdf.set_font('Calibri', size=10)
    pdf.set_xy(px2MM(190), px2MM(y+14))
    pdf.cell(px2MM(420), px2MM(14)," which expression shall unless excluded by or repugnant to the context, be")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(354), px2MM(14),"deemed to include its administrators and permitted assigns) of the")
    
    pdf.set_font('CalibriBold', size=10)
    pdf.set_xy(px2MM(354), px2MM(y))
    pdf.cell(px2MM(100), px2MM(14),"FIRST PART")
    
    y = mm2PX(pdf.get_y())+28
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(45), px2MM(14),"1 Finance")

    pdf.set_font('Calibri', size=10)
    pdf.set_xy(px2MM(125), px2MM(y))
    pdf.cell(px2MM(400), px2MM(14),f"{' '}{' '}provides{' '}{' '} financial{' '}{' '} advisory{' '}{' '} services{' '}{' '} through{' '}{' '}{' '} its{' '}{' '} mobile{' '}{' '} application{' '}{' '} and{' '}{' '} website")

    # pdf.set_font('Calibri', size=10)
    # pdf.set_xy(px2MM(125), px2MM(y))
    # pdf.cell(px2MM(400), px2MM(14),"provides financial advisory services through its mobile application and website")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_text_color(*hex2RGB('#0000FF'))
    pdf.set_font('Calibri',style='U', size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(45), px2MM(14),"www.1finance.co.in")
    
    pdf.set_text_color(*hex2RGB('#000000'))
    pdf.set_font('Calibri', size=10)
    pdf.set_xy(px2MM(165), px2MM(y))
    pdf.cell(px2MM(150), px2MM(14),"under the brand name of")
    
    pdf.set_font('CalibriBold', size=10)
    pdf.set_xy(px2MM(270), px2MM(y))
    pdf.cell(px2MM(150), px2MM(14),"1 Finance. ")
    
    y = mm2PX(pdf.get_y())+28
    pdf.set_xy(px2MM(0), px2MM(y))
    pdf.cell(px2MM(600), px2MM(14),"AND",align='C')
    
    y = mm2PX(pdf.get_y())+28
    pdf.set_font('Calibri', size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(250), px2MM(14),"The Client (Hereinafter referred to as the")
    
    pdf.set_font('CalibriBold', size=10)
    pdf.set_xy(px2MM(253), px2MM(y))
    pdf.cell(px2MM(40), px2MM(14),"“CLIENT”")
    
    pdf.set_font('Calibri', size=10)
    pdf.set_xy(px2MM(293), px2MM(y))
    pdf.cell(px2MM(250), px2MM(14)," which expression shall unless it be repugnant to ")
    
    pdf.set_xy(px2MM(80), px2MM(mm2PX(pdf.get_y())+14))
    pdf.multi_cell(px2MM(420), px2MM(14),f"the{' '} context{' '} or{' '} be{' '} deemed to{' '} mean{' '} and{' '} include,{' '}{' '} its administrators{' '} &{' '} permitted assigns){' '} of{' '} the",fill=True)
    
    pdf.set_font('CalibriBold', size=10)
    pdf.set_xy(px2MM(80), px2MM(mm2PX(pdf.get_y())))
    pdf.cell(px2MM(50), px2MM(14),"SECOND PART;")
    
    pdf.set_xy(px2MM(80), px2MM(mm2PX(pdf.get_y())+28))
    pdf.multi_cell(px2MM(420), px2MM(14),f"Both 1 Finance and the client shall also hereinafter individually have referred to as party & collectively as parties.")
    

    # Behaviour
    pdf.set_xy(px2MM(80), px2MM(mm2PX(pdf.get_y())+12))
    pdf.multi_cell(px2MM(250), px2MM(14),"Definitions:")
    behvior_point1_l1 = f'"Investment Advisor”{" "} or “Investment Adviser” means any person, who for consideration, is engaged"'
    behvior_point1_l2 = f"in the business of{' '} providing {' '}investment advice to clients {' '}or other persons or groups of persons and"
    behvior_point1_l3 = f"includes{' '} any{' '} person{' '} who holds{' '} out{' '} himself{' '} as{' '} an{' '} investment{' '} advisor / investment{' '} advisor, {' '}by"
    behvior_point1_l4 = "whatever name called;"

    # behvior_point1_l1 = '"Investment Advisor” or “Investment Adviser” means any person, who for consideration, is engaged"'
    # behvior_point1_l2 = "in the business of providing investment advice to clients or other persons or groups of persons and"
    # behvior_point1_l3 = "includes any person who holds out himself as an investment advisor/investment adviser, by"
    # behvior_point1_l4 = "whatever name called;"
    # y = mm2PX(pdf.get_y())+28
    # y = mm2PX(pdf.get_y()) + 10
    pdf.set_font('Calibri', size=10.1)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(250), px2MM(y+14),behvior_point1_l1)
    
    y = mm2PX(pdf.get_y()) + 12.5
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(250), px2MM(y),behvior_point1_l2,align="L")
    
    # y = mm2PX(pdf.get_y())+18
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(250), px2MM(y + 25),behvior_point1_l3,align="L")
    
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(250), px2MM(y + 25 + 25),behvior_point1_l4,align="L")

    # Behavior Para 2

    behvior_point2_l1 = f'“Client{" "} or{" "} Member”{" "} means{" "} any individual{" "}, group{" "} of{" "} individuals,{" "} partnership,{" "} trust,{" "} or{" "} company,'
    behvior_point2_l2 = "including, without limit, a fund for whom the advisor acts as an investment advisor."
    # behvior_point2_l1 = '“Client or Member” means any individual, group of individuals, partnership, trust, or company,'
    # behvior_point2_l2 = "including, without limit, a Fund for whom the Adviser acts as an investment advisor."
    y = mm2PX(pdf.get_y())+25
    pdf.set_font('Calibri', size=10.1)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(250), px2MM(y+28),behvior_point2_l1)
    
    # y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri', size=10.1)
    # pdf.set_font('Calibri', size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(250), px2MM(y+28+28),behvior_point2_l2)

    

    # y = mm2PX(pdf.get_y())+28
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(y + 48 + 28 + 28 + 14 + 13),"1.") 

    y = mm2PX(pdf.get_y()) + 48 + 28 + 28+ 48 + 35
    pdf.set_font('CalibriBold', style='U',size=10)
    # pdf.set_xy(px2MM(80), px2MM(y + 48 + 28 + 28+ 48 + 43))
    pdf.set_xy(px2MM(80), px2MM(y + 14))
    pdf.cell(px2MM(420), px2MM(14),"APPOINTMENT OF THE INVESTMENT ADVISOR:")
    
    y = mm2PX(pdf.get_y())+25
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"1.1")
    
    pdf.set_xy(px2MM(100), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""In accordance with the applicable laws, the client hereby appoints, entirely at his / her / its risk, the investment advisor to provide the required services in accordance with the terms and conditions of the agreement as mandated under Regulation 19(1)(d) of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013.""")
    
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"2.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(420), px2MM(14),"CONSENT OF THE CLIENT")
    
    y = mm2PX(pdf.get_y())+28
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(420), px2MM(14),"The client hereby consents to the following:")
    
    y = mm2PX(pdf.get_y())+28
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"2.1")
    
    # pdf.set_xy(px2MM(105), px2MM(y))
    # pdf.multi_cell(px2MM(400), px2MM(14),"""I / We have read and understood the terms and conditions of Investment Advisory services provided by the Investment Adviser along with the fee structure and mechanism for charging and payment of fee.""")
    
    # y = mm2PX(pdf.get_y())+14
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.cell(px2MM(10), px2MM(14),"2.2")
    
    # pdf.set_xy(px2MM(105), px2MM(y))
    # pdf.multi_cell(px2MM(400), px2MM(14),"""Based on our written request to the Investment Adviser, an opportunity was provided by the Investment Adviser to ask questions and interact with ‘person(s) associated with the investment advice.""")
    
    # y = mm2PX(pdf.get_y())+14
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.cell(px2MM(10), px2MM(14),"2.3")
    # pdf.set_xy(px2MM(105), px2MM(y))
    # pdf.multi_cell(px2MM(400), px2MM(14),"""I /We hereby give my consent that my risk profiling is completed.""")
    
    pdf.set_xy(px2MM(99), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""I / We have read and understood the terms and conditions of investment advisory services provided by the investment advisor along with the fee structure and mechanism for charging and payment of fee.""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"2.2")
    
    # pdf.set_xy(px2MM(105), px2MM(y))
    pdf.set_xy(px2MM(99), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""Based on our written request to the investment advisor, an opportunity was provided by the investment advisor to ask questions and interact with the ‘person(s) associated with the investment advice.""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"2.3")
    # pdf.set_xy(px2MM(105), px2MM(y))
    pdf.set_xy(px2MM(99), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""I / We hereby give my consent that my risk profiling is completed.""")
    

    
    
    # y = mm2PX(pdf.get_y())+14
    # pdf.set_xy(px2MM(60), px2MM(y))
    # pdf.cell(px2MM(10), px2MM(14),"3.")
    
    # pdf.set_font('CalibriBold', style='U',size=10)
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.cell(px2MM(420), px2MM(14),"DECLARATION FROM THE INVESTMENT ADVISER")
    
    # y = mm2PX(pdf.get_y())+28
    # pdf.set_font('Calibri',size=10)
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.cell(px2MM(420), px2MM(14),"Investment Adviser hereby declares the following:")
    
    # y = mm2PX(pdf.get_y())+28
    
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.cell(px2MM(10), px2MM(14),"3.1")
    # pdf.set_xy(px2MM(105), px2MM(y))
    # pdf.multi_cell(px2MM(400), px2MM(14),"""Investment Adviser shall neither render any investment advice nor charge any fee until the client has signed this agreement.""")
    
    # y = mm2PX(pdf.get_y())+14
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.cell(px2MM(10), px2MM(14),"3.2")
    
    # pdf.set_xy(px2MM(105), px2MM(y))
    # pdf.multi_cell(px2MM(400), px2MM(14),"""Investment Adviser shall not manage funds and securities on behalf of the client and that it shall only receive such sums of monies from the client as are necessary to discharge the client’s liability towards fees owed to the Investment Adviser.""")
    
    # fpdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
    y = mm2PX(pdf.get_y())+28
    pdf.set_xy(px2MM(0), px2MM(y))
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),align='C')
    img_add(pdf)
    

def page2(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')
    

    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"3.")
    # pdf.cell(px2MM(10), px2MM(14),"4.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(420), px2MM(14),"DECLARATION FROM THE INVESTMENT ADVISOR") #
    # pdf.multi_cell(px2MM(420), px2MM(14),"""FEES SPECIFIED UNDER THE INVESTMENT ADVISER REGULATIONS AND RELEVANT CIRCULARS ISSUED THEREUNDER""")
    
   
    # y = mm2PX(pdf.get_y())+28
    # pdf.set_font('Calibri',size=10)
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.multi_cell(px2MM(420), px2MM(14),"""Investment Adviser hereby declares the following:""")

    y = mm2PX(pdf.get_y())+28
    pdf.set_font('Calibri',size=10.5)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Investment advisor hereby declares the following:""") #


    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"3.1")
    

    pdf.set_font('Calibri',size=10.5)
    pdf.set_xy(px2MM(99), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""Investment advisor shall neither render any investment advice nor charge any fee until the client has signed this agreement.""")
    
#     pdf.set_xy(px2MM(105), px2MM(y))
#     pdf.multi_cell(px2MM(400), px2MM(14),"""“Investment Adviser shall neither render any investment advice nor charge any fee until the
# client has signed this agreement”""")
     
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10.5)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"3.2")
    
    pdf.set_xy(px2MM(99), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""Investment advisor shall not manage funds and securities on behalf of the client and it shall only receive such sums of monies from the client as are necessary to discharge the client’s liability towards fees owed to the investment advisor.""")
#     y = mm2PX(pdf.get_y())+12
#     pdf.set_font('Calibri',size=10)
#     pdf.set_xy(px2MM(80), px2MM(y))
#     pdf.cell(px2MM(10), px2MM(14),"3.2")
    
#     pdf.set_xy(px2MM(105), px2MM(y))
#     pdf.multi_cell(px2MM(400), px2MM(14),"""“Investment Adviser shall not manage funds and securities on behalf of the client and it shall
# only receive such sums of monies from the client as are necessary to discharge the client’s
# liability towards fees owed to the Investment Adviser.”""")
    
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"3.3")
    
    pdf.set_font('Calibri',size=10.5)
    pdf.set_xy(px2MM(99), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""Investment advisor shall not, in the course of performing its services to the client, hold out any investment advice implying any assured returns or minimum returns or target return or percentage accuracy or service provision till achievement of target returns or any other nomenclature that gives the impression to the client that the investment advice is risk-free and/or not susceptible to market risks and or that it can generate returns with any level of assurance.""")
    

#     y = mm2PX(pdf.get_y())+12
#     pdf.set_font('Calibri',size=10)
#     pdf.set_xy(px2MM(80), px2MM(y))
#     pdf.cell(px2MM(10), px2MM(14),"3.3")
    
#     pdf.set_xy(px2MM(105), px2MM(y))
#     pdf.multi_cell(px2MM(400), px2MM(14),"""“Investment Adviser shall not, in the course of performing its services to the client, hold out
# any investment advice implying any assured returns or minimum returns or target return or
# percentage accuracy or service provision till achievement of target returns or any other
# nomenclature that gives the impression to the client that the investment advice is risk-free
# and/or not susceptible to market risks and or that it can generate returns with any level of
# assurance.”""")
    
    
   
    
    
    # y = mm2PX(pdf.get_y())+14
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.multi_cell(px2MM(420), px2MM(14),"""payment modes available on the platform or 1 Finance can pull the money from the client’s bank account based on the bank mandate provided by the client.""")
    
    # y = mm2PX(pdf.get_y())+14
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.multi_cell(px2MM(420), px2MM(14),"""In accordance with SEBI (Investment Adviser) regulations, circulars, and guidelines, the maximum fees that can be charged to clients under Asset under Advice mode shall not exceed2.5 percent of AUA per annum per Client, and under Fixed Fee – shall not exceed INR 1,25,000/- per annum per Client.""")
    

    #Original Code of Point 4
    """
    
    """
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"4.") 

    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""FEES SPECIFIED UNDER THE INVESTMENT ADVISOR REGULATIONS AND RELEVANT CIRCULARS ISSUED THEREUNDER""")

    #Bullets
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'4.1')

    point4_para1 = """The Client(s) shall pay the investment advisor fees for the services rendered as provided in the “My Plan/Subscription” section on the 1 Finance Application. The fees can be paid utilising the payment modes available on the platform or the 1 Finance can pull the money from the client’s bank account based on the bank mandate provided by the client. """
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(99), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),point4_para1)
    

    #Bullets
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'4.2')
    point4_para2 = """In accordance with SEBI (Investment Advisor) regulations, circulars, and guidelines, the maximum fees that can be charged to clients under Asset under Advice mode shall not exceed 2.5 percent of AUA per annum per client and under fixed fee – shall not exceed INR 1,25,000/- per annum per Client."""
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(99), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),point4_para2)
    

    # y = mm2PX(pdf.get_y())+14
    # pdf.set_font('Calibri',size=10)
    # pdf.set_xy(px2MM(83), px2MM(y))
    # pdf.multi_cell(px2MM(420), px2MM(14),f'''The Client(s) shall{" "} pay the Investment Adviser fees for {" "} the services rendered as provided in the "My''')

   
    # y = mm2PX(pdf.get_y())
    # pdf.set_font('Calibri',size=10.1)
    # pdf.set_xy(px2MM(83), px2MM(y))
    # pdf.cell(px2MM(100), px2MM(14),f"""Plan/{" "}Subscription/{" "}Profile”{' '} section on the 1 Finance{' '} Application. The fees can be paid{" "} utilizing the""")

    # y = mm2PX(pdf.get_y()) + 14
    # pdf.set_font('Calibri',size=10.3)
    # pdf.set_xy(px2MM(83), px2MM(y))
    # pdf.cell(px2MM(320), px2MM(14),f"""payment{' '} modes available on the platform {" "}or the 1 Finance can{" "} pull the money{' '} from the client’s""")

    
   
    # y = mm2PX(pdf.get_y()) + 14
    # pdf.set_font('Calibri',size=10)
    # pdf.set_xy(px2MM(83), px2MM(y))
    # pdf.cell(px2MM(320), px2MM(14),"""bank account based on the bank mandate provided by the client.""")

    # point 4 para 1 end.


    # Point 4 para 2 #######
    # y = mm2PX(pdf.get_y()) + 28
    # pdf.set_font('Calibri',size=10.2)
    # pdf.set_xy(px2MM(84), px2MM(y))
    # pdf.cell(px2MM(320), px2MM(14),f"""In {" "}accordance with SEBI{" "}(Investment Adviser) regulations, circulars {" "} and guidelines, the maximum""")

    # y = mm2PX(pdf.get_y()) + 14
    # pdf.set_font('Calibri',size=10.2)
    # pdf.set_xy(px2MM(84), px2MM(y))
    # pdf.cell(px2MM(320), px2MM(14),f"""fees that can be charged to clients under Asset under Advice mode shall not exceed 2.5 percent of""")
    
    # y = mm2PX(pdf.get_y()) + 14
    # pdf.set_font('Calibri',size=10.2)
    # pdf.set_xy(px2MM(84), px2MM(y))
    # pdf.cell(px2MM(320), px2MM(14),f"""AUA {" "}per annum {' '}per Client and{' '} under Fixed Fee{' '}– shall not{' '} exceed INR 1,25,000/- per annum per""")
    
    # y = mm2PX(pdf.get_y()) + 14
    # pdf.set_font('Calibri',size=10)
    # pdf.set_xy(px2MM(84), px2MM(y))
    # pdf.cell(px2MM(320), px2MM(14),"""Client""")
    # Point 4 para 2 end

    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"5.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(420), px2MM(14),"""FEES CHARGED TO THE CLIENT""")
    
    pdf.set_font('Calibri',size=10) 
    y = mm2PX(pdf.get_y())+28
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"5.1")
    
    y = mm2PX(pdf.get_y()) + 28
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"5.2")
    
    y = mm2PX(pdf.get_y()) + 70
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"5.3")
    
    y = mm2PX(pdf.get_y()) + 56
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"5.4")
    
    pt5_text = ("""The client agrees to pay the advisory fee in the manner specified above.""",
                """Fees must be paid in any manner that allows for the traceability of the fund /amount paid. The modalities of payments may include account payee crossed cheques/Demand drafts, as well as a direct credit to bank accounts via NEFT/RTGS/IMPS/UPI or any other manner specified by SEBI from time to time. The fees, however, must not be paid in cash.""",
                """In the event of premature termination of the advisory services as per the terms of the agreement, the client shall be refunded the fees for the unexpired period. However, investment advisor may retain a maximum advisory fee of one-quarter.""",
                """The client will be charged advisory fees, if there is any change/update in the value of assets under advisory.""",
                """More details of the fees will be available on the 1 Finance mobile application.""")
    
    y = mm2PX(pdf.get_y()) - 28 - 70 - 56
    # y = mm2PX(pdf.get_y())+28
    for i in range(5):
        if i == 4:
            pdf.set_xy(px2MM(80), px2MM(y))
            pdf.multi_cell(px2MM(400), px2MM(14),pt5_text[i])
            y = mm2PX(pdf.get_y())+14
        else:
            pdf.set_xy(px2MM(99), px2MM(y))
            pdf.multi_cell(px2MM(400), px2MM(14),pt5_text[i])
            y = mm2PX(pdf.get_y())+14
        
        

    # 6 Point
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"6.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""SCOPE OF SERVICES:""")
    
    # pt6_text = ("""Defining the Financial Behaviour score of the client""",
    #             """Defining the important financial ratios for the client """,
    #             """Aggregation of the client Assets & liability under For You""",
    #             """Providing the overall financial plan along with the financial advisory on the variousFinancial Instruments.""",
    #             """The client shall be provided with a risk profile based on the set of questions and other""",
    #             )
    pt6_text = """Defining the Financial Behaviour Score of the client."""
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),pt6_text)

    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),f"6.1")

    # for i in range(1,6):
    #     pdf.set_xy(px2MM(80), px2MM(y))
    #     pdf.cell(px2MM(10), px2MM(14),f"6.{i}")
        
    #     pdf.set_xy(px2MM(105), px2MM(y))
    #     pdf.multi_cell(px2MM(400), px2MM(14),pt6_text[i-1])
        
    #     y = mm2PX(pdf.get_y())+14
        
    y = mm2PX(pdf.get_y())+32
    pdf.set_xy(px2MM(0), px2MM(y))
    # print(y) # 788
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),'LR',align='C')

    img_add(pdf)
    
    
def page3(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')
    
    # y = mm2PX(pdf.get_y())+32
    # pdf.set_xy(px2MM(105), px2MM(y))
    # pdf.multi_cell(px2MM(400), px2MM(14),"information of a client, required for providing the Investment Advisory.")
    

    # 6.2 to 6.5
    pt6_text = (
                """Defining the important financial ratios for the client.""",
                """Aggregation of the client assets & liability under 1View.""",
                """Providing the overall financial plan along with the financial advisory on the various Financial Instruments.""",
                """The client shall be provided with a risk profile based on the set of questions and other information of a client, required for providing the investment advisory.""",
                )
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    # for i in range(6,11):
    for i in range(5-1):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"6.{i+2}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt6_text[i-4])
        
        y = mm2PX(pdf.get_y())+14

     #6.6 to last
    pt6_text = (
                """The advisory, financial plan, financial behaviour score, and recommendation will be provided only to the client.""",
                """The client has sole discretion to decide on whether to act on the advice of the investment advisor or not based on the client’s own independent assessment of risk and reward of the investment. The investment advisor shall have no rights, power or responsibility, or any obligation to ensure that the client act upon the advice of the investment advisor.""",
                """The investment advisor shall use its best judgement and efforts in rendering the advice to the client under this agreement and in the performance of all its duties under this agreement""",
                """The investment advisor along with its promoter, director, or employee will never execute any transaction on behalf of the client nor will represent a client in any way for any negotiation or transaction of purchase or sale of securities or any assets. The client will be solely responsible for the execution of advice rendered by the investment advisor. """,
                """The services rendered by the investment advisor shall be subject to the activities permitted under the Securities and Exchange Board of India (investment advisors) regulation, 2013.""",
                )
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    # for i in range(6,11):
    for i in range(1,6):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"6.{i+5}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt6_text[i-6])
        
        y = mm2PX(pdf.get_y())+14



    #####
        
    #Point 7
    y = mm2PX(pdf.get_y())+28
    pdf.set_font('CalibriBold',size=10)

    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"7.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""DUTIES & FUNCTIONS OF THE INVESTMENT Advisor""")

    
    """Uncomment This"""
    pt7_text = (
        """Investment advisor shall be in compliance with the SEBI (Investment Advisor) Regulations, 2013 and its amendments, rules, circulars, and notifications. """,
        """Investment advisor shall be in compliance with the eligibility criteria as specified under the IA Regulations at all times. """,
        """Investment advisor shall conduct an audit as per the SEBI (Investment Advisor) Regulations, 2013. """,
        """Investment advisor shall provide the report to the client on potential and current investments.""",
        """Investment advisor shall be responsible for the risk assessment procedure of the client including their risk capacity and risk aversion before offering any recommendation or advice to the client.""",
        f"""Investment advisor shall provide investment advisory services to the client during the term of this agreement on investment in all financial/investment products under all regulated authorities as is permitted under applicable laws and regulations governing investment advisor. The services rendered by the investment advisor are non-binding in nature and the final decision on the type{' '} of instruments; the proportion {' '}of exposure{' '} and the tenure of the investments shall"""
    )

    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    # for i in range(1,8): # OG
    for i in range(1,7):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"7.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt7_text[i-1])
        y = mm2PX(pdf.get_y())+14
    """Uncomment This"""

    pdf.set_xy(px2MM(0), px2MM(y + 14))
    # print(y - 28) 742
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),'LR',align='C')
    img_add(pdf)
    

def page4(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')

    y = mm2PX(pdf.get_y()) + 14

    # remaining_text = """investments shall be taken by the client at their sole discretion."""
    remaining_text = """be taken by the client at their sole discretion."""
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),remaining_text)

    
    # Original
    
    # pt7_text = (
    #     """Investment Adviser shall maintain records of client-wise KYC, advice, risk assessment, analysis reports of investment advice and suitability, terms and conditions document, the rationale of advice, related books of accounts, and register containing a list of clients along with dated investment advice in compliance with the SEBI (Investment Advisers) Regulations, 2013.""",
    #     """Investment Adviser undertakes to abide by the Code of Conduct as specified in the Third Schedule of the SEBI (Investment Advisers) Regulations, 2013."""
    # )
    pt7_text = (
        """Investment advisor shall act in a fiduciary capacity as one of the advisers to the client with respect to managing its investment-related portfolio holistically. The investment-advisor shall act in a bona fide manner for the benefit and in the interest of the client.""",
        """Investment advisor shall maintain records of client-wise KYC, advice, risk assessment, analysis reports of investment advice and suitability, terms and conditions document, the rationale of advice, related books of accounts, and register containing a list of clients along with dated investment advice in compliance with the SEBI (Investment Advisors) Regulations, 2013.""",
        """Investment advisor undertakes to abide by the Code of Conduct as specified in the Third Schedule of the SEBI (Investment Advisors) Regulations, 2013."""
    )
      
    y = mm2PX(pdf.get_y())+12
    pdf.set_font('Calibri',size=10)
    # for i in range(8,10):
    for i in range(8,11):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"7.{i - 1}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt7_text[i-8])
        
        y = mm2PX(pdf.get_y())+14
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"8.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""INVESTMENT OBJECTIVES AND GUIDELINES """)
    
    pt8_text = (
        """Investment advisor undertakes to recommend direct implementation of advice i.e. through direct schemes/ direct codes, and other client specifications/restrictions on investments, if any.""",
        """The investment advisor shall recommend and advise the client based on the risk profile of the client. The client can choose on their own any other investment product which is not recommended as per the risk profile of the client.""",
        """The client shall take independent advice of its own from an independent tax advisor on the impact of taxation in the investment advice given by the investment advisor. The applicable tax will be charged along with the fees for the advisory services by the investment advisor.""",
        """The advisory and the recommendation will be provided by the advisor to the client."""
    )
    
    pdf.set_font('Calibri',size=10)
    y = mm2PX(pdf.get_y())+14
    for i in range(1,5):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"8.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt8_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"9.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""RISK FACTORS""")

    #Bullets
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.1')
    
    y = mm2PX(pdf.get_y()) + 70
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.2')
    
    y = mm2PX(pdf.get_y()) + 56
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.3')
    
    y = mm2PX(pdf.get_y()) + 56
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.4')
    
    y = mm2PX(pdf.get_y()) + 84
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'9.5')
    
    pt9_text= (
        """The investment advisor will not be liable to the client for any loss or damage financially or otherwise due to any of the advice or recommendation by the investment advisor to the client. The client also expressly agrees not to hold the investment advisor liable for any financial loss or otherwise.""",
        """The investments are subject to market risks, and there is no assurance or guarantee that the goal of the investments will be met. Additionally, the investment advisor's past performance does not ensure its future success.""",
        """Changes in government regulations, general interest rate levels, and hazards related to trading volume, liquidity, and settlement systems in the equities and debt markets could all have an impact on performance of the investments/products.""",
        """Investments in the products that the clients have chosen are subject to a wide range of risks, including but not limited to the economic slowdown, stock market volatility and illiquidity, poor corporate performance, changes in the government's and its policies, economic policies, acts of God, acts of war, civil unrest, sovereign action, and/or other events that are beyond the control of the investment advisor or any of its associates.""",
        """In no way do the names of the products or the types of investments imply their prospects or returns."""
    )
    y = mm2PX(pdf.get_y()) - 70 - 56 - 56 - 84
    pdf.set_font('Calibri',size=10)
    for i in range(5):
        pdf.set_xy(px2MM(99), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt9_text[i])
        y = mm2PX(pdf.get_y())+14
        
    # y = mm2PX(pdf.get_y())+14
    
    # y = mm2PX(pdf.get_y())+28
    # pdf.set_xy(px2MM(60), px2MM(y))
    # pdf.cell(px2MM(10), px2MM(14),"10.")
    
    # pdf.set_font('CalibriBold', style='U',size=10)
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.multi_cell(px2MM(420), px2MM(14),"""VALIDITY OF ADVISORY SERVICES""")
    
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(0), px2MM(-60))
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),'LR',align='C')
    img_add(pdf)
    
    
def page5(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')


    # 10th Heading
    # y = mm2PX(pdf.get_y())+14
    y = mm2PX(pdf.get_y())+28
    pdf.set_xy(px2MM(99), px2MM(y))
    page4_remaining_text = """The performance of specific businesses, alterations in the market, and industry-specific and macroeconomic issues all have the potential to negatively impact the performance of the invested asset."""
    pdf.multi_cell(px2MM(400), px2MM(14),page4_remaining_text)
    


    
    y = mm2PX(pdf.get_y())+10
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"10.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""VALIDITY OF ADVISORY SERVICES""")

    
    pt10_text = (
        """The advisory service agreement will be valid from the date of signing this agreement.""",
        """The agreement will be auto renewed subject to the payment of fees by the client.""",
        """The client or the investment advisor can terminate this agreement by giving 30 days’notice to the other party."""
    )
    pdf.set_font('Calibri',size=10)
    # y = mm2PX(pdf.get_y())+32 #Og
    y = mm2PX(pdf.get_y())+10
    for i in range(1,4):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"10.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt10_text[i-1])
        
        y = mm2PX(pdf.get_y())+5
        
    y = mm2PX(pdf.get_y())+12
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"11.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""AMENDMENTS""")
    
    pdf.set_font('Calibri',size=10)
    y = mm2PX(pdf.get_y())+12
    
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),f"11.1")
    
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""With the mutual consent of both parties the agreement can be amended and after amendment, the amended clause shall form a part of this agreement and constitute a legal binding between the parties.""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"12.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""TERMINATION""")
    
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(mm2PX(pdf.get_y())+14))
    pdf.multi_cell(px2MM(420), px2MM(14),"This agreement may be terminated under the following circumstances:")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"12.1")
    
    pdf.set_xy(px2MM(130), px2MM(y))
    pdf.multi_cell(px2MM(370), px2MM(12),"Voluntary termination: Either party may terminate this agreement by giving 30 days prior written notice to another party without stating any specific reason for termination.")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"12.2")
    
    pdf.set_xy(px2MM(130), px2MM(y))
    pdf.multi_cell(px2MM(370), px2MM(12),"""Mandatory termination by client: client can mandatorily terminate this agreement without giving any notice to the investment advisor upon the occurrence of any of the following events:""")
    
    chr = ('i.','ii.','iii.','iv.')
    texts = (
        """Any breach of terms by the investment advisor""",
        """If the advisor is barred by any government authority or SEBI or by order of the court to not act as an investment advisor.""",
        """If the investment advisor files for insolvency or becomes insolvent or enters into liquidation.""",
        """If the investment advisor ceases to hold the statutory license required to provide the service of investment advisory."""
    )
    y = mm2PX(pdf.get_y())+14
    for i in range(4):
        pdf.set_xy(px2MM(150), px2MM(y))
        pdf.multi_cell(px2MM(16), px2MM(14),chr[i],border=0)
        
        pdf.set_xy(px2MM(170), px2MM(y))
        pdf.multi_cell(px2MM(330), px2MM(14),texts[i])
        
        y = mm2PX(pdf.get_y())+10
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"12.3")
    
    pdf.set_xy(px2MM(130), px2MM(y))
    pdf.multi_cell(px2MM(370), px2MM(12),"""Mandatory termination by investment advisor: Investment advisor can terminate this agreement without giving any notice to the client upon the occurrence of any of the following events:""")
    
    texts = (
        """If the client commits a breach of any of the terms and conditions of this agreement.""",
        """If the client becomes insolvent or files for insolvency or enters into a liquidation""",
        """If the client gets barred or restricted by any of the regulatory bodies including SEBI."""
    )  
    y = mm2PX(pdf.get_y())+14
    for i in range(3):
        pdf.set_xy(px2MM(150), px2MM(y))
        pdf.multi_cell(px2MM(16), px2MM(14),chr[i],border=0)
        
        pdf.set_xy(px2MM(170), px2MM(y))
        pdf.multi_cell(px2MM(330), px2MM(14),texts[i]) 
        
        y = mm2PX(pdf.get_y())+10  
 
    pdf.set_xy(px2MM(0), px2MM(-60))
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),'LR',align='C')
    img_add(pdf)
    
    
def page6(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')

    ##########
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"12.4")
    
    pdf.set_xy(px2MM(130), px2MM(y))
    pdf.multi_cell(px2MM(370), px2MM(12),"""In the event of suspension of the registration certificate of the investment advisor by SEBI, the client may choose to terminate this agreement.""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"12.5")
    
    pdf.set_xy(px2MM(130), px2MM(y))
    pdf.multi_cell(px2MM(370), px2MM(12),"""In the event the client chooses to delete the account/profile from the 1 Finance Mobile Application, the deletion of the account/profile will be treated as the closure of the agreement by the client.""")
    
    ###########
    ########13
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"13.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),""" IMPLICATIONS OF AMENDMENTS AND TERMINATION""")
    
    pdf.set_font('Calibri',size=10)
    y = mm2PX(pdf.get_y())+14
    
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),f"13.1")
    
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),f"""Notwithstanding any such termination,{' '} all rights, liabilities,{' '} and obligations of the parties arising""")
    ########13
    
    pdf.set_font('Calibri',size=10)
    # y = mm2PX(pdf.get_y())+32 # Og
    y = mm2PX(pdf.get_y())+0.1
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""out of or in respect of transactions entered into prior to the termination of this relationship shall continue to subsist and vest in/be binding on the respective parties or his/its respective heirs, executors, administrators, legal representatives or successors, as the case may be;""")
       
    pt13_text = (
        """In case the clients are not satisfied with the services being provided by the investment advisor and wish to terminate/ stop investment advisory services, the client shall have a right to terminate the investment advisory relationship at any time subject (adhering to termination clause of this agreement) to refund of advisory fee after deducting one-quarter fee as breakage fee in case the termination is initiated by the clients.""",
        """In case the investment advisor transfers/sells/assigns its business to any other third party in such event the investment advisor will ensure that the client is provided the services by such new assignee / transferee on the same terms and conditions as stipulated in this agreement.""",
        """If the termination is due to suspension/cancellation of registration or due to any other action taken by other regulatory body/government authority then the fees will be refunded on a pro-rata basis.""",
        """The investment advisor would provide transition support, if requested by client and subsequently approved by management, to the client in the event of termination."""
    )
    
    y = mm2PX(pdf.get_y())+14
    for i in range(2,6):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"13.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt13_text[i-2])
        
        y = mm2PX(pdf.get_y())+14
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)
    pdf.cell(px2MM(10), px2MM(14),"14.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""RELATIONSHIP WITH RELATED PARTIES:""")
    
    pt14_text=(
        """Investment advisor will carry on its activities independently, at an arm's-length basis from all its other activities performed by the investment advisor or by any of the group companies of investment advisor.""",
        """Investment advisor does not have any conflict of interest of the investment advisory activities with its relationship with related parties, such conflict of interest shall be disclosed to the client as and when they arise."""
    )
    pdf.set_font('Calibri',size=10)
    y = mm2PX(pdf.get_y())+14
    for i in range(1,3):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"14.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt14_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
        
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)
    pdf.cell(px2MM(10), px2MM(14),"15.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""INVESTMENT ADVISOR ENGAGED IN OTHER ACTIVITIES""")
    
    pt15_text=(
        """The investment advisor hereby represents that it shall not provide to the client any commission-based distribution services, for securities and investment products, either directly or through its group companies.""",
        """The investment advisor hereby confirms that it shall not provide the investment advisory services for securities and investment products directly or through its group companies to the client who is availing of any commission-based distribution service."""
    )
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    for i in range(1,3):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"15.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt15_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
        
   
    
    pdf.set_xy(px2MM(0), px2MM(-60))
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),'LR',align='C')
    img_add(pdf)
    
def page7(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')

    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)
    pdf.cell(px2MM(10), px2MM(14),"16.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.multi_cell(px2MM(420), px2MM(14),"""INVESTMENT ADVISOR ENGAGED IN OTHER ACTIVITIES""")
    pdf.multi_cell(px2MM(420), px2MM(14),"""NO RIGHT TO SEEK POWER OF ATTORNEY""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"Investment advisor clearly declares that it shall not seek any power of attorney or authorizations from its clients for the implementation of investment advice.")

    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"17.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""REPRESENTATION TO CLIENT""")
    
    point17_text = """The investment advisor represents to the client that it will take all consents and permissions from the client prior to undertaking any actions in relation to the securities or investment product advised by the investment advisor.""" 
    y = mm2PX(pdf.get_y())+7
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),point17_text)
    
    
    
    # pdf.set_font('Calibri',size=10)
    # y = mm2PX(pdf.get_y())+32
    
    # pdf.set_font('Calibri',size=10)
    # pdf.set_xy(px2MM(80), px2MM(y))
    # pdf.multi_cell(px2MM(420), px2MM(14),"permissions from the client prior to undertaking any actions in relation to the securities or investment product advised by the investment adviser. ")
            
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"18.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""NO CONFLICT OF INTEREST""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""The investment advisor does hereby disclose that it does not have any conflict of interest with the client as on date and will disclose any such conflict of interest to the client as and when they arise. The investment advisor also declares that it will not derive any direct or indirect benefit out of the client’s securities or investment product.""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"19.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),""" MAINTENANCE OF ACCOUNTS AND CONFIDENTIALITY """)
    
    pt19_text=(
        """Investment advisor shall be responsible for maintenance of client accounts and data as mandated under the SEBI (Investment Advisors) Regulations, 2013. """,
        """Investment advisor shall not divulge any confidential information about its client, which has come to its knowledge, without taking prior permission of its client, except where such disclosures are required to be made in compliance with any law for the time being in force.""",
        """The client agrees and acknowledges that, pursuant to this agreement or otherwise, the investment advisor may receive confidential information about the client."""
    )
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    for i in range(1,4):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"19.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt19_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"20.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""LIABILITY OF INVESTMENT ADVISOR""")

    #Bullets
    pdf.set_font('Calibri',size=10)
    y = mm2PX(pdf.get_y()) + 14
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'20.1')
    
   
    y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""It is hereby agreed by the client that the investment advisor shall not incur any liability by reason of any loss, which a client may suffer by reason of any depletion in the value of the assets under advice, which may result by reason of fluctuation in asset value, or by reason of non-performance or under-performance of the securities/funds or any other market conditions.""")
    
    #BULLETS
    y = mm2PX(pdf.get_y()) + 14
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.cell(px2MM(10),px2MM(14),'20.2')

    y = mm2PX(pdf.get_y())
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""The client hereby understands that the responsibility of an investment advisor is to provide financial advice that is best suited to the client based on the information and details of a client available with an investment advisor. Client relying on the advice of an investment advisor is solely a decision of the client.""")
       
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"21.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),""" REPRESENTATIONS AND COVENANTS""") 
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""The parties hereto represent, warrant and covenant to each other as under:""")
    
    chr = ('i.','ii.','iii.','iv.')
    # chr = ('a.','b.','iii.','iv.')
    texts = (
       """Each party has the relevant power, capacity, and authority to execute, deliver and perform this agreement and has taken necessary action to authorise the execution and performance of this agreement.""",
       """Each party has required approval, license, permissions, and clearances which are necessary and required for entering into this agreement.""",
       """The investment advisor represents the client, that the investment advisor has the requisite skills, knowledge, experience, infrastructure, and capabilities along with the experienced and trained persons who have required qualification and skill set for performing the functions mentioned in this agreement."""
    )
    y = mm2PX(pdf.get_y())+14
    for i in range(2):
        pdf.set_xy(px2MM(110), px2MM(y))
        pdf.multi_cell(px2MM(15), px2MM(14),chr[i])
        
        pdf.set_xy(px2MM(135), px2MM(y))
        pdf.multi_cell(px2MM(365), px2MM(14),texts[i])
        
        y = mm2PX(pdf.get_y())+10
        
    pdf.set_xy(px2MM(0), px2MM(-60))
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),'LR',align='C')
    img_add(pdf)
    
    
def page8(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')
    
    pdf.set_font('Calibri',size=10)
    y = mm2PX(pdf.get_y())+32
    
    chr = ('iii.','iv','v.','vi.','vii.','viii.')
    # chr = ('c.','d.','e.','f.','g.','h.')
    texts = (
       """The investment advisor represents the client, that the investment advisor has the requisite skills, knowledge, experience, infrastructure, and capabilities along with the experienced and trained persons who have required qualification and skill set for performing the functions mentioned in this agreement.""",
        """The investment advisor represents that the advisor will not derive any direct or indirect benefit out of the client’s securities or investment product.""",
        """The investment advisor will not manage any funds or security, on behalf of the client under the investment advisory agreement""",
        """The investment advisor represents that the advisor, principal officer and person associated with investment advice shall maintain a requisite qualification and certification throughout the validity of this agreement.""",
        """The client represents that he has read and understood the agreement, fee structure, and modes of payment of fees and he is aware of the risks associated with the nature of services and the transaction involved in this agreement.""",
        """The client represents that he/she will keep himself /herself aware of the policies, terms and conditions, regulations, guidelines, and other relevant information related to the investment advisor."""
    )
    
    for i in range(6):
        pdf.set_xy(px2MM(110), px2MM(y))
        pdf.multi_cell(px2MM(20), px2MM(14),chr[i])
        
        pdf.set_xy(px2MM(135), px2MM(y))
        pdf.multi_cell(px2MM(365), px2MM(14),texts[i])
        
        y = mm2PX(pdf.get_y())+10
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)
    pdf.cell(px2MM(10), px2MM(14),"22.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""DEATH OR DISABILITY OF CLIENT: """)
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(83), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""The provisions of this agreement will not automatically end or modify if the Client passes away, becomes disabled, or becomes physically or mentally incompetent. The client's legal heirs or another authorised representative may agree to modify the terms of this agreement or terminate it, provided that doing so is not forbidden by law""")
    
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)

    pdf.cell(px2MM(10), px2MM(14),"23.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""NOTICES""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(83), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""Any notice communication or documents to be given to the other party shall be delivered electronically or may be given by personal delivery, courier, registered post or fax or at the address hereinafter mentioned.""")
    
    y = mm2PX(pdf.get_y())+ 28
    pdf.rect(px2MM(70), px2MM(y-12),px2MM(210), px2MM(20),'FD') #
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y -10))
    pdf.multi_cell(px2MM(210), px2MM(14),"""If to the client:""")
    
    pdf.rect(px2MM(280), px2MM(y-12),px2MM(210), px2MM(20),'FD') #
    pdf.set_xy(px2MM(290), px2MM(y - 10))
    pdf.multi_cell(px2MM(210), px2MM(14),"""If to 1 Finance:""")
    
    y = mm2PX(pdf.get_y()) + 14
    pdf.rect(px2MM(70), px2MM(y-10),px2MM(210), px2MM(70),'FD')
    pdf.set_font('Calibri',size=10)
    pdf.set_xy(px2MM(80), px2MM(y - 5))
    pdf.multi_cell(px2MM(210), px2MM(14),"""The address and email provided by the client""")
    # 
    # pdf.set_xy(px2MM(80), px2MM(y + 5))
    # pdf.multi_cell(px2MM(180), px2MM(14),sys.argv[4]) # Email
    
    # y1 = mm2PX(pdf.get_y()) + 3
    
    # pdf.set_xy(px2MM(80), px2MM(y1 - 3))
    # pdf.multi_cell(px2MM(180), px2MM(9),sys.argv[2]) #Address
    
    pdf.rect(px2MM(280), px2MM(y-10),px2MM(210), px2MM(70),'FD')
    pdf.set_xy(px2MM(290), px2MM(y - 5))
    pdf.multi_cell(px2MM(210), px2MM(14),"""The address mentioned in the agreement""")
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(290), px2MM(y))
    pdf.multi_cell(px2MM(210), px2MM(14),"""Email: compliance@1finance.co.in""")
    
    y = mm2PX(pdf.get_y()) + 63
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)

    pdf.cell(px2MM(10), px2MM(14),"24.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""SETTLEMENT OF DISPUTES AND PROVISION FOR ARBITRATION""")
    
    pt24_text=(
        """No suit, prosecution or other legal proceeding shall lie against the investment advisor for any damage caused or likely to be caused by anything which is done in good faith or intended to be done under the provisions of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013.""",
        """Any grievance or complaint of the client will be redressed by the investment advisor in compliance with the provision of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013.""",
        """No suit, prosecution, or other legal proceedings shall lie against the investment advisor for any damage caused or likely to be caused by anything which is done in good faith or intended to be done under the provisions of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013."""
    )
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    for i in range(1):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"24.{i+1}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt24_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
        
    pdf.set_xy(px2MM(0), px2MM(-60))
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),'LR',align='C')
    img_add(pdf)
    
    
def page9(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')
    
    pdf.set_font('Calibri',size=10)
    y = mm2PX(pdf.get_y())+32
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),f"24.2")
    text = """Any grievance or complaint of the client will be redressed by the investment advisor in compliance with the provision of the Securities and Exchange Board of India (Investment Advisors) Regulations, 2013."""
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),text)



    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),f"24.3")
    text2 = """All disputes, differences, claims, and questions whatsoever arising from this agreement between the client and investment advisor and/or their respective representatives touching these presents shall be in accordance with and subject to the provisions of The Arbitration and Conciliation Act, 1996, or any statutory modification or re-enactment thereof for the time being in force. Such as arbitration proceedings shall be held at"""
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),text2)
    
    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(335), px2MM(172))
    pdf.cell(px2MM(50),px2MM(14),'Mumbai',border=0)

    # x = mm2PX(pdf.get_x())
    # y = mm2PX(pdf.get_y())
    pdf.set_font('Calibri',size=10)
    bold_mumbai_remaining = """and the language of arbitration"""
    pdf.set_xy(px2MM(372), px2MM(172))
    pdf.multi_cell(px2MM(140),px2MM(14),bold_mumbai_remaining)
    
    bold_mumbai_remaining_2 = """will be English."""
    pdf.set_xy(px2MM(105), px2MM(172+14))
    pdf.multi_cell(px2MM(140),px2MM(14),bold_mumbai_remaining_2)
    

    
    y = mm2PX(pdf.get_y())+7
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)

    pdf.cell(px2MM(10), px2MM(14),"25.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""ADHERENCE TO GRIEVANCE REDRESSAL TIMELINES""")
    
    pt25_text=(
        """Investment advisor shall be responsible to resolve the grievances within the timelines specified under SEBI circulars issued from time to time.""",
        """The Client understands and confirms to send all the complaints and queries in case of any grievance or complaint arising out of and in the course of this agreement, on the email address at grievance@1finance.co.in."""
    )
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    for i in range(1,3):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"25.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt25_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)

    pdf.cell(px2MM(10), px2MM(14),"26.") 
        
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),""" INDEMNITY""")
    
    pt26_text=(
        """The client hereby agrees that he has understood the risks associated with investments and is fully conscious of the same. It is hereby agreed that investment advisor shall not be liable in respect of any loss resulting from such risks.""",
        """Investment advisor shall not be responsible for any loss or damage occasioned as a result of any factor whatsoever other than fraud or gross and wilful negligence on its part. Without prejudice to the above, the client specifically agrees not to hold investment advisor responsible for any loss or damage occasioned by adverse market conditions, force majeure circumstances, delays on the part of companies or other authorities including government authorities in registering transfer of shares and securities, errors of judgement on investment advisor’s part or other factors beyond its control. Notwithstanding the generality of the foregoing, investment advisor shall not be liable if any or all of the securities and/or shares become illiquid due to force majeure circumstance, adverse market conditions, court statutory or regulatory injunctions, attachments or other prohibitions affecting them and/or other factors beyond their control."""
        )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=10)
    for i in range(1,3):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"26.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt26_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
        
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)

    pdf.cell(px2MM(10), px2MM(14),"27.") 
        
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""SEVERABILITY""")
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=10)

    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.cell(px2MM(10), px2MM(14),"27.1")
    
    pdf.set_xy(px2MM(105), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"""If any provision of this agreement shall be held or made invalid by a court decision, statute, rule or otherwise, the remainder of this agreement shall not be affected thereby.""")
    
    
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)

    pdf.cell(px2MM(10), px2MM(14),"28.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),"""FORCE MAJEURE""")
    
    pt28_text=(
        """The investment advisor shall not be liable for delays or errors occurring by reason of circumstances beyond its control, including but not limited to acts of civil or military authority, national emergencies, work stoppages, fire, flood, catastrophe, acts of God, insurrection, war, riot, or failure of communication or power supply.""",
    """The investment advisor shall not be liable in the event of equipment breakdowns beyond its control, the investment advisor shall take reasonable steps to minimise service interruptions but shall have no liability with respect thereto."""
    )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=10)
    for i in range(1,3):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"28.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt28_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
        
        
    pdf.set_xy(px2MM(0), px2MM(-60))
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),'LR',align='C')
    img_add(pdf)
    
    
def page10(pdf):
    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')

    y = mm2PX(pdf.get_y())+14
    pdf.set_xy(px2MM(60), px2MM(y))
    pdf.set_font('CalibriBold',size=10)

    pdf.cell(px2MM(10), px2MM(14),"29.")
    
    pdf.set_font('CalibriBold', style='U',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(420), px2MM(14),""" MISCELLANEOUS""")
    
    pt29_text=(
        """All payments made under this agreement will be made in INR.""",
    """No failure on the part of any party to exercise, and no delay on its part in exercising any right or remedy under this agreement will operate as a waiver thereof, nor will any single or partial exercise of any right. """
    )
    
    y = mm2PX(pdf.get_y())+10
    pdf.set_font('Calibri',size=10)
    for i in range(1,3):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"29.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt29_text[i-1])
        
        y = mm2PX(pdf.get_y())+14
    
    # pdf.set_font('Calibri',size=10)
    # y = mm2PX(pdf.get_y())+32
    
    # pdf.set_xy(px2MM(105), px2MM(y))
    # pdf.multi_cell(px2MM(400), px2MM(14),"""single or partial exercise of any right.""")
    
    pt29_text=(

       """The advice or recommendations given to the client are intended to the benefit of client only, no other person shall be entitled to rely on such information.""",
       """Other than as specifically permitted under this agreement, the client shall not publish or broadcast advertisements, circulars, or other publicity material referring to the investment advisor without the prior written consent of the investment advisor.""",
       """Each party agrees to perform such further actions and execute such further agreements as are necessary to effectuate the purposes hereof."""
       
    )
    
    y = mm2PX(pdf.get_y())+14
    pdf.set_font('Calibri',size=10)
    for i in range(3,6):
        pdf.set_xy(px2MM(80), px2MM(y))
        pdf.cell(px2MM(10), px2MM(14),f"29.{i}")
        
        pdf.set_xy(px2MM(105), px2MM(y))
        pdf.multi_cell(px2MM(400), px2MM(14),pt29_text[i-3])
        
        y = mm2PX(pdf.get_y())+14
        

# _____

    pdf.set_font('CalibriBold',size=10)
    pdf.set_xy(px2MM(80), px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"Agreed and Accepted by Client & 1 Finance:",align='L')

    pdf.set_xy(px2MM(0), px2MM(-60))
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),align='C')


    img_add(pdf)


def page11(pdf):

    pdf.add_page()
    pdf.set_fill_color(*hex2RGB('#FFFFFF'))
    pdf.rect(0, 0, px2MM(2480), px2MM(3508), 'F')

    y = mm2PX(pdf.get_y())+ 32
    
    #### Details of Investment Advisers ####
    pdf.set_font('CalibriBold',style="U",size=12)
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.multi_cell(px2MM(400), px2MM(14),"Details of Investment Advisors:")


    #x = mm2PX(pdf.get_x() + 20)
    x = 80
    y = mm2PX(pdf.get_y() + 7)
    
    """Col 1 Vals"""
    
    col1_vals = ['Name as registered with SEBI','Brand name','Type of registration','Registration Number ','Validity of registration','Corporate Office Address', 'Principal Officer', 'Contact details',
    'Corresponding SEBI regional/local \noffice address']

    for i in range(9):
        if i == 0:
            pdf.set_font('CalibriBold',size=10)
            pdf.set_xy(px2MM(x),px2MM(y + 3))
            pdf.rect(px2MM(80), px2MM(math.floor(y)), px2MM(160), px2MM(20),'D')
            pdf.multi_cell(px2MM(400), px2MM(14),col1_vals[i])

        elif i == 5:
            pdf.rect(px2MM(80), px2MM(math.floor(y)), px2MM(160), px2MM(60),'D')
            pdf.set_font('Calibri',size=10)
            pdf.set_xy(px2MM(x),px2MM(y + 6))
            pdf.multi_cell(px2MM(400), px2MM(14),col1_vals[i])
            y  += 40
        elif i == 8:
            pdf.rect(px2MM(80), px2MM(math.floor(y)), px2MM(160), px2MM(65),'D')
            pdf.set_font('Calibri',size=10)
            pdf.set_xy(px2MM(x),px2MM(y + 6))
            pdf.multi_cell(px2MM(400), px2MM(14),col1_vals[i])
            y += 45
        else:
            pdf.set_font('Calibri',size=10)
            pdf.set_xy(px2MM(x),px2MM(y + 3))
            pdf.rect(px2MM(80), px2MM(math.floor(y)), px2MM(160), px2MM(20),'D')
            pdf.multi_cell(px2MM(400), px2MM(14),col1_vals[i])
        y += 20
    y = 94 #Resseting y to the begining of the table


    # Col2 ######################################3
    col2_vals = ['1 Finance Private Limited','1 Finance','Non-Individual', 'INA000017523','December 22, 2022 - Perpetual','Unit No. 1101 & 1102, 11th Floor, B-Wing, Lotus \nCorporate Park, Goregaon (E), Mumbai-400063','Mr. Akhil Rathi','po@1finance.co.in','Securities and Exchange Board of India, \nSEBI Bhavan II, Plot No: C7, “G” Block, \nBandra Kurla Complex, Bandra (East), Mumbai-400051']

    #x = mm2PX(pdf.get_x()+75)
    x = 241
    y = 94
    for i in range(9):
        pdf.set_font("Calibri",  size=10)
        pdf.set_text_color(*hex2RGB('#000000'))

        if i == 0 or i == 1 or i == 2 or i == 3:
            pdf.set_font('CalibriBold',size=10)
            pdf.set_xy(px2MM(x),px2MM(y + 3))
            pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(40))
            pdf.multi_cell(px2MM(400), px2MM(14),col2_vals[i])

        elif i == 5:
            pdf.set_font('Calibri',size=10)
            pdf.set_xy(px2MM(x),px2MM(y + 6))
            pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(60))
            pdf.multi_cell(px2MM(280), px2MM(14),col2_vals[i])
            y += 40

        elif i == 7:
                pdf.set_font("Calibri",style = "U" , size=10)   
                pdf.set_xy(px2MM(x),px2MM(y + 3))
                pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(20))
                # pdf.set_text_color(*hex2RGB('#0000FF')) # Initially It was set to Blue
                pdf.set_text_color(*hex2RGB('#000000'))
                pdf.multi_cell(px2MM(280), px2MM(14),col2_vals[i])

        elif i == 8:
            pdf.set_font('Calibri',size=10)
            pdf.set_xy(px2MM(x),px2MM(y + 6))
            pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(65))
            pdf.multi_cell(px2MM(280), px2MM(14),col2_vals[i])
            y += 45


        else:   
            pdf.set_font('Calibri',size=10)
            pdf.set_xy(px2MM(x),px2MM(y + 3))
            pdf.rect(px2MM(x-1), px2MM(y), px2MM(230), px2MM(20))
            pdf.multi_cell(px2MM(400), px2MM(14),col2_vals[i])
        y += 20


    

### Details Of Client Table ####
    y = y + 14
    pdf.set_font("CalibriBold",style="U",  size=12)
    pdf.set_xy(px2MM(80),px2MM(y))
    pdf.multi_cell(px2MM(600), px2MM(14),"Details of Client")

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
        pdf.set_font("Calibri",  size=10)
        x =  len(table2_col2_vals[i]) / 50
        if x < int(x):
            x+=1
        else:
            x+=1
        x=int(x)
        if i == 5:
            pdf.set_font("CalibriBold",  size=10)
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

    pdf.set_xy(px2MM(0), px2MM(-60))
    pdf.multi_cell(px2MM(600), px2MM(14),str(pdf.page_no()),align='C')
    img_add(pdf)
pdf_creator(pdf)

