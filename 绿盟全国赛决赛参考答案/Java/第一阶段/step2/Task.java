package step2;

public class Task {
    
	public int virusArea(int n,int m,char[][] area){
		/********* Begin *********/
		if (area == null || area.length == 0 
				|| area[0].length == 0)
			return 0;

		int count = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)

				if (area[i][j] == 'o') {
					count++;
					change(area, i, j, n, m);
				}
		return count++;
		/********* End *********/	
	}

	private void change(char[][] area, 
			int i, int j, int n, int m) {
		if (i < 0 || i >= n || j < 0 || j >= m)
			return;
		if (area[i][j] != 'o')
			return;

		area[i][j] = '0';
		change(area, i + 1, j, n, m);
		change(area, i - 1, j, n, m);
		change(area, i, j + 1, n, m);
		change(area, i, j - 1, n, m);
 
	}
}

