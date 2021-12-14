#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include <iomanip>
#include<cmath>
#include<queue>
#include<math.h>

using namespace std;
typedef long long ll;

#define MOD 1000000007

double pi=3.1415926533589793238;

int main(){
	int N,M;
	cin >> N >> M;
    vector<vector<int>> G(N+1);
    int a,b;
    for(int i=0;i<M;i++){
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    vector<int> C(3);
    bool t=true;
    for(int i=1;i<=N;i++){
        if(G[i].size()>2){
            t=false;
            break;
        }
        C[G[i].size()]++;
    }
    if(!t){
        cout << "No" << endl;
        return 0;
    }
    if(C[1]+C[2]<=N && C[2]<=N-2){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
/*
	vector<long long> A(N);
	for(int i=0;i<N;i++){
		cin >> A[i];
	}
    */
  //cout << round(N) << endl;
  //cout << fixed << setprecision(10);
  //cout << ans << endl;
}