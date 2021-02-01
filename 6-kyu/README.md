<details>
<summary> Equal Sides Of An Array</summary>

  + [solution](/6-kyu/Equal%20Sides%20Of%20An%20Array.py) | 
    [codewars link](https://www.codewars.com/kata/5679aa472b8f57fb8c000047)
>You are going to be given an array of integers. Your job is to take that 
> array and find an index N where the sum of the integers to the left of N is 
> equal to the sum of the integers to the right of N. If there is no index that 
> would make this happen, return `-1`.
>
>Example:
> 
>Let's say you are given the array `{1,2,3,4,3,2,1}`:  
>Your function will return the index `3`, because at the 3rd position of the array, 
>the sum of left side of the index `({1,2,3}) `and the sum of the right side of the 
>index `({3,2,1})` both equal `6`.
</details>

<details>
<summary>Create Phone Number</summary>

  + [solution](/6-kyu/Create%20Phone%20Number.py) | 
    [codewars link](https://www.codewars.com/kata/525f50e3b73515a6db000b83)    

> Write a function that accepts an array of 10 integers (between 0 and 9), that 
> returns a string of those numbers in the form of a phone number.
> 
>Example:  
> `create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"`  
> The returned format must be correct in order to complete this challenge.   
> Don't forget the space after the closing parentheses!
</details>

<details>
<summary>Does my number look big in this?</summary>

  + [solution](/6-kyu/Does%20my%20number%20look%20big%20in%20this%3F.py) | 
    [codewars link](https://www.codewars.com/kata/5287e858c6b5a9678200083c)

>A Narcissistic Number is a positive number which is the sum of its own digits, 
> each raised to the power of the number of digits in a given base. In this Kata, 
> we will restrict ourselves to decimal (base 10).
> 
> Example:  
> take 153 (3 digits), which is narcisstic:  
> `1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`  
> and 1652 (4 digits), which isn't:  
>` 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938`  
The Challenge:  
Your code must return true or false depending upon whether the given number is a 
> Narcissistic number in base 10.
</details>

<details>
<summary>Detect Pangram</summary>

  + [solution](/6-kyu/Detect%20Pangram.py) | 
    [codewars link](https://www.codewars.com/kata/545cedaa9943f7fe7b000048)

> A pangram is a sentence that contains every single letter of the alphabet at 
> least once. For example, the sentence "The quick brown fox jumps over the lazy 
> dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).   
> Given a string, detect whether or not it is a pangram. Return `True` if it is, 
> `False` if not. Ignore numbers and punctuation.
</details>

<details>
<summary>Find The Parity Outlier</summary>

[solution](/6-kyu/Find%20The%20Parity%20Outlier.py) | 
[codewars link](https://www.codewars.com/kata/5526fc09a1bbd946250002dc)

> You are given an array (which will have a length of at least 3, but could be 
> very large) containing integers. The array is either entirely comprised of 
> odd integers or entirely comprised of even integers except for a single 
> integer N. Write a method that takes the array as an argument and returns this "outlier" N.   
> 
> Examples:  
> `[2, 4, 0, 100, 4, 11, 2602, 36] # Should return: 11 (the only odd number)`  
> `[160, 3, 1719, 19, 11, 13, -21] # Should return: 160 (the only even number)`  
</details>

<details>
<summary>Consecutive strings</summary>

  + [solution](/6-kyu/Consecutive%20strings.py) | 
    [codewars link](https://www.codewars.com/kata/56a5d994ac971f1ac500003e)

>You are given an array(list) `strarr` of strings and an integer `k`. Your task is 
> to return the first longest string consisting of `k` consecutive strings taken in the array.  
> n being the length of the string array, if `n = 0` or `k > n `or `k <= 0` return `""`.
> 
> Example:  
> `strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2`  
> `Concatenate the consecutive strings of strarr by 2, we get:`  
> `treefoling   (length 10)  concatenation of strarr[0] and strarr[1]`  
> `folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]`  
> `trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]`  
> `blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]`  
> `abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]`  
> `Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".`  
> `The first that came is "folingtrashy" so `  
> `longest_consec(strarr, 2) should return "folingtrashy".`  
> `In the same way:`  
> `longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"`
</details>

<details>
<summary>Highest Scoring Word</summary>

  + [solution](/6-kyu/Highest%20Scoring%20Word.py) | 
    [codewars link](https://www.codewars.com/kata/57eb8fcdf670e99d9b000272)

> Given a string of words, you need to find the highest scoring word.  
> Each letter of a word scores points according to its position in the alphabet: `a = 1, b = 2, c = 3` etc.   
> You need to return the highest scoring word as a string.   
> If two words score the same, return the word that appears earliest in the original string.  
> All letters will be lowercase and all inputs will be valid.  
</details>

<details>
<summary>Multiples of 3 or 5</summary>

  + [solution](/6-kyu/Multiples%20of%203%20or%205.py) | 
    [codewars link](https://www.codewars.com/kata/514b92a657cdc65150000006)

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
> get 3, 5, 6 and 9. The sum of these multiples is 23.   
> Finish the solution so that it returns the sum of all the multiples of 3 or 5 
> below the number passed in. 
> > Note: If the number is a multiple of both 3 and 5, only count it once. Also, 
> > if a number is negative, return 0(for languages that do have them)

</details>
