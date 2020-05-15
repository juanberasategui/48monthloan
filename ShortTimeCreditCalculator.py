#Santander Bank loan calculator adjusted to interest rates and inflation

initial_loan = float(input('Please the amount of your loan'))
first_commision = 0.15*initial_loan
total_financed = initial_loan+first_commision
months = int(input('For how long do you want to hold the credit for? (max 48)'))
EAR = 0.0595      #EAR is from Santander, but it is possible to change it and the the program would still work
inflation_2024 = (0.0105, 0.0143, 0.0155, 0.0164, 0.0177)
EAR_month = (1+EAR)**(1/12)-1
interest_rates = 0.0      #Interest rates and inflation are limited to Spain, but can be adjusted to other countries
growth_money = ((EAR_month + interest_rates - (inflation_2024[1]/12)),
                (EAR_month + interest_rates - (inflation_2024[2]/12)),
                (EAR_month + interest_rates - (inflation_2024[3]/12)),
                (EAR_month + interest_rates - (inflation_2024[4]/12)))

#Inflation rates are retrieved the 13/05/2020 from: https://www.statista.com/statistics/271077/inflation-rate-in-spain/
#Interest rates are retrieved the 13/05/2020 from: https://tradingeconomics.com/spain/interest-rate

if months <= 12:
    total_payment = round(total_financed/((1+(growth_money[0]))**months), 4)
    total_permonth = round(total_payment/months, 4)

    print('With a loan of:', initial_loan, 'for', months, 'months\n' 
          'You will have to pay a total of:', total_payment,'which is equivalent to:', total_permonth, 'per month')
elif months <= 24:
    moneypermonth = total_financed/months
    firstyear = ((moneypermonth*12)/((1+(growth_money[0]))**12))
    secondyear = ((moneypermonth)*(months-12))/((1+(growth_money[1]))**(months-12))
    total_payment = round(firstyear+secondyear, 2)
    total_permonth = round(total_payment/months, 2)

    print('With a loan of:', initial_loan, 'for', months, 'months\n' 
          'You will have to pay a total of:', total_payment,'which is equivalent to:', total_permonth, 'per month')

elif months <= 36:
    moneypermonth = (total_financed / months)
    firstyear = ((moneypermonth * 12) / ((1 + (growth_money[0])) ** 12))
    secondyear = ((moneypermonth * 12) / ((1 + (growth_money[1])) ** 12))
    thirdyear = ((moneypermonth) * (months - 24)) / ((1 + (growth_money[2])) ** (months - 24))
    total_payment = round(firstyear+secondyear+thirdyear,2)
    total_permonth = round(total_payment/months, 2)

    print('With a loan of:', initial_loan, 'for', months, 'months\n'
    'You will have to pay a total of:', total_payment, 'which is equivalent to:', total_permonth, 'per month')


elif months <=48:
    moneypermonth = (total_financed / months)
    firstyear = ((moneypermonth * 12) / ((1 + (growth_money[0])) ** 12))
    secondyear = ((moneypermonth * 12) / ((1 + (growth_money[1])) ** 12))
    thirdyear = (moneypermonth * 12) / ((1 + (growth_money[2])) ** 12)
    fourthyear = ((moneypermonth) * (months - 36)) / (1 + (growth_money[3])) ** (months - 36)
    total_payment = round(firstyear + secondyear + thirdyear + fourthyear,2)
    total_permonth = round(total_payment / months, 2)

    print('With a loan of:', initial_loan, 'for', months, 'months\n'
                                                          'You will have to pay a total of:', total_payment,
          'which is equivalent to:', total_permonth, 'per month')
    
else:
  print('Please try again. We only offer loans up to, and including, 48 months')
