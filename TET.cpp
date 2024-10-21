#include <iostream>
#include <cmath>
#include <iomanip>
#include <stdexcept>

using namespace std;

double equation(double x, int q, int r, int s, int t, int u) {
    return q * sin(x) + r * cos(x) + s * tan(x) + t * x * x + u;
}

double bisection(int q, int r, int s, int t, int u, double a, double b, double tol) {
    double fa = equation(a, q, r, s, t, u);
    double fb = equation(b, q, r, s, t, u);

    if (fa * fb > 0) {
        throw runtime_error("Không tìm thấy nghiệm trong đoạn [0, 1]");
    }

    double c;
    while ((b - a) >= tol) {
        c = (a + b) / 2;
        double fc = equation(c, q, r, s, t, u);

        if (fc == 0.0) {
            return c; // Nghiệm chính xác
        } else if (fa * fc < 0) {
            b = c;
            fb = fc;
        } else {
            a = c;
            fa = fc;
        }
    }
    return (a + b) / 2; // Trả về nghiệm gần đúng
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T;
    cin >> T;

    while (T--) {
        int q, r, s, t, u;
        cin >> q >> r >> s >> t >> u;

        try {
            double root = bisection(q, r, s, t, u, 0.0, 1.0, 1e-8);
            cout << fixed << setprecision(6) << root << endl;
        } catch (runtime_error &e) {
            cout << "No solution\n";
        }
    }

    return 0;
}