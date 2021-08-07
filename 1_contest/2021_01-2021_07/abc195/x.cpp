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
    template<typename A, size_t N, typename T> void Fill(A (&array)[N], const T &val){std::fill( (T*)array, (T*)(array+N), val );}

    /* for debug */
    #define DEBUG(x) dbg(#x,x)
    template<class T> void dbg(string name, T x){cerr<<name<<": "<<x<<"\n";}
    template<> void dbg<P>(string name, P x){cerr<<name<<": ("<<x.first<<","<<x.second<<")\n";}
    template<class T> void dbg(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr<<'\n';}
    template<> void dbg<P>(string name, vector<P> xl){cerr<<name<<": "; for(P x:xl){cerr<<"("<<x.first<<","<<x.second<<"), ";}cerr<<"\n";}
    template<class T> void dbg(string name, vector<vector<T>> xl){ cerr<<name<<": \n"; int ml=1;for(vector<T> row: xl){for(T x:row){stringstream sstm; sstm<<x; ml=max(ml,(int)sstm.str().size());}}; for(vector<T> row: xl){{for(T x:row) cerr<<std::right<<std::setw(ml+1)<<x;} cerr << '\n';}}
    template<class T> void dbg(string name, set<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    template<class T> void dbg(string name, multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    template<class T> void dbg(string name, unordered_set<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    template<class T> void dbg(string name, unordered_multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x;cerr<<'\n';}
    template<class T, class U> void dbg(string name, map<T,U> xl){cerr<<name<<": \n"; for(auto &[k,v]:xl)cerr<<"  "<<k<<": "<<v<<'\n';}
    template<class T, class U> void dbg(string name, unordered_map<T,U> xl){cerr<<name<<": \n"; for(auto &[k,v]:xl)cerr<<"  "<<k<<": "<<v<<'\n';}
}
using namespace defines;

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;
// const int MOD = 998244353;
// using mint = modint1000000007;
// using mint = modint998244353;

vector<ll> primes(ll n){
    vector<bool> is_prime(n+1, true);
    is_prime[0] = false;
    is_prime[1] = false;
    for(ll i = 2 ; i*i <= n ; i++){
        if(is_prime[i]){
            for(ll j = i*2 ; j <= n ; j+=i){
                is_prime[j] = false;
            }
        }
    }
    vector<ll> ps;
    for(ll i = 2 ; i <= n ; i++){
        if(is_prime[i]) ps.push_back(i);
    }
    return ps;
}

void solve(){
    ll a,b; cin >> a >> b;
    vector<ll> ps=primes(72);
    unordered_set<ll> facs;
    FOR(i,a,b+1){
        for(ll p:ps){
            if(i%p==0) facs.insert(p);
        }
    }
    int c=0;
    unordered_map<ll,ll> d;
    for(ll f:facs){
        // DEBUG(f);
        d[f]=(1<<c);
        c++;
    }

    vector<vector<ll>> dp(b-a+2, vector<ll>(1<<(d.size()), 0));
    dp[0][0]=1;

    FOR(i,a,b+1){
        vector<ll> fs;
        for(ll p:ps){
            if(i%p==0) fs.push_back(p);
        }
        for(ll p:fs){
            ll pd=d[p];
            REP(j,1<<(d.size())){
                if(pd&j==0) dp[i+1-a][pd+j]+=dp[i-a][j];
            }
        }
        REP(j,1<<(d.size())){
            dp[i+1-a][j]+=dp[i-a][j];
        }
    }
    ll ans=0;
    for(ll v:dp[b-a+1]){
        ans+=v;
    }
    cout<<ans<<endl;
    DEBUG(facs);
    DEBUG(dp);
    DEBUG(ps);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}