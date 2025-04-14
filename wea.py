import datetime
import random

DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

PAST_WEATHER_DATA = {
    day: (random.randint(-15, 30), random.choice(["Солнечно", "Дождь", "Облачно", "Гроза", "Снег"]))
    for day in DAYS
}

def generate_weather_report(city):
    """Генерация случайного прогноза погоды для города."""
    temperatures = [random.randint(-10, 35) for _ in range(7)]
    conditions = [random.choice(["Солнечно", "Дождь", "Облачно", "Гроза", "Снег"]) for _ in range(7)]
    return list(zip(temperatures, conditions))

def display_weather_report(city, report):
    """Вывод прогноза погоды на неделю."""
    print(f"\nПрогноз погоды для города {city} на неделю:")
    for i, (temp, cond) in enumerate(report):
        print(f"{DAYS[i]}: {temp}°C, {cond}")

    avg_temp = sum(temp for temp, _ in report) / 7
    print(f"\nСредняя температура за неделю: {avg_temp:.1f}°C")

    if avg_temp > 25:
        print("Ожидается жаркая неделя! Не забудьте солнцезащитный крем.")
    elif avg_temp < 5:
        print("Холодная неделя! Одевайтесь теплее.")

def display_past_weather():
    """Вывод истории погоды за прошлую неделю."""
    print("\nИстория погоды за прошлую неделю:")
    for day in DAYS:
        temp, condition = PAST_WEATHER_DATA[day]
        print(f"{day}: {temp}°C, {condition}")

def analyze_temperature_trends(report):
    """Анализ повышения или понижения температуры."""
    trend = "повышение" if report[-1][0] > report[0][0] else "понижение"
    diff = abs(report[-1][0] - report[0][0])
    print(f"\nТренд температуры: {trend} на {diff}°C за неделю.")

def suggest_clothing(report):
    """Рекомендации по одежде на основе прогноза погоды."""
    recommendations = {
        "Солнечно": "Легкая одежда, солнцезащитные очки",
        "Дождь": "Зонт или дождевик",
        "Облачно": "Легкая куртка или свитер",
        "Гроза": "Плотная одежда и водонепроницаемая обувь",
        "Снег": "Зимняя одежда, шапка и перчатки"
    }
    print("\nРекомендации по одежде на неделю:")
    for day, (_, condition) in enumerate(report):
        print(f"{DAYS[day]}: {recommendations.get(condition, 'Одежда по погоде')}")

def compare_with_past_weather(report):
    """Сравнение прогноза с погодой прошлой недели."""
    print("\nСравнение с предыдущей неделей:")
    for i in range(7):
        today_temp, today_cond = report[i]
        past_temp, past_cond = PAST_WEATHER_DATA[DAYS[i]]
        temp_diff = today_temp - past_temp
        print(f"{DAYS[i]}: изменение температуры {temp_diff:+}°C ({past_temp}°C → {today_temp}°C), былo: {past_cond}, будет: {today_cond}")

def main():
    city = input("Введите название города: ")
    report = generate_weather_report(city)
    display_weather_report(city, report)
    analyze_temperature_trends(report)
    suggest_clothing(report)
    display_past_weather()
    compare_with_past_weather(report)
    print("\nПрогноз погоды составлен: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
