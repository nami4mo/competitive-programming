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

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m;
    cin >> n >> m;

    vector<P> al;
    for(int i=0; i<n; i++) {
        ll a; cin >> a;
        al.push_back(P(a,1));
    }

    for(int i=0; i<m; i++) {
        ll b,c; cin >> b >> c;
        al.push_back(P(c,b));
    }

    sort(al.begin(), al.end());
    reverse(al.begin(), al.end());
    ll curr_cnt = 0;
    ll ans = 0;
    for( auto num_cnt : al ){
        ll num = num_cnt.first;
        ll cnt = num_cnt.second;
        if (cnt + curr_cnt <= n){
            ans += num*cnt;
            curr_cnt += cnt;
        }
        else{
            ll rem = n - curr_cnt;
            ans += rem*num;
            break;
        }
    }
    cout << ans << endl;

}