public class SumEvenSquares{
    public static boolean isEven(int number){
        return (number % 2 == 0);
    }
    
    


    public static int sumOfSquaresOfEvenNumbers(int limit){
        int sum = 0;
        for(int count = 0; count <= limit; count++){
            if(isEven(count)){
                sum += count * count; 
            }  
        
        }
        return sum;
    
    }
    
    
    public static void main(String[] args){
        System.out.println(sumOfSquaresOfEvenNumbers(6));       
    
    
    
    
    }
    
}
