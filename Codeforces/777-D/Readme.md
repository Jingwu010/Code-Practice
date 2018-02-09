### [777/D](http://codeforces.com/contest/777/problem/D) Cloud of Hashtags

#### 1. Abstract:

​	Given #**n** lines of **strings**, delete any charactors in each string to make all the strings being lexicographically displayed

#### 2. Samples

~~~~
input
  3
  #book
  #bigtown
  #big
output
  #b
  #big
  #big
  
input
  3
  #book
  #cool
  #cold
output
  #book
  #co
  #cold
  
...
~~~~



#### 3. Idea

​	Backtracing String arrays, making each string[i] lexicographically less than string[i+1]



#### 4. Pitfalls and Tips

- Large Data Set input and output, Try using a different way rather than using scanner.readline()

- A new read method is needed to cut down data input speed

  ​



#### 5. Algorithm Complexity 

+ For backtracing all strings o(1) maximum — 500,000

  ​



#### 6. Core blocks

~~~~java
/*
    ATTENTION:
        The InputReader Class is copied from 
        http://codeforces.com/profile/spar5h
*/
static class InputReader
{
    private InputStream stream;
    private byte[] buf = new byte[1024];
    private int curChar;
    private int numChars;
    private SpaceCharFilter filter;
  
    public InputReader(InputStream stream)
    {
        this.stream = stream;
    }

    public int read()
    {
        if (numChars==-1) 
            throw new InputMismatchException();

        if (curChar >= numChars)
        {
            curChar = 0;
            try 
            {
                numChars = stream.read(buf);
            }
            catch (IOException e)
            {
                throw new InputMismatchException();
            }

            if(numChars <= 0)				
                return -1;
        }
        return buf[curChar++];
    }

    public String nextLine()
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String str = "";
        try
        {
            str = br.readLine();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return str;
    }
    public int nextInt()
    {
        int c = read();

        while(isSpaceChar(c)) 
            c = read();

        int sgn = 1;

        if (c == '-') 
        {
            sgn = -1;
            c = read();
        }

        int res = 0;
        do 
        {
            if(c<'0'||c>'9') 
                throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        }
        while (!isSpaceChar(c)); 

        return res * sgn;
    }

    public long nextLong() 
    {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        int sgn = 1;
        if (c == '-') 
        {
            sgn = -1;
            c = read();
        }
        long res = 0;

        do 
        {
            if (c < '0' || c > '9')
                throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        }
        while (!isSpaceChar(c));
            return res * sgn;
    }

    public double nextDouble() 
    {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        int sgn = 1;
        if (c == '-') 
        {
            sgn = -1;
            c = read();
        }
        double res = 0;
        while (!isSpaceChar(c) && c != '.') 
        {
            if (c == 'e' || c == 'E')
                return res * Math.pow(10, nextInt());
            if (c < '0' || c > '9')
                throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        }
        if (c == '.') 
        {
            c = read();
            double m = 1;
            while (!isSpaceChar(c)) 
            {
                if (c == 'e' || c == 'E')
                    return res * Math.pow(10, nextInt());
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                m /= 10;
                res += (c - '0') * m;
                c = read();
            }
        }
        return res * sgn;
    }

    public String readString() 
    {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        StringBuilder res = new StringBuilder();
        do 
        {
            res.appendCodePoint(c);
            c = read();
        } 
        while (!isSpaceChar(c));

        return res.toString();
    }

    public boolean isSpaceChar(int c) 
    {
        if (filter != null)
            return filter.isSpaceChar(c);
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    public String next() 
    {
        return readString();
    }

    public interface SpaceCharFilter 
    {
        public boolean isSpaceChar(int ch);
    }
}
~~~~



~~~~java
public static void calculateLowest(){
    for(int i = n - 2; i >= 0; i--){
        int j = 0;
        boolean isSame = true;
        // compare two strings at index j
        for(j = 1; j < strings[i+1].length(); j++){
            // if current string run out of charactors
            if(j >= strings[i].length()){
                break;
            }
            // compare two charactors at index j from two strings
            Character c1 = new Character(strings[i].charAt(j));
            Character c2 = new Character(strings[i+1].charAt(j));
            int res = c1.compareTo(c2);
            if(res > 0){
                // if current string lexicographically greater at index j
                // get rid of all charactors after j
                break;
            } else if(res < 0){
                // else if current string lexicographically smaller at index j
                // preserve all charactors after j
                isSame = false;
            }
        }
        if(isSame == true) strings[i] = strings[i].substring(0, j);
    }
}
~~~~

