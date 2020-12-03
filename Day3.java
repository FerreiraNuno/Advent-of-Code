package com.company;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.text.CharacterIterator;
import java.text.StringCharacterIterator;

public class Day3 {
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> array = importStringArray();
        System.out.println(part2(array));

    }

    static int part1(ArrayList<ArrayList<Integer>> array) {
        int treeHitCounter = 0;
        for(int i = 0, j = 0; i <= array.size() - 1; i++, j += 3) {
            if (array.get(i).get(j) == 1){
                treeHitCounter ++;
            }
        }
        return treeHitCounter;
    }

    static long part2(ArrayList<ArrayList<Integer>> array) {
        //Right 1, down 1.
        long treeHitCounter1 = 0;
        for(int i = 0, j = 0; i <= array.size() - 1; i++, j++) {
            if (array.get(i).get(j) == 1){
                treeHitCounter1 ++;
            }
        }
        System.out.println(treeHitCounter1);
        //Right 3, down 1. (This is the slope you already checked.)
        long treeHitCounter2 = part1(array);
        //Right 5, down 1.
        System.out.println(treeHitCounter2);
        long treeHitCounter3 = 0;
        for(int i = 0, j = 0; i <= array.size() - 1; i++, j += 5) {
            if (array.get(i).get(j) == 1){
                treeHitCounter3 ++;
            }
        }
        System.out.println(treeHitCounter3);
        //Right 7, down 1.
        long treeHitCounter4 = 0;
        for(int i = 0, j = 0; i <= array.size() - 1; i++, j += 7) {
            if (array.get(i).get(j) == 1){
                treeHitCounter4 ++;
            }
        }
        System.out.println(treeHitCounter4);
        //Right 1, down 2.
        long treeHitCounter5 = 0;
        for(int i = 0, j = 0; i <= array.size() - 1; i+= 2, j++) {
            if (array.get(i).get(j) == 1){
                treeHitCounter5 ++;
            }
        }
        System.out.println(treeHitCounter5);

        //treeHitCounter1 * treeHitCounter2 * treeHitCounter3 * treeHitCounter4 * treeHitCounter5
        return treeHitCounter1 * treeHitCounter2 * treeHitCounter3 * treeHitCounter4 * treeHitCounter5;
    }

    static ArrayList<ArrayList<Integer>> importStringArray(){
        ArrayList<ArrayList<Integer>> array = new ArrayList<>();
        try {
            File file = new File("C:\\Users\\Paulo\\Google Drive\\Programmier Projekte\\IdeaProjects\\AdventofCode\\src\\com\\company\\input.txt");
            Scanner input = new Scanner(file);
            try {
                for (int i = 0; i < 323; i++) {
                    //create arrayList for one line of the map
                    ArrayList<Integer> oneLineArray = new ArrayList<>();
                    //declare two empty Strings and extend the line
                    String inputString = input.nextLine();
                    String repeatedString = "";
                    for (int j = 0; j < 150; j++){
                        repeatedString += inputString;
                    }
                    //convert symbols into 1s and 0s
                    CharacterIterator it = new StringCharacterIterator(repeatedString);
                    while (it.current() != CharacterIterator.DONE) {
                        if (it.current() == '#'){
                            oneLineArray.add(1);
                        }
                        else if (it.current() == '.'){
                            oneLineArray.add(0);
                        }
                        it.next();
                    }
                    array.add(oneLineArray);

                }
            } catch (NoSuchElementException e) {
                System.out.println("");
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return array;
    }


}