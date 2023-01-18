from smlt import Brain


class Tour:
    def __init__(self, plist):
        self.plist = plist
        brain= Brain()
        categ = []
        n = 0
        for x in range(len(plist)):
            n = n + int(plist[x])
            if x == 0:
                cate = 'CR'
            elif x == 1:
                cate = 'DF'
            elif x == 2:
                cate = 'TFT'
            elif x == 3:
                cate = 'SP'
            elif x == 4:
                cate = 'NP'
            elif x == 5:
                cate = 'TF2T'
            else:
                cate = 'RP'
            if int(plist[x] > 0):
                for k in range(int(plist[x])):
                    categ.append(cate)

        i = 0

        result = [[0] * (n+1) for _ in range(n+1)]
        result[0][0]=''

        x=1
        while x<n+1:
            result[0][x] = categ[x-1]
            result[x][0] = categ[x-1]
            x+=1



        result2 = []

        while i < n-1:

            j = i+1

            c = 1

            while j <n:
                p1 = categ[i]
                p2 = categ[j]
                d = 0
                p1p = ''
                p2p = ''
                p1p2 = ''
                p2p2 = ''
                pointp1 = 0
                pointp2 = 0
                while d < 20:

                    movep1= brain.return_player_type(p1,d,p2p,p2p2)
                    p1p2=p1p
                    p1p=movep1


                    movep2 = brain.return_player_type(p2,d,p1p,p1p2)
                    p2p2=p2p
                    p2p=movep2

                    if movep1== 'c' and movep2== 'c':
                        pointp1 = pointp1 + 4
                        pointp2 = pointp2 + 4
                    elif movep1=='c' and movep2=='d':
                        pointp2 = pointp2 + 5
                    elif movep1== 'd' and movep2== 'd':
                        pointp1 = pointp1 + 2
                        pointp2 = pointp2 + 2
                    elif movep1=='d' and movep2=='c':
                        pointp1 = pointp1 + 5

                    d = d+1


                result[i+1][j+1]= str(pointp1) + '(' + str(pointp2) + ')'
                result[j+1][i+1]=str(pointp2) + '(' + str(pointp1) + ')'



                c = c+1
                j = j+1

            i = i+1
        for a in result:
            print(a)

        for index,o in enumerate(result):
            playerp = 0
            for indexq,z in enumerate(o):
                z=str(z)
                if (z.split('(')[0]).isdigit():
                    playerp+=int(z.split('(')[0])

            result2.append(playerp)
        print('')
        print(categ)
        print(result2[1:])
        p=0
        a=0
        while p<n:
            t=int(plist[a])
            y=0
            avg=0
            while y<t:
                avg+=result2[p+1]
                y+=1
                p+=1
            if t!=0:
                print(avg/t)
            a+=1





