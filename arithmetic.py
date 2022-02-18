# Arithmetic Exam Application
import random


class Calculator:

    def __init__(self):
        self.num_qs = 5
        self.level = 0
        self.score = 0
        self.questions = 0
        self.x = 0
        self.y = 0
        self.operation = '+'
        self.level_desc = {'1': '1 - simple operations with numbers 2-9', '2':  '2 - integral squares of 11-29'}

    def get_level(self):
        print('Which level do you want? Enter a number:')
        for key, item in self.level_desc.items():
            print(item)
        while True:
            self.level = int(input())
            if self.level in [1, 2]:
                break
            else:
                print('Incorrect format.')
        return

    def new_question(self):
        if self.level == 1:
            self.x = random.randint(2, 9)
            self.y = random.randint(2, 9)
            self.operation = random.choice("+-*")
            print(f'{self.x} {self.operation} {self.y}')
        elif self.level == 2:
            self.x = random.randint(11, 29)
            print(self.x)

    def calc_result(self):
        if self.level == 1:
            return eval(f'{self.x} {self.operation} {self.y}')
        elif self.level == 2:
            return pow(self.x, 2)

    def check_input(self):
        while True:
            try:
                answer = int(input())
                break
            except ValueError:
                print('Wrong format! Try again.')
        self.check_answer(answer)

    def check_answer(self, answer):
        result = self.calc_result()
        if answer == result:
            print('Right!')
            self.score += 1
        else:
            print('Wrong!')  # add correct answer also ?

    def save_result(self):
        print(f'Your mark is {self.score} / {self.num_qs} Would you like to save the result? Enter yes or no.')
        save = input()
        if save in ['y', 'Y', 'yes', 'Yes', 'YES']:
            name = input('What is your name?: ')
            quiz = self.level_desc[str(self.level)]
            filename = 'results.txt'
            content = f'{name}: {self.score}/{self.num_qs} in Level {self.level} ({quiz}).'
            try:
                with open(filename, 'a') as f:
                    f.write(content + "\n")
                print(f'The results are saved in "{filename}".')
            except:
                print('There may have been an issue saving the results')


def main():
    my_calc = Calculator()
    my_calc.get_level()
    for i in range(1, my_calc.num_qs + 1):
        my_calc.new_question()
        my_calc.calc_result()
        my_calc.check_input()
    my_calc.save_result()


if __name__ == '__main__':
    main()
