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

tuple<ll,ll,ll> get_type(ll x, ll y, ll dx, ll dy){ // y切片, xMOD, 移動回数?
    ll y_inter=dx*y-dy*x;
    ll x_mod=(x%dx+dx)%dx;
    ll move=(x-x_mod)/dx;
    return {y_inter, x_mod, move};
}

// https://sucrose.hatenablog.com/entry/2012/10/13/231449
// namespace std {
//     template <>
//     class hash<std::pair<ll, ll>> {
//     public:
//         size_t operator()(const std::pair<int, int>& x) const{
//             return hash<int>()(x.first) ^ hash<int>()(x.second);
//         }
//     };
// }

void solve(){
    string s; cin>>s;
    ll k; cin>>k;
    unordered_map<P, vector<ll>, boost::hash<P>> mp;
    ll cy=0, cx=0;
    unordered_set<P, boost::hash<P>> st;
    st.insert({0,0});
    for(char c:s){
        if(c=='R') cx++;
        if(c=='L') cx--;
        if(c=='U') cy++;
        if(c=='D') cy--;
        st.insert({cx,cy});
    }
    ll dx=cx, dy=cy;
    
    if(dy==0 && dx==0){
        cout<<st.size()<<endl;
        return;
    }

    if(dx==0){
        st.clear();
        cy=0, cx=0;
        st.insert({0,0});
        for(char c:s){
            if(c=='R') cy++;
            if(c=='L') cy--;
            if(c=='U') cx++;
            if(c=='D') cx--;
            st.insert({cx,cy}); // swap x-y
        }
        dx=cx, dy=cy;
    }

    for(auto &[x,y]:st){
        auto [y_inter, x_mod, move]=get_type(x,y,dx,dy);
        mp[{y_inter,x_mod}].push_back(move);
    }

    DEBUG(cx);
    DEBUG(cy);
    ll ans=0;
    for(auto &[key_, vec]:mp){
        // DEBUG(vec);
        sort(ALL(vec));
        REP(i, vec.size()-1){
            ll cnt=vec[i+1]-vec[i];
            cnt=min(k,cnt);
            ans+=cnt;
        }
        ans+=k;
    }
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}