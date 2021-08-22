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

    /* for debug print */
    #define DEBUG(x) cerr << #x << ": " << x << '\n'
    #define DEBUGP(x) cerr << #x << ": (" << x.first << ", " << x.second << ")" << '\n' 
    #define DEBUGL(xl) dbgl_f(#xl,xl)
    #define DEBUGLP(xl) dbglp_f(#xl,xl)
    #define DEBUGLL(xll) dbgll_f(#xll,xll)
    #define DEBUGM(xl) dbgm_f(#xl,xl)
    template<class T> void dbgl_f(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr << '\n';}
    template<class T, class U> void dbgm_f(string name, map<T,U> xl){cerr<<name<<": ";for(auto x: xl)cerr<<"("<<x.first<<": "<<x.second<<") ";cerr<<'\n';}
    template<class T> void dbglp_f(string name, vector<T> xl){cerr<<name<<": ";for(T x: xl)cerr<<"("<<x.first<<", "<< x.second<<") ";cerr<<'\n';}
    template<class T> void dbgll_f(string name, vector<vector<T>> xll){
        cerr<< name << ": " << '\n'; 
        for(vector<T> xl: xll){
            for(T x : xl) cerr << x << " ";
            cerr << '\n';
        }
    }
}
using namespace defines;

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;


void solve(){
    ll n; cin >> n;
    string s; cin >> s;
    ll q; cin >> q;
    vector<set<int>> c_sets(26);
    REP(i,n){
        int c = s[i]-'a';
        c_sets[c].insert(i);
    }
    REP(hoge,q){
        string com,a,b;
        cin >> com>>a>>b;
        if(com=="1"){
            int i = stoi(a)-1;
            int c = b[0]-'a';
            int prev_c = s[i]-'a';
            c_sets[prev_c].erase(i);
            c_sets[c].insert(i);
            s[i] = b[0];
        }
        else{
            int l = stoi(a)-1;
            int r = stoi(b)-1;
            int ans = 0;
            REP(v,26){
                // auto iter_r = c_sets[v].upper_bound(r);
                // int cnt_r = distance(c_sets[v].begin(), iter_r)+1;
                // auto iter_l = c_sets[v].upper_bound(l-1);
                // int cnt_l = distance(c_sets[v].begin(), iter_l)+1;
                // if(cnt_r > cnt_l){
                //     ans++;
                // }
                auto iter1 = c_sets[v].lower_bound(l);
                if( iter1 == c_sets[v].end() ){
                    continue;
                }
                int val1 = *iter1;
                if(val1 <= r){
                    ans++;
                }
            }
            cout<<ans<<endl;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}