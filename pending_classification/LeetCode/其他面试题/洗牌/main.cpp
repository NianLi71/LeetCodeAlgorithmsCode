#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <deque>
#include <map>
using namespace std;


class Deck
{
private:
	int num;
	deque<int> deck;
	deque<int> pile_A;
	deque<int> pile_B;
public:
	Deck() { num = 52; init_deck(); pile_A = deck;  }
	Deck(int inputnum) : num(inputnum) { init_deck(); pile_A = deck; }

	void init_deck()
	{
		for (int i = 0; i < num; i++)
			deck.push_back(i);

		// cout << "initial deck: ";
		// for (int x : deck)
		// 	cout << x << " ";
		// cout << endl;
	}

	void cut_deck() // i = (i + num/2) % num;
	{
		int temp;
		for (int i = 0; i < num / 2; i++)
		{
			temp = pile_A.back();
			pile_A.pop_back();
			pile_A.push_front(temp);
		}

		/*cout << "Cut deck: " << endl;
		for (int x : pile_A)
			cout << x << " ";
		cout << endl;*/
	}

	void shuffle_once()
	{
		// Pull the top card from pile_A and put it on pile_B
		pile_B.push_back(pile_A.back());
		pile_A.pop_back();
		if (pile_A.empty()) return;
		/*-------------------------------------------------*/

		// Pull the top card from pile_A and put it on the bottom of pile_A
		pile_A.push_front(pile_A.back());
		pile_A.pop_back();
	}

	void shuffle_a_round()
	{
		cut_deck();

		while (!pile_A.empty())
			shuffle_once();


		// for (int x : pile_B)
		// 	cout << x << " ";
		// cout << endl;

		pile_A = pile_B;
		pile_B.clear();
	}

	map<int, int> FromTo()
	{
		map<int, int> fromto;
		vector<int> v1;
		v1.reserve(num);
		for (auto itr = pile_A.begin(); itr != pile_A.end(); ++itr)
			v1.emplace_back(*itr);

		shuffle_a_round();

		vector<int> v2;
		v2.reserve(num);
		for (auto itr = pile_A.begin(); itr != pile_A.end(); ++itr)
			v2.emplace_back(*itr);

		for (int i = 0; i < num; i++)
		{

		}


	}


	void smart1_shuffle_a_round()
	{
		// Cut first
		for (int i = 0; i < num; i++)
			pile_A[i] = (i + (num - 1) / 2 + 1) % num; // (num - 1 ) / 2 + 1 to accormmodate floor ;

		// Shuffle by index
		while (!pile_A.empty())
			shuffle_once();






		//int cap_ptr = num - 1;
		/*int j = 0;
		int hop = 2;
		int index = (num - 1) - hop * j;

		while (pile_B.size() < (deck.size() - 1) / 2 + 1)
		{
			pile_B.push_back(pile_A[index]);
			j++;
			index = (num - 1) - hop * j;
		}
*/



	}
	int resurrection()
	{
		shuffle_a_round();
		int times = 1;
		while (pile_A != deck)
		{
			shuffle_a_round();
			times++;
		}

		return times;
	}

};




int main()
{
	int n;
	cout << "Input number of cards: ";
	cin >> n ;
	Deck TX1(n);
	//TX1.cut_deck();
	//TX1.shuffle_a_round();
	//Deck TX2(n);
	//TX2.smart1_shuffle_a_round();

	//cout << "Shuffle deck: " << endl;
	cout << TX1.resurrection() << endl;


	getchar();
	getchar();
}
