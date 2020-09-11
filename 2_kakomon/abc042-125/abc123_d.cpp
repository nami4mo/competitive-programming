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
typedef pair<ll,ll> P;

#define REP(i,n) for(ll i=0 ; i<ll(n) ; i++)
#define ALL(x) x.begin(),x.end()

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int x,y,z,k;
    cin >> x >> y >> z >> k;

    vector<ll> xl(x), yl(y),zl(z);
    REP(i,x) cin >> xl[i];
    REP(i,y) cin >> yl[i];
    REP(i,z) cin >> zl[i];
    vector<ll> xyl;
    for(int i = 0 ; i < x; i++ ){
        for(int j=0 ; j < y ; j++){
            xyl.push_back(xl[i]+yl[j]);
        }
    }
    sort(xyl.begin(), xyl.end(), greater<ll>());
    
    vector<ll> xyzl;
    for(int i=0 ; i<min(k,x*y) ; i++){
        for(int j=0 ; j < z; j++){
            xyzl.push_back(xyl[i]+zl[j]);
        }
    }

    sort(xyzl.begin(), xyzl.end(), greater<ll>());
    for(int i = 0; i < k ; i++){
        cout << xyzl[i] << endl;
    }

}