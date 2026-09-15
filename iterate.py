print("===== Iterable object & Range =====")
# Iterable objects => string, dict, tuple, list, map, range, filter

range_obj = range(3)
print(range_obj)
for ele in range_obj:
    print(f"the element: {ele}")

text = "MIT"
for tap in text:
    print(f"the letter: {tap}")


print("===== Dictionary =====")
# Dictionary is JSON object
person = {
    "name": "Justin",
    "age": 25,
    "sigle": True
}
person_obj = dict(name="Justin1", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

for key in person_obj:
    print(f"key: {key}")

for key, value in person_obj.items():
    print(f" {key}  = {value}")

del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} > value: {person_obj.get(key)}")
