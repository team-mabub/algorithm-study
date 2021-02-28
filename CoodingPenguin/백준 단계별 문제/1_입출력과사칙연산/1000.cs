using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practice
{
    class Program
    {
        static void Main()
        {
            string[] input = Console.ReadLine().Split(' ');
            int add = 0;
            for(int i = 0;i < input.Length; i++)
            {
                add += int.Parse(input[i]);
            }
                
            Console.WriteLine(add);
        }
    }
}