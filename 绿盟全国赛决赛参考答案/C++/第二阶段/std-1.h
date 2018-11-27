#ifndef SOLVER_H_
#define SOLVER_H_

#include <bits/stdc++.h>
using namespace std;

class Solver {
 public:
  double solve(double x1, double y1, double r1,
               double x2, double y2, double r2) {
    /*********begin*********/
    static const double kPi = acos(-1.0);

    double d = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
    double area1 = r1 * r1 * kPi;
    double area2 = r2 * r2 * kPi;
    if (d >= r1 + r2) {
      return area1 + area2;
    } else if (d <= r1 - r2 || d <= r2 - r1) {
      return max(area1, area2);
    } else {
      double alpha = 2.0 * acos((d * d + r1 * r1 - r2 * r2) / (2.0 * d * r1));
      double beta = 2.0 * acos((d * d + r2 * r2 - r1 * r1) / (2.0 * d * r2));
      double area = area1 * (2.0 * kPi - alpha) / (2.0 * kPi) + 
                    area2 * (2.0 * kPi - beta) / (2.0 * kPi) + 
                    0.5 * r1 * r1 * sin(alpha) + 
                    0.5 * r2 * r2 * sin(beta);
      return area;
    }
    /*********end*********/
  }
};

#endif
