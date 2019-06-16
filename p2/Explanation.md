# Problem 1 - Floored square root

## Approach
Since the problem statement required an O(log n) solution, I tried to find a divide & conquer approach. I initially came up with a floating point method, each time halving the remaining candidates (see `approx_sqrt`). But this way it turns out to be near impossible to find the _floored_ root. So I had to find another integer-based solution (see `_sqrt`). As I didn't find this to be a very elegant method, I also added the Newton method (see `newton_sqrt`), which I found out about after some research.

## Efficiency
My _sqrt method has the required complexity of O(log n), because it halves the number of solutions at each step.


# Problem 2 - Rotated array search

## Approach
Initially, I tried to find a method to solve it in one go, but then reverted back to two steps: First, find the pivot using divide & conquer, then find the requested index using a normal binary search in the correct half of the array.
There are a number of edge cases here that made it quite difficult to get the if-conditions right.

## Efficiency
This solution has a complexity of O(log n + log n - 1) = O(log n), as required.


# Problem 3 - Rearrange array digits

## Approach
This solution is again in two steps. At first the array is sorted, in order to be able to find the largest sums in the second step. For sorting, I picked the quicksort algorithm. I found another implementation than the one from the course materials (through a web research), that I find easier to read.
The sum is then simply formed by traversing the array and multiplying the factor by 10 at every second step.

## Efficiency
Quicksort has a complexity of O(n log n), when the rare worst case is ignored, so the overall complexity is O(n log(n) + n) = O(n log n).

# Problem 4 - Dutch National Flag

## Approach
The problem solution was directly given in the course materials, so I really just pasted it from there. Of course I made sure to understand it properly.

## Efficiency
The complexity of this algorithm is O(n), using just a single traversal.


# Problem 5 - Autocomplete with Tries

## Approach
This is relying on a trie implementation, re-using much of what was learned in the previous sections on tree data structures and recursion. The node's children are kept in a dict that maps every possible follow-up character to another node. Each completed word is marked using a flag on the final character node.

## Efficiency
The most interesting algorithm here is probably `suffixes`. This is very similar to find_files from the previous section. As discussed there, the complexity is O(k), due to the relatively ineffcient array concatenation using `extend`.


# Problem 6 - Unsorted Integer Array

## Approach
Here I went for the straightforward approach to traverse the array once and keep tabs on the min and max value. I'm not sure this is the intended solution, though. There might be a slighty more effective approach using divide & conquer that requires fewer comparisons, but I could not find it.

## Efficiency
With one array traversal, the complexity is O(n).


# Problem 7 - Routing with Tries

## Approach
This is again a relatively direct trie implementation, just using path elements instead of characters as dict keys. Instead of the word end marker, here the handler is attached to 'end nodes'. Some extra care was required to get the path splitting right and cover all special cases.

## Efficiency
The most interesting algorithm is probably `lookup`. Path stripping is O(n), but the find algorithm is something like O(n * n/2), so the overall complexity is O(n^2).