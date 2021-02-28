using System;

namespace Practice
{
    class Program
    {
        static void Main()
        {
            int num1 = int.Parse(Console.ReadLine());
            int num2 = int.Parse(Console.ReadLine());
            
            int[] element = new int[3];
            element[0] = num2 / 100;
            element[1] = (num2 % 100) / 10;
            element[2] = num2 % 10;
            
            Console.WriteLine(num1 * element[2]);
            Console.WriteLine(num1 * element[1]);
            Console.WriteLine(num1 * element[0]);
            Console.WriteLine((num1 * element[2]) + (num1 * element[1] * 10) + (num1 * element[0] * 100));
        }
    }
}