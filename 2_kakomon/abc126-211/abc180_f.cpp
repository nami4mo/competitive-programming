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
    template<> void dbg<modint1000000007>(string name, vector<modint1000000007> xl){cerr<<name<<": "; for(modint1000000007 x:xl){cerr<<x.val()<<" ";}cerr<<"\n";}
    template<class T> void dbg(string name, vector<vector<T>> xl){ cerr<<name<<": \n"; int ml=1;for(vector<T> row: xl){for(T x:row){stringstream sstm; sstm<<x; ml=max(ml,(int)sstm.str().size());}}; for(vector<T> row: xl){{for(T x:row) cerr<<std::right<<std::setw(ml+1)<<x;} cerr << '\n';}}
    template<> void dbg<modint1000000007>(string name, vector<vector<modint1000000007>> xl){ cerr<<name<<": \n"; int ml=1;for(vector<modint1000000007> row: xl){for(modint1000000007 x:row){stringstream sstm; sstm<<x.val(); ml=max(ml,(int)sstm.str().size());}}; for(vector<modint1000000007> row: xl){{for(modint1000000007 x:row) cerr<<std::right<<std::setw(ml+1)<<x.val();} cerr << '\n';}}

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
using mint = modint1000000007;
// using mint = modint998244353;

const int MAX = 310;
long long fac[MAX], finv[MAX], inv[MAX];
void com_init() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

long long com(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}

ll perm(int n, int r){
    if(n<r) return 1;
    if(n<0 || r<0) return 1;
    return fac[n] * (finv[n-r] % MOD) % MOD; 
}


void solve(){
    // cout<<"a"<<endl;
    ll n,m,l; cin >> n >> m >> l;
    com_init();

    vector<vector<mint>> gs_open(n+1, vector<mint>(n+1,0));
    vector<vector<mint>> gs_close(n+1, vector<mint>(n+1,0));
    FOR(sz,1,n+1){
        REP(cnt,n+1){
            if(sz*cnt>300)break;
            mint vo=1; 
            mint vc=1;
            ll rem=sz*cnt;
            REP(i,cnt){
                vo*=com(rem,sz);
                vo*=perm(sz,sz-2);
                vc*=com(rem,sz);
                vc*=perm(sz-1,sz-1);
                if(sz>=3) vc/=2;
                rem-=sz;
            }
            ll db=perm(cnt,cnt);
            vo/=db;
            vc/=db;
            gs_open[sz][cnt]=vo;
            gs_close[sz][cnt]=vc;
        }
    }
    // DEBUG(gs_close);
    ll open_group_cnt=n-m;

    // mint dp[301][301][301];
    vector< vector<vector<mint>> > dp(open_group_cnt+1, vector<vector<mint>>(l+1,vector<mint>(n+1,0) ) );
    // REP(i,301)REP(j,301)REP(k,301)dp[i][j][k]=0;
    dp[0][0][0]=1;
    REP(group,open_group_cnt+1){
        FOR(sz,1,l+1){
            FOR(j,group,n+1){
                REP(cnt,301){
                    if(j+sz*cnt>n) break;
                    if(group+cnt>open_group_cnt) break;
                    dp[group+cnt][sz][j+sz*cnt]+=dp[group][sz-1][j]*com(n-j,sz*cnt)*gs_open[sz][cnt];
                }
            }
        }
    }
    // DEBUG(dp[1]);

    mint ans=0;
    FOR(op_n, open_group_cnt, n+1){
        ll rem=n-op_n;
        // mint dpc[301][301];
        // REP(i,301)REP(j,301)dpc[i][j]=0;
        vector<vector<mint>> dpc(l+1, vector<mint>(rem+1,0));
        dpc[0][0]=1;
        dpc[1][0]=1;
        FOR(sz,2,l+1){
            REP(j,rem+1){
                REP(cnt,rem+1){
                    if(j+sz*cnt>rem)break;
                    dpc[sz][j+sz*cnt]+=dpc[sz-1][j]*com(rem-j,sz*cnt)*gs_close[sz][cnt];
                }
            }
        }
        // DEBUG(op_n);
        // DEBUG(dpc);
        mint dpc_not_l=dpc[l-1][rem];
        // mint dpc_l=dpc[rem][l]-dpc_not_l;
        mint dpc_l=dpc[l][rem];

        mint dp_not_l=dp[open_group_cnt][l-1][op_n];
        // mint dp_l=dp[open_group_cnt][l][op_n]-dp_not_l;
        mint dp_l=dp[open_group_cnt][l][op_n];

        ans+=(dpc_l*dp_l-dpc_not_l*dp_not_l);
    }
    cout<<ans.val()<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}