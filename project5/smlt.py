import  random

class Brain:
    status = False 

    def return_player_type(self,pt,round,p1p,p1p2):

        if round == 0 :
            self.status= False

        if pt == 'CR':
            return 'c'
        elif pt == 'DF':
            return 'd'
        elif pt== 'TFT':
            if round==0:
                return 'c'
            else:
                return p1p
        elif pt=='SP':
            if p1p == 'd':
                self.status = True
            if round==0:
                return 'c'
            elif self.status == True:
                return 'd'
            else:
                return 'c'
        elif pt=='NP':
            if p1p=='d':
                return 'd'
            else:
                num = random.random()
                if(num <= 0.1):
                    return 'd'
                else:
                    return 'c'
        elif pt=='TF2T':
            if round == 0 or round == 1:
                return 'c'
            elif p1p=='d' and p1p2 == 'd':
                return 'd'
            else:
                return 'c'
        elif pt=='RP':
            num=random.randint(1,2)
            if num==1:
                return 'c'
            else:
                return 'd'



