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
    int n; cin >> n;
    vector<ll> al(n); REP(i,n) cin >> al[i];
    vector<ll> cumsums(n+1,0);
    REP(i,n){
        cumsums[i+1] = cumsums[i]+al[i];
    }

    ll ans = INF;
    FOR(i,2,n-1){
        // DEBUG(i);

        ll left_sum = cumsums[i];
        ll p2,q2,p,q;
        auto iter3 = lower_bound(ALL(cumsums), left_sum/2);
        int ind3 = iter3 - cumsums.begin();
        int ind4 = ind3-1;
        if(ind3 <= 0) ind3 = 1;
        if(ind3 >= i) ind3 = i-1;
        p = cumsums[ind3];
        q = cumsums[i]-cumsums[ind3];


        if(ind4 <= 0) ind4 = 1;
        if(ind4 >= i) ind4 = i-1;
        p2 = cumsums[ind4];
        q2 = cumsums[i]-cumsums[ind4];
        if(abs(p-q) > abs(p2-q2)){
            p = p2;
            q = q2;
        }

        ll right_sum = cumsums[n]-cumsums[i];
        // ll right_start = cumsums[i+1];
        ll left_end = cumsums[i];
        ll r2,s2,r,s;
        auto iter = lower_bound(ALL(cumsums), left_end+right_sum/2);
        int ind = iter - cumsums.begin();
        int ind2 = ind-1;
        if(ind <= i) ind = i+1;
        if(ind >= n) ind = n-1;
        r = cumsums[ind]-cumsums[i];
        s = cumsums[n]-cumsums[ind];

        if(ind2 <= i) ind2 = i+1;
        if(ind2 >= n) ind2 = n-1;
        r2 = cumsums[ind2]-cumsums[i];
        s2 = cumsums[n]-cumsums[ind2];
        if(abs(r-s) > abs(r2-s2)){
            r = r2;
            s = s2;
        }
        ans = min(ans, max({p,q,r,s})-min({p,q,r,s}));

        // DEBUG(left_sum);
        // DEBUG(right_sum);
        // DEBUG(left_end);
        // DEBUG(left_end+right_sum/2);
        // DEBUG(max({p,q,r,s})-min({p,q,r,s}));
        // printf("%d, %d, %d, %d\n\n",p,q,r,s);
    }
    cout << ans << endl;
    // DEBUGL(cumsums);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}