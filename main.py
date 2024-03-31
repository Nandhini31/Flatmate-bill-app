from flask import Flask, render_template
from flask.views import MethodView
from wtforms import Form, StringField

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template("index.html")

class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", billform=bill_form)

class ResultsPage(MethodView):
    pass

class BillForm:
    amount = StringField("Bill amount: ")
    period = StringField("Bill period: ")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.run(debug=True)