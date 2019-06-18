# Problem 1 - Floored square root

## Approach
Since the problem statement required an O(log n) solution, I tried to find a divide & conquer approach. I initially came up with a floating point method, each time halving the remaining candidates (see `approx_sqrt`). But this way it turns out to be near impossible to find the _floored_ root. So I had to find another integer-based solution (see `_sqrt`). As I didn't find this to be a very elegant method, I also added the Newton method (see `newton_sqrt`), which I found out about after some research on [stackoverflow](https://stackoverflow.com/questions/15390807/integer-square-root-in-python).

## Efficiency
My _sqrt method has the required time complexity of O(log n), because it halves the number of solutions at each step. It's essentially similar to doing a binary search in a list of integers.
The space complexity for all algorithms is O(1), as there are a only fixed number of variables created to keep track of the algorithm progress.


# Problem 2 - Rotated array search

## Approach
Initially, I tried to find a method to solve it in one go, but then reverted back to two steps: First, find the pivot using divide & conquer, then find the requested index using a normal binary search in the correct half of the array.
There are a number of edge cases here that made it quite difficult to get the if-conditions right.

## Efficiency
Due to the two binary searches, this solution has a time complexity two times O(log n), or to be more precise, O(log n + log n - 1) = O(log n), as required.
The space complexity for this algorithm is O(n), just because it needs to store the input array. There are only a few, fixed size auxiliary variables added.


# Problem 3 - Rearrange array digits

## Approach
This solution is again in two steps. At first the array is sorted, in order to be able to find the largest sums in the second step. For sorting, I picked the quicksort algorithm. I found another implementation than the one from the course materials (through a web research), that I find easier to read.
The sum is then simply formed by traversing the array and multiplying the factor by 10 at every second step.

## Efficiency
Quicksort has a time complexity of O(n log n), when the rare worst case is ignored, so the overall complexity is O(n log(n) + n) = O(n log n).
This algorithm has a space complexity of O(n), as it is just re-arranging the input array in place.


# Problem 4 - Dutch National Flag

## Approach
The problem solution was directly given in the course materials, so I really just pasted it from there. Of course I made sure to understand it properly.

## Efficiency
The time complexity of this algorithm is O(n), using just a single traversal.
The space complexity is again O(n), as this algorithm is just re-arranging the given array in place.


# Problem 5 - Autocomplete with Tries

## Approach
This is relying on a trie implementation, re-using much of what was learned in the previous sections on tree data structures and recursion. The node's children are kept in a dict that maps every possible follow-up character to another node. Each completed word is marked using a flag on the final character node.

## Efficiency
The most interesting algorithm here is probably `suffixes`. This is very similar to find_files from the previous section. Each node is only inspected once, but extending the list as opposed to appending to it is relatively expensive. Therefore, its time complexity ends up O(k).
The space complexity for the data structure is O(n*m), where _n_ is the number of words stored in the trie, and _m_ the longest word length (worst case). The various algorithms do not go beyond this, with `suffixes` only adding a list of result words.


# Problem 6 - Unsorted Integer Array

## Approach
Here I went for the straightforward approach to traverse the array once and keep tabs on the min and max value. I'm not sure this is the intended solution, though. There might be a slighty more effective approach using divide & conquer that requires fewer comparisons, but I could not find it.

## Efficiency
With one array traversal, the time complexity is O(n).
The space complexity here is again O(n) due to the input array. The algorithm only uses a few fixed auxiliary variables.


# Problem 7 - Routing with Tries

## Approach
This is again a relatively direct trie implementation, just using path elements instead of characters as dict keys. Instead of the word end marker, here the handler is attached to 'end nodes'. Some extra care was required to get the path splitting right and cover all special cases.

## Efficiency
The most interesting algorithm is probably `lookup`. Path stripping is O(n), and the find algorithm is something like O(n*m), where _n_ is the longest path and _k_ the average number of branches: It has to iterate through the trie nodes (worst case the longest path), and at each level find the next path element out of all branches.
So the overall time complexity is O(n + n * k) = O(n*k).
The space complexity is O(n*m), where _n_ is the number of paths stored in the trie, and _m_ the longest path length (worst case).