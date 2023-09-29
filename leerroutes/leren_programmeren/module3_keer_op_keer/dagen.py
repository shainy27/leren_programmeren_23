


dagen = ["ma","di","wo","do","vr","Za","zo"]

while True:
  dag = input("Welke dag is het vandaag? ma,di,wo,do,vr,za of zo")
  if dag in dagen:
        break

num = 0
restdagen = True

while restdagen:
  print(dagen[num])
  if dag == dagen [num]:
    restdagen = False
  num = num + 1


print(f'nog {num + 1} dagen')












