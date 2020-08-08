#include<algorithm>
#include<bitset>
#include<cmath>
#include<complex>
#include<deque>
#include<functional>
#include<iomanip>
#include<iostream>
#include<iterator>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<unordered_map>
#include<unordered_set>
#include<utility>
#include<vector>

using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    double ans = 0;
    for( int i = 1 ; i <= n ; i++ ){
        int curr_num = i;
        int multi_cnt = 0;
        while(1){
            if( curr_num >= k ){
                break;
            }
            curr_num*=2;
            multi_cnt+=1;
        }
        double prob = 1.0/pow(2,multi_cnt);
        ans += prob;
    }
    ans /= n;
    printf("%.12f",ans);
}