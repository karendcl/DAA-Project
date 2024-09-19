from itertools import combinations
import random
import numpy as np
import matplotlib.pyplot as plt
from math import *

brute = []
greedy = []
n = []
length = []
R = []

not_found = 0

def stats(special = False):
    global brute, greedy, n, length, R
    #calculate the approximate ratio of the average size of hitting set found by brute force to the average size of hitting set found by greedy approach
    diff = np.array(greedy) - np.array(brute)
    percentage = np.mean(diff) / np.mean(brute) * 100
    print(f"Correct ratio: {100-percentage}%")

    if special:
        n_ = [length[i] / R[i] * log(length[i], e) for i in range(len(length))]
    else:
        n_ = [n[i] * log(length[i],e) for i in range(len(n))] #|X|log(n)


    for i in range(1,len(n_)):
        assert n[i] == n[i-1]
        assert length[i] == length[i-1]

    R, n_, brute, greedy, length = zip(*sorted(zip(R, n_, brute, greedy, length), reverse=True))

    proportion_actual = [greedy[i] / brute[i] for i in range(len(brute))]
    proportion_actual = np.mean(proportion_actual)

    proportion_theoretical = [n_[i] / brute[i] for i in range(len(brute))]
    proportion_theoretical = np.mean(proportion_theoretical)

    print(f"Actual proportion: {proportion_actual}")
    print(f"Theoretical proportion: {proportion_theoretical}")


    new_n, new_brute, new_greedy, x = [], [], [], []

    #group by n_ average
    last_n = n_[0]
    max_brute = 0
    max_greedy = 0
    for i in range(len(n_)):
        if n_[i] == last_n:
                max_brute = max(max_brute, brute[i])
                max_greedy = max(max_greedy, greedy[i])
                if i == len(n_)-1:
                    new_n.append(last_n)
                    new_brute.append(max_brute)
                    new_greedy.append(max_greedy)
                    x.append(length[i])
        else:
                    new_n.append(last_n)
                    new_brute.append(max_brute)
                    new_greedy.append(max_greedy)
                    x.append(length[i])
                    last_n = n_[i]
                    max_brute = brute[i]
                    max_greedy = greedy[i]

    x = [i for i in range(1, len(new_n)+1)]

    new_n, new_brute, new_greedy, x = zip(*sorted(zip(new_n, new_brute, new_greedy, x)))

    plt.plot(x, new_brute, label = "Brute force")
    plt.plot(x, new_greedy, label = "Greedy")
    plt.plot(x, new_n, label = "|X|log(n)") if not special else plt.plot(x, new_n, label = "|X|/min(C)log(n)")
    plt.xlabel("Instance")
    plt.ylabel("Hitting set size")
    plt.legend()
    plt.show()




def is_valid_hitting_set(hitting_set, collection):
    """
    Check if hitting_set intersects with every set in the collection.
    """
    for subset in collection:
        if not (hitting_set & subset):  # Check if hitting_set intersects with subset
            return False
    return True


def find_k_hitting_set(X, C, k):
    """
    Find the smallest hitting set of size ≤ k that hits every subset in C.

    :param X: The ground set (list or set)
    :param C: The collection of subsets (list of sets)
    :param k: The maximum size of the hitting set
    :return: The smallest hitting set of size ≤ k or None if no such set exists
    """
    X = set(X)  # Ensure X is a set

    # Generate all combinations of elements from X with size ≤ k
    for size in range(1, k + 1):
        for combination in combinations(X, size):
            hitting_set = set(combination)
            if is_valid_hitting_set(hitting_set, C):
                return hitting_set  # Return the first valid hitting set found

    return None  # No valid hitting set found


def generate_set(length):
    """
    Generate a set of integers from 1 to length.
    """
    return set(range(1, length + 1))

def generate_random_subsets(X):
    """
    Generate a collection of random subsets of X.
    """
    global R
    subsets = []
    seq = list(X)

    min_size = len(X)
    amount = random.randint(4, len(X) - 1)
    for _ in range(amount):
        i = random.randint(1, len(X) - 1)
        subsets.append(set(random.sample(seq, i)))
        if i < min_size:
            min_size = i

    R.append(min_size)
    return subsets


def generate_random_subsets_special_case(X):
    """
    Generate a collection of random subsets of X.
    The amount of subsets is equal to the length of X.
    """
    global R
    subsets = []
    seq = list(X)

    min_size = len(X)

    for _ in range(1, len(X)):
        i = random.randint(1, len(X) - 1)
        subsets.append(set(random.sample(seq, i)))
        if i < min_size:
            min_size = i

    R.append(min_size)
    return subsets

def greedy_k_hitting_set(X, C, k):
    """
    Find a k-sized hitting set using a greedy approach.

    :param X: The ground set (list or set)
    :param C: The collection of subsets (list of sets)
    :param k: The maximum size of the hitting set
    :return: A k-sized hitting set or None if no such set exists
    """
    X = set(X)  # Ensure X is a set
    uncovered_subsets = set(range(len(C)))  # Track uncovered subsets by index
    hitting_set = set()

    while len(hitting_set) < k and uncovered_subsets:
        best_element = None
        best_cover = 0

        # Find the element that covers the most uncovered subsets
        for element in X:
            cover_count = 0
            for idx in uncovered_subsets:
                if element in C[idx]:
                    cover_count += 1

            if cover_count > best_cover:
                best_cover = cover_count
                best_element = element

        if best_element is None:  # No element can cover any remaining uncovered subset
            break

        # Add the best element to the hitting set
        hitting_set.add(best_element)

        # Update the list of uncovered subsets
        uncovered_subsets = {idx for idx in uncovered_subsets if best_element not in C[idx]}

    # If the hitting set size is less than k but all subsets are covered, return the hitting set
    if len(hitting_set) <= k and not uncovered_subsets:
        return hitting_set
    else:
        return None  # No valid hitting set of size ≤ k found

def generate_instance(special=False):
    """
    Generate a random instance of the hitting set problem.
    """
    X = generate_set(random.randint(15, 40)) if not special else generate_set(50)
    C = generate_random_subsets(X) if not special else generate_random_subsets_special_case(X)
    k = len(C) # to not have to worry about the size of the hitting set for the greedy stats

    return X, C, k

def print_answer(X, C, hitting_set, i, greedy_ = False):
    """
    Print the instance and the hitting set found.
    """
    if i % 100 == 0:
        print(f"Instance {i}:")
    if hitting_set:
        # print(f"Found hitting set: {hitting_set}") if not greedy_ else print(f"Found greedy hitting set: {hitting_set}")
        if not greedy_:
            brute.append(len(hitting_set))
        else:
            greedy.append(len(hitting_set))
        return True
    else:
        # print("No hitting set found.")
        return False


def main():
    global not_found, brute, greedy
    for i in range(1000):
        X, C, k = generate_instance(True)
        solved1 = print_answer(X, C, find_k_hitting_set(X, C, k), i)
        solved2 = print_answer(X, C, greedy_k_hitting_set(X, C, k),i, True)

        if solved1:
            if solved2:
                n.append(len(X))
                length.append(len(C))
            else:
                not_found += 1
                brute.pop()

    stats(True)

if __name__ == "__main__":
    main()
