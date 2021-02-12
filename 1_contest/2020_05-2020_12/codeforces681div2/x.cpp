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
    int n; cin >> n;
    vector<int> al(n); 
    vector<int> bl(n); 
    multiset<int> st;


    REP(i,n) {
        int a; cin >> a;
        al[i] = a;
        bl[i] = a;
        st.insert(a);
    }
    if(n==1){
        cout << "YES" << endl;
        return;
    }
    // cout << "here" << endl;
    int r_min = *st.begin();
    int curr_minus = 0;
    REP(i,n-1){
        al[i] -= curr_minus;
        st.erase(st.find(bl[i]));
        // cout << "here" << endl;
        r_min = *st.begin()-curr_minus;
        if(al[i] < al[i+1]-curr_minus){
            int need = (al[i+1]-curr_minus)-al[i];
            // DEBUG(al[i]);
            // DEBUG(al[i+1]);
            if(r_min < need){
                break;
            }
            curr_minus += need;
            // al[i+1] -= need;
        }
    }
    int cnt = 0;
    bool flag = false;
    bool ok = true;
    REP(i,n-1){
        if(al[i+1]-al[i] > 0) {
            if(flag){

            }
            else{
                flag = true;
            }
        }
        else if(flag && al[i+1]-al[i] < 0){
            // cout << "NO" << endl;
            ok = false;
            break;
        }
    }
    if(ok){
        cout << "YES" << endl;
        return;
    }

    // REP(i,n-1){
    //     if(al[i] < al[i+1] ){
    //         cnt++;
    //     }
    // }
    // if(cnt <= 1){
    //     cout << "YES" << endl;
    //     return;
    // }
    // else{
    //     cout << "NO" << endl;
    // }



    // REP(i,n) {
    //     int a; cin >> a;
    //     al[i] = a;
    //     bl[i] = a;
    //     st.insert(a);
    // }
    // cout << "here" << endl;
    // cout << "here" << endl;

    // reverse(ALL(al));
    reverse(ALL(bl));
    // cout << "here" << endl;

    multiset<int> st2;
    REP(i,n){
        al[i] = bl[i];
        st2.insert(bl[i]);
    }
    // cout << "here" << endl;

    r_min = *st2.begin();
    curr_minus = 0;
    REP(i,n-1){
        al[i] -= curr_minus;
        st2.erase(st2.find(bl[i]));
        // cout << "here" << endl;
        r_min = *st2.begin()-curr_minus;
        if(al[i] < al[i+1]-curr_minus){
            int need = (al[i+1]-curr_minus)-al[i];
            // DEBUG(al[i]);
            // DEBUG(al[i+1]);
            if(r_min < need){
                break;
            }
            curr_minus += need;
            // al[i+1] -= need;
        }
    }
    cnt = 0;
    flag = false;
    REP(i,n-1){
        if(al[i+1]-al[i] > 0) {
            if(flag){

            }
            else{
                flag = true;
            }
        }
        else if(flag && al[i+1]-al[i] < 0){
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll t; cin >> t;
    REP(i,t)solve();
    return 0;
}