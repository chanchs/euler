# Cheated

'''
Prompt:
Let S(A) represent the sum of elements in set A of size n. We shall call it a
special sum set if for any two non-empty disjoint subsets, B and C, the
following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

If S(A) is minimised for a given n, we shall call it an optimum special sum
set. The first five optimum special sum sets are given below.

    n = 1: {1}
    n = 2: {1, 2}
    n = 3: {2, 3, 4}
    n = 4: {3, 5, 6, 7}
    n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next
optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the
"middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be
A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the
optimum set, as we have merely applied an algorithm to provide a near optimum
set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with
S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

This problem is related to problems 105 and 106.

Solution: 20313839404245

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

Notes:

    To solve this problem we first use the algorithm described above to get a
starting point. Using that process we find that a not-necessarily-minimal
special sum set for n = 7 is:

    {20, 31, 38, 39, 40, 42, 45}

    After finding this baseline set we make the assumption that the optimum
special sum set for n = 7 is close to this set. Though sets are unordered
collections of members, it is convenient to think of this assumption in the
following way: we assume that the first value in our optimum set is within
three integers of 20 (i.e., the first value in our baseline set), the second
is within three integers of 31, and so on.

    We now move on to the task of finding candidate sets that may be the
optimum special sum set that we are looking for. To generate these candidates
we take the Cartesian product of ranges around each value in our baseline set.
Specifically we take the Cartesian product of lists of integers between three
less than and three more than (inclusive) each member of our baseline set. In
Python, the Cartesian product function returns tuples, so we will hereafter
refer to candidate tuples rather than candidate sets unless otherwise noted.

For each candidate tuple we need to test if it fits our criteria and is
more-optimum than the most-minimal special sum tuple we have found so far.
(The most-minimal special sum tuple so far is initially defined to be our
baseline set.) To do so we check three conditions:

    1. The sum of the candidate tuple must be less than sum of the current-best
        tuple, as we are seeking a minimal value. Any candidate tuple with an
        equal or larger sum is ignored;

    2. Each number in the candidate tuple must be distinct. In Python, tuples
        may contain repetitions of values. As our solution must be a set and
        thus cannot contain duplicates we check the length of the candidate
        tuple when it is converted to a set. This conversion will eliminate
        any duplicates present in the tuple.

            If the length after conversion is less than seven, then the
        candidate tuple contained duplicate values and we move on to the next
        candidate. Only if the length after conversion is equal to seven do we
        continue on to the next condition.

            Note that we do not convert the candidate to a set in place, as
        doing so nearly doubles the execution time of this script. I am not
        sure why this is, but I will update this solution description if I am
        able to deduce the cause of this change in efficiency. Only if a
        candidate tuple has a more-minimal sum than the current-best tuple
        will we convert it to a set permanently; and,

    3. The candidate tuple must represent a special sum set and thus must have
        two properties as described in the problem outline: each subset sum
        must be unique, and every subset must have a larger sum than any
        subsets with which it is disjoint that contain fewer members.

            To check if the candidate tuple has these two properties we first
        create the power set (i.e., the set of all subsets) of our candidate
        tuple. (We will refer to these as subsets despite the fact that the
        candidate is actually a tuple and not a set. Also, we will refer to
        the power set although we will actually be using a list of subsets.)
        It is important to note that the power set contains 2 ** n subsets for
        a set with n members and includes the null set. Since the problem
        requires that we focus on non-empty sets we remove the null set from
        the list of subsets, leaving us with a set of 2 ** n - 1 subsets.

            Next we check that the sum of each subset is unique. Rather than
        comparing every possible pair of subsets, we instead use the fact that
        the number of sets in out modified power set is 2 ** n - 1. To check
        the uniqueness of the subset sums, then, we create a set containing
        the sum of every subset. If the length of this set of sums is equal to
        2 ** n - 1 then it is clear that each subset has a unique sum. If
        the length is actually smaller then we know that at least two subsets
        have the same sum, implying that the candidate tuple does not satisfy
        this required property of special sum sets and can be removed from
        consideration.

            After this we focus on the second property: for every pair of
        disjoint subsets B and C, if B contains more values than C, then
        the sum of B must be larger than the sum of C. Again, rather than
        comparing all possible pairs of disjoint subsets--in this case only
        those with different lengths--we can save a significant amount of time
        through a more-thoughtful approach. We simply focus only on the extreme
        pairs of subsets of different lengths to create three sub-conditions
        that must hold if the candidate tuple represents a special sum set:
            1. The sum of the two-member subset with the smallest sum of all
                two-member subsets must be greater than the sum of the
                one-member subset with the largest sum of all one-member
                subsets (i.e., the largest individual member of the candidate
                set);
            2. The sum of the three-member subset with the smallest sum must
                be greater than the sum of the two-member subset with the
                largest sum; and,
            3. The sum of the four-member subset with the smallest sum must be
                greater than the sum of the three-member subset with the
                largest sum.

            We check these three sub-conditions by first creating a sorted
        list containing the same elements as the candidate tuple except in
        increasing order. We then focus on the first sub-condition by creating
        a variable that is the sum of the first two (i.e., smallest two) items
        in the sorted list and a variable that is equal to the last (i.e.,
        largest) item in the sorted list. If the first variable is larger,
        then we continue by increasing each variable by the appropriate next
        item. That is, we add the third-smallest item to the total of the
        smallest items and the second-largest item to the value of the largest
        item. Again, if the first value is larger we continue by adding
        another item to each sum and comparing again. If for all three
        sub-conditions the sum of the subset containing more members is larger
        then we can finally say that the candidate tuple represents a special
        sum set.

    If the candidate tuple satisfies all three of these conditions and their
sub-conditions and properties, then that candidate tuple represents our new
current-best special sum set. Once we have looped over every candidate tuple,
then the tuple stored as our current-best represents the optimum special sum
set.

The solution, however, is not the set itself, but rather the corresponding set
string. To create the set string we convert our current-best tuple to a
sorted, ascending list and then convert each element to a string, all of which
are then joined into the set string.
'''

import itertools
import time
import lib.utilities as ut


if __name__ == '__main__':
    start_time = time.time()

    # Initializes variables that track the most-optimum special sum set so far:
    current_best = {20, 31, 38, 39, 40, 44, 46}
    current_best_sum = sum(current_best)

    # Loops over each candidate tuple close to the baseline set:
    for candidate in itertools.product(*[list(range(x - 3, x + 4)) for
                                         x in current_best]):

        # Skips any candidate tuples with larger sums than the current minimum:
        if sum(candidate) >= current_best_sum:
            continue

        # Skips any candidate tuples containing duplicate values:
        elif ut.has_duplicates(candidate):
            continue

        # Checks if the candidate is a special sum set:
        elif ut.is_special_sum_set(candidate):
            # Records the new most-optimum candidate set and its sum:
            current_best = set(candidate)
            current_best_sum = sum(candidate)

    # Converts optimum set to a sorted list and then the associated set string:
    optimum_list = sorted(list(current_best))
    solution_set_string = "".join([str(item) for item in optimum_list])
    print("The set string of the optimum special sum set for n = 7 is {}."
          .format(solution_set_string))

    end_time = time.time()
    print("Execution time: {}".format(end_time - start_time))