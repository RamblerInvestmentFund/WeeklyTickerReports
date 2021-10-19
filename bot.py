import slack
import datetime
from fpdf import FPDF
import urllib.request
import os
import requests
from finviz import Screener
import pdfkit
import quantstats as qs

#stock = Screener(tickers=['AAPL'])

#qs.extend_pandas()
#stock = qs.utils.download_returns("AAPL")
#qs.reports.html(returns = stock, benchmark = "SPY", output='aapl.html')
pdfkit.from_file('aapl.html', 'aapl_1.pdf')

# today = datetime.date.today()
# # ---- Cover Page
# pdf = FPDF(orientation='landscape')
# pdf.set_margin(2)
# pdf.add_page()
# pdf.set_fill_color(128, 0, 0)
# pdf.rect(x = 0, y = 0, w = pdf.w, h = 12, style = 'F')
# # ---- Date
# pdf.set_font("Times", size=22)
# pdf.set_font(style='B')
# pdf.set_text_color(237, 232, 228)
# pdf.cell(txt=str(today), align='C')
# # ----
# pdf.set_fill_color(128, 0, 0)
# pdf.rect(x = 0, y = 198, w = pdf.w, h = 12, style = 'F')
# pdf.image(x = -0.5, y = 12, w = pdf.w + 1, name='RIFLogo(B&W).png')

# # ---- Second Page
# pdf.add_page()
# pdf.set_fill_color(128, 0, 0)
# pdf.rect(x = 0, y = 0, w = pdf.w, h = 12, style = 'F')
# pdf.rect(x = 0, y = 198, w = pdf.w, h = 12, style = 'F')
# pdf.set_fill_color(0, 0, 0)
# pdf.rect(x = 0, y = 12, w = pdf.w, h = 186, style = 'F')
# pdf.image(x=1, y=13, w=(pdf.w+1)/2, name='./charts/AAPL_1632970177.png')

# # ---- Third Page
# pdf.add_page()
# pdf.set_fill_color(128, 0, 0)
# pdf.rect(x = 0, y = 0, w = pdf.w, h = 12, style = 'F')
# pdf.rect(x = 0, y = 198, w = pdf.w, h = 12, style = 'F')
# pdf.set_fill_color(0, 0, 0)
# pdf.rect(x = 0, y = 12, w = pdf.w + 1, h = 186, style = 'F')

# # ---- PDF Output
# pdf.output('pdf_2.pdf')


# # ---- Call Bot and Send Portfolio
# # client = slack.WebClient(token = '####')
# # client.files_upload(channels = '#sector-materials', file='./pdf_1.pdf')