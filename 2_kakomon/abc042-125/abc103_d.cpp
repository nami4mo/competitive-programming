#include <bits/stdc++.h>
#include <cmath>

using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
#define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
#define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
#define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
#define ALL(x) x.begin(),x.end()

#define DEBUG(x) cerr << #x << ": " << x << '\n'
#define DEBUGL(xl) dbgl_f(#xl,xl)
#define DEBUGLL(xll) dbgll_f(#xll,xll)
template<class T> void dbgl_f(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr << '\n';}
template<class T> void dbgll_f(string name, vector<vector<T>> xll){
    cerr<< name << ": " << '\n'; 
    for(vector<T> xl: xll){
        for(T x : xl) cerr << x << " ";
        cerr << '\n';
    }
}

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;


void solve(){
    int n,m; cin >> n >> m;
    vector<P> abl;
    REP(i,m){
        int a,b; cin >> a >> b;
        abl.push_back(P(a,b));
    }
    sort(abl.begin(), abl.end());
    int curr_l = 0;
    int curr_r = 0;
    int ans = 0;
    for( P ab : abl ){
        int a = ab.first;
        int b = ab.second;
        if(a < curr_r && curr_r <= b){
        }
        else if( b < curr_r ){
            curr_r = b;
        }
        else if( a >= curr_r ){
            ans += 1;
            curr_r = b;
        }
    }
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}