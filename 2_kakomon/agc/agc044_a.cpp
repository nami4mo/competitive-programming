#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
#endif
using namespace std;
using namespace atcoder;
namespace defines{
    typedef long long ll;
    typedef pair<ll,ll> P;
    #define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
    #define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
    #define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
    #define ALL(x) x.begin(),x.end()
    template<class T> vector<T> make_vec(size_t a){return vector<T>(a);}
    template<class T, class... Ts> auto make_vec(size_t a, Ts... ts){ return vector<decltype(make_vec<T>(ts...))>(a, make_vec<T>(ts...));}

    /* for debug print */
    #define DEBUG(x) cerr << #x << ": " << x << '\n'
    #define DEBUGP(x) cerr << #x << ": (" << x.first << ", " << x.second << ")" << '\n' 
    #define DEBUGL(xl) dbgl_f(#xl,xl)
    #define DEBUGLP(xl) dbglp_f(#xl,xl)
    #define DEBUGLL(xll) dbgll_f(#xll,xll)
    #define DEBUGM(xl) dbgm_f(#xl,xl)
    template<class T> void dbgl_f(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr << '\n';}
    template<class T, class U> void dbgm_f(string name, map<T,U> xl){cerr<<name<<": ";for(auto x: xl)cerr<<"("<<x.first<<": "<<x.second<<") ";cerr<<'\n';}
    template<class T> void dbglp_f(string name, vector<T> xl){cerr<<name<<": ";for(T x: xl)cerr<<"("<<x.first<<", "<< x.second<<") ";cerr<<'\n';}
    template<class T> void dbgll_f(string name, vector<vector<T>> xll){
        cerr<< name << ": " << '\n'; 
        for(vector<T> xl: xll){
            for(T x : xl) cerr << x << " ";
            cerr << '\n';
        }
    }
}
using namespace defines;

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;


void solve(){
    int t; cin >> t;
    vector<ll> ans;
    REP(i,t){
        int n,a,b,c; cin >> n >> a >> b >> c;
        int d; cin >> d;
        vector<ll> dp(n+10, pow(10,18));
        for(ll i = n ; i > 0 ; i--){
            if( i%2 == 0)  dp[i/2] = min(dp[i/2], dp[i]+a);
            if( i%3 == 0)  dp[i/3] = min(dp[i/3], dp[i]+b);
            if( i%5 == 0)  dp[i/5] = min(dp[i/5], dp[i]+c);

            if( i >= 1 ) dp[i-1] = min(dp[i-1], dp[i]+d);
            if( i >= 2 ) dp[i-2] = min(dp[i-2], dp[i]+d*2);
            if( i >= 3 ) dp[i-3] = min(dp[i-3], dp[i]+d*3);
            if( i >= 4 ) dp[i-4] = min(dp[i-4], dp[i]+d*4);

             dp[i+1] = min(dp[i-1], dp[i]+d);
            dp[i+2] = min(dp[i-2], dp[i]+d*2);
             dp[i+3] = min(dp[i-3], dp[i]+d*3);
            dp[i+4] = min(dp[i-4], dp[i]+d*4) ;  
        }
        ans.push_back(dp[0]);
    }
    for(ll a:ans) cout << a << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}

