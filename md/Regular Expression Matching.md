## [Regular Expression Matching](https://github.com/GrEedWish/Code-Practice/blob/master/leetcode/Regular%20Expression%20Matching.py)

Implement regular expression matching with support for `'.'` and `'*'`.

```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```

Notice, isMatch(s, p), first string will always be the text, second string will be the pattern



#### Solution 1 brute-force recursion TLE

Whenever we get two strings, first one is text, second one is pattern,  we want to fit the pattern into the text.

There are mainly two decisions:

1. Is the char in pattern a * or not
   - if it is, then we can use it zero time
   - or multiple times as we want
2. Is the char in pattern and text matches or not
   + if it is, then we can move one step forward towards both string
   + else end here and return a false for this possibility

The first version of my code looks like

```Python
char1 = text[0]
char2 = pattern[0]
flag = False
// is the char in pattern a * or not
if isStar(0, pattern):
    // choice 1 we can skip the * pattern
    if self.isMatch(text, pattern[2:]):
        flag = True
	
    // choice 2, we can use it multiple times
    if isEqual(char1, char2):
        # print("checking ", text[i:], pattern)
        if self.isMatch(text[1:], pattern):
            flag = True

// the char in the pattern is not a *
else:
    // if the two chars are equal, we can move one step forwards on both string
    if isEqual(char1, char2):
        if self.isMatch(text[1:], pattern[1:]):
            flag = True
    // else end here and return False
    else:
        flag = False
return flag
```

Then I came into the problem "How does the algorithm terminates?" My first thought was adding a special character to both end of strings and do not make it paired up with other normal characters. Which proves to be inefficient and complicated.



#### Solution 2 Recursion 2, TLE

The second way to do it is much more efficient and neat. Here comes to my second version, a lot of improvments on condensing the code and make it more understandable.

```python
def isMatch(self, text, pattern):
    // if pattern goes to its end
    // return True is text is also ending
	// or False if there are still some text need to match up
    if not pattern:
        return not text

    // either text is empty return false
	// or the first character in pattern matches with text
    first_match = bool (text) and pattern[0] in {'.', text[0]}

    if len(pattern) > 1 and pattern[1] == '*':
        if self.isMatch(text, pattern[2:]):
            return True
        else:
            return first_match and self.isMatch(text[1:], pattern)
    else:
        return first_match and self.isMatch(text[1:], pattern[1:])
```

The second version is much better than version one. However, it is still Time Limit Exceeded. 



#### Version 3 Dynamic Programming AC

Why dp? Because I have the above recursion skeleton, which is good, but not efficient. Then, it is nature to ask myself, can I store the result of each recursion and make compute uses the result that it previously calculated? Yes, it is the idea of DP! **Key point here is not thinking dp first, think recursion first and then it is nature to think store results of recursion, and it comes to the idea of dp**

Look back at the code, I called isMatch(text, pattern) multiple times in my function, each time I shrinked the length of text and pattern, that means, for each subtext and subpattern, they contribute a subresult for the bigger problem.

That is to say text[i:] and pattern[j:] is useful when calculating isMatch(text, pattern) for each possible i and j

```python
res = {}
def dp(i, j):
    if (i, j) in res:
        return res[i, j]

    if j == len(pattern):
        return i == len(text)

    # if the text is not empty
    # and the pattern matches with text
    first_match = bool (i < len(text)) and pattern[j] in {'.', text[i % len(text)]}


    if len(pattern) - j > 1 and pattern[j + 1] == '*':
        res[i, j] = (dp(i, j + 2) or first_match and dp(i + 1, j))
    else:
        res[i, j] = first_match and dp(i + 1, j + 1)
    return res[i, j]
return dp(0, 0)
```

Congrats to myself! The dynamic programming is such powerful and beautiful.

**Some Insights: Do not think dp first, think recursion(dfs) first and try using memorization and that is the idea of DP! **

