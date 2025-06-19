import time

# Stop Watch
input("Press Enter Start the Stop Watch or type 'exit' to quit: ")
start_time = time.time()
print(start_time)

input("Press Enter Stop the Stop Watch or type 'exit' to quit: ")
end_time = time.time()

print(f"\n Enslaped Time: {round(end_time - start_time,2)}s")

