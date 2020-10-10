lines = input()
lines = int(lines)

sampleList = []
for i in range(lines):
  lineString = "  " * lines

  numbersList = []
  for j in range(i+1):
    if j == 0 or j == i:
      numbersList.append(1)
    else:
      numbersList.append(sampleList[i-1][j-1] + sampleList[i-1][j])
  sampleList.append(numbersList)
  

  numbersString = str(numbersList)

  lineString = lineString[:lines-i] + numbersString + lineString[lines-i:]

  print(lineString)
