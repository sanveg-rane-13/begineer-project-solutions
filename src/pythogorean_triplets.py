def is_triplet(a, b, c):
    hyp = a
    s1 = b
    s2 = c

    if b > a:
        hyp = b
        s1 = a

    if c > a and c > b:
        hyp = c
        s2 = b

    return True if (c * c) == ((a * a) + (b * b)) else False


def verify_triples():
    user_input = input("Please enter the sides: ")
    a, b, c = user_input.split()
    if is_triplet(int(a), int(b), int(c)):
        print("The triangle is a Pythagorean triplet")
    else:
        print("The triangle is Not a Pythagorean triplet")


cont = True
while cont:
    verify_triples()
    inp = input("Do you wish to calculate again? (y/n): ")
    cont = True if inp.lower() == 'y' else False
