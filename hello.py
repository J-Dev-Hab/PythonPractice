# print関数の前
print("こんにちは！")  # ここはコメント文です。
# print関数の後ろ
apple_price=120
print(apple_price)# apple_price=120
x=10
print(x)# x=10
y=100
print(y)# y=100
x=y
print(x)# x=100
# 整数型のデータ=150
apple_price=150# 整数型＝int
# 整数型の変数＝apple_price
print(apple_price)# apple_price=150
name="斉藤"# 文字列型＝str
print(name)# name="斉藤"
weight=12.3# 浮動小数文字型=float
print(weight)# weight=12.3
a_type=type(apple_price)
print(a_type)# a_type=整数型=intつまり何型かを教えてくれる
n_type=type(name)
print(n_type)# n_type=文字列型=strつまり何型かを教えてくれる
w_type=type(weight)
print(w_type)# w_type=浮動小数点型=floatつまり何型かを教えてくれる
x="10"
y=int(x)
print(y)# y=10
print(apple_price,name,weight)# まとめて出る
print(a_type,n_type,w_type)# まとめて出る
math=82
japanese=74
english=60
avg_score=(math+japanese+english)/3
print(avg_score)# avg_score=72.0
surname="鈴木"
given_name="まゆ"
full_name=surname+given_name
print(full_name)# full_name="鈴木まゆ"
price=100
text=f"この商品は{price}円です。"
print(text)# この商品は100円です。
scores=[82,74,60]
avg_score=sum(scores)/len(scores)# sum=scoresの合計　len=scoresの個数
print(avg_score)# 72.0
prices={"バナナ": 250,"みかん":300,"いちご":500}
result=prices["みかん"]
print(result)#　300
prices["ぶどう"]=400
print(prices)# {'バナナ': 250, 'みかん': 300, 'いちご': 500, 'ぶどう': 400}
prices["バナナ"]=200
print(prices)# {'バナナ': 200, 'みかん': 300, 'いちご': 500, 'ぶどう': 400}
fruits=list(prices.keys())# 辞書のキーをリストに変換=keys=キー
print(fruits)# ['バナナ', 'みかん', 'いちご', 'ぶどう']
fruits=list(prices.values())# 辞書の値をリストに変換=values=値
print(fruits)# [200, 300, 500, 400]
scores={"数学":82,"国語":74,"英語":60,"理科":92,"社会":70}
diff=scores["理科"]-scores["社会"]
text=f"{diff}点"
print(text)# 22点
scores=list(scores.values())
avg_scores=sum(scores)/len(scores)
print(f"{avg_scores}点")# 75.6
prefecture="東京"
if prefecture=="東京":
    print("日本の首都です")
    prefecture="ワシントン"
if prefecture=="東京":
    print("日本の首都です")
elif prefecture=="ワシントン":
    print("アメリカの首都です")
    number=11
if number%2==0:
    print("偶数です")# 10
else:
    print("奇数です")# 11
scores=[90,30,49]
for x in scores:
    print(x)
for x in scores:
    print(x+1)
fruits={"apple":130,"banana":350,"lemon":100}
for name, price in fruits.items():
    print(f"{name}は{price}円です。")
for x in range(5):
    print(x)
for x in range(-8,-2):
    print(x)
names=["佐藤","佐々木","鈴木"]
for x in names:
    print(f"{x}さん")
scores={"数学":82,"国語":74,"英語":60,"理科":92,"社会":70}
for keys,values in scores.items():
    print(f"{keys}は{values}点です。")
for i in range(1,11):
    print(i)
year = 2000
if year %400==0:
    print("閏年です。")
elif year %100==0:
    print("平年です")
elif year %4==0:
    print("閏年です")
else:
    print("平年です")
for number in range(1,101):
    if number % 15==0:
        print("FizzBuzz")
    elif number %3==0:
        print("FIzz")
    elif number %5==0:
        print("Buzz")
    else:
        print(number)
def add_sub_numbers(a,b):
    c =a+b
    r =a-b
    return c,r
x,z=add_sub_numbers(100,10)
print(x)
print(z)

print("こんにちは、Python！")