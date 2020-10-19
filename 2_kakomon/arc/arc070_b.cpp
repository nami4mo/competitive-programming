#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
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
    ll n,k; cin >> n >> k;
    vector<int> al(n); REP(i,n) cin >> al[i];

    vector<vector<bool>> dp(n+1, vector<bool>(k,false));
    vector<vector<bool>> dpr(n+1, vector<bool>(k,false));
    dp[0][0] = true;
    dpr[0][0] = true;

    REP(i,n){
        ll a = al[i];
        REP(j,k){
            if(dp[i][j]){
                dp[i+1][j] = true;
                if(a+j<k) dp[i+1][a+j] = true;     
            }
        }
        ll ar = al[n-i-1];
        REP(j,k){
            if(dpr[i][j]){
                dpr[i+1][j] = true; 
                if(ar+j<k) dpr[i+1][ar+j] = true;           
            }
        }
    }

    vector<vector<int>> dpi(n+1);
    vector<vector<int>> dpri(n+1);
    REP(i,n+1){
        REP(j,k){
            if(dp[i][j]){
                dpi[i].push_back(j);
            }
            if(dpr[i][j]){
                dpri[i].push_back(j);
            }
        }
    }

    // DEBUGLL(dpi);
    // DEBUGLL(dpri);

    int not_ans = 0;
    REP(i,n){
        int a = al[i];
        for( int lv : dpi[i] ){
            auto cnt1 = lower_bound(dpri[n-i-1].begin(), dpri[n-i-1].end(), k-lv);
            auto cnt2 = lower_bound(dpri[n-i-1].begin(), dpri[n-i-1].end(), k-lv-a);
            int cnt = cnt1-cnt2;
            if(cnt != 0){
                not_ans++;
                break;
            }
        }
    }
    cout << n-not_ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}