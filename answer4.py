import subprocess

log_file = "update_errors.log"

print("Checking for updates")
subprocess.run(["sudo", "apt", "update"])

result = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True)
updates = result.stdout.splitlines()[1:]

if len(updates) == 0:
    print("All packages are up to date.")
    exit()

print("Available Updates:")
for i in range(len(updates)):
    print(i+1, updates[i])

choice = input("Update all or choose specific? (all/select): ").lower()

if choice == "all":
    packages = []
    for update in updates:
        packages.append(update.split(' ')[0])
elif choice == "select":
    selected = input("Enter numbers of packages: ")
    indexes = selected.split(",")
    packages = []
    for index in indexes:
        package_name = updates[int(index) - 1].split(' ')[0]
        packages.append(package_name)
else:
    print("Invalid choice.")
    exit()

for package in packages:
    print("Updating", package)
    subprocess.run(["sudo", "apt", "install", "--yes", package])
