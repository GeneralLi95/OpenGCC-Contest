#ifndef _TEST
#define _TEST
#include <iostream>
#include <vector>
using namespace std;  
 
class Task{

	public:
		int sort(vector<int> arr){
			/********* Begin *********/
            int swapped1 = 0;
            int swapped2 = 0;
            int i, temp, left = 0, right = arr.size() - 1;
            while (left < right) {
                for (i = left; i < right; i++) {
                    if (arr[i] > arr[i + 1]) {
                        temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                        swapped1 = 1;
                        //打印过程
                        for(int i=0;i<arr.size();i++)
                            cout << arr[i] << " ";
                        cout << endl;
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
                        for(int i=0;i<arr.size();i++)
                            cout << arr[i] << " ";
                        cout << endl;
                    }
                }
                left++;
            }
			//如果没有进行交换，直接打印输出
            if(swapped1 == 0 && swapped2 == 0){
                for(int i=0;i<arr.size();i++)
                    cout << arr[i] << " ";
                cout << endl;
            }
			/********* End *********/
		}
};
#endif