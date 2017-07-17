/*
* Build a minimum heught tree given an increasing order sorted array
*/

public class minimalTree {

  class TreeNode {
    TreeNode LeftNode;
    TreeNode RightNode;
    int data;

    public TreeNode(int newData){
      data = newData;
      LeftNode = null;
      RightNode = null;
    }
  }

  TreeNode minBST(int array[], int startIndex, int endIndex) {
    if(endIndex < startIndex) {
      return null;
    }

    int mid = (startIndex + endIndex)/2;

    TreeNode n = new TreeNode(mid);

    // Break less-than-mid values into a left subtree and
    // more-than-mid values into a right subtree and recursively call on these
    // subarrays
    n.LeftNode = minBST(array, startIndex, mid-1);
    n.RightNode = minBST(array, mid+1, endIndex);

    System.out.print(n.data+"\n");
    return n;
  }

  public static void main(String[] args) {
    int array[] = new int[5];
    array[0] = 10;
    array[1] = 12;
    array[2] = 14;
    array[3] = 15;
    array[4] = 33;

    minimalTree m = new minimalTree();

    m.minBST(array, 0, array.length-1);
  }

}
