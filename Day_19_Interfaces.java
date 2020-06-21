#Task
#Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. 
#The implementation for the divisorSum(n) method must return the sum of all divisors of n.

class Calculator implements AdvancedArithmetic{
    public int divisorSum(int n){
        // n has no divisors other than itself
        if(n == 1){
            return n;
        }
        
        // Find and sum divisors:
        int half=n/2;
        int sum=n;
        do{
            if(n % half == 0){
                sum += half;
            }
        }while( half-- > 1 );
        
        return sum;
    }
}
