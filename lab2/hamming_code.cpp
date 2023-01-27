#include <bits/stdc++.h>
#include <string>
using namespace std;
int check_err(int s1, int s2, int s3){
	return s3*pow(2,2)+s2*pow(2,1)+s1*pow(2,0);
}
main(){
	string bits;
	int s1,s2,s3,s;
	bool err_bit, entered_bits;
	do {
		entered_bits = true;
		cout << "Enter 7 bits: ";
		getline(cin,bits);
		if(bits.length() == 7){
			for(int i=0; i<7; i++){
				if(bits[i] < 48 || bits[i] > 49){
					entered_bits = false;
				}
			}
		}
		else entered_bits = false;
		if(!entered_bits) cout << "Please enter correct bits!!!"<< endl;
	}
	while(!entered_bits);
	s1 = (bits[0]^bits[2]^bits[4]^bits[6]);
	s2 = (bits[1]^bits[2]^bits[5]^bits[6]);
	s3 = (bits[3]^bits[4]^bits[5]^bits[6]);
	s = check_err(s1,s2,s3);
	if(s!=0){
		cout << "Error in " << s << " bit" << endl;
		err_bit = !(bool)bits[s-1];
		bits[s-1] = (int)err_bit+48;
		cout << "Corrected information bits: " << bits[2] << bits[4] << bits[5] << bits[6];
	}
	else{
		cout << "No errors found!";
	}
	return 0; 
}

