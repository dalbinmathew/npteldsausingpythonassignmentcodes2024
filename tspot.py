# consider an array of coins represented by 1's and 0's, such as [1,1,0,1], 
# where 1 signifies a point and 0 signifies a deduction of 1 point. 
# Two players are involved in a game where player 1 always starts. 
# The goal is to determine the minimum position at which player 1 can 
# stop playing to ensure his score is higher than player 2's. 
# In this scenario, if Player 1 stops at position 2, he scores 2 points (1 + 1), 
# while Player 2 scores 0 points, as a result of scoring -1 due to the 0 in the array 
# and then adding 1 to the score because of the 1 in the array.



# def maxpoints(arr):
#     s1,s2=0,0    
#     for i in range(1,len(arr)):
#         x=arr[:i]
#         y=arr[i:]
#         for m in x:
#             if m == 1:
#                 s1+=1
#             else:
#                 s1-=1
#         for n in y:
#             if n == 1:
#                 s2+=1
#             else:
#                 s2-=1
#         if s1>s2:
#             return i


# optimized soln

def maxpoints(arr):
    total_score = 0 # Total score of all elements
    for i in arr:
        if i==1:
            total_score+=1
        else:
            total_score-=1
    player1_score = 0

    for i in range(len(arr)):
        # Update Player 1's score incrementally
        player1_score += 1 if arr[i] == 1 else -1
        # Player 2's score is the remaining score
        player2_score = total_score - player1_score
        
        # Check if Player 1's score is greater than Player 2's
        if player1_score > player2_score:
            return i + 1  # Return the 1-based position

    return -1  # In case no such position exists


        
            
arr=[1,1,0,1]
print(maxpoints(arr))
            