def arithmetic_arranger(problems,optional=False):
    #problems=args[0]
    if len(problems)>5:
        return "Error: Too many problems."
        #print("Error:Too many problems.")
    space = 4    
    vals = list()
    line1 =""
    line2 =""
    line3 =""
    line4 =""

    for prob in range(len(problems)):
        vals.append(problems[prob])
        l = list()
    for i in range(len(vals)):
        l.append(vals[i].split())

    for jj in range(len(l)):
        if l[jj][1] not in ["+","-"]:
            return "Error: Operator must be '+' or '-'."
        if l[jj][0].isdigit()==False:
            return "Error: Numbers must only contain digits."
        if l[jj][2].isdigit()==False:
            return "Error: Numbers must only contain digits."
        if len(l[jj][0])>4:
            return "Error: Numbers cannot be more than four digits."
        if len(l[jj][2])>4:
            return "Error: Numbers cannot be more than four digits."
        maxi  = max(len(l[jj][0]),len(l[jj][2]))
        maxi = maxi+2
        #maxim  = abs(len(l[jj][2])-len(l[jj][0]))
        #line1 = line1+" "*(space-len(l[jj][0])-1) + l[jj][0]
        if len(l[jj][0])>=len(l[jj][2]):
            line1 = line1+ " "*2+l[jj][0] +" "*(space) 
            #line2 = line2+l[jj][1]+" "+l[jj][2]+" "*(space)
        if len(l[jj][0])<len(l[jj][2]):
            diff = len(l[jj][2])-len(l[jj][0])
            line1 = line1 +" "*(2+diff)+l[jj][0]+" "*(space) 
            #line2 = line2+l[jj][1]+" "+l[jj][2]+" "*(space)
            #line1 = line1.lstrip()
        if len(l[jj][2])>=len(l[jj][0]):
            # = line1+ " "*2+l[jj][0] +" "*(space) 
            line2 = line2+l[jj][1]+" "+l[jj][2]+" "*(space)
        if len(l[jj][2])<len(l[jj][0]):
            diff = len(l[jj][0])-len(l[jj][2])
            #line1 = line1 +" "*(2+diff)+l[jj][0]+" "*(space) 
            line2 = line2+l[jj][1]+" "*(diff+1)+l[jj][2]+" "*(space)

        #if len(l[jj][2])>=len(l[jj][0]):
        
        #line2 = line2+ " "*(4)+l[jj][1]+" "+l[jj][2]
            #line2 = line2+ " "*(space)+l[jj][1]+" "+l[jj][2]
       
        line3 = line3+"-"*maxi+" "*space
        if l[jj][1] =="+":
            ans =len(str(int(l[jj][0])+int(l[jj][2])))
            #dif =abs(len(l[jj][0])-ans)
    
            line4 = line4+ " "*(maxi-ans)+str(int(l[jj][0])+int(l[jj][2]))+" "*space
        if l[jj][1] =="-":
            ans =len(str(int(l[jj][0])-int(l[jj][2])))
            #dif =abs(len(l[jj][0])-ans)
    
            line4 = line4+ " "*(maxi-ans)+str(int(l[jj][0])-int(l[jj][2]))+" "*space
    line1 =line1.rstrip()
    
    line2=line2.rstrip()
    line3=line3.rstrip()
    line4=line4.rstrip()    
    if  optional:
        arranged_problems = line1+"\n" +line2+"\n" +line3+"\n" +line4
        print(len(arranged_problems))
    else:
        arranged_problems = line1+'\n'+line2+"\n"+line3
        #arranged_problems =arranged_problems
        print((len(arranged_problems)))
    return arranged_problems
# def arithmetic_arranger(problems,optional=False):
#     #problems=args[0]
#     if len(problems)>5:
#         return "Error: Too many problems."
#         #print("Error:Too many problems.")
#     space = 6    
#     vals = list()
#     line1 =''
#     line2 =''
#     line3 =''
#     line4 =''

#     for prob in range(len(problems)):
#         vals.append(problems[prob])
#         l = list()
#     for i in range(len(vals)):
#         l.append(vals[i].split())

#     for jj in range(0,len(l)):
#         if l[jj][1] not in ["+","-"]:
#             return "Error: Operator must be '+' or '-'."
#         if l[jj][0].isdigit()==False:
#             return "Error: Numbers must only contain digits."
#         if l[jj][2].isdigit()==False:
#             return "Error: Numbers must only contain digits."
#         if len(l[jj][0])>4:
#             return "Error: Numbers cannot be more than four digits."
#         if len(l[jj][2])>4:
#             return "Error: Numbers cannot be more than four digits."

#         line1 = line1+" "*space + l[jj][0]

#         if len(l[jj][2])>=len(l[jj][0]):
#             maxim  = len(l[jj][2])-len(l[jj][0])
#             line2 = line2+ " "*(space-maxim-2)+l[jj][1]+" "+l[jj][2]
#             maxi  = max(len(l[jj][0]),len(l[jj][2]))
#             maxi = maxi+2
#             line3 =line3+" "*(space-maxim-2)+"-"*maxi
#             if l[jj][1] =="+":
#                 ans =len(str(int(l[jj][0])+int(l[jj][2])))
#                 dif =abs(len(l[jj][0])-ans)
        
#                 line4 = line4+ " "*(space-dif)+str(int(l[jj][0])+int(l[jj][2]))
#             if l[jj][1] =="-":
#                 ans =len(str(int(l[jj][0])-int(l[jj][2])))
#                 dif =abs(len(l[jj][0])-ans)
        
#                 line4 = line4+ " "*(space-dif)+str(int(l[jj][0])-int(l[jj][2]))
#         if len(l[jj][2])<len(l[jj][0]):

#             maxim  = len(l[jj][0])-len(l[jj][2])+1
#             maxi  = max(len(l[jj][0]),len(l[jj][2]))
#             maxi = maxi+2
#             line2 = line2+ " "*(space-2)+l[jj][1]+" "*(maxim)+l[jj][2]
#             line3 =line3+" "*(space-2)+"-"*maxi
#             if l[jj][1] =="+":
#                 ans =len(str(int(l[jj][0])+int(l[jj][2])))
#                 dif =abs(len(l[jj][0])-ans)
        
#                 line4 = line4+ " "*(space-dif)+str(int(l[jj][0])+int(l[jj][2]))
#             if l[jj][1] =="-":
#                 ans =len(str(int(l[jj][0])-int(l[jj][2])))
#                 dif =abs(len(l[jj][0])-ans)
        
#                 line4 = line4+ " "*(space-dif)+str(int(l[jj][0])-int(l[jj][2]))
#     # line1 =line1.lstrip()
#     # line1 = "    "+line1
#     # line2=line2.lstrip()
#     # line3=line3.lstrip()
#     # line4=line4.lstrip()
#     # line4 = "  "+line4    
    
#     if  optional:
#         arranged_problems = line1+"\n" +line2+"\n" +line3+"\n" +line4
#     else:
#         arranged_problems = line1+'\n'+line2+"\n"+line3
#     return arranged_problems

# def arithmetic_arranger(problems,optional=False):
#     #problems=args[0]
#     if len(problems)>5:
#         return "Error: Too many problems."
#         #print("Error:Too many problems.")
        
#     vals = list()
#     line1 =''
#     line2 =''
#     line3 =''
#     line4 =''

#     for prob in range(len(problems)):
#         vals.append(problems[prob])
#         l = list()
#     for i in range(len(vals)):
#         l.append(vals[i].split())

#     for jj in range(0,len(l)):
#         if l[jj][1] not in ["+","-"]:
#             return "Error: Operator must be '+' or '-' "
#         if l[jj][0].isdigit()==False:
#             return "Error: Numbers must only contain digits"
#         if l[jj][2].isdigit()==False:
#             return "Error: Numbers must only contain digits"
#         if len(l[jj][0])>4:
#             return "Error: Numbers cannot be more than four digits."
#         if len(l[jj][2])>4:
#             return "Error: Numbers cannot be more than four digits."

#         line1 = line1+" "*10 + l[jj][0]

#         if len(l[jj][2])>=len(l[jj][0]):
#             maxim  = len(l[jj][2])-len(l[jj][0])
#             line2 = line2+ " "*(10-maxim-2)+l[jj][1]+" "+l[jj][2]
#             maxi  = max(len(l[jj][0]),len(l[jj][2]))
#             maxi = maxi+2
#             line3 =line3+" "*(10-maxim-2)+"-"*maxi
#             if l[jj][1] =="+":
#                 ans =len(str(int(l[jj][0])+int(l[jj][2])))
#                 dif =abs(len(l[jj][0])-ans)
        
#                 line4 = line4+ " "*(10-dif)+str(int(l[jj][0])+int(l[jj][2]))
#             if l[jj][1] =="-":
#                 ans =len(str(int(l[jj][0])-int(l[jj][2])))
#                 dif =abs(len(l[jj][0])-ans)
        
#                 line4 = line4+ " "*(10-dif)+str(int(l[jj][0])-int(l[jj][2]))
#         if len(l[jj][2])<len(l[jj][0]):

#             maxim  = len(l[jj][0])-len(l[jj][2])+1
#             maxi  = max(len(l[jj][0]),len(l[jj][2]))
#             maxi = maxi+2
#             line2 = line2+ " "*8+l[jj][1]+" "*(maxim)+l[jj][2]
#             line3 =line3+" "*(8)+"-"*maxi
#             if l[jj][1] =="+":
#                 ans =len(str(int(l[jj][0])+int(l[jj][2])))
#                 dif =abs(len(l[jj][0])-ans)
        
#                 line4 = line4+ " "*(10-dif)+str(int(l[jj][0])+int(l[jj][2]))
#             if l[jj][1] =="-":
#                 ans =len(str(int(l[jj][0])-int(l[jj][2])))
#                 dif =abs(len(l[jj][0])-ans)
        
#                 line4 = line4+ " "*(10-dif)+str(int(l[jj][0])-int(l[jj][2]))
        
    
#     if  optional:
#         arranged_problems = line1 +'\n'+line2+"\n"+line3+"\n"+line4
#     else:
#         arranged_problems = line1 +'\n'+line2+"\n"+line3
#     return arranged_problems