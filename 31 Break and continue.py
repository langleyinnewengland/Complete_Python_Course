cars = ["ok", "ok", "ok", "faulty", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping production")
        #terminate the loop
        break

    print(f"The car status is {status}")

#iterates through list.  Notifies when finds bad car
cars = ["ok", "ok", "ok", "faulty", "ok"]

for status in cars:
    if status == "faulty":
        print("found bad car, skipping...")
        #continue on
        continue
    print(f"The car status is {status}")
    print("Shipping car")