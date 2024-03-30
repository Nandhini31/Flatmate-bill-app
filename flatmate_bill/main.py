import webbrowser

from fpdf import FPDF

from bill import Bill
from flatmate import Flatmate


class PDFReport:
    """
    Contains a pdf file that data about flatmates and bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_amount = flatmate1.pays(bill=bill, flatmate2=flatmate_two)
        flatmate2_amount = flatmate2.pays(bill=bill, flatmate2=flatmate_one)
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=24)

        pdf.cell(w=0, h=80, txt="Flatmates Bill",  align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period:")
        pdf.cell(w=100, h=40, txt=f"{bill.period}",  ln=1)
        pdf.cell(w=200, h=40, txt="Total amount:")
        pdf.cell(w=100, h=40, txt=f"£ {bill.amount}",  ln=1)
        pdf.cell(w=100, h=40, txt=f"{flatmate1.name}:")
        pdf.cell(w=100, h=40, txt=f"£ {flatmate1_amount}",  ln=1)
        pdf.cell(w=100, h=40, txt=f"{flatmate2.name}:")
        pdf.cell(w=100, h=40, txt=f"£ {flatmate2_amount}",  ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


total_bill_amount = int(input("What is the bill amount for the total period "))
total_bill_period = input("What is the bill period ")
flatmate_name_one = str(input("What is the name of flatmate one "))
flatmate_name_two = str(input("What is the name of flatmate two "))
flatmate_period_one = int(input(f"How many days did {flatmate_name_one} stay in the house "))
flatmate_period_two = int(input(f"How many days did {flatmate_name_two} stay in the house "))
bill = Bill(amount=total_bill_amount, period=total_bill_period)
flatmate_one = Flatmate(name=flatmate_name_one, days_in_house=flatmate_period_one)
flatmate_two = Flatmate(name=flatmate_name_two, days_in_house=flatmate_period_two)

print(f"{flatmate_name_one} pays", flatmate_one.pays(bill=bill, flatmate2=flatmate_two))
print(f"{flatmate_name_two} pays", flatmate_two.pays(bill=bill, flatmate2=flatmate_one))
pdf = PDFReport("bill.pdf").generate(flatmate_one, flatmate_two, bill)