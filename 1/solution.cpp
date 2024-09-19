#include <bits/stdc++.h>
#pragma GCC optimize("Ofast,O3,unroll-loops")
#pragma GCC target("avx,avx2")
#define file(s) if (fopen(s".in", "r")) freopen(s".in", "r", stdin), freopen(s".out", "w", stdout)
#define Respaabs1equal2xdoner cin.tie(nullptr)->sync_with_stdio(false);
#define pll pair < long long , long long >
#define all(x) x.begin() , x.end()
#define pii pair < int , int >
#define	pofik continue
#define int long long
#define pb push_back
#define ins insert
#define sz size()
#define F first
#define S second
const long long N = 1000 + 77 , inf = 1e18 + 77 , MOD = 1e9 + 7;
const long double eps = 1e-11;
using namespace std;
int binpow(int a , int b){
	if(!b) return 1;
	int val = binpow(a , b / 2);
	if(b % 2 == 0) return val * val % MOD;
	else return val * val * a % MOD;
}

int n , k , ans;

vector <int> g[N], dpr[N][N], answ;
int dp[N][N];
int rebro[N][N];

void dfs(int v , int p = 0){
	dp[v][1] = 0;
	for(int to : g[v]) if(to != p){
		dfs( to, v );
		for(int i = n; i >= 1; i--){
			if(dp[v][i] > 500) pofik;
			for(int j = 1; j <= n; j++){
				if(dp[v][i + j] > dp[to][j] + dp[v][i]){
					dp[v][i + j] = dp[to][j] + dp[v][i];
					dpr[v][i + j] = dpr[to][j];
					for(auto ab : dpr[v][i]) dpr[v][i + j].pb(ab);
				}
			}
			dp[v][i]++;
			dpr[v][i].pb(rebro[v][to]);
		}
	}
	if(dp[v][k] + (p != 0) < ans){
		ans = dp[v][k] + (p != 0);
		answ = dpr[v][k];
		if(p) answ.pb( rebro[p][v] );
	}

}

void solve(){
    cin >> n >> k;
    for(int i = 1; i < n; i++){
    	int v , u;
    	cin >> v >> u;
    	g[v].pb(u);
    	g[u].pb(v);
    	rebro[v][u] = rebro[u][v] = i;
    }
    for(int i = 0; i <= n; i++){
    	for(int j = 0; j <= k; j++){
    		dp[i][j] = inf;
    	}
    }
    ans = inf;
    dfs(1);
    cout << answ.sz << '\n';
    for(int it : answ){
    	cout << it << ' ';
    }
}

signed main(){
    Respaabs1equal2xdoner
	solve();
}

