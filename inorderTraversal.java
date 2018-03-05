/* Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    // Left, Middle, Right
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inorderArray = new ArrayList<>();
        inorderArray = iterativeInOrder(root);
        return inorderArray;
    }
    
    public void tailRecursiveTraverse(TreeNode root, List<Integer> inorderArray) {
        if(root != null) {
            if(root.left != null) {
                tailRecursiveTraverse(root.left, inorderArray);
            }
            inorderArray.add(root.val);
            if(root.right != null) {
                tailRecursiveTraverse(root.right, inorderArray);
            }
        }
    }
    
    public List<Integer> iterativeInOrder(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> recursiveStackEmulator = new Stack<>();
        TreeNode current = root;
        while(!recursiveStackEmulator.empty() || current != null) {
            while(current != null) {
                recursiveStackEmulator.push(current);
                current = current.left;
            }
            current = recursiveStackEmulator.pop();
            result.add(current.val);
            current = current.right;
        }
        return result;
    }
}
