#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;


#define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
#define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
#define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
#define ALL(x) x.begin(),x.end()
#define debug(x) cerr << #x << ": " << x << '\n' // Too slow. Please delete it when submtting the code.

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;


void solve(){
    string s; cin >> s;
    int ans = 0;
    int cnt = 0;
    REP(i,s.size()){
        // debug(i);
        if(i%2==0 && s[i]=='0') cnt+=1;
        else if(i%2==1 && s[i]=='1') cnt+=1;
    }
    ans = cnt;
    cnt = 0;
    REP(i,s.size()){
        if(i%2==0 && s[i]=='1') cnt+=1;
        else if(i%2==1 && s[i]=='0') cnt+=1;
    }
    ans = min(ans,cnt);
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}