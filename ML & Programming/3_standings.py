def parse_match_result(match_result):
    team1, score_str, team2 = match_result.split()
    score1, score2 = map(int, score_str.split(":"))
    return team1, team2, score1, score2

def build_tournament_table(matches):
    teams = set()
    results = {}
    
    for match in matches:
        team1, team2, score1, score2 = parse_match_result(match)
        teams.add(team1)
        teams.add(team2)
        
        if score1 > score2:
            results.setdefault(team1, {"W": 0, "D": 0, "L": 0, "Points": 0})
            results.setdefault(team2, {"W": 0, "D": 0, "L": 0, "Points": 0})
            results[team1]["W"] += 1
            results[team1]["Points"] += 3
            results[team2]["L"] += 1
        elif score1 < score2:
            results.setdefault(team1, {"W": 0, "D": 0, "L": 0, "Points": 0})
            results.setdefault(team2, {"W": 0, "D": 0, "L": 0, "Points": 0})
            results[team2]["W"] += 1
            results[team2]["Points"] += 3
            results[team1]["L"] += 1
        else:
            results.setdefault(team1, {"W": 0, "D": 0, "L": 0, "Points": 0})
            results.setdefault(team2, {"W": 0, "D": 0, "L": 0, "Points": 0})
            results[team1]["D"] += 1
            results[team1]["Points"] += 1
            results[team2]["D"] += 1
            results[team2]["Points"] += 1
            
    sorted_teams = sorted(teams)
    table = []
    
    for i, team in enumerate(sorted_teams, start=1):
        points = results[team]["Points"]
        wins = results[team]["W"]
        losses = results[team]["L"]
        draws = results[team]["D"]
        position = i
        
        table.append((team, wins, draws, losses, points, position))
    
    return table

def print_tournament_table(table):
    print("{:<5} {:<30} {:<3} {:<3} {:<3} {:<3} {:<3}".format("Pos", "Team", "W", "D", "L", "Pts", "Pos"))
    for row in table:
        team, wins, draws, losses, points, position = row
        print("{:<5} {:<30} {:<3} {:<3} {:<3} {:<3} {:<3}".format(position, team, wins, draws, losses, points, position))

if __name__ == "__main__":
    matches = [
        "TeamA 2:1 TeamB",
        "TeamC 0:0 TeamA",
        "TeamB 1:1 TeamC",
    ]
    
    tournament_table = build_tournament_table(matches)
    print_tournament_table(tournament_table)


"""
Давайте оценим сложность данного алгоритма.
Функция parse_match_result(match_result) разбивает строку match_result на отдельные значения 
и выполняет преобразование в целые числа. Время работы этой функции зависит от длины входной строки 
и количества символов в числах. Давайте обозначим m - максимальное количество символов в числах.
Основной цикл в функции build_tournament_table(matches) выполняется для каждого матча в списке matches. 
Пусть k - количество матчей в списке matches.
В цикле выполняются операции добавления/обновления элементов словаря results, 
а также операции добавления элементов в множество teams. 
Вставка/обновление элемента словаря и добавление элемента в множество выполняются за O(1).
Затем выполняется сортировка множества teams, что занимает O(t log t), где t - количество уникальных команд в матчах.
Далее, формируется таблица table с информацией о каждой команде. Создание таблицы занимает O(t), 
где t - количество уникальных команд в матчах.
Наконец, функция print_tournament_table(table) выполняет вывод таблицы. 
Вывод одной строки таблицы выполняется за O(t), где t - количество уникальных команд в матчах.
Таким образом, общая сложность алгоритма будет составлять O(km + t log t), 
где k - количество матчей в списке matches, m - максимальное количество символов в числах, и t - 
количество уникальных команд в матчах. В большинстве случаев t будет меньше или равно k, 
поэтому сложность может быть приближенно записана как O(km + k log k).

Оценка O(km + t log t) показывает, что алгоритм хорошо масштабируется и должен быстро обрабатывать 
даже большие списки матчей, но при этом стоит учитывать, что время работы может зависеть от количества 
уникальных команд t и максимального количества символов в числах m.
"""