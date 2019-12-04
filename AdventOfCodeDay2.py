# https://adventofcode.com/2019/day/2

puzzleInput = [
  1,0,0,3,
  1,1,2,3,
  1,3,4,3,
  1,5,0,3,
  2,1,10,19,
  1,19,5,23,
  2,23,9,27,
  1,5,27,31,
  1,9,31,35,
  1,35,10,39,
  2,13,39,43,
  1,43,9,47,
  1,47,9,51,
  1,6,51,55,
  1,13,55,59,
  1,59,13,63,
  1,13,63,67,
  1,6,67,71,
  1,71,13,75,
  2,10,75,79,
  1,13,79,83,
  1,83,10,87,
  2,9,87,91,
  1,6,91,95,
  1,9,95,99,
  2,99,10,103,
  1,103,5,107,
  2,6,107,111,
  1,111,6,115,
  1,9,115,119,
  1,9,119,123,
  2,10,123,127,
  1,127,5,131,
  2,6,131,135,
  1,135,5,139,
  1,9,139,143,
  2,143,13,147,
  1,9,147,151,
  1,151,2,155,
  1,9,155,0,
  99,2,0,14,
  0]


def ExecuteOpcodes(memory, noun=0, verb=1):
  memory[1] = noun
  memory[2] = verb

  i = 0
  while(i<len(memory)):
    opcode = memory[i]
    pos_one = memory[i+1]
    pos_two = memory[i+2]
    pos_three = memory[i+3]

    if opcode == 99:
      #print(f"Opcode is 99. Exiting...")
      break
    elif opcode == 1:
      memory[pos_three] = memory[pos_one] + memory[pos_two]
      #print(f"Opcode is 1 for add.")
      #print(f"{memory[pos_three]} = {memory[pos_one]} + {memory[pos_two]}")
    elif opcode == 2:
      #print(f"pos_one- {pos_one} pos_two- {pos_two}, pos_three- {pos_three}")
      memory[pos_three] = memory[pos_one] * memory[pos_two]
      #print(f"Opcode is 2 for multiply.")
      #print(f"{memory[pos_three]} = {memory[pos_one]} * {memory[pos_two]}")

    i += 4
  
  return memory[0]

#result = ExecuteOpcodes(puzzleInput)
#print(result)

def ExecuteOpcodesPart2():
  target = 19690720
  i = 0
  j = 0

  memory = puzzleInput.copy()
  for i in range(100):
    for j in range(100):
      print(f"i={i}, j={j}")
      #print(memory)
      if ExecuteOpcodes(memory, i, j) == target:
        print("we found a match")
        return (100 * i) + j
      #intcode.clear()
      memory = puzzleInput.copy()
      

print(ExecuteOpcodesPart2())


