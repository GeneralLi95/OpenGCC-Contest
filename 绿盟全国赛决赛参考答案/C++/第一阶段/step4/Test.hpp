#ifndef _TEST
#define _TEST
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;  

class Task{

	public:
		void love(int n){
			/********* Begin *********/
			if(n == 1){
                for( float y = 1.3 ; y >= -1.1 ; y -= 0.06 ){
                    for( float x = -1.2 ; x <= 1.2 ; x += 0.025 )
                        if( pow((x*x+y*y-1.0),3) - x*x*y*y*y <= 0.0 )
                            cout<<' ';
                    else
                        cout<<'$';
                    cout<<endl;
                } 
            }
            else{
                string s = "I love you!";
                for( float y = 1.3 ; y >= -1.1 ; y -= 0.06 ){
                    int index = 0;
                    for( float x = -1.1 ; x <= 1.1 ; x += 0.025 )
                        if( x*x + pow(5.0*y/4.0-sqrt(fabs(x)),2) - 1 <= 0.0 )
                            cout<<s[(index++)%s.size()];
                        else
                            cout<<' ';
                    cout<<endl;
                }            
            }

			/********* End *********/
		}
};
#endif