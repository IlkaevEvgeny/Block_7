# "Форматирование строк":
team1 = 'Волшебники Данных'
team2 = 'Мастера кода'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 10717.6 #из первого условия нет данных о времени второй команды

#challenge_result = "Мастера кода"
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/tasks_total
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = team1
elif score_2 > score_1 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = team2
else: challenge_result = 'ничья'

# Используем %
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

# Используем format
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {}c!".format(team1_time))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')
print (f'Результат битвы: победа команды {challenge_result}!')
print (f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!.")