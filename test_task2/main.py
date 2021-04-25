# Импорт модуля для случайного определения действий и последовательности ходов
import random


# Абстрактный класс для компьютера и игрока
class Unit:
    def __init__(self, name='Computer'):
        # В конструкторе указываем количество здоровья и если это не компьютер кладём в переменную name никнейм игрока
        self.health = 100
        self.name = name

    # Нормальная атака, с помощью метода randint получаем случайное число, отнимаеи его от здоровья противника
    # и надпись о том, кто атаковал и здоровье, которое осталось
    def normal_attack(self, enemy):
        enemy.health -= random.randint(18, 25)
        print(f'{self.name} attacked {enemy.name} with normal attack! {self.name}={self.health} : {enemy.name}={enemy.health}')

    # То же самое делаем для этого вида атаки, что и для обычной, но корректируем диапазон случайных чисел
    def heavy_attack(self, enemy):
        enemy.health -= random.randint(10, 35)
        print(f'{self.name} attacked {enemy.name} with heavy attack! {self.name}={self.health} : {enemy.name}={enemy.health}')

    # Здесь мы получаем случайное число и добавляем его к сдоровью, т.к. это лечение
    # и выводим результат
    def heal(self, enemy):
        random_heal = random.randint(18, 25)
        self.health += random_heal
        print(f'{self.name} healed himself for {random_heal}! {self.name}={self.health} : {enemy.name}={enemy.health}')

    # Создаём список из всех возможных действий
    def random_action(self, enemy):
        actions = [self.normal_attack, self.heavy_attack, self.heal]
        # Случайным образом выбираем одно из действий и сразу его выполняем
        random.choice(actions)(enemy)


# Класс игрока, который наследует класс Unit, создан, чтобы можно было вводить свой никнейм
class Player(Unit):
    def set_name(self):
        self.name = input('What is your name? ')


# В классе Computer мы переопределяем метод вызова случайного действия и делаем так, чтобы компьютер имел
# трёхкратный шанс на лечение при уровне здоровья ниже 35 единиц
class Computer(Unit):
    def random_action(self, enemy):
        if self.health > 35:
            actions = [self.normal_attack, self.heavy_attack, self.heal]
            random.choice(actions)(enemy)
        else:
            actions = [self.normal_attack, self.heavy_attack, self.heal, self.heal, self.heal]
            random.choice(actions)(enemy)


# В это классе происходит сама игра между игроком и компьютером
class Game:
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player

    # Проверка на то, что уровень здоровья и игрока, и компьютера выше 0
    def is_game_finished(self):
        return self.first_player.health > 0 and self.second_player.health > 0

    # Выводит в консоль победителя
    def print_winner(self):
        if self.first_player.health > self.second_player.health:
            print(f'{self.first_player.name} won!')
        elif self.second_player.health > self.first_player.health:
            print(f'{self.second_player.name} won!')

    # Метод который по сути и есть игрой между игроком и компьютером, реализован с помощью цикла while
    # до того момента, пока уровень здоровья любого из игроков не упадёт ниже 0
    # в конце выводит победителя, когда игра завершилась
    # Очередность ходов является случайной и зависит от того, какое случайное число от 1 до 2 нам вернет метод randint
    def play_game(self):
        while self.is_game_finished():
            random_int = random.randint(1, 2)
            if random_int == 1:
                self.first_player.random_action(self.second_player)
            elif random_int == 2:
                self.second_player.random_action(self.first_player)
        self.print_winner()


if __name__ == '__main__':
    # Создаем объекты классов Player и Computer
    player = Player()
    computer = Computer()
    # Спрашиваем никнейм у пользователя для подальшего вывода
    player.set_name()
    # Создаём объект игры, передаем туда два объекта (игрока и компьютер) в качестве параметров
    game = Game(player, computer)
    # Вызываем метод начала игры
    game.play_game()
