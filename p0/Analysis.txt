# Runtime Analysis

## Task 0

* Array access via index has a complexity of O(1).

The complexity of this algorithm is therefore O(1+1) = O(1) overall.

## Task 1

* For-loop over all inputs has a complexity of O(n).
* Set.add has an average complexity of O(1), because sets are implemented as hash tables.

The complexity of this algorithm is therefore roughly O(n*1) = O(n) overall.

## Task 2

* For-loop over all inputs has a complexity of O(n).
* Checking for existence in a list has a complexity of O(n).
* Array access via index has a complexity of O(1).
* The addiional for-loop has a complexity of O(n).

The complexity of this algorithm is therefore roughly O(n * (n+1) + n) = O(n^2) overall.

## Task 3

* For-loop over all inputs has a complexity of O(n).
* Area code checks are string operations with a complexity of O(1).
* Checking for existence in a list has a complexity of O(n).
* Appending an item to a list has a complexity of O(1).
* Sorting a list has a complexity of O(n log n).

The complexity of this algorithm is therefore roughly O(n * (1 + n + 1) + n * log n) = O(n^2) overall.

## Task 4

* For-loop over all inputs has a complexity of O(n).
* Checking for existence in a list has a complexity of O(n).
* Appending an item to a list has a complexity of O(1).
* Removing an item from a list has a complexity of O(n).
* Sorting a list has a complexity of O(n log n).

The complexity of this algorithm is therefore roughly O(n * (n + n) + n * log n) = O(n^2) overall.