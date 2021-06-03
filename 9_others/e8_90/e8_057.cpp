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


long long pow_mod(long long x, long long n, long long mod){
    if(n == 0) { return 1; }
    ll xx = x;
    ll nn = n;
    ll k = 1;
    while(nn > 1){
        if(nn%2 != 0){ k *= xx; }
        xx *= xx;
        nn = nn/2;
        xx%=mod;
    }
    return k * xx;
}


// for XOR max
const int MAX_BIT = 300;
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

void solve(){
    ll n,m; cin >> n >> m;
    vector<bitset<MAX_BIT>> mat;
    REP(i,n){
        int t;cin>>t;
        bitset<MAX_BIT> bt(0);
        REP(j,t){
            int a; cin>>a; a--;
            bt.set(a);
        }
        mat.push_back(bt);
    }
    bitset<MAX_BIT> wanted(0);
    REP(i,m){
        int a; cin>>a;
        if(a==1) wanted.set(i);
    } 

    ll rank = gauss_jordan(mat);
    int cbit=0;
    bitset<MAX_BIT> currbit(0);
    REP(i,n){
        // DEBUG(mat[i]);
        int lsb=-1;
        for(int bit=MAX_BIT-1 ; bit>=0 ; bit--){
            if(mat[i].test(bit)){
                lsb=bit; break;
            }
        }
        if(lsb==-1)break;
        if(wanted.test(lsb)){
            currbit^=mat[i];
        }
    }
    if(currbit==wanted){
        cout<<pow_mod(2,n-rank,998244353)<<endl;
    }
    else{
        cout<<0<<endl;
    }
}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}