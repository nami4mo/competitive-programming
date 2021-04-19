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

ll rec(int l, int r, vector<ll> &al, vector<vector<ll>> &dp){
    if(dp[l][r]!=INF) return dp[l][r];
    if(l==r) return dp[l][r]=0;

    ll v1,v2;
    v1=rec(l+1,r,al,dp)+(al[r]-al[l]);
    v2=rec(l,r-1,al,dp)+(al[r]-al[l]);
    dp[l][r]=min(v1,v2);
    return dp[l][r];
}


ll p2[62];
ll allps[22];

P solve(ll n, ll k){
    if(n==1) return {1,1};
    ll cp=n-2;
    ll cnt=1;
    ll csum=0;
    REP(i,62){
        if(cp<0)break;
        if(csum+p2[cp]>=k) break;
        cnt++;
        csum+=p2[cp];
        cp--;
    }
    return {cnt,csum};
}

void solve(){
    int t;cin>>t;
    REP(i,62){
        p2[i]=(1<<i);
    }
    allps[0]=1;
    REP(i,22){
        if(i==0)continue;
        allps[i]=allps[i-1]*i;
    }
    REP(aaaaa,t){
        ll n,k; cin>>n>>k;
        ll orig_n=n;
        if(n<21){
            // if(allps[n]<k){
            if((1<<(n-1))<k){
                cout<<-1<<endl;
                continue;
            }
        }
        ll rem=k;
        ll cmax=0;
        ll ccc=0;
        vector<ll> al;
        while(rem>1){
            auto [cnt,csum]=solve(n,rem);
            n-=cnt;
            rem-=csum;
            cmax+=cnt;
            REP(i,cnt){
                // al.push_back(cmax-i);
                ccc++;
                cout<<cmax-i<<" ";
            }
        }
        // ll cnt=orig_n-al.size();
        ll cnt=orig_n-ccc;
        cmax+=1;
        REP(i,cnt){
            // al.push_back(cmax+i);
            cout<<cmax+i<<" ";
        }
        // for(ll a:al){
        //     cout<<a<<" ";
        // }
        cout<<endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}