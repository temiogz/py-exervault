'''

  class: SSP
    -> fruit_counter

'''

def fruit_counter():
  available_fruits = ['apple', 'pears', 'lemon', 'grape', 'strawberry', 'mango', 'orange', 'banana']
  fruit_count = {fruit: 0 for fruit in available_fruits}

  while True:
    fruit = input("Enter the name of a fruit ('exit' to quit): ").lower()

    if fruit == 'exit':
      break

    if fruit in fruit_count:
      fruit_count[fruit] += 1
    else:
      error_message = f"Sorry, '{fruit}' could not be found in the list of available fruits."
      print(error_message)

  print("\nFruit count, count of each type of fruit entered.")
  
  for fruit, count in fruit_count.items():
    print(f"{fruit}: {count}")


if __name__ == "__main__":
  fruit_counter()