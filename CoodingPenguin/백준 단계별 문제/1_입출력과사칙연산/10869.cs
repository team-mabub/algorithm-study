using System;

namespace Practice
{
    class Program
    {
        static void Main()
        {
            string[] parsing = Console.ReadLine().Split(' ');
            int num1 = int.Parse(parsing[0]);
            int num2 = int.Parse(parsing[1]);
            
            Console.WriteLine(num1 + num2);
            Console.WriteLine(num1 - num2);
            Console.WriteLine(num1 * num2);
            Console.WriteLine(num1 / num2);
            Console.WriteLine(num1 % num2);
        }    
    }
}