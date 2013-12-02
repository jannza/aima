import logic



KB = logic.PropKB()

formula = logic.expr('B12 <=> (P13 | P21)')

KB.tell(logic.expr("A & ~B & C & (A | ~D) & (~E | ~D) & (C | ~D) & (~A | ~F) & (E | ~F) & (~D | ~F) & (B | ~C | D) & (A | ~E | F) & (~A | E | D)"))

# formula = logic.expr('S21 <=> (W31 | W22)')
# print(logic.dpll_satisfiable(KB.tell))
