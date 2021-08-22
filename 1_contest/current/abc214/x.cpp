#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
namespace defines{
    typedef long long ll;
    typedef pair<int,int> P;
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

int curr_ind=0;

int check_in(set<int> &st, unordered_map<int,int> &sm, set<int> &et, unordered_map<int,int> &em, int x){
    auto iter3 = st.upper_bound(x);
    if( iter3 == st.begin() ){
        // no such val
        return -1;
    }
    int s = *(--iter3);

    auto iter1 = et.lower_bound(x);
    if( iter1 == et.end() ){
        // no such val
        return -1;
    }
    int e = *iter1;
    if(sm[s]==em[e]){
        return e+1;
    }
    else{
        return -1;
    }
}

// int get(set<int> &st, set<int> &et, int x){

// }

unordered_map<int,int> m2s;
unordered_map<int,int> m2e;

void ins(set<int> &st, unordered_map<int,int> &sm, set<int> &et, unordered_map<int,int> &em, int x){
    auto ee=et.find(x-1);
    auto ss=st.find(x+1);
    if(ee!=et.end() && ss!=st.end()){
        int ind1=em[x-1];
        // int s1=sm[ind1];
        int s1=m2s[ind1];

        int ind2=sm[x+1];
        // int e2=em[ind2];
        int e2=m2e[ind2];

        et.erase(ee);
        st.erase(ss);
        em[e2]=ind1;
        m2e[ind1]=e2;
    }
    else if(ee!=et.end()){
        int ind=em[x-1];
        et.erase(ee);
        et.insert(x);
        em[x]=ind;
        m2e[ind]=x;
    }
    else if(ss!=st.end()){
        int ind=sm[x+1];
        st.erase(ss);
        st.insert(x);
        sm[x]=ind;
        m2s[ind]=x;
    }
    else{
        st.insert(x);
        et.insert(x);
        sm[x]=curr_ind;
        em[x]=curr_ind;
        m2s[curr_ind]=x;
        m2e[curr_ind]=x;
        curr_ind++;
    }

}

void solve(){
    int t; cin>>t;
    REP(loop,t){
        curr_ind=0;
        int n;cin>>n;
        vector<P> rls(n);
        set<int> st;
        unordered_map<int,int> sm;
        set<int> et;
        unordered_map<int,int> em;

        REP(i,n){
            int l,r; cin>>l>>r;
            rls[i]={r,l};
        }
        sort(ALL(rls));
        bool ok=true;
        // DEBUG(rls);
        for(auto &[r,l] : rls){
            int res=check_in(st,sm,et,em,l);
            if(res==-1){
                ins(st,sm,et,em,l);
            }
            else{
                if(res>r){
                    ok=false;
                    break;
                }
                ins(st,sm,et,em,res);
            }
            // DEBUG(st);DEBUG(et);DEBUG(sm);DEBUG(em);
        }
        if(ok) cout<<"Yes"<<'\n';
        else cout<<"No"<<'\n';
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}