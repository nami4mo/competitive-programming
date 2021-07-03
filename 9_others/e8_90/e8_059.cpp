#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
namespace defines{
    typedef unsigned long long ll;
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



// ll n;
// const int MAX_BIT = 64;
// void solve2(vector<vector<ll>> &gl, vector<P> &ql){
//     int qn=ql.size();
//     vector<ll> dp(n);
//     REP(i,qn){
//         auto &[l,r]=ql[i];
//         dp[l]|=(1L<<i);
//     }
//     REP(i,n){
//         for(ll neib:gl[i]){
//             dp[neib]|=dp[i];
//         }
//     }
//     REP(i,qn){
//         auto &[l,r]=ql[i];
//         if(dp[r]&(1L<<i)) cout<<"Yes"<<endl;
//         else cout<<"No"<<endl;
//     } 
// }

ll n;
// const int MAXQ = 100001;
const int MAX_BIT = 64;
void solve2(vector<vector<ll>> &gl, vector<P> &ql){
    int qn=ql.size();
    vector<bitset<MAX_BIT>> dp(n);
    // vector<bitset<MAXQ>> dp(n); // MLE
    REP(i,qn){
        auto &[l,r]=ql[i];
        dp[l].set(i);
    }
    REP(i,n){
        for(ll neib:gl[i]){
            dp[neib]|=dp[i];
        }
    }
    REP(i,qn){
        auto &[l,r]=ql[i];
        if(dp[r].test(i)) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    } 
}

void solve(){
    ll m,q; cin >> n >> m >> q;
    vector<vector<ll>> gl(n);
    REP(i,m){
        ll x,y; cin>>x>>y; x--;y--;
        gl[x].push_back(y);
    }
    vector<P> ql;
    REP(i,q){
        ll l,r; cin >> l >> r;
        ql.push_back({l-1,r-1});
        if(i%64==63 || i==q-1){
            solve2(gl,ql);
            ql.clear();
        }
    }
}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}