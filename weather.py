import datetime
import random

DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
CONDITIONS = ["Солнечно", "Дождь", "Облачно", "Гроза", "Снег"]
RECOMMENDATIONS = {
    "Солнечно": "Легкая одежда, солнцезащитные очки",
    "Дождь": "Зонт или дождевик",
    "Облачно": "Легкая куртка или свитер",
    "Гроза": "Плотная одежда и водонепроницаемая обувь",
    "Снег": "Зимняя одежда, шапка и перчатки"
}

class WeatherDay:
    def __init__(self, day, temp, condition):
        self.day = day
        self.temp = temp
        self.condition = condition

    def recommendation(self):
        return RECOMMENDATIONS.get(self.condition, "Одежда по погоде")

    def __str__(self):
        return f"{self.day}: {self.temp}°C, {self.condition}"

class WeatherReport:
    def __init__(self, city):
        self.city = city
        self.forecast = self._generate_week()
        self.past_data = self._generate_past()

    def _generate_week(self):
        return [
            WeatherDay(DAYS[i], random.randint(-10, 35), random.choice(CONDITIONS))
            for i in range(7)
        ]

    def _generate_past(self):
        return {
            day: WeatherDay(day, random.randint(-15, 30), random.choice(CONDITIONS))
            for day in DAYS
        }

    def display_forecast(self):
        print(f"\nПрогноз погоды для города {self.city} на неделю:")
        for day in self.forecast:
            print(day)

        avg = sum(day.temp for day in self.forecast) / len(self.forecast)
        print(f"\nСредняя температура за неделю: {avg:.1f}°C")
        self._comment_on_temperature(avg)

    def _comment_on_temperature(self, avg):
        if avg > 25:
            print("Ожидается жаркая неделя! Не забудьте солнцезащитный крем.")
        elif avg < 5:
            print("Холодная неделя! Одевайтесь теплее.")

    def display_past(self):
        print("\nИстория погоды за прошлую неделю:")
        for day in DAYS:
            print(self.past_data[day])

    def analyze_trend(self):
        start, end = self.forecast[0].temp, self.forecast[-1].temp
        diff = abs(end - start)
        trend = "повышение" if end > start else "понижение"
        print(f"\nТренд температуры: {trend} на {diff}°C за неделю.")

    def suggest_clothing(self):
        print("\nРекомендации по одежде на неделю:")
        for day in self.forecast:
            print(f"{day.day}: {day.recommendation()}")

    def compare_weeks(self):
        print("\nСравнение с предыдущей неделей:")
        for current in self.forecast:
            past = self.past_data[current.day]
            diff = current.temp - past.temp
            print(f"{current.day}: изменение температуры {diff:+}°C ({past.temp}°C → {current.temp}°C), былo: {past.condition}, будет: {current.condition}")

    def run(self):
        self.display_forecast()
        self.analyze_trend()
        self.suggest_clothing()
        self.display_past()
        self.compare_weeks()
        print("\nПрогноз погоды составлен:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def main():
    city = input("Введите название города: ")
    report = WeatherReport(city)
    report.run()

if __name__ == "__main__":
    main()