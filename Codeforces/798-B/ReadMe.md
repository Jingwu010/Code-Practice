

### 798/B Mike String

#### 1. Abstract:

​	Given #**n** Strings, they have equal length, for each step we can move the top character of any string to its end. Question is how many steps do you need to make the strings all the same. Print the least steps you need (-1 means no solution).



#### 2. Samples

```
input
  4
  xzzwo
  zwoxz
  zzwox
  xzzwo
output
  5
	
input
  2
  molzv
  lzvmo
output
  2
  
input
  3
  kc
  kc
  kc
output
  0
  
input
  3
  aa
  aa
  ab
output
  -1
```



#### 3. Idea

​	The general idea of solving this problem is Looping possibilities. 

There are two ways to solve the problem.

1. (My implementation) Use first string as template, record indexes for following string rotate into the first string. 

   For Example

   ~~~~
   xzzwo   -->   [0]
   zwoxz   -->   [2]
   zzwox   -->   [1]
   xzzwo   -->   [0]
   ~~~~

   Then, scan the index from 0 to string length, record the total minimum steps to finish the rotation for all strings

   ~~~~
   	index			Steps
   	 0  		0+3+4+0 = 7
   	 1  		1+4+0+1 = 6
   	 2  		2+0+1+2 = 5
   	 3  		3+1+2+3 = 9
   	 4  		4+2+3+4 = 13
   	 5  		5+3+4+5 = 17
   ~~~~

2. A good implementaion online

   Note that the smallest step must be transforming into an existing string among all the strings. Then we can scan the strings list and calculate the minimum steps for all strings to transform into a given string.

   For Example

   ~~~~
   xzzwo   -->   0+3+4+0 = 7
   zwoxz   -->   2+0+1+2 = 5
   zzwox   -->   1+4+0+1 = 6
   xzzwo   -->   0+3+4+0 = 7
   ~~~~

#### 4. Pitfalls and Tips (For my Implementation)

- Considering the repeated string like abcabcabc, then the indexes for a given string rotate into the first template string should be recorded many numbers. For later usage, loop all the indexes and find the shortest rotate index (step).

  For Examlple

  ~~~~
  abcabcabc   -->   [0]
  bcabcabca   -->   [1,4,7]
  cabcabcab   -->   [2,5,8]
  cabcabcab   -->   [2,5,8]
  ~~~~

#### 5. Algorithm Complexity

- For constructing indexes array — O(n * len)
- For calculation of minimum step — O(n * len * indexes.length)

#### 6. Core blocks

```java
for(int i = 1; i < n; i++){
    String line = sc.nextLine();
    compareString(first, line, i);
    if(indexes[i].size() == 0) flag = false;
}

if(flag == false) System.out.println("-1");
else{
    int mins = Integer.MAX_VALUE;
  
  	// Sorting all the possible Strings derived from
    // template string (The first string) 
    for(int set = 0; set < len; set++){
        int temp = 0;
        for(int i = 0; i < n; i++){
            temp += findNearest(i, set);
        }
        mins = Math.min(mins, temp);
    }
    System.out.println(mins);
}
```



```java
private static void compareString(String first, String second, int pos){
    indexes[pos] = new ArrayList<Integer>();
    String template = first + first;
    int index = 0;
    // Looping all the indexes and record the possible index that
    // make the second string rotate into first string
    while(index < len){
        boolean flag = true;
        for(int i = 0; i < len; i++){
            if(template.charAt(i + index) != second.charAt(i)) {
                flag = false;
                break;
            }
        }
        if (flag == true){
            indexes[pos].add(index);
        }
        index ++;
    }
}
```



~~~~java
private static int findNearest(int pos, int cmp){
		int dis = 51;
  
  	// find the shorest step for a given string rotate into
    // a specific form (cmp)
    for (Integer number : indexes[pos]) {
        int temDis = 0;
        if(number <= cmp) temDis = cmp - number;
        else temDis = len - number + cmp;
        if(temDis < dis)
            dis = temDis;
    }	
    return dis;
}
~~~~