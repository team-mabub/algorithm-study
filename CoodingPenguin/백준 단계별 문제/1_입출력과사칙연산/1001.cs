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
                
            int result = int.Parse(input[0]) - int.Parse(input[1]);
            Console.WriteLine(result);
        }
    }
}