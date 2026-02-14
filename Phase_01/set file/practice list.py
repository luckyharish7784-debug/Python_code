'''
after create group
'''

total_amount= float(input('enter total amount : '))
total_mem = int(input('enter members : '))
rem = total_amount/total_mem
new =0
total =0
print(f'{rem} to every person split amount')
for i in range(total_mem):
    user_amount=int(input('enter user amount : '))
    # if user_amount == 0:
    #     print(f'{rem},to full amount')
    if (total_amount >= user_amount and user_amount > 0):
        if total_amount != total :
            new = rem - user_amount
            print(f'{new}, to pay remaining amount')
        elif total_amount:
            print('more than total amount ')
            print(f'to pay split amount {rem}')
        total += user_amount
    else:
        print('Invalid amount less than total amount ')
    




