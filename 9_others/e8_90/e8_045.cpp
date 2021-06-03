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


void solve(){
    ll n,K; cin >> n >> K;
    vector<P> xyl;
    REP(i,n){
        ll x,y; cin >> x >> y;
        xyl.push_back({x,y});
    }
    vector<ll> max_ds(1<<n,0);
    REP(i,1<<n){
        vector<P> cxyl;
        REP(j,n){
            if(i&(1<<j)) cxyl.push_back(xyl[j]);
        }
        int l=cxyl.size();
        ll dmax=0;
        REP(j,l){
            auto [x,y]=cxyl[j];
            FOR(k,j+1,l){
                auto [x1,y1]=cxyl[k];
                ll d=(x1-x)*(x1-x)+(y1-y)*(y1-y);
                dmax=max(dmax,d);
            }
        }
        max_ds[i]=dmax;
    }

    ll ok=pow(10,18)+1, ng=0;
    while(abs(ok-ng)>1){
        ll mid=(ok+ng)/2;
        vector<int> dp(1<<n, 20);
        dp[0]=1;
        if(max_ds[(1<<n)-1]<=mid){
            ok=mid;
            continue;
        }

        REP(i,1<<n){
            if(max_ds[i]<=mid) {
                dp[i]=1;
                continue;
            }
            int val=20;
            for(ll bits=(i-1)&i ; bits>i/2 ; bits=(bits-1)&i){
                ll comp=bits^i;
                val=min(val,dp[bits]+dp[comp]);
            }
            dp[i]=val;
        }
        if(dp[(1<<n)-1]<=K) ok=mid;
        else ng=mid;
    }
    cout<<ok<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}