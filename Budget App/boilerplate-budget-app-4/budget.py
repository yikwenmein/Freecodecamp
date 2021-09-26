


class Category:
    test =[]
    def __init__(self, budget_category):
        self.budget_category =budget_category
        self.ledger =list()
        self.withdraws = 0
    def check_funds(self,amount):
        check =0
        for x in self.ledger:
  
            check= check+list(x.values())[0]
        if check >= amount:
            return True
        else:
            return False

    def deposit(self,amount, description=""):
        self.ledger.append({"amount":amount,"description":description})
        #self.test.append({"amount":amount,"description":description})
    def withdraw(self,amount, description=""):
        
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            self.withdraws = self.withdraws+amount
            print("True")
            return True
        else:
            print("False")
            return False
    def get_balance(self):
        balance =0
        for val in self.ledger:
  
            balance= balance+list(val.values())[0]
        return balance

    def transfer(self,amount,new_category):
        # current =0
        # for p in self.ledger:
        
        #     current= current+list(p.values())[0]
        if self.check_funds(amount):
            
            self.withdraw(amount,"Transfer to "+ new_category.budget_category)
            #self.withdraws = self.withdraws+amount
            new_category.deposit(amount,"Transfer from "+ self.budget_category)
            
            #self.ledger.append({"amount":amount,"description":"Transfer from "})

            #print("True")
            return True
        else:
           # print("False")
            return False
    def __str__(self):
        title =self.budget_category.center(30,"*")
        size =list()
        balance = self.get_balance()
        total = "Total: "+format(balance,".2f")
        for x in self.ledger:
            new=list(x.values())[0]
            new1 =list(x.values())[1]
            new1 = new1[:23]
            new  = format(new,".2f")
            new = new.rjust(30-len(new1))
            final = new1+new
            size.append(final)
        listings =title+"\n"+"\n".join(size)+"\n"+total
        return listings
def create_spend_chart(category_list):
    title  = "Percentage spent by category"
    lent  =len(category_list)
    total_spendings = 0
    percentages =list()
    Category_names =list()
    for i in range(lent):
        total_spendings+=category_list[i].withdraws
        Category_names.append(category_list[i].budget_category)
    for i in range(lent):
        percentage = ((category_list[i].withdraws)/total_spendings)*100
        percentages.append(percentage)

    #for i in category_list:
    #chart = [x for x in range(0,100,10)]
    chart =list()
    value = 100
    while value >= 0:
        y = f"{value:3d}|"
        gap = ""
        for i in range(len(percentages)):
            if percentages[i] >= value:
                markings = " o "
            else:
                markings = "   "
            gap+=markings
        chart.append(y + gap + ' ')
        value-=10
    length = max(map(len, Category_names))

    x = []
    i = length

    while i > 0:
        l="    "
        for j in range(len(Category_names)):
            try:
                l+=Category_names[j][length-i].center(3, ' ')
            except:
                l+='   '
        l+= ' '
        x.append(l)
        i-=1  

    final = ('    ') + ('-' * len(category_list) * 3) + '-'

    return title + '\n' + '\n'.join(chart) + '\n' + final + '\n' + '\n'.join(x)