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

ll w,h;
void rec(int cnt, ll a, ll b, vector<P> &res){
    if(cnt==w){
        res.push_back({a,b});
        return;
    }
    ll p2=(1<<(cnt-1));
    if(a>=p2 || b>=p2){
        rec(cnt+1,a,b,res);
    }
    else{
        rec(cnt+1,a+p2*2,b,res);
        rec(cnt+1,a,b+p2*2,res);
        rec(cnt+1,a,b,res);
    }
}

void solve(){
    cin>>h>>w;
    vector<string> cl(h);
    REP(i,h) cin>>cl[i];

    vector<P> pairs;
    rec(1,0,0,pairs);
    rec(1,0,1,pairs);
    rec(1,1,0,pairs);

    // vector<vector<ll>> dp(h, vector<ll>(1<<w,0));
    vector<ll> dp(1<<w,0);

    ll val=0;

    REP(i,1<<w){
        bool ok=true;
        ll last=-2;
        REP(j,w){
            if( (i&(1<<j))==0 ) continue;
            if(cl[0][j]=='#' || last+1==j){
                ok=false;break;
            } 
            last=j;
        }
        // if(ok) dp[0][i]=1;
        if(ok) dp[i]=1;
    }

    REP(y,h-1){
        vector<ll> new_dp(1<<w,0);
        ll val=0;
        REP(x,w){
            if(cl[y][x]=='.') val+=(1<<x);
        }
        for(auto &[u,v]:pairs){
            if( (val^u)&u )continue;
            // dp[y+1][v]+=dp[y][u];
            // dp[y+1][v]%=MOD;
            new_dp[v]+=dp[u];
            new_dp[v]%=MOD;
        }
        dp=new_dp;
    }

    val=0;
    REP(x,w){
        if(cl[h-1][x]=='.') val+=(1<<x);
    }
    ll ans=0;
    REP(i,1<<w){
        if( (val^i)&i ) continue;
        // ans+=dp[h-1][i];
        ans+=dp[i];
        ans%=MOD;
    }
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}