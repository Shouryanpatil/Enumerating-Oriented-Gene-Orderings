from itertools import permutations, product

def generate_signed_permutations(n):
    # Generate all permutations of numberes from 1 to n
    base_perms = permutations(range(1, n + 1))

    signed_perms = []
    for perm in base_perms:
        # Each number in the permutation can be + or -
        for signs in product([1, -1], repeat=n):
            signed_perm = [a * sign for a, sign in zip(perm, signs)]
            signed_perms.append(signed_perm)

    # Output
    print(len(signed_perms))
    for sp in signed_perms:
        print(' '.join(map(str, sp)))

# Example input
n = 2
generate_signed_permutations(n)
