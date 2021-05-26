from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight,AKnave)),
    #Biconditional(AKnight,Not(AKnave)),
    #Biconditional(AKnave,Not(AKnight)),
    #end of general rules section
    Biconditional(And(AKnave, AKnight),AKnight)
    #Biconditional(Not(And(AKnave, AKnight)),AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    #end of general rules section
    Biconditional(And(AKnave, BKnave),AKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    #end of general rules section
    Implication(Or(And(AKnave, BKnave),And(AKnight, BKnight)),AKnight),
    Biconditional(Or(And(AKnave, BKnave),And(AKnight, BKnight)),BKnave)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.  
# B says "A said 'I am a knave'."   
# B says "C is a knave."           
# C says "A is a knight."           
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Not(And(CKnight,CKnave)),
    #end of general rules section
    Biconditional(AKnight, CKnight),
    Biconditional(BKnight, CKnave),
    Biconditional(Not(Or(AKnave, AKnight)),BKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
