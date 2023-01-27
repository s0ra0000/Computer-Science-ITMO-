#include <string>
#include <vector>
#include <sstream>
#include <string>
using namespace std;
int main()
{
    vector<int> vev;

	int x;
	int n;

while(cin>>n)
	{
	cin>>x;
	vec.push_back(x);
		
		}
    bubbleSort(vec);
    printVector(vec);
    
}

void bubbleSort(vector<int> a)
{
    bool swapp = true;
    while(swapp)
    {
        swapp = false;
        for (int i = 0; i < a.size()-1; i++)
        {
            if (a[i]>a[i+1] )
            {
                a[i] += a[i+1];
                a[i+1] = a[i] - a[i+1];
                a[i] -=a[i+1];
                swapp = true;
            }
        }
    }
}

void printVector(vector<int> a)
{
    for (int i=0;  i <a.size();  i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
