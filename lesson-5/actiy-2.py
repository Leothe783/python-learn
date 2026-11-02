actual_cost=float(input('enter actual cost'))
sale_amount=float(input('enter sale amount'))

if sale_amount > actual_cost :
    amount= sale_amount-actual_cost
    print('total profit ={0}'.format(amount))
else:
     print('no profit')