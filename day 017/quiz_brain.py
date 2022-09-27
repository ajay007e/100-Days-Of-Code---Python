class QuestionBrain:
    def __init__(self,l):
        self.n=0
        self.qlist = l
        self.score = 0

    def nextQuestion(self):
        que = self.qlist[self.n]
        self.n+=1
        a = input(f"Q.{self.n}: {que.text} (True/False) ? :")
        self.check(a,que.answer)

    def still_have_question(self):
        return self.n < len(self.qlist)

    def check(self,ans,crt):
        if ans.lower()==crt.lower():
            self.score +=1
            print("You are Right")
        else:
            print("You are Wrong")
        print(f"Your score : {self.score}/{self.n}")

    def finish(self):
        print(f"You have completed the quiz..\nYour final score : {self.score}/{self.n}")

