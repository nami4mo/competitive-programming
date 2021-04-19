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

const ll MAX=2*100000;
void solve(){
    ll n,q; cin >> n >> q;
    multiset<ll> st;
    vector<multiset<ll>> k_sets(MAX);
    vector<ll> pos(n,-1);
    vector<ll> rate(n,-1);
    REP(i,n){
        ll a,b; cin >> a >> b;
        b--;
        pos[i]=b;
        rate[i]=a;
        k_sets[b].insert(a);
    }
    REP(i,MAX){
        if(!(k_sets[i].empty())){
            ll ma=*k_sets[i].rbegin();
            st.insert(ma);
        }
    }
    DEBUG(st);
    vector<ll> ansl;
    REP(i,q){
        DEBUG(i);
        ll c,d; cin >> c >> d;
        c--; d--;
        ll prev=pos[c];

        ll prev_ma=*k_sets[prev].rbegin();
        st.erase(st.find(prev_ma));
        k_sets[prev].erase(k_sets[prev].find(rate[c]));
        if(!k_sets[prev].empty()){
            ll new_ma=*k_sets[prev].rbegin();
            st.insert(new_ma);
        }


        if(!k_sets[d].empty()){
            ll prev_ma2=*k_sets[d].rbegin();
            st.erase(st.find(prev_ma2));
        }
        k_sets[d].insert(rate[c]);
        ll new_ma2=*k_sets[d].rbegin();
        st.insert(new_ma2);

        ll ans=*st.begin();
        ansl.push_back(ans);
        pos[c]=d;
    }
    for(ll a:ansl) cout<<a<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}