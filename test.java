// Java
	/*
	Rearranged Palindrome
	Is there any way we can rearrange the letters of the string to form a palindrome?
	Reminder: A palindrome is a string that reads the same forwards as it does backwards.
	Palindrome examples: 'racecar', '10001'

	Notes-
	Ignore character case
	*/

import java.util.*;

public class test {

	public static void main(String args[]) {
		// Test Cases
		ArrayList<String> tests = new ArrayList<String>();
		tests.add("aab"); tests.add("racecar"); 
		tests.add("aabbbcccaa"); tests.add("palindromepalindrome");
		tests.add("woOw"); tests.add("dis  issi sid");
		// Test Case answers
		boolean[] answers = {true, true, false, true, true, true};
		// Validation
		int correct = 0;
		for (int i=0; i<tests.size(); i++) {
			boolean userAnswer = isPalindrome(tests.get(i));
			boolean actual = answers[i];
			System.out.print(tests.get(i) + ": " + userAnswer + " - ");
			if(userAnswer == actual){
				System.out.println("Correct");
				correct++;
			}else
				System.out.println("Incorrect");
		}

		System.out.println("Results: " + correct + "/" + tests.size());
	}

	public static boolean isPalindrome(String s) {
		HashMap<Character, Integer> map = new HashMap<Character,Integer>();

		for (int i=0; i<s.length(); i++)
			map.put(s.charAt(i), map.getOrDefault(s.charAt(i),0)+1);

		int odds = 0;
		for (char c : map.keySet())
			if (map.get(c) % 2 != 0)
				odds++;

		if (odds <= 1)
			return true;

		return false;
	}

}