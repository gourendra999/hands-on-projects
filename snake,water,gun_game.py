import random

# def result(n,user):                      # method 1.
#     if user==n :
#         return 'Its DRAW'
#     elif user=='snake' and n=='water':
#         return 'You WIN'
#     elif user=='snake' and n=='gun':
#         return 'You LOSE'
#     elif user=='water' and n=='snake':
#         return 'You LOSE'
#     elif user=='water' and n=='gun':
#         return 'You WIN'
#     elif user=='gun' and n=='water':
#         return 'You LOSE'
#     elif user=='gun' and n=='snake':
#         return 'You WIN'
#     return result

def check(n,player):                      # method 2.
    if player==0:
        if n==0:
            return 'Its DRAW'
        elif n==1:
            return 'You WIN'
        elif n==2:
            return 'You LOSE'
    elif player==1:
        if n==0:
            return 'You LOSE'
        elif n==1:
            return 'Its DRAW'
        elif n==2:
            return 'You WIN' 
    elif player==2:
        if n==0:
            return 'You WIN'
        elif n==1:
            return 'You LOSE'
        elif n==2:
            return 'Its DRAW'   
    return check
user1=str(input('Choose your player between (snake,water,gun)\n '))
user2=int(input('Choose your player between (0 for snake,1 for water,2 for gun)\n '))
n2=random.randint(0,2)
print(n2)
comp_list=['snake','water','gun']
n1=random.choice(comp_list)
print(n1)
# print(result(n1,user1))
print(check(n2,user2))