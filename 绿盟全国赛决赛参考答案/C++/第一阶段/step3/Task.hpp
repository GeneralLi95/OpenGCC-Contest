#ifndef _TEST
#define _TEST
#include <iostream>
#include <vector>

using namespace std;  
 
class Task{

	public:
		int concaveValley(vector<int> arr){
			/********* Begin *********/
			int res = 0;
			int up = 0;
			int down = 0;
			for (int i = 1; i < arr.size(); i++) {
				if(up > 0 && arr[i - 1] > arr[i] || arr[i - 1] == arr[i])  up = down = 0;					
				if(arr[i - 1] < arr[i])   up +=1;
				if(arr[i - 1] > arr[i])   down+=1;
				if( up > 0 && down > 0 && up + down + 1 > res)   res = up + down + 1;		
				
			}
			return res;
			/********* End *********/
		}

};
#endif