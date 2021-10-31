#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;


#define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
#define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
#define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
#define ALL(x) x.begin(),x.end()
#define debug(x) cerr << #x << ": " << x << '\n'

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;

void SubFindCentroids(int v, int n, vector<vector<int>>& tree, vector<int>& sizeSubtree, vector<int>& centroids, int parent_of_v = -1) {
    sizeSubtree[v] = 1;
    bool isCentroid = true;
    for (auto ch : tree[v]) {
        if (ch == parent_of_v) continue;
        SubFindCentroids(ch, n, tree, sizeSubtree, centroids, v);
        if (sizeSubtree[ch] > n / 2) isCentroid = false;
        sizeSubtree[v] += sizeSubtree[ch];
    }
    if (n - sizeSubtree[v] >  n / 2) isCentroid = false;
    if (isCentroid) centroids.push_back(v);
}


void solve(){
    int n; cin >> n;
    vector<vector<int>> tree(n); 
    vector<int> sizeSubtree(n);
    vector<int> centroids;
    int fx,fy;
    REP(i,n-1){
        int x,y; cin >> x >> y;
        tree[x-1].push_back(y-1);
        tree[y-1].push_back(x-1);
        fx = x;
        fy = y;
    }
    centroids.clear();
    SubFindCentroids(0, n, tree, sizeSubtree, centroids, n);
    if( centroids.size() == 1 ){
        cout << fx << " " << fy << endl;
        cout << fx << " " << fy << endl;
    }
    else{
        int c1 = centroids[0];
        int c2 = centroids[1];
        int ans = -1;
        for( int v : tree[c2] ){
            if( v != c1){
                cout << c2+1 << " " << v+1 << endl;
                cout << c1+1 << " " << v+1 << endl;
                return;
            }
        }
    }
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    REP(i,t) {solve();}
}
