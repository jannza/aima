import logic



KB = logic.PropKB()


#initial state
KB.tell(logic.expr("At_0(C1, SFO)"))
KB.tell(logic.expr("~At_0(C1, JFK)"))
KB.tell(logic.expr("At_0(C2, JFK)"))
KB.tell(logic.expr("~At_0(C2, SFO)"))

KB.tell(logic.expr("At_0(P1, SFO)"))
KB.tell(logic.expr("~At_0(P1, JFK)"))

KB.tell(logic.expr("At_0(P2, JFK)"))
KB.tell(logic.expr("~At_0(P2, SFO)"))



KB.tell(logic.expr("~In_0(C1, P1)"))
KB.tell(logic.expr("~In_0(C2, P1)"))
KB.tell(logic.expr("~In_0(C1, P2)"))
KB.tell(logic.expr("~In_0(C2, P2)"))







#first part
KB.tell(logic.expr("~Load_0(C1, SFO, P1) | At_0(C1, SFO)"))
KB.tell(logic.expr("~Load_0(C1, SFO, P1) | At_0(P1, SFO)"))
KB.tell(logic.expr("~Load_0(C1, SFO, P2) | At_0(C1, SFO)"))
KB.tell(logic.expr("~Load_0(C1, SFO, P2) | At_0(P2, SFO)"))
KB.tell(logic.expr("~Load_0(C2, JFK, P1) | At_0(C2, JFK)"))
KB.tell(logic.expr("~Load_0(C2, JFK, P1) | At_0(P1, JFK)"))
KB.tell(logic.expr("~Load_0(C2, JFK, P2) | At_0(C2, JFK)"))
KB.tell(logic.expr("~Load_0(C2, JFK, P2) | At_0(P2, JFK)"))


# KB.tell(logic.expr("~Load_1(C1, SFO, P1) | At_1(C1, SFO)"))
# KB.tell(logic.expr("~Load_1(C1, SFO, P1) | At_1(P1, SFO)"))
# KB.tell(logic.expr("~Load_1(C1, SFO, P2) | At_1(C1, SFO)"))
# KB.tell(logic.expr("~Load_1(C1, SFO, P2) | At_1(P2, SFO)"))
# KB.tell(logic.expr("~Load_1(C2, JFK, P1) | At_1(C2, JFK)"))
# KB.tell(logic.expr("~Load_1(C2, JFK, P1) | At_1(P1, JFK)"))
# KB.tell(logic.expr("~Load_1(C2, JFK, P2) | At_1(C2, JFK)"))
# KB.tell(logic.expr("~Load_1(C2, JFK, P2) | At_1(P2, JFK)"))

#second part

KB.tell(logic.expr("~Load_0(C1, SFO, P1) | In_1(C1, P1)"))
KB.tell(logic.expr("~Load_0(C1, SFO, P2) | In_1(C1, P2)"))
KB.tell(logic.expr("~Load_0(C2, JFK, P1) | In_1(C2, P1)"))
KB.tell(logic.expr("~Load_0(C2, JFK, P2) | In_1(C2, P2)"))

# KB.tell(logic.expr("~Load_1(C1, SFO, P1) | In_2(C1, P1)"))
# KB.tell(logic.expr("~Load_1(C1, SFO, P2) | In_2(C1, P2)"))
# KB.tell(logic.expr("~Load_1(C2, JFK, P1) | In_2(C2, P1)"))
# KB.tell(logic.expr("~Load_1(C2, JFK, P2) | In_2(C2, P2)"))

#third part

KB.tell(logic.expr("~Load_0(C1, SFO, P1) | ~At_1(C1, SFO)"))
KB.tell(logic.expr("~Load_0(C1, SFO, P2) | ~At_1(C1, SFO)"))
KB.tell(logic.expr("~Load_0(C2, JFK, P1) | ~At_1(C2, JFK)"))
KB.tell(logic.expr("~Load_0(C2, JFK, P2) | ~At_1(C2, JFK)"))


# KB.tell(logic.expr("~Load_1(C1, SFO, P1) | ~At_2(C1, SFO)"))
# KB.tell(logic.expr("~Load_1(C1, SFO, P2) | ~At_2(C1, SFO)"))
# KB.tell(logic.expr("~Load_1(C2, JFK, P1) | ~At_2(C2, JFK)"))
# KB.tell(logic.expr("~Load_1(C2, JFK, P2) | ~At_2(C2, JFK)"))

#fourth part

KB.tell(logic.expr("At_0(C1, SFO) | ~At_1(C1, SFO)"))
KB.tell(logic.expr("At_0(C2, SFO) | ~At_1(C2, SFO)"))
KB.tell(logic.expr("At_0(C1, JFK) | ~At_1(C1, JFK)"))
KB.tell(logic.expr("At_0(C2, JFK) | ~At_1(C2, JFK)"))

KB.tell(logic.expr("At_0(P1, SFO) | ~At_1(P1, SFO)"))
KB.tell(logic.expr("At_0(P2, SFO) | ~At_1(P2, SFO)"))
KB.tell(logic.expr("At_0(P1, JFK) | ~At_1(P1, JFK)"))
KB.tell(logic.expr("At_0(P2, JFK) | ~At_1(P2, JFK)"))

KB.tell(logic.expr("In_0(C1, P1) | ~In_1(C1, P1) | Load_0(C1, SFO, P1)"))
KB.tell(logic.expr("In_0(C2, P1) | ~In_1(C2, P1) | Load_0(C2, JFK, P1)"))
KB.tell(logic.expr("In_0(C1, P2) | ~In_1(C1, P2) | Load_0(C1, SFO, P2)"))
KB.tell(logic.expr("In_0(C2, P2) | ~In_1(C2, P2) | Load_0(C2, JFK, P2)"))


# KB.tell(logic.expr("At_1(C1, SFO) | ~At_2(C1, SFO)"))
# KB.tell(logic.expr("At_1(C2, SFO) | ~At_2(C2, SFO)"))
# KB.tell(logic.expr("At_1(C1, JFK) | ~At_2(C1, JFK)"))
# KB.tell(logic.expr("At_1(C2, JFK) | ~At_2(C2, JFK)"))
# 
# KB.tell(logic.expr("At_1(P1, SFO) | ~At_2(P1, SFO)"))
# KB.tell(logic.expr("At_1(P2, SFO) | ~At_2(P2, SFO)"))
# KB.tell(logic.expr("At_1(P1, JFK) | ~At_2(P1, JFK)"))
# KB.tell(logic.expr("At_1(P2, JFK) | ~At_2(P2, JFK)"))
# 
# KB.tell(logic.expr("In_1(C1, P1) | ~In_2(C1, P1) | Load_1(C1, SFO, P1)"))
# KB.tell(logic.expr("In_1(C2, P1) | ~In_2(C2, P1) | Load_1(C2, JFK, P1)"))
# KB.tell(logic.expr("In_1(C1, P2) | ~In_2(C1, P2) | Load_1(C1, SFO, P2)"))
# KB.tell(logic.expr("In_1(C2, P2) | ~In_2(C2, P2) | Load_1(C2, JFK, P2)"))

#fifth part

KB.tell(logic.expr("~At_0(C1, SFO) | At_1(C1, SFO) | Load_0(C1, SFO, P1) | Load_0(C1, SFO, P2)"))
KB.tell(logic.expr("~At_0(C2, SFO) | At_1(C2, SFO)"))
KB.tell(logic.expr("~At_0(C1, JFK) | At_1(C1, JFK) | Load_0(C1, JFK, P1) | Load_0(C1, JFK, P2)"))
KB.tell(logic.expr("~At_0(C2, JFK) | At_1(C2, JFK)"))

KB.tell(logic.expr("~At_0(P1, SFO) | At_1(P1, SFO)"))
KB.tell(logic.expr("~At_0(P2, SFO) | At_1(P2, SFO)"))
KB.tell(logic.expr("~At_0(P1, JFK) | At_1(P1, JFK)"))
KB.tell(logic.expr("~At_0(P2, JFK) | At_1(P2, JFK)"))

KB.tell(logic.expr("~In_0(C1, P1) | In_1(C1, P1)"))
KB.tell(logic.expr("~In_0(C2, P1) | In_1(C2, P1)"))
KB.tell(logic.expr("~In_0(C1, P2) | In_1(C1, P2)"))
KB.tell(logic.expr("~In_0(C2, P2) | In_1(C2, P2)"))


# KB.tell(logic.expr("~At_1(C1, SFO) | At_2(C1, SFO) | Load_1(C1, SFO, P1) | Load_1(C1, SFO, P2)"))
# KB.tell(logic.expr("~At_1(C2, SFO) | At_2(C2, SFO)"))
# KB.tell(logic.expr("~At_1(C1, JFK) | At_2(C1, JFK) | Load_1(C1, JFK, P1) | Load_1(C1, JFK, P2)"))
# KB.tell(logic.expr("~At_1(C2, JFK) | At_2(C2, JFK)"))
# 
# KB.tell(logic.expr("~At_1(P1, SFO) | At_2(P1, SFO)"))
# KB.tell(logic.expr("~At_1(P2, SFO) | At_2(P2, SFO)"))
# KB.tell(logic.expr("~At_1(P1, JFK) | At_2(P1, JFK)"))
# KB.tell(logic.expr("~At_1(P2, JFK) | At_2(P2, JFK)"))
# 
# KB.tell(logic.expr("~In_1(C1, P1) | In_2(C1, P1)"))
# KB.tell(logic.expr("~In_1(C2, P1) | In_2(C2, P1)"))
# KB.tell(logic.expr("~In_1(C1, P2) | In_2(C1, P2)"))
# KB.tell(logic.expr("~In_1(C2, P2) | In_2(C2, P2)"))

actions = ["Load_0(C1, SFO, P1)","Load_0(C1, SFO, P2)","Load_0(C2, JFK, P1)","Load_0(C2, JFK, P2)"]


actions2 = ["Load_1(C1, SFO, P1)","Load_1(C1, SFO, P2)","Load_1(C2, JFK, P1)","Load_1(C2, JFK, P2)"]

#sixth part

for elem in actions:
    for elem2 in actions:
        if elem != elem2:
            KB.tell(logic.expr("~"+elem+" | ~"+elem2))


# for elem in actions2:
#     for elem2 in actions2:
#         if elem != elem2:
#             KB.tell(logic.expr("~"+elem+" | ~"+elem2))


#seventh part
seventh =""
for elem in actions:
    seventh = seventh + elem + " | "
    
    
seventh = seventh[:-3]
# print(seventh)
KB.tell(logic.expr(seventh))



# seventh =""
# for elem in actions2:
#     seventh = seventh + elem + " | "
#     
#     
# seventh = seventh[:-3]
# # print(seventh)
# KB.tell(logic.expr(seventh))



#goal
KB.tell(logic.expr("In_1(C1, P1)"))
# KB.tell(logic.expr("In_2(C2, P2)"))


#some manual cnf
string = ""
for elem in KB.clauses:
#     print(elem)
#     elem = logic.to_cnf(str(elem))
    string = string + str(elem) + " & "
    
string = string[:-2]    


# print(string)

#print only true values
# answer = logic.dpll_satisfiable(string)
# if answer != False: 
#     for elem in answer:
#         if answer[elem]:
#             print(str(elem)+ " : " +str(answer[elem]))
# else:
#     print(answer)
print(logic.dpll_satisfiable(string))