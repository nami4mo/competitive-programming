#include <bits/stdc++.h>
#include <cmath>

using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
#define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
#define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
#define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
#define ALL(x) x.begin(),x.end()

#define DEBUG(x) cerr << #x << ": " << x << '\n'
#define DEBUGL(xl) dbgl_f(#xl,xl)
#define DEBUGLL(xll) dbgll_f(#xll,xll)
template<class T> void dbgl_f(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr << '\n';}
template<class T> void dbgll_f(string name, vector<vector<T>> xll){
    cerr<< name << ": " << '\n'; 
    for(vector<T> xl: xll){
        for(T x : xl) cerr << x << " ";
        cerr << '\n';
    }
}

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;


void solve(){
    int n,q; cin >> n >> q;
    vector<int> al(n); REP(i,n) cin >> al[i];
    sort(al.begin(), al.end());

    set<int> st;
    multiset<int> dst;
    int a;
    int prev_a = -1;
    // int max_diff = 0;
    // REP(i,n){
    for( int a : al ){
        // cin >> a;
        if(prev_a == -1){
            prev_a = a;
        }
        else{
            // max_diff = max(max_diff, a-prev_a);
            dst.insert(a-prev_a);
            // DEBUG(a-prev_a);
        }
        st.insert(a);
        prev_a = a;
    }
    
    vector<int> ansl;
    int smin = *st.begin();
    int smax = *st.rbegin();
    int dmax;
    if(dst.size() > 0){
        dmax = *dst.rbegin();
        int ans = smax-smin-dmax;
        cout << ans << endl;
    }
    else{
        cout << 0 << endl;
    }
    REP(i,q){
        int t,x; cin >> t >> x;
        if(t == 0){
            st.erase(x);
            if(dst.size() > 0){
                auto itr = st.lower_bound(x);
                if(itr != st.end() && itr != st.begin()){
                    int r = *itr;
                    int l = *(--itr);
                    dst.erase(dst.find(r-x));
                    dst.erase(dst.find(x-l));
                    dst.insert(r-l);
                }
                else if(itr == st.end()){
                    dst.erase( dst.find(x-*st.rbegin()));
                }
                else{
                    dst.erase(dst.find(*st.begin()-x));
                }
            }
        }
        else{
            // st.insert(x);
            if(st.size() > 1){
                auto itr = st.lower_bound(x);
                if(itr != st.end() && itr != st.begin()){
                    int r = *itr;
                    int l = *(--itr);
                    dst.insert(r-x);
                    dst.insert(x-l);
                    dst.erase(dst.find(r-l));
                }
                else if(itr == st.end()){
                    dst.insert(x-*st.rbegin());
                }
                else{
                    dst.insert(*st.begin()-x);
                }
            }
            else if(st.size() == 1){
                dst.insert(abs(*st.begin()-x));
            }
            st.insert(x);
        }
        DEBUG(x);
        if( st.size() <= 2){
            cout << 0 << endl;
        }
        else{
            smin = *st.begin();
            smax = *st.rbegin();
            dmax = *dst.rbegin();
            cout << smax-smin-dmax << endl;
            // cout << endl;
        }


        // cout << "---" << endl;

    }
    // for( int a : ansl) cout << a << endl;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}