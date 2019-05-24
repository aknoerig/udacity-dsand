# Problem 1 - LRU Cache

## Approach

Since the cache is supposed to hold any type of key, I chose a dictionary/map for it.
And since a dictionary isn't ordered, I chose a list to track cache usage history separately. In particular, I opted for a deque, because most of the time items get removed from one end and added to another, almost like a ring buffer.

## Efficiency
As required, I tried to keep all operation within a complexity of O(1) and chose the data structures accordingly. 
The only place where I could not satisfy this requirement is the `get` operation, in which a list remove operation sometimes has O(n).


# Problem 2 - Find files

## Approach

This task seems to be a perfect candidate for a recursive algorithm. The trick here was to use `append` in the base case and `extend` in the recursive case for building the list.

## Efficiency

Each file is only inspected once, but extending the list as opposed to appending to it is relatively expensive. According to the Python wiki entry on time complexity, this has O(k), both when implemented as a list/array or as a deque/doubly linked list. 
(I do understand this in the case of an array, but not in the case of a doubly linked list. Here, all that's necessary is to redirect two links.)


# Problem 3 - Huffman Encoding

## Approach

I found the given explanations confusing and had to do some further research beyond the given links to better understand the principle.
I first used a map to collect character frequencies, before turning that into a sorted list.
The key seems to me that the frequency list doesn't just contain `(value, frequency)` tuples, but the actual tree nodes. This simplifies the algorithm for building the tree significantly. I used a list, but reversed its order compared to the algorithm visualizations, so that it's faster to pop off the lowest frequencies.
Another challenge was to realize that by "trimming" it is meant to "condense" the tree to a map of the leaf codes. This step, as well as the decoding step, were obvious candidates for recursive algorithms.

## Efficiency

There's a lot going on here!

* create_frequency_list: O(n^2)
* sort_frequencies: O(n log n)
* build_huff_tree: n^2 +  n log n + (n * n log n) => O(n^2 log n)
* trim_huff_tree: O(n) for tree traversal and O(n) for dict update => O(n^2)
* decode_next: O(n)
* huffman_encoding: O(n^2 log n)
* huffman_decoding: O(n^2)


# Problem 4 - User in group

## Approach

This was another straighforward candidate for a recursive algorithm that exits once the answer is clearly true or false, respectively.

## Efficiency

This algorithm has a complexity of O(n), because each group and user (the input) will be checked at most once.


# Problem 5 - Blockchain

## Approach

The problem statement didn't specify any requirements, so I chose a simple list to build the blockchain. This allows simple appending, as well as direct access of individual blocks by index.
I added a `verify` function to make the problem slightly more interesting. It checks whether (and where) the blockchain has been compromised.

## Efficiency

All operations are basic list modifications with O(1).


# Problem 6 - List union & intersection

## Approach

This problem statement again was not very clear. Does the union/intersection of two lists keep duplicates? Does it keep an order of some sort? In my solution, duplicates are removed, and order is by input order.
The algorithm for both is straightforward, but I modified the list implementation to make it more efficient by keeping track of the count and the tail element. 
I also added an iterator to make the code more readable.

## Efficiency

The union algorithm has a complexity of O(n^2). The intersection algorithm has a complexity of O(n^3).