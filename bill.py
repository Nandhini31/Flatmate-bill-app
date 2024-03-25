from fpdf import FPDF


class Bill:

    """
    Object that contains data about a bill, such as total amount and period
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """ Creates a flatmate object """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return round(to_pay, 2)


class PDFReport:
    """
    Contains a pdf file that data about flatmates and bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_amount = flatmate1.pays(bill=bill, flatmate2=mary)
        flatmate2_amount = flatmate2.pays(bill=bill, flatmate2=john)
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=80, txt="Flatmates Bill",  align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period:")
        pdf.cell(w=100, h=40, txt=f"{bill.period}",  ln=1)
        pdf.cell(w=200, h=40, txt="Total amount:")
        pdf.cell(w=100, h=40, txt=f"{bill.amount}",  ln=1)
        pdf.cell(w=100, h=40, txt=f"{flatmate1.name}:")
        pdf.cell(w=100, h=40, txt=f"£ {flatmate1_amount}",  ln=1)
        pdf.cell(w=100, h=40, txt=f"{flatmate2.name}:")
        pdf.cell(w=100, h=40, txt=f"£   {flatmate2_amount}",  ln=1)
        pdf.output(self.filename)



bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print("John pays", john.pays(bill=bill, flatmate2=mary))
print("Mary pays", mary.pays(bill=bill, flatmate2=john))
pdf = PDFReport("bill.pdf").generate(john, mary, bill)