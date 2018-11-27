package step1;

public class Task {
	
	public void sort(Integer[] arr){
		/********* Begin *********/
        
        int swapped1 = 0;
        int swapped2 = 0;
        int i, temp, left = 0, right = arr.length - 1;
        while (left < right) {
            for (i = left; i < right; i++) {
                if (arr[i] > arr[i + 1]) {
                    temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    swapped1 = 1;
                    //打印过程	
                    for(int a:arr)
                        System.out.print(a + " ");				
                    System.out.println();
                }
            }
            right--;
            for (i = right; i > left; i--)
            {
                if (arr[i - 1] > arr[i])
                {
                    temp = arr[i];
                    arr[i] = arr[i - 1];
                    arr[i - 1] = temp;
                    swapped2 = 1;
                    //打印过程	
                    for(int a:arr)
                        System.out.print(a + " ");				
                    System.out.println();
                }
            }
            left++;
        }
        if(swapped1 == 0 && swapped2 == 0){
            for(int a:arr)
                System.out.print(a + " ");				
            System.out.println();
        }

		/********* End *********/
	}
}