import requests

# question_data = []
# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

class Data:
    def __init__(self):
        self.question_data=[]
        self.amount=10
        self.category=9
        self.difficulty='easy'
        self.category_name = [
            {'name':"General Knowledge","id":"9"},
            {'name':"Books","id":"10"},
            {'name':"Films","id":"11"},
            {'name':"Musics","id":"12"},
            {'name':"Musical & Theatre","id":"13"},
            {'name':"Television","id":"14"},
            {'name':"Video Games","id":"15"},
            {'name':"Board Games","id":"16"},
            {'name':"Science & Nature","id":"16"},
            {'name':"Computer","id":"18"},
            {'name':"Maths","id":"19"},
            {'name':"Mythology","id":"20"},
            {'name':"Sports","id":"21"},
            {'name':"Geology","id":"22"},
            {'name':"History","id":"23"},
            {'name':"Politics","id":"24"},
            {'name':"Art","id":"25"},
            {'name':"Celebrity","id":"26"},
            {'name':"Animal","id":"27"},
            {'name':"Vehical","id":"28"},
            {'name':"Comics","id":"29"},
            {'name':"Gadgets","id":"30"}
            ]

    def showCategory(self):
        for i in self.category_name:
            print(f"{i['name']}--{int(i['id'])-9}",end="       ")
        print()

    def create(self):
        self.amount = int(input("Number of Questions (less than 50):"))%51
        self.showCategory()
        self.category = ((int(input("Choose a Category:"))%22) + 9)
        t= True
        while t:
            self.difficulty = input("Choose a difficulty level (easy/medium/hard): ").lower()
            if self.difficulty =="easy" or self.difficulty =="medium" or self.difficulty == "hard":
                break
            else: print("Choose a correct_difficulty level..")
        self.create_data()
    
    def printdata(self):
        print(self.difficulty, self.amount, self.category)

    def create_data(self):
        # self.printdata()
        url = f'https://opentdb.com/api.php?amount={self.amount}&category={self.category}&difficulty={self.difficulty}&type=boolean'
        # print(url)
        res =requests.get(url).json()
        for i in res['results']:
            d = {"text":i['question'],"answer":i['correct_answer']}
            self.question_data.append(d)

        if len(self.question_data)==0:
            url = f'https://opentdb.com/api.php?amount={self.amount}&type=boolean'
            res =requests.get(url).json()
            for i in res['results']:
                d = {"text":i['question'],"answer":i['correct_answer']}
                self.question_data.append(d)
            print(f"\n\nUnable to find as per your request, {res['results'][0]['category']} is the category we choose for you")
        else:print("\n\n")