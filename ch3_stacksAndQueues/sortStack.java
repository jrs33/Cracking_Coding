/*
* Sorting a stack with minimum elements on top using only one additional temp stack
*/

import java.util.*;

public class sortStack {

  public static void sorter(Stack<Integer> s) {
    Stack<Integer> sortedStack = new Stack<Integer>();

    while(!s.isEmpty()){
      int tmp = s.pop();

      // If the sorted stack is not empty, push elements greater than tmp on to the old stack to
      // find the proper storage place in the sorted stack
      while(!sortedStack.isEmpty() && sortedStack.peek() > tmp) {
        s.push(sortedStack.pop());
      }
      sortedStack.push(tmp);
    }

    // Copy back to get the correct ordering, since larger numbers will be at the top
    // of the sorted stack
    while(!sortedStack.isEmpty()){
      System.out.print(sortedStack.peek());
      System.out.print("\n");
      s.push(sortedStack.pop());
    }

  }

  public static void main(String[] args) {

    Stack<Integer> oldStack = new Stack<Integer>();
    oldStack.push(8);
    oldStack.push(2);
    oldStack.push(82);
    oldStack.push(18);
    sorter(oldStack);

  }

}


/*
* This algorithm runs in O(N^2) time, where N is the number of elements in the stack
*/
