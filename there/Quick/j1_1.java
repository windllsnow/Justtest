import java.util.Scanner;

public class j1_1 {
        public static void main(String args[]) {
                int num;
                num = 2;

                System.out.println("I have " + num + "dog ");// A + B 這裡+是連接子串的方法
                System.out.println("You have " + num + " dogs, too");// 這是註解
                /* System.out.println(args[0] + " & " + args[1]); */

                long lmax = java.lang.Long.MAX_VALUE;
                int imax = java.lang.Integer.MAX_VALUE;
                System.out.println(lmax);// 範圍，最大值
                System.out.println(imax);

                System.out.println("i=" + imax);
                System.out.println("i=" + (imax + 1));// 溢位
                System.out.println("i=" + (imax + 2L));// 溢位處理
                System.out.println("i=" + ((long) imax + 3));// 溢位處理

                int num1 = 5;
                int num2 = 10;
                int sum = Math.addExact(num1, num2); // 使用 Math.addExact 方法相加兩個整數
                System.out.println(sum);
                int num01 = 5;
                int num02 = 10;
                num01 += num02;/// 將 num2 的值添加到 num1 中，結果存回 num1
                System.out.println(num01);
                int[] array1 = { 1, 2, 3 };
                int[] array2 = { 4, 5, 6 };
                int[] sumArray = new int[array1.length];

                for (int i = 0; i < array1.length; i++) {
                        sumArray[i] = array1[i] + array2[i]; // 將兩個數組中對應位置的元素相加
                        System.out.println(sumArray[i]);
                }
                char ch1 = 71; // unicode 編碼71 = G
                char ch2 = 'G'; //
                char ch3 = '\u0047'; /* \ u 為十六進位 */
                System.out.println("ch1=" + ch1);
                System.out.println("ch2=" + ch2);
                System.out.println("ch3=" + ch3);

                int dec = 42; // 要轉換的整數
                // 轉換為2進位
                String binary = Integer.toBinaryString(dec);
                System.out.println("2進位表示：" + binary);
                // 轉換為8進位
                String octal = Integer.toOctalString(dec);
                System.out.println("8進位表示：" + octal);
                // 轉換為10進位
                String decimal = Integer.toString(dec);
                System.out.println("10進位表示：" + decimal);
                // 轉換為16進位
                String hexadecimal = Integer.toHexString(dec);
                System.out.println("16進位表示：" + hexadecimal);

                String str1 = "1234"; // 要轉換的字串
                int number1 = Integer.parseInt(str1); // 將字串轉換為整數
                System.out.println("整數表示：" + number1);
                int number = 1234; // 要轉換的整數
                String str = Integer.toString(number); // 將整數轉換為字串
                System.out.println("字串表示：" + str);
                if (str instanceof String) {
                        System.out.println("str 是字串。");
                } else {
                        System.out.println("str 不是字串。");
                }

                Object obj = 1234; // 整數物件
                if (obj instanceof Integer) {
                        System.out.println("obj 是整數。");
                } else {
                        System.out.println("obj 不是整數。");
                }
                Object obj2 = 1234; // 整數物件
                if (obj2.getClass() == Integer.class) {
                        System.out.println("obj 是整數。");
                } else {
                        System.out.println("obj 不是整數。");
                }
                int num4 = 1234; // 基本數據類型 int
                if (num4 >= Integer.MIN_VALUE && num4 <= Integer.MAX_VALUE) {
                        System.out.println("num 是整數。");
                } else {
                        System.out.println("num 不是整數。");
                }

                int xy = 100;
                double yy = 10.5;
                String ss = "Deep";
                System.out.printf("xy =%7d%n", xy);
                System.out.printf("yy =%-11.4f%n", yy);
                System.out.printf("ss =%12s%n", ss);

                Scanner scn = new Scanner(System.in); //
                String name;
                int age;

                System.out.print("What's your name? ");
                name = scn.nextLine(); // 
                System.out.print("How old are you? ");
                age = scn.nextInt(); //

                System.out.print("Hi, " + name + ", you're ");
                System.out.println(age + " years old.");
        }
}
