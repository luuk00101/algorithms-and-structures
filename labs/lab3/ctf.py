"""
Capture The Flag (CTF) Team Optimization

This script solves a dynamic programming problem for a CTF (Capture The Flag) competition.
Three team members need to solve a series of tasks in relay fashion, where:
- Each member must solve at least one task
- Tasks must be solved in order (from first to last)
- The order of team members can be chosen freely
- Each task has a difficulty rating (1-5) for each team member
- The goal is to minimize the total difficulty

The algorithm:
1. Considers all possible permutations of team members
2. For each permutation, uses dynamic programming to find the optimal assignment of tasks
3. Returns the minimum total difficulty achievable

Input format:
- First line: Number of tasks N (3 ≤ N ≤ 100,000)
- Next three lines: N integers each, representing difficulty ratings (1-5) for each team member

Output:
- A single integer representing the minimum total difficulty

Example:
Input:
7
2 4 1 5 1 1 2
3 3 2 5 3 2 2
1 1 5 4 3 3 3

Output:
12
"""

from typing import List, Optional

MEMBER_COUNT: int = 3


def find_min() -> None:
    """
    Main function to find the minimum total difficulty for the CTF team.

    Uses dynamic programming to calculate the optimal assignment of tasks to team members,
    considering all possible permutations of team members.

    Returns:
        None: Prints the minimum total difficulty to standard output
    """
    # Read the number of exercises/tasks
    excercise_count: int = int(input())

    # Read difficulty ratings for each team member
    member_arrays: List[List[int]] = [[], [], []]
    for i in range(MEMBER_COUNT):
        member_arrays[i] = [int(el) for el in input().split()]

    # All possible permutations of team members (0, 1, 2)
    member_permutations: List[List[int]] = [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0],
    ]

    best_diff: Optional[int] = None

    # Iterate through all permutations of team members
    for perm in member_permutations:
        # Rearrange member arrays according to current permutation
        member_arrays_copy: List[List[int]] = member_arrays.copy()
        member_arrays_copy[0], member_arrays_copy[1], member_arrays_copy[2] = (
            member_arrays[perm[0]],
            member_arrays[perm[1]],
            member_arrays[perm[2]],
        )

        # Initialize DP table: values[member][task] represents minimum difficulty
        # for member to complete tasks up to that point
        values: List[List[int]] = [[0] * excercise_count for _ in range(MEMBER_COUNT)]

        # Fill the DP table
        for row in range(3):  # Team members 0, 1, 2
            for column in range(excercise_count - (2 - row)):
                # Skip invalid configurations (each member must solve at least one task)
                if column < row:
                    continue

                if row == 0:  # First team member
                    if column == 0:  # First task
                        values[row][column] = member_arrays_copy[row][column]
                    else:  # Subsequent tasks for first member
                        values[row][column] = (
                            values[row][column - 1] + member_arrays_copy[row][column]
                        )
                else:  # Second or third team member
                    if row == column:  # Minimum tasks for this member (just one)
                        values[row][column] = (
                            values[row - 1][column - 1]
                            + member_arrays_copy[row][column]
                        )
                    else:  # More than minimum tasks
                        # Choose minimum between:
                        # 1. Previous member does his task
                        # 2. Current member continues from their previous task
                        values[row][column] = (
                            min(values[row - 1][column - 1], values[row][column - 1])
                            + member_arrays_copy[row][column]
                        )

        # The final result is in the bottom-right cell of the DP table
        bottom_right: int = values[2][excercise_count - 1]
        if best_diff is None:
            best_diff = bottom_right
        elif bottom_right < best_diff:
            best_diff = bottom_right

    # Print the minimum total difficulty
    print(best_diff)


if __name__ == "__main__":
    find_min()
