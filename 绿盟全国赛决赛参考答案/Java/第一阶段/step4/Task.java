package step4;
public class Task {
    
	public void love(int n){
		/********* Begin *********/
        if(n == 1){
            for( double y = 1.3 ; y >= -1.101 ; y -= 0.06 ){
                for( double x = -1.2 ; x <= 1.2 ; x += 0.025 )
                    if( Math.pow((x*x+y*y-1.0),3) - x*x*y*y*y <= 0.0 )
                        System.out.print(' ');
                    else
                        System.out.print('$');
                System.out.println();
            }        
        }
        else{
            String s1 = "I love you!";
            for( double y = 1.3 ; y >= -1.1 ; y -= 0.06 ){
                int index = 0;
                for( double x = -1.1 ; x <= 1.1 ; x += 0.025 )
                    if( x*x + Math.pow(5.0*y/4.0-Math.sqrt(Math.abs(x)),2) - 1 <= 0.0 ){
						char[] s = s1.toCharArray();
                        System.out.print(s[(index++)%s.length]);}
                    else
                        System.out.print(' ');
                System.out.println();
            }
        
        }
		/********* End *********/	
	}
}