import logic


KB = logic.PropKB()

#initial state
KB.tell(logic.expr("At_0(Flat, Axle) & At_0(Spare, Trunk)"))
#initial locations imply parts are not elsewhere at the same time
KB.tell(logic.expr("~At_0(Flat, Axle) | (~At_0(Flat, Trunk) & ~At_0(Flat, Ground))"))
KB.tell(logic.expr("~At_0(Spare, Trunk) | (~At_0(Spare, Axle) & ~At_0(Spare, Ground))"))



#first

first = ["~Remove_Time(Spare, Trunk) | At_Time(Spare, Trunk)", "~PutOn_Time(Spare, Axle) | At_Time(Spare, Ground)",
         "~PutOn_Time(Spare, Axle) | ~At_Time(Flat, Axle)", "~Remove_Time(Spare, Axle) | At_Time(Spare, Axle)",
         "~Remove_Time(Flat, Axle) | At_Time(Flat, Axle)", "~PutOn_Time(Flat, Axle) | At_Time(Flat, Ground)",
         "~PutOn_Time(Flat, Axle) | ~At_Time(Flat, Axle)", "~Remove_Time(Flat, Trunk) | At_Time(Flat, Trunk)"]


for x in range(0, 3):
    for elem in first:
        KB.tell(logic.expr(elem.replace("Time", str(x))))



#second

second = ["~Remove_Time(Spare, Trunk) | At_Time2(Spare, Ground)", "~PutOn_Time(Spare, Axle) | At_Time2(Spare, Axle)",
          "~Remove_Time(Spare, Axle) | At_Time2(Spare, Ground)", "~Remove_Time(Flat, Axle) | At_Time2(Flat, Ground)",
          "~PutOn_Time(Flat, Axle) | At_Time2(Flat, Axle)", "~Remove_Time(Flat, Trunk) | At_Time2(Flat, Ground)"]


for x in range(0, 3):
    for elem in second:
        KB.tell(logic.expr(elem.replace("Time", str(x)).replace("Time2", str(x+1))))



#third

third = ["~Remove_Time(Spare, Trunk) | ~At_Time2(Spare, Trunk)", "~PutOn_Time(Spare, Axle) | ~At_Time2(Spare, Ground)",
         "~Remove_Time(Spare, Axle) | ~At_Time2(Spare, Axle)","~Remove_Time(Flat, Axle) | ~At_Time2(Flat, Axle)",
         "~PutOn_Time(Flat, Axle) | ~At_Time2(Flat, Ground)","~Remove_Time(Flat, Trunk) | ~At_Time2(Flat, Trunk)",
         "~LeaveOvernight_Time | ~At_Time2(Spare, Ground)","~LeaveOvernight_Time | ~At_Time2(Spare, Axle)",
         "~LeaveOvernight_Time | ~At_Time2(Spare, Trunk)","~LeaveOvernight_Time | ~At_Time2(Flat, Ground)",
         "~LeaveOvernight_Time | ~At_Time2(Flat, Axle)","~LeaveOvernight_Time | ~At_Time2(Flat, Trunk)"]


# for x in range(0, 3):
#     for elem in third:
#         KB.tell(logic.expr(elem.replace("Time", str(x)).replace("Time2", str(x+1))))
        



        

KB.tell(logic.expr("~Remove_0(Spare, Trunk) | ~At_1(Spare, Trunk)"))
KB.tell(logic.expr("~PutOn_0(Spare, Axle) | ~At_1(Spare, Ground)"))
KB.tell(logic.expr("~Remove_0(Spare, Axle) | ~At_1(Spare, Axle)"))
KB.tell(logic.expr("~Remove_0(Flat, Axle) | ~At_1(Flat, Axle)"))
KB.tell(logic.expr("~PutOn_0(Flat, Axle) | ~At_1(Flat, Ground)"))
KB.tell(logic.expr("~Remove_0(Flat, Trunk) | ~At_1(Flat, Trunk)"))


KB.tell(logic.expr("~LeaveOvernight_0 | ~At_1(Spare, Ground)"))
KB.tell(logic.expr("~LeaveOvernight_0 | ~At_1(Spare, Axle)"))
KB.tell(logic.expr("~LeaveOvernight_0 | ~At_1(Spare, Trunk)"))
KB.tell(logic.expr("~LeaveOvernight_0 | ~At_1(Flat, Ground)"))
KB.tell(logic.expr("~LeaveOvernight_0 | ~At_1(Flat, Axle)"))
KB.tell(logic.expr("~LeaveOvernight_0 | ~At_1(Flat, Trunk)"))

KB.tell(logic.expr("~Remove_1(Spare, Trunk) | ~At_2(Spare, Trunk)"))
KB.tell(logic.expr("~PutOn_1(Spare, Axle) | ~At_2(Spare, Ground)"))
KB.tell(logic.expr("~Remove_1(Spare, Axle) | ~At_2(Spare, Axle)"))
KB.tell(logic.expr("~Remove_1(Flat, Axle) | ~At_2(Flat, Axle)"))
KB.tell(logic.expr("~PutOn_1(Flat, Axle) | ~At_2(Flat, Ground)"))
KB.tell(logic.expr("~Remove_1(Flat, Trunk) | ~At_2(Flat, Trunk)"))


KB.tell(logic.expr("~LeaveOvernight_1 | ~At_2(Spare, Ground)"))
KB.tell(logic.expr("~LeaveOvernight_1 | ~At_2(Spare, Axle)"))
KB.tell(logic.expr("~LeaveOvernight_1 | ~At_2(Spare, Trunk)"))
KB.tell(logic.expr("~LeaveOvernight_1 | ~At_2(Flat, Ground)"))
KB.tell(logic.expr("~LeaveOvernight_1 | ~At_2(Flat, Axle)"))
KB.tell(logic.expr("~LeaveOvernight_1 | ~At_2(Flat, Trunk)"))


KB.tell(logic.expr("~Remove_2(Spare, Trunk) | ~At_3(Spare, Trunk)"))
KB.tell(logic.expr("~PutOn_2(Spare, Axle) | ~At_3(Spare, Ground)"))
KB.tell(logic.expr("~Remove_2(Spare, Axle) | ~At_3(Spare, Axle)"))
KB.tell(logic.expr("~Remove_2(Flat, Axle) | ~At_3(Flat, Axle)"))
KB.tell(logic.expr("~PutOn_2(Flat, Axle) | ~At_3(Flat, Ground)"))
KB.tell(logic.expr("~Remove_2(Flat, Trunk) | ~At_3(Flat, Trunk)"))

KB.tell(logic.expr("~LeaveOvernight_2 | ~At_3(Spare, Ground)"))
KB.tell(logic.expr("~LeaveOvernight_2 | ~At_3(Spare, Axle)"))
KB.tell(logic.expr("~LeaveOvernight_2 | ~At_3(Spare, Trunk)"))
KB.tell(logic.expr("~LeaveOvernight_2 | ~At_3(Flat, Ground)"))
KB.tell(logic.expr("~LeaveOvernight_2 | ~At_3(Flat, Axle)"))
KB.tell(logic.expr("~LeaveOvernight_2 | ~At_3(Flat, Trunk)"))


#fourth
KB.tell(logic.expr("At_0(Spare, Ground) | ~At_1(Spare, Ground) | Remove_0(Spare, Trunk) | Remove_0(Spare, Axle)"))
KB.tell(logic.expr("At_0(Spare, Trunk) | ~At_1(Spare, Trunk)"))
KB.tell(logic.expr("At_0(Spare, Axle) | ~At_1(Spare, Axle) | PutOn_0(Spare, Axle)"))
KB.tell(logic.expr("At_0(Flat, Axle) | ~At_1(Flat, Axle) | PutOn_0(Flat, Axle)"))
KB.tell(logic.expr("At_0(Flat, Ground) | ~At_1(Flat, Ground) | Remove_0(Flat, Axle) | Remove_0(Flat, Trunk)"))
KB.tell(logic.expr("At_0(Flat, Trunk) | ~At_1(Flat, Trunk)"))


KB.tell(logic.expr("At_1(Spare, Ground) | ~At_2(Spare, Ground) | Remove_1(Spare, Trunk) | Remove_1(Spare, Axle)"))
KB.tell(logic.expr("At_1(Spare, Trunk) | ~At_2(Spare, Trunk)"))
KB.tell(logic.expr("At_1(Spare, Axle) | ~At_2(Spare, Axle) | PutOn_1(Spare, Axle)"))
KB.tell(logic.expr("At_1(Flat, Axle) | ~At_2(Flat, Axle) | PutOn_1(Flat, Axle)"))
KB.tell(logic.expr("At_1(Flat, Ground) | ~At_2(Flat, Ground) | Remove_1(Flat, Axle) | Remove_1(Flat, Trunk)"))
KB.tell(logic.expr("At_1(Flat, Trunk) | ~At_2(Flat, Trunk)"))



KB.tell(logic.expr("At_2(Spare, Ground) | ~At_3(Spare, Ground) | Remove_2(Spare, Trunk) | Remove_2(Spare, Axle)"))
KB.tell(logic.expr("At_2(Spare, Trunk) | ~At_3(Spare, Trunk)"))
KB.tell(logic.expr("At_2(Spare, Axle) | ~At_3(Spare, Axle) | PutOn_2(Spare, Axle)"))
KB.tell(logic.expr("At_2(Flat, Axle) | ~At_3(Flat, Axle) | PutOn_2(Flat, Axle)"))
KB.tell(logic.expr("At_2(Flat, Ground) | ~At_3(Flat, Ground) | Remove_2(Flat, Axle) | Remove_2(Flat, Trunk)"))
KB.tell(logic.expr("At_2(Flat, Trunk) | ~At_3(Flat, Trunk)"))

#fifth
KB.tell(logic.expr("~At_0(Spare, Ground) | At_1(Spare, Ground) | PutOn_0(Spare, Axle) | LeaveOvernight_0"))
KB.tell(logic.expr("~At_0(Spare, Trunk) | At_1(Spare, Trunk) | Remove_0(Spare, Trunk) | LeaveOvernight_0"))
KB.tell(logic.expr("~At_0(Spare, Axle) | At_1(Spare, Axle) | Remove_0(Spare, Axle)  | LeaveOvernight_0"))
KB.tell(logic.expr("~At_0(Flat, Axle) | At_1(Flat, Axle) | Remove_0(Flat, Axle) | LeaveOvernight_0"))
KB.tell(logic.expr("~At_0(Flat, Ground) | At_1(Flat, Ground) | PutOn_0(Flat, Axle) | LeaveOvernight_0"))
KB.tell(logic.expr("~At_0(Flat, Trunk) | At_1(Flat, Trunk) | Remove_0(Flat, Trunk) | LeaveOvernight_0"))


KB.tell(logic.expr("~At_1(Spare, Ground) | At_2(Spare, Ground) | PutOn_1(Spare, Axle) | LeaveOvernight_1"))
KB.tell(logic.expr("~At_1(Spare, Trunk) | At_2(Spare, Trunk) | Remove_1(Spare, Trunk) | LeaveOvernight_1"))
KB.tell(logic.expr("~At_1(Spare, Axle) | At_2(Spare, Axle) | Remove_1(Spare, Axle) | LeaveOvernight_1"))
KB.tell(logic.expr("~At_1(Flat, Axle) | At_2(Flat, Axle) | Remove_1(Flat, Axle) | LeaveOvernight_1"))
KB.tell(logic.expr("~At_1(Flat, Ground) | At_2(Flat, Ground) | PutOn_1(Flat, Axle) | LeaveOvernight_1"))
KB.tell(logic.expr("~At_1(Flat, Trunk) | At_2(Flat, Trunk) | Remove_1(Flat, Trunk) | LeaveOvernight_1"))


KB.tell(logic.expr("~At_2(Spare, Ground) | At_3(Spare, Ground) | PutOn_2(Spare, Axle) | LeaveOvernight_2"))
KB.tell(logic.expr("~At_2(Spare, Trunk) | At_3(Spare, Trunk) | Remove_2(Spare, Trunk) | LeaveOvernight_2"))
KB.tell(logic.expr("~At_2(Spare, Axle) | At_3(Spare, Axle) | Remove_2(Spare, Axle) | LeaveOvernight_2"))
KB.tell(logic.expr("~At_2(Flat, Axle) | At_3(Flat, Axle) | Remove_2(Flat, Axle) | LeaveOvernight_2"))
KB.tell(logic.expr("~At_2(Flat, Ground) | At_3(Flat, Ground) | PutOn_2(Flat, Axle) | LeaveOvernight_2"))
KB.tell(logic.expr("~At_2(Flat, Trunk) | At_3(Flat, Trunk) | Remove_2(Flat, Trunk) | LeaveOvernight_2"))

#list of all possible actions
actions = ["Remove_0(Spare, Trunk)", "PutOn_0(Spare, Axle)", "Remove_0(Spare, Axle)", 
           "Remove_0(Flat, Axle)", "PutOn_0(Flat, Axle)", "Remove_0(Flat, Trunk)", "LeaveOvernight_0"]

actions2 = ["Remove_1(Spare, Trunk)", "PutOn_1(Spare, Axle)", "Remove_1(Spare, Axle)", 
           "Remove_1(Flat, Axle)", "PutOn_1(Flat, Axle)", "Remove_1(Flat, Trunk)", "LeaveOvernight_1"]

actions3 = ["Remove_2(Spare, Trunk)", "PutOn_2(Spare, Axle)", "Remove_2(Spare, Axle)", 
           "Remove_2(Flat, Axle)", "PutOn_2(Flat, Axle)", "Remove_2(Flat, Trunk)", "LeaveOvernight_2"]


#sixth, this can somewhat be automated

for elem in actions:
    for elem2 in actions:
        if elem != elem2:
            KB.tell(logic.expr("~"+elem+" | ~"+elem2))
            
for elem in actions2:
    for elem2 in actions2:
        if elem != elem2:
            KB.tell(logic.expr("~"+elem+" | ~"+elem2))
            
for elem in actions3:
    for elem2 in actions3:
        if elem != elem2:
            KB.tell(logic.expr("~"+elem+" | ~"+elem2))


#seventh, can be also automated
seventh = ""
for elem in actions:    
    seventh = seventh + elem + " | "
seventh = seventh[:-2]
 
KB.tell(logic.expr(seventh))


seventh = ""
for elem in actions2:    
    seventh = seventh + elem + " | "
seventh = seventh[:-2]
 
KB.tell(logic.expr(seventh))


seventh = ""
for elem in actions3:    
    seventh = seventh + elem + " | "
seventh = seventh[:-2]
 
KB.tell(logic.expr(seventh))

#add goal
KB.tell(logic.expr("At_1(Flat, Ground) & At_2(Spare, Ground) & At_3(Spare, Axle)"))



#some manual cnf
string = ""
for elem in KB.clauses:
    elem = logic.to_cnf(str(elem))
    string = string + str(elem) + " & "
    
string = string[:-2]    


# print(string)

#print only true values
answer = logic.dpll_satisfiable(string)
if answer != False: 
    for elem in answer:
        if answer[elem]:
            print(str(elem)+ " : " +str(answer[elem]))
else:
    print(answer)
# print(logic.dpll_satisfiable(string))


