// 
// Function to check if a binary tree is balanced
//

public class checkBalance {

	class TreeNode {
	
		TreeNode right;
		TreeNode left;
		int data;

	}

	// Check that the tree is balanced while we recurse down each subtree
	int isBalanced(TreeNode root, int lHeight, int rHeight) {
		int leftHeight;
		int rightHeight;
		
		if(root == null) return -1;

		if(root.left != null) {
			isBalanced(root.left, lHeight + 1, rHeight); 
		}
		else {
			int leftHeight = lHeight;
		}

		if(root.right != null) {
			isBalanced(root.right, lHeight, rHeight + 1);
		}
		else {
			int rightHeight = rHeight;
		}	

		
		if(abs(leftHeight-rightHeight) > 1) {
			System.out.println("ERROR: Imbalanced \n");
			return;
		}
		else {
			return 1;
		}
	
	}

}

//
// This algorithm keeps track of the height as we recursively traverse down the tree,
// and, individually goes down the right and left subtrees of each node to assure the
// heights of these individual subtrees is less or equal to 1, since this will determine 
// if the tree is balanced. This will run in O(N) time.
//
