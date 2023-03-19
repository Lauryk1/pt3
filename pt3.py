def get_data(filename):
    
    #loop for validating date format
    while True:
        date = input('Enter the "from date" in mm/dd/yyyy format or "all": ')
        
        #if "all" is entered this will throw error and therefore we have except block
        try:
            date_attributes = list(map(int, date.split('/')))
            if 1 <= date_attributes[0] <= 12 and 1 <= date_attributes[1] <= 31:
                break
            else:
                print('Enter the date in mm/dd/yyyy format or "all".')
        except:
            if date.lower() == 'all':
                break
            else:
                print('Enter the date in mm/dd/yyyy format or "all".')
                
    #initializing dictionary to store data
    data_dict = {
        'total_employee': 0,
        'total_hours' : 0,
        'total_tax' : 0,
        'total_net_pay' : 0
    }
    
    #reading text file
    with open(filename) as file:
        data = file.readlines()
        
    #printing format
    print('{:<15} {:<15} {:<25} {:<15} {:<12} {:<8} {:<15} {:<12} {:<15}'.format(
            'From Date',
            'To date',
            'Employee Name',
            'Hours Worked',
            'Hourly Rate',
            'Gross Pay',
            'Income Tax Rate',
            'Income Taxes',
            'Net Pay'))
    
    #processing line by line
    for line in data:
        line = line.split('|')
        from_date = line[0]
        from_date_attributes = list(map(int, date.split("/")))
        
        #checking whether date is in range
        try:
            if from_date_attributes[2] >= date_attributes[2]:
                if from_date_attributes[1] >= date_attributes[1]:
                    if from_date_attributes[0] >= date_attributes[0]:
                        pass
                    else:
                        continue
                else:
                    continue
            else:
                continue
        
        #if try throws error that means user has entered "all"
        except:
            pass
        
        to_date = line[1]
        employee_name = line[2]
        hours_worked = float(line[3])
        pay_rate = float(line[4])
        income_tax_rate = float(line[5])
        gross_pay = hours_worked*pay_rate
        income_taxes = gross_pay * (income_tax_rate/100)
        net_pay = gross_pay - income_taxes
        
        #increasing attributes
        data_dict['total_employee'] += 1
        data_dict['total_hours'] += hours_worked
        data_dict['total_tax'] += income_taxes
        data_dict['total_net_pay'] += net_pay
        
        #printing the data
        print('{:<15} {:<15} {:<25} {:<15} {:<12} {:<8} {:<15} {:<12} {:<15}'.format(
            from_date,
            to_date,
            employee_name,
            hours_worked,
            pay_rate,
            gross_pay,
            income_tax_rate,
            income_taxes,
            net_pay))
    #printing final attributes
    print('{:<30} {:<15} {:<20} {:<20}'.format(
            'Total Number of Employees',
            'Total Hours',
            'Total Tax',
            'Total Net Pay'))
    
    print('{:<30} {:<15} {:<20} {:<20}'.format(
            data_dict['total_employee'],
            data_dict['total_hours'],
            data_dict['total_tax'],
            data_dict['total_net_pay']))

#initializing empty list for writing to file
data_list = []

#runnning loop until user decides to break
while True:
    
    #getting details
    print('Enter the following details:')
    from_date = input('Enter the from date: ')
    to_date = input('Enter the to date: ')
    employee_name = input('Enter the employee name: ')
    hours_worked  = input('Enter the hours worked: ')
    pay_rate = input('Enter the pay rate: ')
    income_tax_rate = input('Enter the income tax rate: ')
    
    #appending to data list
    data_list.append(from_date+'|'+to_date+'|'+employee_name+'|'+hours_worked+'|'+pay_rate+'|'+income_tax_rate+'\n')
    
    #asking for choice
    choice = input('Enter "Q" to quit or any key to continue adding more employees: ').lower()
    if choice == 'q':
        break
        
file_name = 'data.txt'
#writing to file line by line
with open(file_name, 'a') as file:
    file.writelines(data_list)

#calling function to retrieve data
get_data(file_name)