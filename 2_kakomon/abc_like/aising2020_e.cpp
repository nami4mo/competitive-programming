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
    template<typename A, size_t N, typename T> void Fill(A (&array)[N], const T &val){std::fill( (T*)array, (T*)(array+N), val );}
}
using namespace defines;

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;
// const int MOD = 998244353;
// using mint = modint1000000007;
// using mint = modint998244353;

// struct Camel{
//     ll k;
//     ll l;
//     ll r;
//     Camel(ll k, ll r, ll l):k{k},l{l},r{r}{}
// };

void solve(){
    ll n; cin >> n;
    vector<vector<ll>> lefts(n+1);
    vector<vector<ll>> rights(n+1);
    ll ans = 0;
    ll left_start = -1;
    REP(i,n){
        ll k,l,r; cin >> k >> l >> r;
        k-=1;
        if(l>=r){
            lefts[k].push_back(l-r);
            left_start++;
        }
        else{
            rights[k].push_back(r-l);
        }
        ans += min(l,r);
    }

    // DEBUGLL(lefts);
    // DEBUGLL(rights);

    priority_queue<ll> ql;
    for(int i = n-1 ; i > left_start ; i--){
        for(ll val : lefts[i]){
            ql.push(val);
        }
    }
    for(int i = left_start ; i >= 0 ; i--){
        for(ll val : lefts[i]){
            ql.push(val);
        }
        if(!ql.empty()){
            ans+=ql.top();
            ql.pop();
        }
    }

    priority_queue<ll> qr;
    for(int i = 1; i <= left_start ; i++){
        for(ll val : rights[i-1]){
            qr.push(val);
        }
    }
    for(int i = left_start+1 ; i < n ; i++){
        for(ll val : rights[i-1]){
            qr.push(val);
        }
        if(!qr.empty()){
            ans+=qr.top();
            qr.pop();
        }
    }
    cout << ans << endl;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin>>t;
    REP(i,t)solve();
    return 0;
}