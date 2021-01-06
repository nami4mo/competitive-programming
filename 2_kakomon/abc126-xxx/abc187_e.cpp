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
    template<class T> void dbg(string name, multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x;cerr<<'\n';}
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

vector<int> eulers;
vector<vector<int>> gl(200100);

// make euler tour
void dfs(int node, int pare){
    for(int neib : gl[node]){
        if(neib!=pare){
            eulers.push_back(neib);
            dfs(neib,node);
        }
    }
    eulers.push_back(node);
}

ll op(ll a, ll b){ return max(a,b);}
ll e(){ return 0;}
ll mapping(ll f, ll x){ return f+x;}
ll composition(ll f, ll g){ return f+g;}
ll id() {return 0;}

void solve(){
    ll n; cin >> n;
    vector<P> el;
    REP(i,n-1){
        ll a,b; cin >> a >> b;
        a-=1;b-=1;
        gl[a].push_back(b);
        gl[b].push_back(a);
        el.push_back(P(a,b));
    }
    eulers.push_back(0);
    dfs(0,-1);
    vector<int> ins(n,-1);
    vector<int> outs(n,-1);
    REP(i,2*n){
        int node=eulers[i];
        if(ins[node]==-1)ins[node]=i;
        else outs[node]=i;
    }
    lazy_segtree<ll, op, e, ll, mapping, composition, id> seg(2*n);
    int q;cin>>q;
    REP(i,q){
        ll t,e,x; cin >> t >> e >> x;
        auto [a,b]=el[e-1];
        if(t==2) swap(a,b);
        int a_in=ins[a];
        int a_out=outs[a];
        int b_in=ins[b];
        int b_out=outs[b];
        if(a_in>b_in){
            seg.apply(a_in,a_out,x);
        }
        else{
            seg.apply(0,2*n,x);
            seg.apply(b_in,b_out,(-1)*x);
        }
    }
    REP(i,n){
        cout<<seg.prod(ins[i],ins[i]+1)<<'\n';
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}