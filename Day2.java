package com.company;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Day2 {
    public static void main(String[] args) {
        ArrayList<String> array = importStringArray();
        System.out.println(part1(array));
        System.out.println(part2(array));
    }


    static ArrayList<String> importStringArray(){
        ArrayList<String> array = new ArrayList<>();
        try {
            File file = new File("C:\\Users\\Paulo\\Google Drive\\Programmier Projekte\\IdeaProjects\\AdventofCode\\src\\com\\company\\input.txt");
            Scanner input = new Scanner(file);
            try {
                for (int i = 0; i < 1000; i++) {
                    array.add(input.nextLine());
                }
            } catch (NoSuchElementException e) {
                System.out.println("");
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return array;
    }

    static int part1(ArrayList<String> array) {
        int correctPasswords = 0;
        for (String item : array) {
            //returns max-min letter count
            int index_of_dash = item.indexOf("-");
            int min_count = Integer.parseInt(item.substring(0, index_of_dash));
            int index_of_first_space = item.indexOf(" ");
            int max_count = Integer.parseInt(item.substring(index_of_dash + 1, index_of_first_space));

            //returns letter to scan for
            int index_of_char = item.indexOf(":") - 1;
            String test_char = item.substring(index_of_char, index_of_char + 1);

            //returns password
            int index_of_password = item.lastIndexOf(" ") + 1;
            String password = item.substring(index_of_password);

            //counts occurences of char appearance
            String[] string_array = password.split("");
            int occurence_count = 0;
            for (String letter : string_array){
                if (letter.equals(test_char)) {
                    occurence_count += 1;
                }
            }


            if (min_count <= occurence_count && occurence_count <= max_count){
                correctPasswords += 1;
            }
        }
        return correctPasswords;
    }

    static int part2(ArrayList<String> array) {
        int correctPasswords = 0;
        for (String item : array) {
            //returns indexes of check letters
            int index_of_dash = item.indexOf("-");
            int first_index = Integer.parseInt(item.substring(0, index_of_dash));
            int index_of_first_space = item.indexOf(" ");
            int second_index = Integer.parseInt(item.substring(index_of_dash + 1, index_of_first_space));

            //returns letter to scan for
            int index_of_char = item.indexOf(":") - 1;
            String test_char = item.substring(index_of_char, index_of_char + 1);

            //returns password
            int index_of_password = item.lastIndexOf(" ") + 1;
            String password = item.substring(index_of_password);

            //counts occurences of char appearance in item
            String[] string_array = password.split("");
            int occurence_count = 0;
            if (string_array[first_index - 1].equals(test_char)) {
                occurence_count += 1;
            }
            if (string_array[second_index - 1].equals(test_char)) {
                occurence_count += 1;
            }

            // counts correct password appearances
            if (occurence_count == 1){
                correctPasswords += 1;
            }
        }
        return correctPasswords;

    }
}

