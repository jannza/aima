import logic
import itertools

KB = logic.PropKB()

#initial state
KB.tell(logic.expr("OnTable_0(A)"))
KB.tell(logic.expr("OnTable_0(B)"))
KB.tell(logic.expr("~OnTable_0(C)"))
KB.tell(logic.expr("~On_0(A, B)"))
KB.tell(logic.expr("~On_0(A, C)"))
KB.tell(logic.expr("~On_0(B, A)"))
KB.tell(logic.expr("~On_0(B, C)"))
KB.tell(logic.expr("On_0(C, A)"))
KB.tell(logic.expr("~On_0(C, B)"))

KB.tell(logic.expr("~Clear_0(A)"))
KB.tell(logic.expr("Clear_0(B)"))
KB.tell(logic.expr("Clear_0(C)"))
KB.tell(logic.expr("Handempty_0"))
KB.tell(logic.expr("~Holding_0(A)"))
KB.tell(logic.expr("~Holding_0(B)"))
KB.tell(logic.expr("~Holding_0(C)"))



moves = 6

#first preconditions


for i in range(0,moves):
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, B) | On_"+str(i)+"(A, B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, B) | Clear_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, B) | Handempty_"+str(i)))
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, C) | On_"+str(i)+"(A, C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, C) | Clear_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, C) | Handempty_"+str(i)))
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, A) | On_"+str(i)+"(B, A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, A) | Clear_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, A) | Handempty_"+str(i)))    
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, C) | On_"+str(i)+"(B, C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, C) | Clear_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, C) | Handempty_"+str(i)))
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, A) | On_"+str(i)+"(C, A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, A) | Clear_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, A) | Handempty_"+str(i)))
    
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, B) | On_"+str(i)+"(C, B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, B) | Clear_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, B) | Handempty_"+str(i)))
    
    
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, B) | Holding_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, B) | Clear_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, C) | Holding_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, C) | Clear_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, A) | Holding_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, A) | Clear_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, C) | Holding_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, C) | Clear_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, A) | Holding_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, A) | Clear_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, B) | Holding_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, B) | Clear_"+str(i)+"(B)"))
       
    KB.tell(logic.expr("~Pickup_"+str(i)+"(A) | OnTable_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(A) | Clear_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(A) | Handempty_"+str(i)))

    KB.tell(logic.expr("~Pickup_"+str(i)+"(B) | OnTable_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(B) | Clear_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(B) | Handempty_"+str(i)))    
    
    KB.tell(logic.expr("~Pickup_"+str(i)+"(C) | OnTable_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(C) | Clear_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(C) | Handempty_"+str(i)))
    
    KB.tell(logic.expr("~Putdown_"+str(i)+"(A) | Holding_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(B) | Holding_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(C) | Holding_"+str(i)+"(C)"))

    



#second positive effects
for i in range(0,moves):
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, B) | Holding_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, B) | Clear_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, C) | Holding_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, C) | Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, A) | Holding_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, A) | Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, C) | Holding_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, C) | Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, A) | Holding_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, A) | Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, B) | Holding_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, B) | Clear_"+str(i+1)+"(B)"))
    
    
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, B) | On_"+str(i+1)+"(A, B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, B) | Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, B) | Handempty_"+str(i+1)))
    
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, C) | On_"+str(i+1)+"(A, C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, C) | Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, C) | Handempty_"+str(i+1)))
    
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, A) | On_"+str(i+1)+"(B, A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, A) | Clear_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, A) | Handempty_"+str(i+1)))    
    
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, C) | On_"+str(i+1)+"(B, C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, C) | Clear_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, C) | Handempty_"+str(i+1)))
    
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, A) | On_"+str(i+1)+"(C, A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, A) | Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, A) | Handempty_"+str(i+1)))
    
    
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, B) | On_"+str(i+1)+"(C, B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, B) | Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, B) | Handempty_"+str(i+1)))   
    
    KB.tell(logic.expr("~Pickup_"+str(i)+"(A) | Holding_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(B) | Holding_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(C) | Holding_"+str(i+1)+"(C)"))
    
    KB.tell(logic.expr("~Putdown_"+str(i)+"(A) | OnTable_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(A) | Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(A) | Handempty_"+str(i+1)))

    KB.tell(logic.expr("~Putdown_"+str(i)+"(B) | OnTable_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(B) | Clear_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(B) | Handempty_"+str(i+1)))    
    
    KB.tell(logic.expr("~Putdown_"+str(i)+"(C) | OnTable_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(C) | Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(C) | Handempty_"+str(i+1)))

    
#third negative effects

for i in range(0,moves):
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, B) | ~On_"+str(i+1)+"(A, B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, B) | ~Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, B) | ~Handempty_"+str(i+1)))
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, C) | ~On_"+str(i+1)+"(A, C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, C) | ~Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(A, C) | ~Handempty_"+str(i+1)))
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, A) | ~On_"+str(i+1)+"(B, A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, A) | ~Clear_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, A) | ~Handempty_"+str(i+1)))    
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, C) | ~On_"+str(i+1)+"(B, C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, C) | ~Clear_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(B, C) | ~Handempty_"+str(i+1)))
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, A) | ~On_"+str(i+1)+"(C, A)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, A) | ~Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, A) | ~Handempty_"+str(i+1)))
    
    
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, B) | ~On_"+str(i+1)+"(C, B)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, B) | ~Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Unstack_"+str(i)+"(C, B) | ~Handempty_"+str(i+1)))   
    
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, B) | ~Holding_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, B) | ~Clear_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, C) | ~Holding_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(A, C) | ~Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, A) | ~Holding_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, A) | ~Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, C) | ~Holding_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(B, C) | ~Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, A) | ~Holding_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, A) | ~Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, B) | ~Holding_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Stack_"+str(i)+"(C, B) | ~Clear_"+str(i+1)+"(B)"))
    


    KB.tell(logic.expr("~Pickup_"+str(i)+"(A) | ~OnTable_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(A) | ~Clear_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(A) | ~Handempty_"+str(i+1)))

    KB.tell(logic.expr("~Pickup_"+str(i)+"(B) | ~OnTable_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(B) | ~Clear_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(B) | ~Handempty_"+str(i+1)))    
    
    KB.tell(logic.expr("~Pickup_"+str(i)+"(C) | ~OnTable_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(C) | ~Clear_"+str(i+1)+"(C)"))
    KB.tell(logic.expr("~Pickup_"+str(i)+"(C) | ~Handempty_"+str(i+1)))


    KB.tell(logic.expr("~Putdown_"+str(i)+"(A) | ~Holding_"+str(i+1)+"(A)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(B) | ~Holding_"+str(i+1)+"(B)"))
    KB.tell(logic.expr("~Putdown_"+str(i)+"(C) | ~Holding_"+str(i+1)+"(C)"))

#fourth from false to true

for i in range(0,moves):    
    KB.tell(logic.expr("OnTable_"+str(i)+"(A) | ~OnTable_"+str(i+1)+"(A) | Putdown_"+str(i)+"(A)"))
    KB.tell(logic.expr("OnTable_"+str(i)+"(B) | ~OnTable_"+str(i+1)+"(B) | Putdown_"+str(i)+"(B)"))
    KB.tell(logic.expr("OnTable_"+str(i)+"(C) | ~OnTable_"+str(i+1)+"(C) | Putdown_"+str(i)+"(C)"))
    KB.tell(logic.expr("On_"+str(i)+"(A, B) | ~On_"+str(i+1)+"(A, B) | Stack_"+str(i)+"(A, B)"))
    KB.tell(logic.expr("On_"+str(i)+"(A, C) | ~On_"+str(i+1)+"(A, C) | Stack_"+str(i)+"(A, C)"))
    KB.tell(logic.expr("On_"+str(i)+"(B, A) | ~On_"+str(i+1)+"(B, A) | Stack_"+str(i)+"(B, A)"))
    KB.tell(logic.expr("On_"+str(i)+"(B, C) | ~On_"+str(i+1)+"(B, C) | Stack_"+str(i)+"(B, C)"))
    KB.tell(logic.expr("On_"+str(i)+"(C, A) | ~On_"+str(i+1)+"(C, A) | Stack_"+str(i)+"(C, A)"))
    KB.tell(logic.expr("On_"+str(i)+"(C, B) | ~On_"+str(i+1)+"(C, B) | Stack_"+str(i)+"(C, B)"))
    KB.tell(logic.expr("Clear_"+str(i)+"(A) | ~Clear_"+str(i+1)+"(A) | Unstack_"+str(i)+"(B, A) | Unstack_"+str(i)+"(C, A) | Stack_"+str(i)+"(A, B) | Stack_"+str(i)+"(A, C) | Putdown_"+str(i)+"(A)"))
    KB.tell(logic.expr("Clear_"+str(i)+"(B) | ~Clear_"+str(i+1)+"(B) | Unstack_"+str(i)+"(A, B) | Unstack_"+str(i)+"(C, B) | Stack_"+str(i)+"(B, A) | Stack_"+str(i)+"(B, C) | Putdown_"+str(i)+"(B)"))
    KB.tell(logic.expr("Clear_"+str(i)+"(C) | ~Clear_"+str(i+1)+"(C) | Unstack_"+str(i)+"(A, C) | Unstack_"+str(i)+"(B, C) | Stack_"+str(i)+"(C, A) | Stack_"+str(i)+"(C, B) | Putdown_"+str(i)+"(C)"))
    KB.tell(logic.expr("Holding_"+str(i)+"(A) | ~Holding_"+str(i+1)+"(A) | Unstack_"+str(i)+"(A, B) | Unstack_"+str(i)+"(A, C) | Pickup_"+str(i)+"(A)"))
    KB.tell(logic.expr("Holding_"+str(i)+"(B) | ~Holding_"+str(i+1)+"(B) | Unstack_"+str(i)+"(B, A) | Unstack_"+str(i)+"(B, C) | Pickup_"+str(i)+"(B)"))
    KB.tell(logic.expr("Holding_"+str(i)+"(C) | ~Holding_"+str(i+1)+"(C) | Unstack_"+str(i)+"(C, A) | Unstack_"+str(i)+"(C, B) | Pickup_"+str(i)+"(C)"))
    KB.tell(logic.expr("Handempty_"+str(i)+" | ~Handempty_"+str(i+1)+" | Stack_"+str(i)+"(A, B) | Stack_"+str(i)+"(A, C) | Stack_"+str(i)+"(B, A) | Stack_"+str(i)+"(B, C) | Stack_"+str(i)+"(C, A) | Stack_"+str(i)+"(C, B) | Putdown_"+str(i)+"(A) | Putdown_"+str(i)+"(B) | Putdown_"+str(i)+"(C)"))

    
    

#fifth from true to false
for i in range(0,moves):
    KB.tell(logic.expr("~OnTable_"+str(i)+"(A) | OnTable_"+str(i+1)+"(A) | Pickup_"+str(i)+"(A)"))
    KB.tell(logic.expr("~OnTable_"+str(i)+"(B) | OnTable_"+str(i+1)+"(B) | Pickup_"+str(i)+"(B)"))
    KB.tell(logic.expr("~OnTable_"+str(i)+"(C) | OnTable_"+str(i+1)+"(C) | Pickup_"+str(i)+"(C)"))
    KB.tell(logic.expr("~On_"+str(i)+"(A, B) | On_"+str(i+1)+"(A, B) | Unstack_"+str(i)+"(A, B)"))
    KB.tell(logic.expr("~On_"+str(i)+"(A, C) | On_"+str(i+1)+"(A, C) | Unstack_"+str(i)+"(A, C)"))
    KB.tell(logic.expr("~On_"+str(i)+"(B, A) | On_"+str(i+1)+"(B, A) | Unstack_"+str(i)+"(B, A)"))
    KB.tell(logic.expr("~On_"+str(i)+"(B, C) | On_"+str(i+1)+"(B, C) | Unstack_"+str(i)+"(B, C)"))
    KB.tell(logic.expr("~On_"+str(i)+"(C, A) | On_"+str(i+1)+"(C, A) | Unstack_"+str(i)+"(C, A)"))
    KB.tell(logic.expr("~On_"+str(i)+"(C, B) | On_"+str(i+1)+"(C, B) | Unstack_"+str(i)+"(C, B)"))
    KB.tell(logic.expr("~Clear_"+str(i)+"(A) | Clear_"+str(i+1)+"(A) | Unstack_"+str(i)+"(A, B) | Unstack_"+str(i)+"(A, C) | Stack_"+str(i)+"(B, A) | Stack_"+str(i)+"(C, A) | Pickup_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Clear_"+str(i)+"(B) | Clear_"+str(i+1)+"(B) | Unstack_"+str(i)+"(B, A) | Unstack_"+str(i)+"(B, C) | Stack_"+str(i)+"(A, B) | Stack_"+str(i)+"(C, B) | Pickup_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Clear_"+str(i)+"(C) | Clear_"+str(i+1)+"(C) | Unstack_"+str(i)+"(C, A) | Unstack_"+str(i)+"(C, B) | Stack_"+str(i)+"(A, C) | Stack_"+str(i)+"(B, C) | Pickup_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Holding_"+str(i)+"(A) | Holding_"+str(i+1)+"(A) | Stack_"+str(i)+"(A, B) | Stack_"+str(i)+"(A, C) | Putdown_"+str(i)+"(A)"))
    KB.tell(logic.expr("~Holding_"+str(i)+"(B) | Holding_"+str(i+1)+"(B) | Stack_"+str(i)+"(B, A) | Stack_"+str(i)+"(B, C) | Putdown_"+str(i)+"(B)"))
    KB.tell(logic.expr("~Holding_"+str(i)+"(C) | Holding_"+str(i+1)+"(C) | Stack_"+str(i)+"(C, A) | Stack_"+str(i)+"(C, B) | Putdown_"+str(i)+"(C)"))
    KB.tell(logic.expr("~Handempty_"+str(i)+" | Handempty_"+str(i+1)+" | Unstack_"+str(i)+"(A, B) | Unstack_"+str(i)+"(A, C) | Unstack_"+str(i)+"(B, A) | Unstack_"+str(i)+"(B, C) | Unstack_"+str(i)+"(C, A) | Unstack_"+str(i)+"(C, B) | Pickup_"+str(i)+"(A) | Pickup_"+str(i)+"(B) | Pickup_"+str(i)+"(C)"))
    

#list of all possible actions
#actions without timestamp, will be added later

actions = ["Unstack_(A, B)","Unstack_(A, C)","Unstack_(B, A)","Unstack_(B, C)","Unstack_(C, A)","Unstack_(C, B)",
           "Stack_(A, B)","Stack_(A, C)","Stack_(B, A)","Stack_(B, C)","Stack_(C, A)","Stack_(C, B)",
           "Pickup_(A)","Pickup_(B)","Pickup_(C)", "Putdown_(A)","Putdown_(B)", "Putdown_(C)"]



#sixth, only one action can take place

for i in range(0,moves):
    for elem in itertools.combinations(actions, 2):
        KB.tell(logic.expr("~"+elem[0].replace("_","_"+str(i))+" | ~"+elem[1].replace("_","_"+str(i))))



#seventh, one action must take place

for i in range(0,moves):
    seventh = ""
    for elem in actions:    
        seventh += elem.replace("_","_"+str(i)) + " | " 
    seventh = seventh[:-2]
    KB.tell(logic.expr(seventh))



#add goal
KB.tell(logic.expr("OnTable_6(C) & On_6(B, C) & On_6(A, B)"))



#some manual cnf just to be sure
string = ""
for elem in KB.clauses:
    elem = logic.to_cnf(str(elem))
    string = string + str(elem) + " & "
    
string = string[:-2]    


action_stubs = ["Unstack", "Stack", "Pickup", "Putdown"]



#print only true values
answer = logic.dpll_satisfiable(logic.expr(string))


#print out only true actions, leave out facts
if answer != False: 
    for elem in answer:
        if answer[elem]:
            if any(sub in str(elem) for sub in action_stubs):
                print(str(elem)+ " : " +str(answer[elem]))
else:
    print(answer)
# print(logic.dpll_satisfiable(logic.expr(string)))


