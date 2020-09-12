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

void solve(){
    int n; cin >> n;
    string s; cin >> s;
    string ans;
    REP(i,n) {
        ans += s[i*2];
    }
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    for(ll i = 0 ; i < t; i++){
        solve();
    }

}