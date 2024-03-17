# Python Project to Calculate Simple Interest, Compound Interest
# and Annuity Plan

print("What do you want to calculate ? ")
print("""
    Simple Interest(SI)
    Compound Interest(CI)
    Annuity Plan(AP)
""")
answer = input("> ")

if answer.lower() == 'si' :
    # Simple interest
    print("What is the given principal? ")
    principal = int(input("> "))

    print("What is the given rate ? ")
    rate = int(input("> "))

    print("What is the time ?")
    time = int(input("> "))

    simpleInterest = principal * (1 + ((rate / 100) * time))
    print("Simple Interest after " + str(time) + " year(s) is: " + str(simpleInterest) )

elif answer.lower() == 'ci':
    # Compound Interest
    print("What is n ? ")
    n = int(input("> "))

    print("What is the given principal? ")
    principal = int(input("> "))

    print("What is the given rate ? ")
    rate = int(input("> "))

    print("What is the time ?")
    time = int(input("> "))

    compoundInterest = principal * (1 + (rate / n)) ** (n * time)

    print("Compoud Interest after " + str(time) + " year(s) is: " + str(compoundInterest))

elif answer.lower() == 'ap':
    # Annuity Plan
    print("What is the amount for the annuity payment ? ")
    pmt = int(input("> "))

    print("What is the given principal? ")
    principal = int(input("> "))

    print("What is the given rate ? ")
    rate = int(input("> "))

    print("What is the time ?")
    time = int(input("> "))

    print("What is n ? ")
    n = int(input("> "))

    annunityPlan = pmt * (((1 + (rate /n)) ** (n * time) - 1) / (rate / n))
    print("Annuity plan after " + str(time) + " year(s) is: " + str(annunityPlan))
