#ifndef _TEST
#define _TEST
#include <iostream>
#include <vector>

using namespace std;  

class Task{

	public:
		int virusArea(int n,int m,vector<vector<char> >& area){
			/********* Begin *********/
            if (area.empty()|| area.size() == 0 || area[0].size() == 0)
                return 0;

            int count = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    if (area[i][j] == 'o') {
                        count++;
                        change(area, i, j, n, m);
                    }            
            return count++;    
		    /********* End *********/
		}
    private:
        void change(vector<vector<char> >& area, 
            int i, int j, int n, int m) {
            if (i < 0 || i >= n || j < 0 || j >= m)
                return;
            if (area[i][j] != 'o')
                return;

            area[i][j] = '0';
            change(area, i + 1, j, n, m);
            change(area, i - 1, j, n, m);
            change(area, i, j + 1, n, m);
            change(area, i, j - 1, n, m);
        }
};
#endif