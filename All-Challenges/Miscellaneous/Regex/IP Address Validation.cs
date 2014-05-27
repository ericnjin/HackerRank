using System;
using System.Text.RegularExpressions;

class Solution {
static void Main(String[] args)
{
int n = int.Parse(Console.ReadLine());
for(int i=0; i<n; i++)
{
string s = Console.ReadLine();
if(Regex.IsMatch(s + ".", @"^((\d{1,2}|1\d{2}|2([0-4]\d|5[0-5])).){4}$"))
Console.WriteLine("IPv4");
else
if(Regex.IsMatch(s + ":", @"^([\da-f]{1,4}:){8}$"))
Console.WriteLine("IPv6");
else
Console.WriteLine("Neither");
}
}
}
