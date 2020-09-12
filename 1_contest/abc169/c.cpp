#include <set> 
#include <tuple> 
#include <iostream>

using namespace std; 
int main(){
    long long a;
    double b; 
    int bi;
    long long ans;
    cin >> a >> b;

    bi = b*100;
    ans = a*bi;
    cout << ans/100 << endl;
}