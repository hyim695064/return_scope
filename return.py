# score = 10
# #מדפיס גם 10 ןגם 7 פעם אחת את מה שבתוך הפונקציה ןפעם אחת את מה שבחוץ
# def update_score():
#     score = 5
#     score = score + 2
#     print(score)
# update_score()
# print(score)
# name = "agent"
# level = 2
# #כמו לפני הוא מדפיס את מה שבתוך הפונקציה וההדפסה בחוץ 
# #מדפיסה את מה שמחוץ לפונקציה
# def show_info():
#     name = "spy"
#     level =4
#     power = level * 10
#     print(name)
#     print(power)
# show_info()
# print(name)
# print(level)
#3
#זה הדפיס לי 30 מכיוון שבתןך הפרמ היה 5 והוספתי 10 והכפלתי ב2 
#והשני פשןט מדפיס את הגלןבל
# coins = 20 
# def mission_reward(coins):
#     coins = coins +10
#     coins = coins * 2
#     print(coins)
# mission_reward(5)
# print(coins)
#4
#מדפיס לי את הערך של בריא בתוך הפונקציה וגם את הערך של נזק בפונקציה 
#ובחוץ את הערך הגלןבלי של בריא
# health = 100
# def take_damage(damage):
#     health = 100
#     health = health - damage
#     damage = damage + 5
#     print(health)
#     print(damage)
# take_damage(30)
# print(health)
#5
#אני מקבל פעמיים הדפסה גם של מה שבחוץ ןגם את מה שבפנים
items = ["map", "key"]
def add_items():
    items.append("torch")
    items.append("coin")
    print(items)
add_items()
print(items)
