from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
        ["Items", "Price"],
        ["Cereal", "4.99"],
        ["Eggs", "2.99"],
        ["Milk", "1.99"],
        ["Subtotal", "9.97"],
        ["Discount", "2.00"],
        ["Total", "7.97"]
        ]

pdf = SimpleDocTemplate("receipt.pdf", pageSize = A4)
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1
title = Paragraph("Code Ninjas", title_style)

style = TableStyle(
    [
     ("BOX", (0,0), (-1, -1), 1, colors.black),
     ("GRID", (0,0), (5,5), 1, colors.black),
     ("BACKGROUND", (0,0), (3,0), colors.green),
     ("TEXTCOLOR", (0,0), (-1, 0), colors.whitesmoke),
     ("ALIGN", (0,0), (-1, -1), "CENTER"),
     ("BACKGROUND", (0,1), (-1,-1), colors.beige),

     ]
)

table = Table(DATA, style = style)

pdf.build([title, table])