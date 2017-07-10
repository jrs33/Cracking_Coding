/*
* This algorithm finds the k to last element in a singly linked list
*/

import java.util.*;
import java.awt.print.*;

public class kthToLast {

  public static Integer kthIterativeFind(LinkedList<Integer> ll, Integer k) {

    if(k >= ll.size() || k < 0){
      System.out.print("INVALID 'k': RETURNING ");
      return 0;
    }

    // First send a placeholder k indeces into the list. Then, when this placeholder
    // gets to the end, another index from the beginning of the list will be k places
    // from the end of the list
    Iterator<Integer> llIterOne = ll.iterator();

    for(;k > -1; k--){
      llIterOne.next();
    }

    Iterator<Integer> llIterTwo = ll.iterator();

    while(llIterOne.hasNext()){
      llIterOne.next();
      llIterTwo.next();
    }

    return llIterTwo.next();

  }

  public static void main(String[] args) {

    LinkedList<Integer> list = new LinkedList<Integer>();
    list.add(1);
    list.add(2);
    list.add(1);
    list.add(3);
    list.add(3);
    list.add(3);
    list.add(1);
    list.add(10);
    list.add(12);

    // Expect a 3
    System.out.print(kthIterativeFind(list, 3));
    System.out.print("\n");

    // Expect a 12
    System.out.print(kthIterativeFind(list, 0));
    System.out.print("\n");

  }
}

/*
* Overall, this algorithm takes O(n) space since, although we take an iterative
* approach, we still must go through each element of the list since the first
* iterator goes through each value to bring the second iterator length-k elements
* into the list. However, this iterative approach gives us a O(1) space complexity.
*/
