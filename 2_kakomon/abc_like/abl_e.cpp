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

using mint = modint998244353;
vector<mint> keta_to_mint10(200001);
vector<mint> keta_to_mint(200001);

// lazy_segtree<S, op, e, F, mapping, composition, id> seg(int n);

struct S{
    mint v;
    int keta;
    S() : v(1), keta(1) {}
    S(mint v, int keta) : v(v), keta(keta) {}
};

S op(S a, S b){
    return S{a.v*keta_to_mint10[b.keta] + b.v, a.keta+b.keta};
}

S e(){ return S{0,0}; }

using F = int;
const F ID = 0;

S mapping(F f, S x){
    if( f == ID ) {
        return x;
    } else {
        return S{keta_to_mint[x.keta]*f, x.keta};
    }
}

F composition(F f, F g){
    if( f == ID ) return g;
    else return f;
}

F id(){return ID;}

void solve(){
    int n,q; cin >> n >> q;
    keta_to_mint10[0] = 1;
    FOR(i,1,200001){
        keta_to_mint10[i] = keta_to_mint10[i-1]*10;
        keta_to_mint[i] = (keta_to_mint10[i]-1)/9;
    }
    // DEBUG(keta_to_mint10[2].val());
    // DEBUG(keta_to_mint[2].val());

    vector<S> vals(n); 
    lazy_segtree<S, op, e, F, mapping, composition, id> seg(vals);
    // cout << seg.all_prod().v.val() << endl;
    REP(i,q){
        int l,r,d; cin >> l >> r >> d;
        seg.apply(l-1,r,d);
        cout << seg.all_prod().v.val() << endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}