import random

# def randInt(min = 0,max = 100):
#     num = random.randint(min,max)
#     return num

# print(randInt())
# print(randInt(max = 10))
# print(randInt(min = 10))
# print(randInt(10,20))
# ---------------------------------------------

def randomFloatFrom0To1():
    num = random.random() 
    return num

print(randomFloatFrom0To1())

# ---------------------------------------
def randomFloatFrom0To50():
    num = random.random() *50
    return num

print(randomFloatFrom0To50())

# ------------------------------------------
def randomFloatFrom10To35():
    num = random.random() *25 +10
    return num

print(randomFloatFrom10To35())
# -------------------------------------------------
def randomFrom10To35AsInt():
    num = random.random() *25 +10
    return round(num)

print(randomFrom10To35AsInt())

