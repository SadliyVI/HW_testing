
def vote(votes):
    temp = {}
    for number in votes:
        if str(number).isdigit():
            temp[number] = votes.count(number)
            res = max(temp.items(), key=lambda i: i[1])
        else:
            raise ValueError
    return res[0]
if __name__ == '__main__':

    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
    print(vote([-1, -1, -1, 2, 3]))
    print(vote(['a', 'b', 'b', 'd']))
    print(vote([]))