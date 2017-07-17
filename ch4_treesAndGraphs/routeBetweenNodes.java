/*
* This algorithm determines if there is a route between two nodes in a graph
*/

import java.util.*;

// Creating an adjacency list-represented graph
class Graph {

  private int V;
  private LinkedList<Integer> adjList[];

  Graph(int v) {

    V = v;
    adjList = new LinkedList[v];
    for(int i = 0; i < v; ++i){

      adjList[i] = new LinkedList<Integer>();

    }

  }

  void addEdge(int v, int w) {

    adjList[v].add(w);

  }

  boolean BFSPathFinder(int source, int destination) {

    boolean visited[] = new boolean[V];

    LinkedList<Integer> queue = new LinkedList<Integer>();

    visited[source] = true;
    queue.add(source);

    while(queue.size() != 0) {

      source = queue.poll(); // poll from queue to get node we are currently a
      Iterator<Integer> i = adjList[source].listIterator();

      while(i.hasNext()){

        int n = i.next();
        if(!visited[n]){

          if(n == destination){
            return true;
          }

          visited[n] = true;
          queue.add(n);

        }

      }

    }
    return false;
  }

  public static void main(String[] args) {
    Graph g = new Graph(5);

    g.addEdge(1,2);
    g.addEdge(1,3);
    g.addEdge(2,3);
    g.addEdge(4,2);
    g.addEdge(4,5);
    g.addEdge(2,5);

    g.BFSPathFinder(1,5);
  }

}

// This a simple breadth first search implementation which will take O(V + E)
// since we implement with an adjacency list
