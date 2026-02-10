class Conversion:
    def __init__(self):
        self.strDict = {"zero":0,"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, 
            "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eightteen":18, "nineteen":19, "twenty":20,
            "thirty":30, "fourty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, "hundred":100,
            "thousand":1000, "million":1000000, "billion":1000000000, "trillion":1000000000000
            }
        self.intDict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 
            11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eightteen", 19:"nineteen", 20:"twenty",
            30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred",
            1000:"thousand", 10000000:"million", 1000000000:"billion", 1000000000000:"trillion"
            }
        self.strHundreds = ["hundred", "thousand", "million", "billion", "trillion"]
        self.intHundreds = [100, 1000, 1000000, 1000000000, 1000000000000]
    def convertToNum(self, string):
        """Convert words of numbers to an integer number"""
        try:
            string = string.lower()
            strList = string.split()
            answer = 0
            i = 0
            while i < len(strList):
                if strList[i] not in self.strHundreds:
                    subAnswer = self.strDict[strList[i]] 
                    """subAnswer to detect self.strHundreds after a number < 100; e.g: "thirty two"""
                    k = i + 1
                    while k < len(strList):
                        if strList[k % len(strList)] not in self.strHundreds and strList[k - 1] in self.strHundreds: 
                            """ If the next number under 100 is found, AND self.strHundreds already found, break. E.g: six hundred eighteen -> break at 'eighteen' """
                            break
                        elif strList[k % len(strList)] not in self.strHundreds and strList[k - 1] not in self.strHundreds: 
                            """ If there was no self.strHundreds yet, add number to subAnswer. E.g: twenty two -> 20 + 2 """
                            subAnswer += self.strDict[strList[k]]
                            i += 1
                        else:
                            subAnswer *= self.strDict[strList[k]]
                        k += 1
                    answer += subAnswer
                i += 1
            return answer
        except:
            return "Wrong input."
    def convertToString(self, number):
        """Convert integer number to a words of numbers"""
        try:
            answer = []
            if number == 0:
                return "zero"
            i = 0
            compare = 0
            while number != compare:
                i += 1
                compare = number % (10**i)
                if compare != 0:
                    if i > 2:
                        digit = int(compare / (10**(i-1)))
                        if digit != 0:
                            if i > 1 and i < 5:
                                answer.append(self.intDict[10**(i-1)])
                            answer.append(self.intDict[digit])
                    else:
                        if number > 19:
                            if i == 2:
                                if compare % 10 != 0:
                                    answer.append(self.intDict[compare % 10])
                                answer.append(self.intDict[compare - compare % 10])
                        else:
                            answer.append(self.intDict[compare])
                            i += 1
            answer.reverse()
            return " ".join(answer)
        except:
            return "Something went wrong."
