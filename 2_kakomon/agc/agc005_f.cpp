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
    void NEWLINE(){cerr<<'\n';}
    void COMMA(){cerr<<", ";}
    #define DEBUG1(x) dbg(#x,x); NEWLINE();
    #define DEBUG2(x1,x2) dbg(#x1,x1); COMMA(); dbg(#x2,x2); NEWLINE();
    #define DEBUG3(x1,x2,x3) dbg(#x1,x1); COMMA(); dbg(#x2,x2); COMMA(); dbg(#x3,x3); NEWLINE();
    #define DEBUG4(x1,x2,x3,x4) dbg(#x1,x1); COMMA(); dbg(#x2,x2); COMMA(); dbg(#x3,x3); COMMA(); dbg(#x4,x4); NEWLINE();
    #define DEBUG_OVERLOAD(x1, x2, x3, x4, x5, ...) x5
    #define DEBUG(...) DEBUG_OVERLOAD(__VA_ARGS__, DEBUG4, DEBUG3, DEBUG2, DEBUG1)(__VA_ARGS__)
    template<class T> void dbg(string name, T x){cerr<<name<<": "<<x<<"";}
    template<> void dbg<P>(string name, P x){cerr<<name<<": ("<<x.first<<","<<x.second<<")";}
    template<class T> void dbg(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr<<"";}
    template<> void dbg<P>(string name, vector<P> xl){cerr<<name<<": "; for(P x:xl){cerr<<"("<<x.first<<","<<x.second<<"), ";}cerr<<"";}
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
// const int MOD = 1'000'000'007;
const ll MOD = 924844033;
// const int MOD = 998244353;
// using mint = modint1000000007;
// using mint = modint998244353;
using mint = modint;

ll dfs(ll node, ll pare, vector<vector<ll>> &gl, vector<ll> &cnts){
    ll res=1;
    for(int neib:gl[node]){
        if(neib==pare)continue;
        res+=dfs(neib,node,gl,cnts);
    }
    cnts[node]=res;
    return res;
}

void solve(){
    ll n;cin>>n;
    mint::set_mod(MOD);
    vector<vector<ll>> gl(n);   
    vector<ll> cnts(n,0);
    REP(i,n-1){
        ll u,v; cin >> u >> v;
        u--; v--;
        gl[u].push_back(v);
        gl[v].push_back(u);
    }
    dfs(0,-1,gl,cnts);
    // DEBUG(cnts);

    vector<mint> facs(n+1,1);
    vector<ll> tmp2(n+1,1);

    REP(i,n){
        facs[i+1]=facs[i]*(i+1);
        tmp2[i+1]=tmp2[i]*(i+1);

    }
    
    vector<mint> al(n+1,0);
    vector<mint> bl(n+1,0);
    REP(i,n){
        al[cnts[i]]++;
        al[n-cnts[i]]++;
    }

    vector<ll> aal(n+1,0);
    vector<ll> bbl(n+1,0);
    REP(i,n+1){
        // aal[n-i]=(al[i].val()*facs[i].val())%MOD;
        aal[n-i]=(al[i]*facs[i]).val();
        bl[i]=facs[i].inv();
        bbl[i]=bl[i].val();
    }

    aal[0]=0; aal[n]=0;

    vector<ll> cl = convolution<924844033>(aal, bbl);
    FOR(k,1,n+1){
        mint ans=((n-1)*facs[n])/(facs[n-k]*facs[k]);
        ans=ans-cl[n-k]/facs[k];
        ans+=(facs[n])/(facs[n-k]*facs[k]);
        cout<<ans.val()%MOD<<'\n';
    }
    
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}