#include <iostream>
#include <fstream>
using namespace std;

int lastKLines(char* filename, int K) {

	// Create a stream to read data into the program from the file
	ifstream file(filename);
	
	string lineArray[K];
	int index = 0;

	// Creating a circular array by updating the oldest item using the index tracker
	while(file.peek() != EOF){
		// getline extracts line in file and stores it in lineArray[index]
		getline(file, lineArray[index % K]);
		index++;
	}
	
	int startIndex = 0;
	int minimum = index;
	if(index > K) {
		startIndex = index % K;
		minimum = K;
	}

	for(int i = 0; i < minimum; i++){
		cout<<lineArray[(startIndex + i) % K]<<endl;
	}

}

// Utilizes a circular array to save memory
