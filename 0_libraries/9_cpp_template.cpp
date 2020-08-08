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
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    int n;
    cin >> n >> cout;

    int l;
    vector<int> ls(n);
    REP(i,n) cin >> ls[i];

    sort(ALL(l));
    ll ans = 0;
    for( int i = 0 ; i < n-2 ; i++ ){
        for ( int j = i+1 : j < n-1 ; j++ ){
            ll cnt = 0;
            cnt = lower_bound(ls.begin()+j+1, ls.end());
            ans += cnt
        }
    }
    cout << ans << endl;

}