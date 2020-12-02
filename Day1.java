package com.company;

import java.io.FileNotFoundException;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;


public class Day1 {
    public static void main(String[] args) {
        ArrayList<Integer> array = new ArrayList<>();
        try {
            File file = new File("C:\\Users\\Paulo\\Google Drive\\Programmier Projekte\\VSC Projekte\\Advent of Code\\Day1Part1Input.txt");
            Scanner input = new Scanner(file);
            try {
                for (int i = 0; i < 600; i++) {
                    array.add(input.nextInt());
                }
            }
            catch(NoSuchElementException e) {
                System.out.println("");
            }
        }
        catch(FileNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println("part1: " + part1(array));

        System.out.println("part2: " + part2(array));
    }

    static int part2(ArrayList<Integer> array){
        for (int i : array) {
            for (int j : array) {
                for (int k : array) {
                    if (i + j + k == 2020){
                        return i * j * k;
                    }
                }
            }
        }
        return 0;
    }

    static int part1(ArrayList<Integer> array){
        ArrayList<Integer> seen = new ArrayList<>();
        for (int item : array) {
            int complement = 2020 - item;

            if (seen.contains(complement)){
                return complement * item;
            }
            seen.add(item);
        }
        return 0;
    }
}

