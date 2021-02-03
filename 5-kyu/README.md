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
    [codewars link](https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa)
    
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
