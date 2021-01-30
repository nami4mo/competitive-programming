#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
namespace defines{
    typedef unsigned long long ll;
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




// for XOR max
const int MAX_BIT = 60;
int gauss_jordan(vector<bitset<MAX_BIT>> &mat){
    int rank=0;
    for(int i=MAX_BIT-1 ; i>=0 ; i--){
        int found_row=-1;
        for(int j=rank ; j<mat.size() ; j++){
            if(mat[j][i]){
                found_row = j;
                break;
            }
        }
        if(found_row==-1) continue;
        swap(mat[rank], mat[found_row]);
        for(int j=0 ; j<mat.size() ; j++){
            if(j==rank) continue;
            if(mat[j][i]) mat[j]^=mat[rank];
        }
        rank++;
    }
    return rank;
}

void solve(ll n, vector<ll> al){
    vector<bitset<MAX_BIT>> mat;
    ll bitcnt=0;
    REP(i,n){
        bitcnt=bitcnt^al[i];
    }
    DEBUG(bitcnt);
    bitset<MAX_BIT> bitcnts(bitcnt);
    vector<ll> onebits;
    vector<ll> twobits;
    ll ans=0;
    REP(i,MAX_BIT){
        if(bitcnts[i]) ans+=(1ll<<i);
        // if(bitcnts[i]) ans+=pow(2,i); // NG!
        else twobits.push_back(i);
    }
    DEBUG(twobits);

    vector<bitset<MAX_BIT>> bital;
    REP(i,n){
        bitset<MAX_BIT> newbita(0);
        bitset<MAX_BIT> bita(al[i]);
        for(int j=0 ; j<twobits.size() ; j++){
            newbita[j]=bita[twobits[j]];
        }
        bital.push_back(newbita);
    } 
    gauss_jordan(bital);
    bitset<MAX_BIT> ansbit(0);
    REP(i,n){
        ansbit=ansbit^bital[i];
    }
    ll ans1=0;
    REP(i,MAX_BIT){
        if(ansbit[i]){
            ans1+=(1ll<<twobits[i])*2;
        }
    }
    cout<<ans+ans1<<endl;
}

void solve2(ll n, vector<ll> al){
    ll ans=0;
    for(int i=1;i<(1<<n)-1;i++){
        ll a=0;
        ll b=0;
        REP(j,n){
            if((i>>j)%2==0) a^=al[j];
            else b^=al[j];
        }
        ans=max(ans,a+b);
    }
    cout<<ans<<endl;
}

int main(){
    ll n; cin >> n;
    vector<ll> al(n); REP(i,n) cin >> al[i];
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve(n,al);
    return 0;
}