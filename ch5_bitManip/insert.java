/*
* Inserts N into a 32 bit M given i and j starting and ending positions
*/

import java.util.*;

public class insert {

	public static void insBits(LinkedList<Integer> N, LinkedList<Integer> M, int i, int j) {

		for(int it = 0; it < i; it++) {

			// Adding i bits to the end of M
			M.add(0);	

		}

		for(int it_two = 0; it_two <= j; it_two++) {
			
			// Creating a bit mask and and-ing in the i -> j positions to effectively insert
			// M into the correct positions
			int check = M.get(it_two);

			N.set(it_two, 1 & check);	

		} 

	}
	
	public static void main(String[] args) {

		LinkedList<Integer> N = new LinkedList<Integer>();
		LinkedList<Integer> M = new LinkedList<Integer>();

		N.add(1);
		N.add(0);
		N.add(0);
		N.add(0);
		N.add(0);
		N.add(0);
		N.add(0);
		N.add(0);
		N.add(0);
		N.add(0);
		N.add(0);

		M.add(1);
		M.add(0);
		M.add(0);
		M.add(1);
		M.add(1);

		insBits(N,M,2,6);
		for(int i = 0; i < N.size(); i++) {
	
			System.out.print(N.get(i));		

		}
	}

}
