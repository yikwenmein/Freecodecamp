def add_time(start, duration,weekday=False):
    days_past =0
    extra_hour =0
    #extra_mins=0
    days_after =""
    new_day =""
    start_time,period =start.split()
    hr,mins =start_time.split(":")
    hr = int(hr)
    mins= int(mins)
   
    end_time_hr,end_time_mins =duration.split(":")
    end_time_hr =int(end_time_hr)
    end_time_mins =int(end_time_mins)
    result_hr = hr+end_time_hr
   
    result_mins = mins+end_time_mins
    #new_time =str(result_hr)+":"+str(result_mins)
    if result_mins>=60:
        extra_hour =result_mins//60
        #print("extra_hour_one", extra_hour)
        result_hr =result_hr+extra_hour
        result_mins =result_mins%60
        #print("First result hour",result_hr)
        #result_hr=result_hr+extra_hour
        
    if result_hr< 12 and hr<12:
        if period =="AM":
            new_period =" AM"
        if period =="PM":
            new_period=" PM"
                    
    if result_hr>=12 and hr<12:
        
        am_pm =result_hr//12
        #print("am_pm",am_pm)
        if am_pm%2==0 and period =="AM":
            new_period=" AM"
        if am_pm%2==0 and period =="PM":
            new_period=" PM"
        if am_pm%2==1 and period =="AM":
            new_period=" PM"
        if am_pm%2==1 and period =="PM":
            new_period=" AM"
            days_past= 1
                
    if result_hr>=12 and hr==12:
        am_pm =result_hr//12
      
        if am_pm%2==0 and period =="AM":
           new_period=" PM"
        if am_pm%2==0 and period =="PM":
            new_period=" AM"
            days_past =1
        if am_pm%2==1 and period =="AM":
            new_period=" AM"
        if am_pm%2==1 and period =="PM":
            new_period=" PM"

    #print("period after",period)
    days = result_hr//24+ days_past
    #print("Days past",days)
    result_hr =result_hr%12
    if result_hr==0:
        result_hr=12
        
   
    #print("Days past",days)    
        
   
    
    if len(str(result_mins))!=2:
        result_mins ="0"+str(result_mins)
    
    if days==1:
        days_after =" (next day)"
    if days>1:
        days_after =" ("+str(days)+" days later)"

    if weekday:
         days_check =days%7
         days_dict = {0:"monday",1:"tuesday",2:"wednesday",3:"thursday",4:"friday",5:"saturday",6:"sunday"}
         week_day =weekday.lower()
         for k,v in days_dict.items():
             if v==week_day:
                 #week_num =k
                 final =(k+days_check)%7
                 new_day =days_dict[final]
                 new_day1 =new_day[0].capitalize()
                 rest_newday=new_day[1:]
                 final_day =new_day1+rest_newday
                 new_time= str(result_hr)+":"+str(result_mins)+new_period+", "+final_day+days_after
                 new_time =new_time.rstrip()
                 return new_time
    new_time = str(result_hr)+":"+str(result_mins)+new_period+days_after
    new_time =new_time.rstrip()
    return new_time