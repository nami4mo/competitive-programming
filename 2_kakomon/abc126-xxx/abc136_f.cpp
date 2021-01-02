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
using mint = modint998244353;

ll op(ll a, ll b){return a+b;}
ll e(){return 0;}

void solve(){
    ll n; cin >> n;
    vector<P> xyl;
    vector<ll> xl;
    vector<ll> yl;
    REP(i,n){
        ll x,y; cin >> x >> y;
        xyl.push_back(P(x,y));
        xl.push_back(x);
        yl.push_back(y);
    }
    sort(ALL(xyl));
    sort(ALL(xl));
    sort(ALL(yl));
    // compress only y
    unordered_map<ll,ll> ycomp;
    REP(i,n){
        ycomp[yl[i]]=i;
    }

    segtree<ll, op, e> segl(n);
    vector<ll> tmp(n,1);
    segtree<ll, op, e> segr(tmp);
    // segr.set(ycomp[xyl[0].second],0);
    // ll hold_y = ycomp[xyl[0].second];

    ll hold_y = -1;

    mint ans=0;
    REP(i,n){
        auto [x,y] = xyl[i];
        ll yy = ycomp[y];

        if(hold_y>=0){
            segl.set(hold_y,1);
        }
        segr.set(yy,0);
        hold_y=yy;

        ll left_up = segl.prod(yy,n);
        ll left_bottom = i-left_up;
        ll right_up = segr.prod(yy,n);
        ll right_bottom = n-1-i-right_up;
        // DEBUG(i);
        // DEBUG(x);
        // DEBUG(yy);
        // DEBUG(left_up);
        // DEBUG(left_bottom);
        // DEBUG(right_up);
        // DEBUG(right_bottom);

        ans+=(mint(2).pow(n)-1);
        ans-=(mint(2).pow(left_up+left_bottom)-1);
        ans-=(mint(2).pow(right_up+right_bottom)-1);
        ans-=(mint(2).pow(left_up+right_up)-1);
        ans-=(mint(2).pow(left_bottom+right_bottom)-1);
        ans+=(mint(2).pow(left_up)-1);
        ans+=(mint(2).pow(left_bottom)-1);
        ans+=(mint(2).pow(right_up)-1);
        ans+=(mint(2).pow(right_bottom)-1);
        // DEBUG(ans.val());
    }
    cout<<ans.val()<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}