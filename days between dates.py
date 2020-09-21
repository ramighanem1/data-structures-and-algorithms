#return number of days in each month
#February is 28 days
def num_day(month):
    if month==2:
        return 28
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    else:
        return 30

#return the next day 
def get_next(birth_year,birth_month,birth_day):
    if birth_month==12 and birth_day==num_day(12):
        return birth_year+1,1,1
    else:
        if birth_day==num_day(birth_month):
            return birth_year,birth_month+1,1
        else:
            return birth_year,birth_month,birth_day+1
            
        
def is_befor(birth_year,birth_month,birth_day,current_year,current_month,current_day):
    if birth_year < current_year:
        return True
    if birth_year==current_year:
         if birth_month < current_month:
             return True
         if birth_month == current_month:
             return birth_day < current_day
    return False
          
        
      
    
def is_accepted(birth_year,birth_month,birth_day,current_year,current_month,current_day):
    if(birth_month>12 or birth_month<=0):
        return False
    if(current_month>12 or current_month<=0):
        return False
    if(birth_day>num_day(birth_month) or birth_day<=0):
        return False
    if(current_day>num_day(current_month) or current_day<=0):
        return False
    
    return True
    

def daysbetweendates(birth_year,birth_month,birth_day,current_year,current_month,current_day):
    
    if (is_accepted(birth_year,birth_month,birth_day,current_year,current_month,current_day)):
        
        if(is_befor(birth_year,birth_month,birth_day,current_year,current_month,current_day)):
            days=0
            while(birth_year !=current_year or birth_month != current_month or birth_day!=current_day):
                days=days+1
                birth_year,birth_month,birth_day=get_next(birth_year,birth_month,birth_day)

            return days
        else:
            return -1
    else:
        return -1
        
    
        

    
    
        
#return -1 if the curent date befor birth date or input is not accepted 
print("{0} days".format(daysbetweendates(2020,2,28,2021,2,28)))

