/*
* Checks if a Linked List is a Palindrome assuming we know the size of the list using
* an OOP approach
*/
import java.util.*;


  public class palinLinkedList {

    private Node head;

    private static class Node {

      private Character value;
      private Node next;

      // Node setter
      Node(char value) {
        this.value = value;
      }

    }

    public void appendList(Node node) {
      if(head == null){
        head = node;
      }
      else {
        Node temp = head;
        while (temp.next != null){
          temp = temp.next;
        }

        temp.next = node;
      }
    }

    public void reversal(Node currentNode) {
      Node previousNode=null;
      Node nextNode;
      while(currentNode!=null)
      {
       nextNode=currentNode.next;
       currentNode.next=previousNode;

       previousNode=currentNode;
       System.out.print(currentNode.value);
       currentNode=nextNode;
      }
    }

    public void printList(Node head) {
      Node temp = head;
      while (temp != null) {
       System.out.format("%c ", temp.value);
       temp = temp.next;
      }
      System.out.println();
    }

    public static void main(String[] args){

      palinLinkedList list = new palinLinkedList();

      Node head = new Node('a');

      list.appendList(new Node('a'));
      list.appendList(new Node('b'));
      list.appendList(new Node('a'));

      // Check equality of these two reversals
      list.printList(list.head);
      list.reversal(list.head);
      list.printList(list.head);

    }

  }
