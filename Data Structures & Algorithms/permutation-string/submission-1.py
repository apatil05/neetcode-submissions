class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
        So initally I am thinking of an implenetation that uses a sliding window.  This will be done with two pointers

        Question, does a valiuad substring need to be allocated in contiguous indicies, or do indicies not need to neccesarily be contiguous?

        Thoughts:

        We create a dict of values that basically count the frequecy of each letter within s1 --> suboptimal as we are above reccomeneded space complexity

        Then we can loop through s2 and decrement the counter for each letter in our dict as it is encountered within s2.  We can begin decrementing the dict as soon as we start looping through and encounter a char within our dict.  The only thing is that we need to ensure that our window does not exceed the len(s1)--> This raises two new considerations:

        When do we move our left and right pointers / under what circumstances
        --> Sub Question:
                What happens to our dict when we do move our pointers

                For this we need to think of what it means to move pointers, whenever the right pointer is moved, we would need to add that char to our 
                dict if it isnt present, else increment the val of that letter 

                When the left pointer moves, before incrementing we must first decrement the count of that charachter within our dict, and then add a new 
                char or increment count of another char

        --> Sub Question 2:

                When we are moving pointers we need to have a reliable way of tracking what chars are in our window

        """
        if s1 == "":
            return True
        
        if len(s1) > len(s2):
            return False
        

        charMap = {}
        for i in s1:
            if i not in charMap:
                charMap[i] = 1
            else:
                charMap[i] += 1

        print(charMap)

      
        
        #Now our charMap is properly initialized
        s2Map = {}
        left = 0

        def addToMap(char:str) -> None:
            if char not in s2Map:
                s2Map[char] = 1
            else:
                s2Map[char] += 1

        for right in range(len(s2)):
            print(f"before if : {right - left}")
            print(f"before if : {s2Map}")
            if right - left > len(s1) -1  :
                
                s2Map[s2[left]] -= 1
                if s2Map[s2[left]] == 0:
                    del s2Map[s2[left]]
                left += 1
                addToMap(s2[right])
            else:
                addToMap(s2[right])
            print(f"after if :{right - left}")
            print(f"after if : {s2Map}")
            
            if s2Map == charMap:
                return True
        
        return False

            
            
            

            





