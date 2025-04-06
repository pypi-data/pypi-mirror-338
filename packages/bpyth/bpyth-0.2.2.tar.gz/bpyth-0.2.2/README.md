# bpyth
Some boring Python Tools, see `jupyter` directory.

## Try out
The directory `jupyter` contains many notebooks with examples. They are very easy to try out interactively online, with Google Colab. Just click the link at the top of the page and then select Runtime/Run all from the menu in Colab.

## Install
`pip install bpyth`

## Files Tools
* `dump_pickle`: open, dump, close
* `load_pickle`: open, load, close
* `StreamFiles`: Iterable, returns all filenames of a parent directory
* `StreamLines`: Iterable, returns all lines of a text file

## Human Tools
* `human_readable_number`: Rounds a number to a fixed number of significant digits.
* `human_readable_seconds`: Converts seconds to human readable time
* `human_readable_bytes`:   Converts Bytes to human readable size

## Iterable Tools
* `minivenn`: Compare two sets
* `flatten`: Yield all items from any nested iterable
* `remove_dups`: Remove dups from a list whilst-preserving-order
* `sort_by_priority_list`: Sort a list by a list or tuple of prioritized objects
* `cut_counter`: Truncates rare values of a counter
* `ranking_from_counter`: Converts a counter into a ranking

## Object Analysis Tools
* `rtype`: Recursive type. Parses an n-dimensional object and returns a tuple of stype for the scalar in the top left corner.
* `shape`: Recursive len. Parses an n-dimensional object and returns a tuple of sizes.
* `has_shape`: Does an object have additional dimensions? (Skalars: No, Strings: No, Empty Iterables: No,
    Other Iterables: Yes)
* `memory_consumption`: Returns the memory consumption of Python objects.    
    
## String Tools
* `superstrip`     : Removes Unicode whitespaces
* `remove_words`   : Removes stopwords 
* `remove_dupwords`: Removes dup words from a string whilst-preserving-order
* `longest_substr` : Finds the longest common substring in a list of strings
* `random_str`     : Returns a random string 


```python

```
