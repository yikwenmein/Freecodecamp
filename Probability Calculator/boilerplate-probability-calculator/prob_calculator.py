import random
import copy
class Hat:
    def __init__(self,**kwargs):
        self.contents =list()
        self.drawn_balls =list()
        for color, number in kwargs.items():
            self.contents.extend([color] * number)
        
    def draw(self, num):
        if (num< len(self.contents)):
            self.drawn_balls = random.sample(self.contents, num)
            for i in self.drawn_balls:
                self.contents.remove(i)
            return self.drawn_balls
        if (len(self.contents)< num):
            self.drawn_balls = self.contents
            self.contents =[]
            return self.drawn_balls
def experiment(hat=None, expected_balls=None, num_balls_drawn=None, num_experiments=None):
    #balls = hat.draw(num_balls_drawn)
    hat_copy = copy.deepcopy(hat.contents)
    histogram ={}
    count =0
    match =0
    balls= []
    
    i = 0
    while i< (num_experiments):
        balls = hat.draw(num_balls_drawn)
        
        for n in balls:
            if n not in histogram.keys():
                histogram[n] = 1
            # print(histogram)
            else:
                histogram[n] = histogram[n]+1 
        
        #print(histogram)
        for key in histogram.keys():
            if key in expected_balls.keys():
                if histogram[key] >= expected_balls[key]:
                    count=count+1
                    if count==len(expected_balls):
                        match += 1
        
        hat.contents = copy.deepcopy(hat_copy)               
        histogram.clear()
        balls.clear()
        count = 0
        i +=1
    return match/num_experiments 

