/*
*
* Removing duplicates from an unsorted linked list using
* temporary buffers
*
*/

import java.util.*;
import java.awt.print.*;

public class remDups {

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

      int hashTable[] = new int[Collections.max(list)];

      for(int i = 0; i < list.size(); i++) {
        hashTable[list.get(i) - 1] = hashTable[list.get(i) - 1] + 1;
      }

      LinkedList<Integer> newList = new LinkedList<Integer>();
      for(int i = 0; i < hashTable.length; i++) {
        if(hashTable[i] == 1) {
          newList.add(i+1);
        }
      }

      for(int i = 0; i < newList.size(); i++){
        System.out.print(newList.get(i));
        System.out.print(" ");
      }

    }

}

/*
* This algorithm to remove duplicates runs in O(n) time where n is maximum value
* in the linked list
*/
