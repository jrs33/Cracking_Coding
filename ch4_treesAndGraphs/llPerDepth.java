/*
* This algorithm creates a linked list for each depth of the tree
*/
import java.util.*;

public class llPerDepth {

    class TreeNode {
      TreeNode Leftnode;
      TreeNode Rightnode;
      int data;
    }

    // Implement a Depth-First Search, with a pre-order traversal pattern
    void llLevelCreator(TreeNode node, ArrayList<LinkedList<TreeNode>> levelList, int level) {

      if(node == null) return; // bump off the call stack if we reached the last level

      LinkedList<TreeNode> list;
      if(levelList.size() == level) { // level we are visiting will at first match the list size

        list = new LinkedList<TreeNode>();
        levelList.add(list);

      }
      else
      {

        list = levelList.get(level);

      }

      // Pre-order pattern
      levelList.add(node); // Node
      llLevelCreator(node.LeftNode, levelList, level + 1); // Left
      llLevelCreator(node.RightNode, levelList, level + 1); // Right

    }

}

//
// Here we implement a recursive depth first search and visits each element which
// is O(n) and uses O(logN) recursive stack space
//
