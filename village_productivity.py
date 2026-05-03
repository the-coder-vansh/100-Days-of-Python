#village_productivity
#logic= enumerate+ short hand if-else

tasks = ["Python Video 44", "Maths Ex 2.1", "GitHub Upload", "Mama ke ghar enjoy"]

print("--- 🚀 MY GAON PRODUCTIVITY TRACKER ---")

# Task check logic
for index, task in enumerate(tasks, start=1):
    status = "COMPLETED ✅" if index <= 2 else "PENDING ⏳"
    print(f"Task {index}: {task} | Status: {status}")

# Special Message
travel_mode = True
message = "Coding is on even in Village! 🦾" if travel_mode else "Back to home base."
print(f"\nStatus Update: {message}")
