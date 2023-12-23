# Constants
totalTenure = 21
fundAmount = 500000
numberOfParticipants = 20
bid_value = int(input("Enter the bid Value :"))
interest_rate = float(input("Entere the inteset rate :"))
currentMonth = int(input("Enter Current Month :"))
# Functions
def calculate_simple_interest(bid_value, interest_rate):
    return (fundAmount - bid_value) * interest_rate / 12

def commission(bid_value):
    return bid_value / numberOfParticipants

def monthly_payment(bid_value):
    return (fundAmount - bid_value) / numberOfParticipants

def stats(current_month, bid_value, interest_rate):
    print(f"Current Month {current_month}, Commission is :{commission(bid_value)} and you need to pay for this Month {monthly_payment(bid_value)}")
    count = 1
    for each_coming_month in range(current_month, totalTenure + 1):
        interest = count * calculate_simple_interest(bid_value, interest_rate)
        print(f"For month {each_coming_month}, Collected Interest is: {interest}")
        count += 1

# Main Execution
if __name__ == "__main__":
    # Validating input values
    stats(currentMonth, bid_value, interest_rate)
