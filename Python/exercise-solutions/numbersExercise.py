# EXERCISE 1

cost_per_hour = 0.51
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day

print('How much does it cost to operate one server per day?')
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('How much does it cost to operate one server per month?')
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))

# EXERCISE 2

cost_per_day_twenty = 20 * cost_per_day
cost_per_month_twenty = 20 * cost_per_month

budget = 918
operational_days = budget / cost_per_day

print('How much does it cost to operate one server per day?')
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))

print('How much does it cost to operate one server per month?')
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))

print('How much does it cost to operate twenty servers per day?')
print('Cost to operate twenty servers per day is ${:.2f}.'.format(cost_per_day_twenty))

print('How much does it cost to operate twenty servers per month?')
print('Cost to operate twenty servers per month is ${:.2f}.'.format(cost_per_month_twenty))

print('How many days can I operate one server with $918?')
print('A server can operate on a ${0:.2f} budget for {1:.0f} days.'.format(budget, operational_days))