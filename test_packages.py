from flask import Flask, render_template, request

app = Flask(__name__)

# Constants
totalTenure = 21
fundAmount = 500000
numberOfParticipants = 20

# Functions
def calculate_simple_interest(bid_value, interest_rate):
    return (fundAmount - bid_value) * interest_rate / 12

def commission(bid_value):
    return bid_value / numberOfParticipants

def monthly_payment(bid_value):
    return (fundAmount - bid_value) / numberOfParticipants

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bid_value = int(request.form.get('bid_value'))
        interest_rate = float(request.form.get('interest_rate')) / 100
        current_month = int(request.form.get('current_month'))

        commission_val = commission(bid_value)
        monthly_payment_val = monthly_payment(bid_value)
        interest_list = []

        count = 1
        for each_coming_month in range(current_month, totalTenure + 1):
            interest = count * calculate_simple_interest(bid_value, interest_rate)
            interest_list.append((each_coming_month, interest))
            count += 1

        return render_template('results.html', 
                               current_month=current_month,
                               commission=commission_val,
                               monthly_payment=monthly_payment_val,
                               interests=interest_list)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
