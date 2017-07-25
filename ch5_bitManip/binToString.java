/*
* This converts a binary decimal between 0-1 to a string
*/

class binToString {

	static String binaryConverter(double num) {

		StringBuilder binString = new StringBuilder();

		while(num > 0) {

			if(binString.length() >= 32){

				return "ERROR";			

			}

			double r = num * 2;

			if(r >=1) {

				binString.append(1);
				num = r - 1;			

			}
			else {

				binString.append(0);
				num = r;

			}
		
		}
	
		return binString.toString();

	}

	public static void main(String[] args) {

		System.out.print(binaryConverter(0.72));

	}	

}
