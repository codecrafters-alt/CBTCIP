#include <iostream>
using namespace std;
//recursion 
int factorial(int n){
    //base case mandatory 
   if(n==0){
      return 1;
   }
   return n*factorial(n-1);
}



int main() {
    
int n;
cin>>n;
 int result=factorial(n);
 cout<<result;


    return 0;
}