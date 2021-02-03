# Codewars Kata Solutions

### [Link to my profile](https://www.codewars.com/users/TimRock)
## 7 Kyu

<details>
<summary>Square Every Digit</summary>


  + [solution](/7-kyu/Square%20Every%20Digit.py) | 
  [codewars link](https://www.codewars.com/kata/546e2562b03326a88e000020)

>Welcome. In this kata, you are asked to square every digit of a number and concatenate them.  
>For example, if we run `9119` through the function, `811181` will come out, 
> because `9^2` is `81` and `1^2` is `1`.
>Note: The function accepts an integer and returns an integer
</details>

<details>
<summary>Isograms</summary>


  + [solution](/7-kyu/Isograms.py) | 
  [codewars link](https://www.codewars.com/kata/54ba84be607a92aa900000f1)

> An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
> Implement a function that determines whether a string that contains only letters 
> is an isogram. Assume the empty string is an isogram. Ignore letter case.
>
>Examples:
>
>`is_isogram("Dermatoglyphics" ) == true`
>`is_isogram("aba" ) == false`
</details>

<details>
<summary>Two to One</summary>


  + [solution](/7-kyu/Two%20to%20One.py) | 
  [codewars link](https://www.codewars.com/kata/5656b6906de340bd1b0000ac)

>Take 2 strings `s1` and `s2` including only letters from `a` to `z`. Return a 
> new sorted string, the longest possible, containing distinct letters - each 
> taken only once - coming from s`1` or `s2`.  
> 
> Examples:
> 
>`a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"`
`longest(a, b) -> "abcdefklmopqwxy"`
</details>

<details>
<summary>Ones and Zeros</summary>


  + [solution](/7-kyu/Ones%20and%20Zeros.py) | 
  [codewars link](https://www.codewars.com/kata/578553c3a1b8d5c40300037c)    

>Given an array of ones and zeroes, convert the equivalent binary value to an integer.  
Eg: `[0, 0, 0, 1]` is treated as 0001 which is the binary representation of `1`.
>
>Examples:
>
>`Testing: [0, 0, 1, 0] ==> 2`  
>`Testing: [0, 1, 0, 1] ==> 5`  
>`Testing: [1, 0, 0, 1] ==> 9`  
>`Testing: [1, 1, 1, 1] ==> 15`
</details>

<details>
<summary>Find the divisors! </summary>


  + [solution](/7-kyu/Find%20the%20divisors!.py) | 
  [codewars link](https://www.codewars.com/kata/544aed4c4a30184e960010f4)

> Create a function named `divisors`/`Divisors` that takes an integer `n > 1` and returns an array 
> with all of the integer's divisors(except for 1 and the number itself), from smallest to largest.   
> If the number is prime return the string `(integer) is prime`.
> 
> Examples:
> 
> `divisors(12); #should return [2,3,4,6]`
>`divisors(13); #should return "13 is prime"`
</details>

<details>
<summary>Binary Addition</summary>


  + [solution](/7-kyu/Binary%20Addition.py) | 
  [codewars link](https://www.codewars.com/kata/551f37452ff852b7bd000139)

>Implement a function that adds two numbers together and returns their sum in binary. 
> The conversion can be done before, or after the addition.  
>The binary number returned should be a string.
</details>

<details>
<summary>Growth of a Population</summary>


  + [solution](/7-kyu/Growth%20of%20a%20Population.py) | 
  [codewars link](https://www.codewars.com/kata/563b662a59afc2b5120000c6)

> In a small town the population is `p0` at the beginning of a year. The population regularly increases 
> by `percent` per year and moreover `aug` new inhabitants per year come to live in the town.   
> How many years does the town need to see its population greater or equal to `p` inhabitants?    
> More generally given parameters:    
>`p0`, `percent`, `aug` (inhabitants coming or leaving each year), `p` (population to surpass)  
>the function `nb_year` should return `n` number of entire years needed to get a population greater or equal to `p`.  
>`aug` is an integer, `percent` a positive or null floating number, `p0` and `p` are positive integers (> 0)
>
>Examples:  
>`nb_year(1500, 5, 100, 5000) -> 15`  
>`nb_year(1500000, 2.5, 10000, 2000000) -> 10`
</details>

<details>
<summary>Get decimal part of the given number</summary>


  + [solution](/7-kyu/Get%20decimal%20part%20of%20the%20given%20number.py) | 
  [codewars link](https://www.codewars.com/kata/586e4c61aa0428f04e000069) 

>Write a function that returns only the decimal part of the given number.  
>You only have to handle valid numbers, not `Infinity`, `NaN`, or similar. Always return a positive decimal part.  
>
>Examples  
>`get_decimal(2.4)  # 0.4`  
>`get_decimal(-0.2) # 0.2`
</details>

<details>
<summary>Vowel Count</summary>


  + [solution](/7-kyu/Vowel%20Count.py) | 
  [codewars link](https://www.codewars.com/kata/54ff3102c1bad923760001f3)

>Return the number (count) of vowels in the given string.  
>We will consider `a, e, i, o, u` as vowels for this Kata (but not `y`).  
>The input string will only consist of lower case letters and/or spaces.  
</details>


## 6 Kyu

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

## 5 Kyu

<details>
<summary>Human Readable Time</summary>


  + [solution](/5-kyu/Human%20Readable%20Time.py) | 
    [codewars link](https://www.codewars.com/kata/52685f7382004e774f0001f7)

> Write a function, which takes a non-negative integer (seconds) as input and 
> returns the time in a human-readable format (`HH:MM:SS`)
> * `HH` = hours, padded to 2 digits, range: 00 - 99 
> * `MM` = minutes, padded to 2 digits, range: 00 - 59 
> * `SS` = seconds, padded to 2 digits, range: 00 - 59 
> 
> The maximum time never exceeds 359999 (`99:59:59`)
> You can find some examples in the test fixtures.

</details>

<details>
<summary>Moving Zeros To The End</summary>


  + [solution](/5-kyu/Moving%20Zeros%20To%20The%20End.py) | 
    [codewars link](https://www.codewars.com/kata/52597aa56021e91c93000cb0)

> Write an algorithm that takes an array and moves all of the zeros to the end, 
> preserving the order of the other elements. 
> `move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]`
</details>

<details>
<summary>Rot13</summary>


  + [solution](/5-kyu/Rot13.py) | 
    [codewars link](https://www.codewars.com/kata/530e15517bc88ac656000716)

> ROT13 is a simple letter substitution cipher that replaces a letter with the 
> letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.   
> Create a function that takes a string and returns the string ciphered with 
> Rot13. If there are numbers or special characters included in the string, they 
> should be returned as they are. Only letters from the latin/english alphabet 
> should be shifted, like in the original Rot13 "implementation".   
> Please note that using encode is considered cheating.

</details>

<details>
<summary>Best travel</summary>

  + [solution](/5-kyu/Best%20travel.py) | 
    [codewars link](https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python)
    
> John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet 
> of paper a list of distances between these towns. `ls = [50, 55, 57, 58, 60]`. John is 
> tired of driving and he says to Mary that he doesn't want to drive more than `t = 174 `
> miles and he will visit only 3 towns. Which distances, hence which towns, they will 
> choose so that the sum of the distances is the biggest possible to please Mary and John?   
> 
> Example:  
> With list `ls` and 3 towns to visit they can make a choice between:   
> `[50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].`     
> The sums of distances are then: `162, 163, 165, 165, 167, 168, 170, 172, 173, 175`.   
> The biggest possible sum taking a limit of `174` into account is then `173` and 
> the distances of the `3` corresponding towns is `[55, 58, 60]`.   
> The function `chooseBestSum` (or `choose_best_sum `or ... depending on the language) 
> will take as parameters `t` (maximum sum of distances, integer >= 0), `k` (number of 
> towns to visit, k >= 1) and `ls` (list of distances, all distances are positive or 
> null integers and this list has at least one element). The function returns the 
> "best" sum ie the biggest possible sum of `k` distances less than or equal to the 
> given limit `t`, if that sum exists, or otherwise nil, null, None, Nothing, depending 
> on the language.
> 
> Examples:  
> `ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163`  
> `xs = [50] choose_best_sum(163, 3, xs) -> null`  
> `ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228  `   
> 
> Note:  
> don't modify the input list ls  

</details>

<details>
<summary>Gap in Primes</summary>

  + [solution](/5-kyu/Gap%20in%20Primes.py) | 
    [codewars link](https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa)
    
> The prime numbers are not regularly spaced. For example from `2` to `3` the gap is `1`. 
> From `3` to `5` the gap is `2`. From `7` to `11` it is `4`. Between `2` and `50 `we have the 
> following pairs of 2-gaps primes: `3-5`, `5-7`, `11-13`, `17-19`, `29-31`, `41-43`  
> A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes [link](http://mathworld.wolfram.com/PrimeGaps.html).  
> We will write a function gap with parameters:  
> `g` (integer >= 2) which indicates the gap we are looking for  
> `m` (integer > 2) which gives the start of the search (m inclusive)  
> `n` (integer >= m) which gives the end of the search (n inclusive)  
> `n` won't go beyond 1100000.  
> In the example above `gap(2, 3, 50)` will return `[3, 5]` which is the first 
> pair between 3 and 50 with a 2-gap.  
> So this function should return the first pair of two prime numbers spaced with 
> a gap of `g` between the limits `m`, `n` if these numbers exist otherwise None.  
> 
> Examples:  
> `gap(2, 5, 7) --> [5, 7]`  
> `gap(2, 5, 5) --> None`  
> `gap(4, 130, 200) --> [163, 167]`

</details>

<details>
<summary>PaginationHelper</summary>

  + [solution](/5-kyu/PaginationHelper.py) | 
    [codewars link](https://www.codewars.com/kata/515bb423de843ea99400000a)
    
> For this exercise you will be strengthening your page-fu mastery. You will 
> complete the PaginationHelper class, which is a utility class helpful for 
> querying paging information related to an array.  
> The class is designed to take in an array of values and an integer indicating 
> how many items will be allowed per each page. The types of values contained within 
> the collection/array are not relevant.  
> The following are some examples of how this class is used:  
> `helper = PaginationHelper(['a','b','c','d','e','f'], 4)`  
> `helper.page_count() # should == 2`  
> `helper.item_count() # should == 6`  
> `helper.page_item_count(0)  # should == 4`  
> `helper.page_item_count(1) # last page - should == 2`  
> `helper.page_item_count(2) # should == -1 since the page is invalid`  
> `# page_index takes an item index and returns the page that it belongs on`  
> `helper.page_index(5) # should == 1 (zero based index)`  
> `helper.page_index(2) # should == 0`  
> `helper.page_index(20) # should == -1`  
> `helper.page_index(-10) # should == -1 because negative indexes are invalid`  

</details>

<details>
<summary>Number of trailing zeros of N!</summary>

  + [solution](/5-kyu/Number%20of%20trailing%20zeros%20of%20N!.py) | 
    [codewars link](https://www.codewars.com/kata/52f787eb172a8b4ae1000a34)
    
> Write a program that will calculate the number of trailing zeros in a factorial of a given number.  
> `N! = 1 * 2 * 3 * ... * N  `
> Be careful 1000! has 2568 digits...  
> For more info, see: http://mathworld.wolfram.com/Factorial.html
> 
> Examples  
> `zeros(6) = 1   # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero  `
> `zeros(12) = 2   # 12! = 479001600 --> 2 trailing zeros`

</details>
