#include <bits/stdc++.h>
// #include <boost/functional/hash.hpp>
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
// const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;
// const int MOD = 998244353;
// using mint = modint1000000007;
// using mint = modint998244353;


using S = long long;
using F = long long;

const S INF = 8e18;

S op(S a, S b){ return std::min(a, b); }
S e(){ return INF; }
S mapping(F f, S x){ return f+x; }
F composition(F f, F g){ return f+g; }
F id(){ return 0; }

void solve(){
    ll n,q; cin >> n >> q;
    string s;
    vector<char> sl;
    vector<S> v(n,0);
    ll val=0;
    cin >>s;
    REP(i,n){
        if(s[i]=='(')val++;
        else val--;
        v[i]=val;
        sl.push_back(s[i]);
    }
    lazy_segtree<S, op, e, F, mapping, composition, id> seg(v);
    REP(i_,q){
        ll a,b,c; cin >> a >> b >> c;
        b--; c--;
        if(a==1){
            if(sl[b]=='(' && sl[c]==')'){
                sl[b]=')'; sl[c]='(';
                seg.apply(b,c,-2);
                // seg.apply(c,n,1);
            }
            else if(sl[b]==')' && sl[c]=='('){
                sl[b]='('; sl[c]=')';
                seg.apply(b,c,2);
                // seg.apply(c,n,-1);
            }
        }
        else{
            bool ok=false;
            ll lv=0;
            if(b>0) lv=seg.get(b-1);
            ll rv=seg.get(c);
            if(lv==rv && seg.prod(b,c+1)>=rv){
                cout<<"Yes"<<'\n';
            }
            else{
                cout<<"No"<<'\n';
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}