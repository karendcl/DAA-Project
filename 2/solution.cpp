#include <bits/stdc++.h>
#define ll long long int
using namespace std;

const int N = 4002;
int dp[N][N], a[N][N], prefix[N][N], n , k;

int cost(int l,int r) {
    return (prefix[r][r] - prefix[l - 1][r] - prefix[r][l - 1] + prefix[l - 1][l - 1]) >> 1;
}

void compute(int group, int l, int r, int optL, int optR) {
    if(l > r) return;
    int mid = (l + r) >> 1;
    int opt = -1;
    for(int i = optL; i <= min(mid, optR + 1); i++) {
        int val = dp[i][group - 1] + cost(i + 1, mid);
        if(val <= dp[mid][group]) {
            dp[mid][group] = val;
            opt = i;
        }
    }
    compute(group, l, mid - 1, optL, opt);
    compute(group, mid + 1, r, opt, optR);
}

void solve()
{
   cin >> n >> k;
   for(int i = 1; i <= n; i++) {
    for(int j = 1; j <= n; j++) {
        getchar(), a[i][j] = getchar() - '0';
    }
   }
   for(int i = 1; i <= n; i++) {
    for(int j = 1; j <= n; j++) {
        prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + a[i][j];
    }
   }
   for(int i = 0; i <= n; i++) {
    for(int j = 0; j <= n; j++) {
        dp[i][j] = 1e9;
    }
   }
    for(int i = 1; i <= n; i++) {
     dp[i][1] = cost(1, i);
    }
    for(int g = 2; g <= k; g++) compute(g, 1, n, 1, n);


    cout << dp[n][k] << '\n';

}
int32_t main()
{
    solve();
    return 0;
}