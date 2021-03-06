package step1;

import java.util.*;

public class Task {

	public static void main(String[] args) {
		int n = 50;
		int m = n * (n - 1) / 2;
		System.out.println(m);
	}
	
	public double solve(double x1, double y1, double r1, double x2, double y2, double r2) {
		/********* Begin *********/
		double kPi = Math.acos(-1.0);

		double d = Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
		double area1 = r1 * r1 * kPi;
		double area2 = r2 * r2 * kPi;
		if (d >= r1 + r2) {
			return area1 + area2;
		} else if (d <= r1 - r2 || d <= r2 - r1) {
			return Math.max(area1, area2);
		} else {
			double alpha = 2.0 * Math.acos((d * d + r1 * r1 - r2 * r2) / (2.0 * d * r1));
			double beta = 2.0 * Math.acos((d * d + r2 * r2 - r1 * r1) / (2.0 * d * r2));
			double area = area1 * (2.0 * kPi - alpha) / (2.0 * kPi) + area2 * (2.0 * kPi - beta) / (2.0 * kPi)
					+ 0.5 * r1 * r1 * Math.sin(alpha) + 0.5 * r2 * r2 * Math.sin(beta);
			return area;
			/********* End *********/
		}
	}
}
