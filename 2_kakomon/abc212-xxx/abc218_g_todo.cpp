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

// const ll MAX=100010;
const ll MAX=10;
vector<ll> i2a;
unordered_map<ll,ll> a2i;
fenwick_tree<ll> bit(MAX);
vector<ll> vals;
vector<ll> dists;
vector<ll> al;


ll bisect(ll target){
    ll ok = 0;
    ll ng = MAX-1;
    while(abs(ok-ng)>1){
        ll mid = (ok+ng)/2;
        ll v=bit.sum(0,mid+1);
        // DEBUG(mid);
        // DEBUG(v);
        if(v<=target){
            ok=mid;
        }
        else{
            ng=mid;
        }
    }
    return ok;
}

ll get_med(ll dist){
    if(dist%2==0){ // 奇数個
        ll target=dist/2+1;
        ll ind=bisect(target);
        return i2a[ind];
    }
    else{
        ll target1=dist/2+1;
        ll ind1=bisect(target1);
        ll target2=dist/2+2;
        ll ind2=bisect(target2);
        DEBUG(target1);
        DEBUG(target2);
        DEBUG(ind1);
        DEBUG(ind2);
        DEBUG(i2a[ind1]);
        DEBUG(i2a[ind2]);
        return (i2a[ind1]+i2a[ind2])/2;
    }
}

void dfs(int node, int pare, ll dist, vector<vector<ll>> &gl){
    int v=a2i[al[node]];
    dists[node]=dist;
    bit.add(v,1);
    if(gl[node].size()==1 && node!=0){
        DEBUG(node);
        ll med=get_med(dist);
        vals[node]=med;
    }
    else{
        for(ll neib:gl[node]){
            if(neib==pare)continue;
            dfs(neib,node,dist+1,gl);
        }
    }
    DEBUG(v);
    bit.add(v,-1);
}

void solve(){
    ll n; cin>>n;
    al=vector<ll>(n);
    vals=vector<ll>(n,-1);
    dists=vector<ll>(n,0);
    set<ll> st;
    REP(i,n) {
        cin>>al[i];
        st.insert(al[i]);
    }
    i2a = vector<ll>(st.begin(), st.end());
    REP(i, i2a.size()){
        a2i[i2a[i]]=i;
    }
    
    vector<vector<ll>> gl(n);
    REP(i,n-1){
        ll u,v; cin >> u >> v;
        u--; v--;
        gl[u].push_back(v);
        gl[v].push_back(u);
    }
    dfs(0,-1,0,gl);
    DEBUG(vals);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}