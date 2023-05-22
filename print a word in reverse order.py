class Word:
    def __init__(self):
        self.letter=[]
        
    def push(self,word):
        self.letter.append(word)
        
        
    def pop(self,word):
        for i in range(len(self.letter)):
             word.append(self.letter.pop())
    
        return word
word=Word()
word.push("h")
word.push("e")
word.push("l")
word.push("l")
word.push("o")
print(word.letter)
print(word.pop([]))




        
        
    
     
     
