import datetime
import datetime as dt
from reportlab.lib.enums import TA_CENTER,TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


class WelderLabel:

    def __init__(self, work_order_id, customer_number, plate_code, body_code, mfg_end_code, end_code, tda,line_id):
        # add Paragraph style ##
        my_Style = ParagraphStyle('My Para style',
                                  fontName="Helvetica-Bold",
                                  fontSize=18,
                                  alignment=TA_LEFT,
                                  textColor='grey',
                                  borderWidth=.5,
                                  borderColor='grey',
                                  backColor='white',
                                  borderPadding=(10, 20, 20),
                                  leading=20
                                  )
        my_Style1 = ParagraphStyle('My Para style',
                                   fontName="Helvetica",
                                   fontSize=18,
                                   alignment=TA_LEFT,
                                   textColor='grey',
                                   borderWidth=0,
                                   borderColor='grey',
                                   backColor='white',
                                   borderPadding=(10, 20, 20),
                                   leading=20
                                   )
        width, height = A4  # size of the file
        my_path = 'test.pdf'
        top_margin=40
        c = canvas.Canvas(my_path, pagesize=A4)
        p1 = Paragraph('Work Order Number:', my_Style1)  # add style
        p1.wrapOn(c, 400, 50)  # width , height of Paragraph
        p1.drawOn(c, width - 500, height - (60+top_margin))  # location of Paragraph

        p11 = Paragraph(work_order_id, my_Style)  # add style
        p11.wrapOn(c, 400, 50)  # width , height of Paragraph
        p11.drawOn(c, width - 500, height - (100+top_margin))  # location of Paragraph

        p2 = Paragraph('Customer Number:', my_Style1)  # add style
        p2.wrapOn(c, 400, 50)  # width , height of Paragraph
        p2.drawOn(c, width - 500, height - (160+top_margin))  # location of Paragraph

        p21 = Paragraph(customer_number, my_Style)  # add style
        p21.wrapOn(c, 400, 50)  # width , height of Paragraph
        p21.drawOn(c, width - 500, height - (200+top_margin))  # location of Paragraph

        p3 = Paragraph('MFG Plate Code:', my_Style1)  # add style
        p3.wrapOn(c, 400, 50)  # width , height of Paragraph
        p3.drawOn(c, width - 500, height - (260+top_margin))  # location of Paragraph

        p31 = Paragraph(plate_code, my_Style)  # add style
        p31.wrapOn(c, 400, 50)  # width , height of Paragraph
        p31.drawOn(c, width - 500, height - (300+top_margin))  # location of Paragraph

        p4 = Paragraph('Body Code:', my_Style1)  # add style
        p4.wrapOn(c, 400, 50)  # width , height of Paragraph
        p4.drawOn(c, width - 500, height - (360+top_margin))  # location of Paragraph

        p41 = Paragraph(body_code, my_Style)  # add style
        p41.wrapOn(c, 400, 50)  # width , height of Paragraph
        p41.drawOn(c, width - 500, height - (400+top_margin))  # location of Paragraph

        p5 = Paragraph('MFG End Code:', my_Style1)  # add style
        p5.wrapOn(c, 400, 50)  # width , height of Paragraph
        p5.drawOn(c, width - 500, height - (460+top_margin))  # location of Paragraph

        p51 = Paragraph(mfg_end_code, my_Style)  # add style
        p51.wrapOn(c, 400, 50)  # width , height of Paragraph
        p51.drawOn(c, width - 500, height - (500+top_margin))  # location of Paragraph

        p6 = Paragraph('End Code:', my_Style1)  # add style
        p6.wrapOn(c, 400, 50)  # width , height of Paragraph
        p6.drawOn(c, width-500, height-(560+top_margin))  # location of Paragraph

        p61 = Paragraph(end_code, my_Style)  # add style
        p61.wrapOn(c, 400, 50)  # width , height of Paragraph
        p61.drawOn(c, width-500, height-(600+top_margin))  # location of Paragraph

        p7 = Paragraph('TDA:', my_Style1)  # add style
        p7.wrapOn(c, 400, 50)  # width , height of Paragraph
        p7.drawOn(c, width - 500, height - (660+top_margin))  # location of Paragraph

        p71 = Paragraph(tda, my_Style)  # add style
        p71.wrapOn(c, 400, 50)  # width , height of Paragraph
        p71.drawOn(c, width - 500, height - (700+top_margin))  # location of Paragraph

        date = dt.datetime.now()
        format_date = f"{date:%a, %b %d %Y}"
        pheader = Paragraph(line_id, my_Style1)  # add style
        pheader.wrapOn(c, 400, 50)  # width , height of Paragraph
        pheader.drawOn(c, width - 500, height - 40)  # location of Paragraph

        pfooter = Paragraph(format_date, my_Style1)  # add style
        pfooter.wrapOn(c, 400, 50)  # width , height of Paragraph
        pfooter.drawOn(c, width - 500, height - (760+top_margin))  # location of Paragraph

        c.save()
