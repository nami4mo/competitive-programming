#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;

#define REP(i,n) for(ll i=0 ; i<ll(n) ; i++)   // for i in range(n)
#define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
#define ALL(x) x.begin(),x.end()
#define MOD 1'000'000'007
#define debug(x) cerr << #x << ": " << x << '\n'


void solve(){
    ll p,f; cin >> p >> f;
    ll cs,cw; cin >> cs >> cw;
    ll ws,ww; cin >> ws >> ww;

    if(ws > ww){
        swap(cs,cw);
        swap(ws,ww);
    }
    ll ans = 0;
    REP(s1,cs+1){
        // cout << "--" << s1 <<endl; 
        ll p_cnt = 0;
        ll f_cnt = 0;
        ll rem_s = cs;
        ll rem_w = cw;
        if( s1*ws <= p ){
            p_cnt += s1;
            ll pw = min((p-s1*ws)/ww, cw);
            p_cnt += pw;
            rem_s -= s1;
            rem_w -= pw;
            // cout << pw << " ";
        }
        else{
            ll ps = p/ws;
            rem_s -= ps;
            p_cnt += ps;
        }
        ll fs = min(f/ws, rem_s);
        ll fw = min((f-fs*ws)/ww, rem_w);
        // cout << fs << " " << fw << endl;
        ans = max(ans, p_cnt+fs+fw);
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