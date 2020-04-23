if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    final = []
    for i in arr:
        if i not in final:
            final.append(i)

    final.sort()
    runner = final[-2]
    print(runner)
    
