# Time and Space Complexity
- It is a mesaure of how the time taken or space required for execution varies with input.
- We always compute the worst case scenario when we measure time or space complexity.
- To measure time or space complexity we use the Big O notation. This provides us a simplified way of understanding of how input is affecting the output.

# Time Complexity
It is a measure of how the time taken scales with input. Here we cannot always calculate the time for each piece of code. Hence we use number of operations as a measure.

# Space Complexity
It is a measure total space taken to solve the given problem. Here the total space consists of two things 
1. Input Space
2. Auxiliary Space: Space that is used other than what is used by the input, to solve the problem.
We can and want to manage the Auxiliary space effectively while thinking of the solution.

# Rules for measuring using Big O notation
1. Always calculate for Worst case scenario.
2. Avoid constants.
3. Avoid lower values. avoid lower degrees

# Example of Big O notation:
Taking a for loop example 
<pre> ```javascript for(let i=0;i<n;i++){if(i%2 == 0){print("Even")}else{print("Odd")}}``` </pre>

In the above example:
1. Time Complexity
  - per iteration 'i<n', 'i++' , if(i%2==0) or else with print statements are executed. With let 'i=0' as one statement that runs on the first iteration.
  - so the number of operations would be 4n + 1.
  - Applying the rules of Big O notation we get O(4n + 1) -> O(n) for time complexity.
2. Space Complexity
  - We only have i as an extra variable so the space required is 1
  - Applying the rules of Big O notation we get O(1)
