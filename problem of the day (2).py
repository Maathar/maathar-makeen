import math

s1 = [(-10, 20), (-10, -18)]
s2 = [(-10, 20), (0, 3)]
s3 = [(0, 3), (11, 12)]
s4 = [(8, 17), (10, -16)]
s5 = [(10, -16), (-10, -18)]

vectors = [s1, s2, s3, s4, s5]

print("Vector\tLength\tSlope")
for i in range(len(vectors)):
    x1,y1 = vectors[i][0]
    x2,y2 = vectors[i][1]
    length = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 1)
    if x2 - x1 == 0:
        slope = "Na"
    else:
        slope = round((y2-y1)/(x2-x1), 1)
    print(f"s{i+1}\t{length}\t{slope}")

y_max = max([y for s in vectors for x,y in s])
y_min = min([y for s in vectors for x,y in s])
print(f"y max={y_max}")
print(f"y min={y_min}")