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
# items = ["map", "key"]
# def add_items():
#     items.append("torch")
#     items.append("coin")
#     print(items)
# add_items()
# print(items)
#6
#פעם אחת מדפיס לי רק את מה שבפוקציה מכיוון שהפעם הגדרתי אותו בפנים
#פעם שניה מדפיס לי את מה שבחוץ
# items = ["map", "key"]
# def replace_items():
#     items = ["potion"]
#     items.append("shield")
#     print(items)
# replace_items()
# print(items)
#7
#מדפיס פעמיים 20 מכיוון שבתוך הפונקציה אני מצביע לגלובל 
#ןאז הוא דןרס אותו עם השינוי
# points = 3
# def add_points():
#     global points
#     points = points + 7
#     points = points * 2
#     print(points)
# add_points()
# print(points)
#8
#הראשון הוא מדפיס את ,רץ, כי הוא ההדפסה הראשונה ץהשני הוא מדפיס לי את 
#,מוכן, כי זה ההדפסה השניה וזה מה שהגדרתי לו ץ השלישי הוא חוזר לגלובלי 
#ומדפיס אותו
# status = "waiting"
# def outer():
#     status = "ready"
    
#     def inner():
#         status = "running"
#         print(status)
#     inner()
#     print(status)
# outer()
# print(status)

coins = 10
#ההדפסה הראשונה והשניה מקבל 16 מכייון שהם משתמשים במשתנה מטבעות השני
#וההדפסה השלישית פשוט מקבלת 10 כמו המשתנה הראשון
# def outer():
#     coins = 5

#     def inner():
#         nonlocal coins 
#         coins = coins + 3
#         coins = coins * 2
#         print(coins)
#     inner()
#     print(coins)

# outer()
# print(coins)
score = 1
bag = ["key"]
#שניההדפסות הראשונות עושות את אותו הדבר השלישי בסך הכל מדפיס 1
#כמו בגלובל , מה שלא משתנה זה ההדפסה של שקית מכיוון שלא הגדרתי את זה
#עוד פעם רק בגלובל אז כל הוספה הולכת לגלובל 
def outer():
    score = 10 
    bag.append("map")

    def inner():
        nonlocal score
        score = score + 5
        bag.append("coin")
        print(score)
        print(bag)
    score = score * 2
    inner()
    print(score)
    print(bag)

outer()
print(score)
print(bag)