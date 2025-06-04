from collections import deque

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def push(self, ch):
        self.stack.append(ch)

    def enqueue(self,ch):
        self.queue.append(ch)

    def pop(self):
        return self.stack.pop()

    def dequeue(self):
        return self.queue.popleft()


s= input("Enter a word of choice: ").strip()

obj_review = Solution()

for ch in s :
    obj_review.push(ch)
    obj_review.enqueue(ch)

is_palindrome = True

for i in range(len(s) // 2):
    if obj_review.pop() != obj_review.dequeue():
        is_palindrome = False
        break

if is_palindrome:
    print(f"The word:'{s}' is a palindrome.")
else:
    print(f"The word:'{s}' is not a palindrome.")